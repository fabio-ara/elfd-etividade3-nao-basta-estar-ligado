"""Gera uma entrada ELPX a partir do modelo oficial; exportação final feita no editor.

Fonte do modelo: exelearning/exelearning, test/fixtures/really-simple-test-project.elpx.
Executar a partir da raiz. Não confundir o pacote de entrada com o ELPX reexportado.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json, copy, re, io
from lxml import etree as E

ROOT=Path(__file__).resolve().parents[1]
NS='http://www.intef.es/xsd/ode'
def tag(n):return '{'+NS+'}'+n
def el(parent,n,text=None):
    x=E.SubElement(parent,tag(n));x.text=text;return x
def props(parent,container,item,values):
    out=el(parent,container)
    for k,v in values.items():
        p=el(out,item);el(p,'key',k);el(p,'value',str(v).lower() if isinstance(v,bool) else str(v))
    return out
def idof(prefix,n):return '20261023140000'+prefix+str(n).zfill(5)
def read(name):return (ROOT/'conteudo'/name).read_text(encoding='utf-8')
def textdata(html,feedback=''):
    return {'textTextarea':html,'textFeedbackInput':'Ver uma possibilidade','textFeedbackTextarea':feedback,'textInfoDurationInput':'','textInfoDurationTextInput':'Duração','textInfoParticipantsInput':'','textInfoParticipantsTextInput':'Participação'}
def quiz(question,instruction,answers,right,wrong):
    return {'evaluation':False,'isScorm':0,'weighted':100,'repeatActivity':True,'questionsRandom':False,'percentageQuestions':100,'time':0,'passRate':5,'showSlider':False,'addBtnAnswers':False,'eXeFormInstructions':'','eXeIdeviceTextAfter':'','msgs':{'msgCheck':'Conferir respostas','msgReset':'Tentar novamente','msgShowAnswers':'Consultar explicações','msgOk':'','msgKO':'','msgScore':'','msgUnansweredQuestions':'Selecione as ações que considera úteis.','msgAllQuestions':'Selecione as ações que considera úteis.'},'questionsData':[{'activityType':'selection','selectionType':'multiple','baseText':'<div class="red"><h2>'+question+'</h2><p>'+instruction+'</p></div>','answers':answers,'feedbackRight':right,'feedbackWrong':wrong}]}

first_feedback='''<h3>Procurar o estudo</h3><p>Ajuda a perceber o que foi realmente investigado: que tarefas foram comparadas, quem participou e como se avaliou a aprendizagem.</p><h3>Dar mais peso a quem usa mais aplicações</h3><p>A familiaridade com aplicações pode ajudar a utilizá-las. Para avaliar esta afirmação, é preciso examinar as pesquisas sobre a aprendizagem.</p><h3>Comparar pesquisas</h3><p>Permite verificar se outros trabalhos sustentam a afirmação e em que condições chegaram a resultados semelhantes ou diferentes.</p><h3>Confiar no número de partilhas</h3><p>As partilhas mostram que uma publicação circulou. Para decidir se a informação é fiável, procure a sua origem e os resultados apresentados.</p><p>Ana e Estevão têm idades e experiências digitais diferentes. A capacidade de avaliar esta informação observa-se na forma como procuram, comparam e interpretam as fontes. <a href="https://doi.org/10.1016/j.tate.2017.06.001">Kirschner e De Bruyckere (2017)</a>.</p>'''
first=quiz('O que devem fazer para avaliar esta afirmação?','Selecione as duas ações mais úteis.',[
    [True,'Procurar o estudo em que a publicação se baseia.'],
    [False,'Dar mais peso à opinião de quem utiliza mais aplicações.'],
    [True,'Comparar a afirmação com outras pesquisas sobre o assunto.'],
    [False,'Confiar na publicação que recebeu mais partilhas.']
],'<p>Procurar o estudo e comparar pesquisas permite examinar as razões apresentadas para a afirmação.</p>'+first_feedback,'<p>Reveja as escolhas tendo em conta a origem da informação e as pesquisas que a sustentam.</p>'+first_feedback)

final_feedback='''<h3>Aceitar formatos acessíveis e uma entrega reservada</h3><p>Permite participar com diferentes condições de acesso e protege os dados pessoais. Peça que cada estudante escolha os recursos que melhor explicam o tema e justifique essa escolha.</p><h3>Reservar tempo para consultar fontes e rever</h3><p>Cria condições para ler com atenção, verificar a informação e melhorar a explicação. Acompanhe as fontes utilizadas e as alterações que os estudantes conseguem justificar.</p><h3>Pedir comentários aos colegas</h3><p>Ajuda a confrontar interpretações antes da entrega. Oriente os comentários para a clareza das ideias e a sua fundamentação. Peça que a versão final mostre como foram consideradas essas contribuições.</p><h3>Aumentar o peso dos gostos</h3><p>Os gostos dependem da circulação da publicação e da reação do público. Para avaliar a aprendizagem, use critérios como a clareza da explicação, a qualidade das fontes e a justificação das revisões.</p>'''
final=quiz('Que mudanças ajudariam os estudantes a aprender e a participar?','Selecione as mudanças que considera úteis.',[
    [True,'Aceitar diferentes formatos acessíveis e permitir a entrega num espaço reservado.'],
    [True,'Reservar tempo para consultar fontes e rever o trabalho.'],
    [True,'Pedir aos colegas que comentem as explicações antes da entrega.'],
    [False,'Aumentar o peso dos gostos na nota final.']
],'<p>As três medidas escolhidas ajudam os estudantes a explicar o tema, rever o trabalho e participar com condições adequadas.</p>'+final_feedback,'<p>Considere como cada medida ajuda a compreender o tema e a participar na atividade.</p>'+final_feedback)

page_specs=[
 ('Início',[('A situação','text',textdata(read('01-problema.html'))),('Avaliar a afirmação','form',first)]),
 ('Gerações digitais',[('Nativos e imigrantes digitais','text',textdata(read('02-conceitos.html')))]),
 ('Aprender em rede',[('Fontes e interlocutores','text',textdata(read('03-rede.html')))]),
 ('Criar e colaborar',[('Criar e aprender em grupo','text',textdata(read('04-praticas.html'))),('Melhorar o trabalho de grupo','text',textdata(read('04-sintese.html'),'<div class="red"><p>Organizem uma conversa sobre a primeira versão do vídeo. Cada participante pode identificar uma ideia que precisa de ser explicada melhor e propor uma alteração apoiada nas fontes consultadas. Depois, revejam o vídeo em conjunto e expliquem como as contribuições do grupo ajudaram a melhorar a resposta.</p></div>'))]),
 ('Atenção e inclusão',[('Estudar, avaliar fontes e participar','text',textdata(read('05-transferencia.html'))),('Melhorar a atividade','form',final),('Referências e autoria','text',textdata(read('05-referencias.html')))])]

template=ROOT/'tmp/modelo-oficial.elpx'
if not template.exists():template=ROOT/'editavel/nao-basta-estar-ligado.elpx'
with ZipFile(template) as z:
    original={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
root=E.Element(tag('ode'),nsmap={None:NS},version='2.0')
props(root,'userPreferences','userPreference',{'theme':'base'})
props(root,'odeResources','odeResource',{'odeId':idof('R',1),'odeVersionId':idof('V',1),'exe_version':'3.0'})
css=read('estilo.css');js=read('interacoes.js')
metadata={'pp_title':'Como aprendemos com a tecnologia?','pp_subtitle':'','pp_author':'Fabio Eidi Ara','pp_description':'Recurso sobre nativos e imigrantes digitais, conectivismo e seis práticas educativas. ELFD 2026/2027, METD, IE, Universidade de Lisboa.','pp_lang':'pt','pp_license':'creative commons: attribution - share alike 4.0','pp_licenseUrl':'https://creativecommons.org/licenses/by-sa/4.0/','pp_theme':'base','pp_exelearning_version':'4.0.5','pp_addExeLink':True,'pp_addPagination':False,'pp_addSearchBox':False,'pp_addAccessibilityToolbar':False,'pp_addMathJax':False,'exportSource':True,'pp_extraHeadContent':'<style id="red-editorial">\n'+css+'\n</style>\n<script>\n'+js+'\n</script>','footer':'<p>Fabio Eidi Ara<br><a href="#referencias" data-final-anchor="referencias">Referências</a><br><a href="#autoria-fotografias" data-final-anchor="autoria-fotografias">Autoria e fotografias</a></p>'}
props(root,'odeProperties','odeProperty',metadata)
nav=el(root,'odeNavStructures');count=0;spec=[]
for pi,(title,blocks) in enumerate(page_specs,1):
    pid=idof('P',pi);page=el(nav,'odeNavStructure');el(page,'odePageId',pid);el(page,'odeParentPageId','');el(page,'pageName',title);el(page,'odeNavStructureOrder',str(pi-1))
    props(page,'odeNavStructureProperties','odeNavStructureProperty',{'titlePage':title,'titleNode':title,'hidePageTitle':True,'visibility':True})
    bs=el(page,'odePagStructures');spec.append({'id':pid,'title':title,'blocks':[]})
    for bi,(name,kind,data) in enumerate(blocks,1):
        count+=1;bid=idof('B',count);iid=idof('I',count);data=copy.deepcopy(data);data['ideviceId']=iid
        if kind=='form':data['id']=iid
        b=el(bs,'odePagStructure');el(b,'odePageId',pid);el(b,'odeBlockId',bid);el(b,'blockName',name);el(b,'iconName','');el(b,'odePagStructureOrder',str(bi))
        props(b,'odePagStructureProperties','odePagStructureProperty',{'visibility':True,'teacherOnly':False,'allowToggle':False,'minimized':False,'cssClass':'red-block'})
        c=el(el(b,'odeComponents'),'odeComponent');el(c,'odePageId',pid);el(c,'odeBlockId',bid);el(c,'odeIdeviceId',iid);el(c,'odeIdeviceTypeName',kind)
        if kind=='text':
            html='<div class="exe-text-template"><div class="textIdeviceContent"><div class="exe-text-activity">'+data['textTextarea']+'</div>'
            if data.get('textFeedbackTextarea'):
                html+='<div class="iDevice_buttons feedback-button js-required"><input type="button" class="feedbacktooglebutton" value="Ver uma possibilidade"></div><div class="feedback js-feedback js-hidden" style="display:none">'+data['textFeedbackTextarea']+'</div>'
            html+='</div></div>'
        else:html='<div class="exe-form-container"><p>Atividade de seleção com feedback explicativo. Ative JavaScript para interagir.</p></div>'
        el(c,'htmlView').text=E.CDATA(html);el(c,'jsonProperties').text=E.CDATA(json.dumps(data,ensure_ascii=False));el(c,'odeComponentsOrder','1')
        props(c,'odeComponentsProperties','odeComponentsProperty',{'visibility':True,'teacherOnly':False})
        spec[-1]['blocks'].append({'name':name,'type':kind,'properties':data})
xml=E.tostring(root,encoding='UTF-8',xml_declaration=True,pretty_print=True,doctype='<!DOCTYPE ode SYSTEM "content.dtd">')
(ROOT/'editavel/content.xml').write_bytes(xml)
(ROOT/'editavel/estrutura.json').write_text(json.dumps({'metadata':metadata,'pages':spec},ensure_ascii=False,indent=2),encoding='utf-8')
dtd=E.DTD(io.StringIO(original['content.dtd'].decode('utf-8')))
if not dtd.validate(E.fromstring(xml)):
    raise ValueError(str(dtd.error_log))
out=ROOT/'tmp/entrada.elpx';out.parent.mkdir(parents=True,exist_ok=True)
with ZipFile(out,'w',ZIP_DEFLATED) as z:
    for n,v in original.items():
        if n!='content.xml' and not n.startswith(('html/','content/resources/imagens/')):z.writestr(n,v)
    z.writestr('content.xml',xml)
    p=ROOT/'recursos/imagens/computacao.jpg'
    z.write(p,'content/resources/imagens/computacao.jpg')
print(f'ELPX de entrada: {out.name}; {len(page_specs)} páginas; {count} componentes; DTD válido. Importar e reexportar no editor para os artefactos finais.')
