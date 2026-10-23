"""Verifica a exportação e o ELPX local. Não publica e não consulta o GitHub."""
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import urljoin, urlsplit, unquote
from concurrent.futures import ThreadPoolExecutor
from zipfile import ZipFile
from lxml import etree, html
import argparse, io, json, re

ROOT=Path(__file__).resolve().parents[1]
WEB=ROOT/'website'
parser=argparse.ArgumentParser()
parser.add_argument('--base',default='http://127.0.0.1:8768/')
parser.add_argument('--references',action='store_true',help='Confere ligações externas das referências por HTTP.')
args=parser.parse_args()
assert urlsplit(args.base).hostname in ('127.0.0.1','localhost'), 'Esta revisão só permite validação local.'
names=['Início','Gerações digitais','Aprender em rede','Criar e colaborar','Atenção e inclusão']
pages=[WEB/'index.html',WEB/'html/geracoes-digitais.html',WEB/'html/aprender-em-rede.html',WEB/'html/criar-e-colaborar.html',WEB/'html/atencao-e-inclusao.html']
assert set(pages)==set([WEB/'index.html',*(WEB/'html').glob('*.html')])
missing=[]; anchors=[]; external=set(); word_counts=[]
for p in pages:
    d=html.fromstring(p.read_bytes())
    assert [x.text_content().strip() for x in d.xpath('//*[@id="siteNav"]//a')]==names
    assert len(d.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," red ")]/h1'))==1
    word_counts.append({'page':str(p.relative_to(WEB)),'words':len(d.text_content().split())})
    for e in d.xpath('//*[@src or @href]'):
        for attr in ('src','href'):
            v=e.get(attr)
            if not v:continue
            if e.get('data-final-anchor'):
                dest=pages[-1]; fragment=e.get('data-final-anchor')
            else:
                u=urlsplit(v)
                if u.scheme or u.netloc:
                    if attr=='href' and u.scheme in ('https','http'):external.add(v)
                    continue
                dest=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
                fragment=u.fragment
            if not dest.is_file():missing.append((str(p.relative_to(WEB)),v))
            if fragment and dest.suffix=='.html' and dest.is_file():
                target=html.fromstring(dest.read_bytes())
                if not target.xpath('//*[@id=$id]',id=unquote(fragment)):anchors.append((str(p.relative_to(WEB)),v))
assert not missing,missing
assert not anchors,anchors
with ZipFile(ROOT/'editavel/nao-basta-estar-ligado.elpx') as z:
    xml=z.read('content.xml')
    x=etree.fromstring(xml)
    dtd=etree.DTD(io.StringIO(z.read('content.dtd').decode()))
    assert dtd.validate(x),str(dtd.error_log)
    assert [e.text for e in x.findall('.//{*}pageName')]==names
    assert len(x.findall('.//{*}odeComponent'))==9
    assert z.read('content/resources/imagens/computacao.jpg')==(ROOT/'recursos/imagens/computacao.jpg').read_bytes()
    assert 'content/resources/imagens/catalogo.jpg' not in z.namelist()
    assert z.read('screenshot.png')==(ROOT/'validacao/capa1280.png').read_bytes()
    assert xml==(ROOT/'editavel/content.xml').read_bytes()
with ZipFile(ROOT/'editavel/website-exportado.zip') as z:
    entries=[n for n in z.namelist() if not n.endswith('/')]
    for n in entries:assert z.read(n)==(WEB/n).read_bytes(),n
spec=json.loads((ROOT/'editavel/estrutura.json').read_text(encoding='utf-8'))
prose=[]
def collect_html(s):
    d=html.fragment_fromstring(s,create_parent='div')
    prose.append(d.text_content())
    prose.extend(d.xpath('//@alt | //@aria-label | //@title'))
for page in spec['pages']:
    for block in page['blocks']:
        data=block['properties']
        for key in ('textTextarea','textFeedbackTextarea','eXeFormInstructions'):
            if data.get(key):collect_html(data[key])
        for q in data.get('questionsData',[]):
            for key in ('baseText','feedbackRight','feedbackWrong'):collect_html(q[key])
            prose.extend(t for _,t in q['answers'])
prose.append((ROOT/'conteudo/interacoes.js').read_text(encoding='utf-8'))
joined='\n'.join(prose)
for pattern in [r'\b(?:Lia|Rui)\b',r'por si só',r'[«»“”‘’—]',r'·',r'Práticas [14] a [36]',r'Não basta estar ligado',r'Uma geração não é um diagnóstico',r'As ligações precisam de fazer sentido',r'Aprender também é fazer uma pausa']:
    assert not re.search(pattern,joined,re.I),pattern
assert sum(len(html.fromstring((ROOT/'conteudo'/name).read_bytes()).xpath('//*[@data-practice]')) for name in ['04-praticas.html','05-transferencia.html'])==6
network=html.fromstring((ROOT/'conteudo/03-rede.html').read_bytes())
assert len(network.xpath('//*[@data-node]'))==5
assert len(network.xpath('//*[@data-source-note]'))==5
assert all(len(n.findall('p'))==2 for n in network.xpath('//*[@data-source-note]'))
def check(item):
    path=item.relative_to(WEB).as_posix()
    with urlopen(urljoin(args.base,path),timeout=15) as r:
        data=r.read();assert r.status==200
    assert data==item.read_bytes(),path
    return {'path':path,'status':200,'same_bytes':True,'bytes':len(data)}
files=[p for p in WEB.rglob('*') if p.is_file() and not p.name.startswith('.')]
with ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(check,files))
links=[]
if args.references:
    def check_reference(url):
        try:
            with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as r:
                return {'url':url,'status':r.status,'resolved':r.url,'type':r.headers.get('Content-Type')}
        except Exception as e:return {'url':url,'error':str(e)}
    with ThreadPoolExecutor(max_workers=5) as pool:links=list(pool.map(check_reference,sorted(external)))
report={'base':args.base,'scope':'revisão local, sem publicação','pages':names,'local_links':'OK','local_anchors':'OK',
    'editorial_checks':'OK','six_practices':'OK','files_checked':len(results),'local_http':results,'external_references':links,
    'elpx':{'DTD':'valid','pages':5,'components':9,'photo_embedded':True,'actual_screenshot':True,'web_zip_matches':True}}
(ROOT/'validacao/http-e-integridade.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'LOCAL: {len(results)} ficheiros HTTP 200 e bytes confirmados; cinco páginas; seis práticas; ligações, âncoras e restrições editoriais OK; ELPX válido com nove componentes.')
if links:print(json.dumps(links,ensure_ascii=False,indent=2))
