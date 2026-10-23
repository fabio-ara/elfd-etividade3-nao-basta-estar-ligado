"""Verifica publicação real por HTTP sem credenciais e integridade do pacote."""
from pathlib import Path
from urllib.request import urlopen,Request
from urllib.parse import urljoin,urlsplit,unquote
from concurrent.futures import ThreadPoolExecutor
from zipfile import ZipFile
from lxml import etree,html
import io,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
WEB=ROOT/'website';BASE='https://fabio-ara.github.io/elfd-etividade3-nao-basta-estar-ligado/'
pages=[WEB/'index.html',*sorted((WEB/'html').glob('*.html'))]
assert len(pages)==5
missing=[];anchors=[]
for p in pages:
    d=html.fromstring(p.read_bytes())
    for attr in ['src','href']:
        for v in d.xpath('//@'+attr):
            u=urlsplit(v)
            if u.scheme or u.netloc:continue
            dest=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
            if not dest.is_file():missing.append((str(p.relative_to(WEB)),v))
            if u.fragment and dest.suffix=='.html' and dest.is_file():
                target=html.fromstring(dest.read_bytes())
                if not target.xpath('//*[@id=$id]',id=unquote(u.fragment)):anchors.append((str(p.relative_to(WEB)),v))
assert not missing,missing
assert not anchors,anchors
def check(p):
    path=p.relative_to(WEB).as_posix()
    try:
        with urlopen(Request(urljoin(BASE,path),headers={'User-Agent':'RED-validation/1.0'}),timeout=30) as r:
            data=r.read();status=r.status
        local=p.read_bytes()
        if p.suffix in ['.html','.xml','.css','.js']:data=data.replace(b'\r\n',b'\n');local=local.replace(b'\r\n',b'\n')
        return {'path':path,'status':status,'same_bytes':data==local,'bytes':len(data)}
    except Exception as e:return {'path':path,'error':str(e)}
files=[p for p in WEB.rglob('*') if p.is_file() and not p.name.startswith('.')]
with ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(check,files))
assert all(r.get('status')==200 and r.get('same_bytes') for r in results),[r for r in results if r.get('status')!=200 or not r.get('same_bytes')]
with ZipFile(ROOT/'editavel/nao-basta-estar-ligado.elpx') as z:
    x=etree.fromstring(z.read('content.xml'));dtd=etree.DTD(io.StringIO(z.read('content.dtd').decode()))
    assert dtd.validate(x),str(dtd.error_log)
    assert len(x.findall('.//{*}odeNavStructure'))==5
    assert len(x.findall('.//{*}odeComponent'))==10
    assert z.read('screenshot.png')==(ROOT/'validacao/capa1280.png').read_bytes()
    for name in ['computacao.jpg','catalogo.jpg']:
        assert z.read('content/resources/imagens/'+name)==(ROOT/'recursos/imagens'/name).read_bytes()
report={'base':BASE,'pages':5,'local_links':'OK','local_anchors':'OK','files_checked':len(results),'public_http':results,'elpx':{'DTD':'valid','pages':5,'components':10,'photos_embedded':True,'actual_screenshot':True}}
(ROOT/'validacao/http-e-integridade.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'PUBLICAÇÃO: {len(results)} arquivos HTTP 200 e integridade confirmada; 5 páginas, links/âncoras locais OK; ELPX válido, 10 componentes, imagens e capa incorporadas.')
