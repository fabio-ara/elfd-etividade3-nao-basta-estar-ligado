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
    return {'textTextarea':html,'textFeedbackInput':'Comparar com uma resposta fundamentada','textFeedbackTextarea':feedback,'textInfoDurationInput':'','textInfoDurationTextInput':'Duração','textInfoParticipantsInput':'','textInfoParticipantsTextInput':'Participação'}
def quiz(question,answers,right,wrong):
    return {'evaluation':False,'isScorm':0,'weighted':100,'repeatActivity':True,'questionsRandom':False,'percentageQuestions':100,'time':0,'passRate':5,'showSlider':False,'addBtnAnswers':False,'eXeFormInstructions':'<p><strong>Selecione todas as evidências pertinentes.</strong> Depois, examine a explicação. Você pode refazer a escolha.</p>','eXeIdeviceTextAfter':'','msgs':{'msgCheck':'Examinar as escolhas','msgReset':'Reconsiderar','msgShowAnswers':'Ver escolhas fundamentadas','msgOk':'Escolha fundamentada.','msgKO':'Reveja os critérios.','msgScore':'','msgUnansweredQuestions':'Examine as opções antes de continuar.','msgAllQuestions':'Selecione as opções para examinar a decisão.'},'questionsData':[{'activityType':'selection','selectionType':'multiple','baseText':'<p>'+question+'</p>','answers':answers,'feedbackRight':right,'feedbackWrong':wrong}]}

first_feedback='<p><strong>Idade, familiaridade e avaliação do conhecimento são dimensões diferentes.</strong> Encontrar a fonte original, confrontar evidências independentes e justificar uma revisão são ações observáveis de avaliação da informação.</p><p>Publicar com rapidez mostra familiaridade com uma ferramenta; a data de nascimento só informa a idade. Nenhuma das duas permite concluir quem sabe verificar a mensagem. Lia e Rui podem aprender com orientação e prática. Observe o processo de ambos.</p>'
first=quiz('O que observar em Lia e Rui?',[
    [False,'A idade de cada pessoa, para prever quem verifica melhor.'],
    [True,'Se localizam a origem da mensagem, a autoria e a evidência apresentada.'],
    [False,'A rapidez com que publicam vídeos, como prova de pensamento crítico.'],
    [True,'Se comparam a mensagem com fontes independentes e pertinentes.'],
    [True,'Se justificam a confiança e revêm a conclusão perante informação nova.']
],first_feedback,'<p><strong>Reveja o que conta como evidência de competência.</strong></p>'+first_feedback)

final_feedback='<p><strong>Uma atividade melhor torna visível o raciocínio.</strong> Escolher formatos e explicar decisões trabalha produção multimodal; debater e rever em pares trabalha colaboração; receber retorno explicativo trabalha autorregulação.</p><p>Separar leitura, análise e revisão protege a atenção. Confrontar a fonte original com outras evidências desenvolve avaliação crítica. Oferecer uma versão leve e acessível, com participação sem exposição pública obrigatória, favorece inclusão e privacidade.</p><p>Mais aplicações, efeitos visuais ou gostos não demonstram compreensão. Avalie a síntese, as fontes e as justificações das revisões. Escolha uma destas medidas e formule um indicador para a sua próxima atividade.</p>'
final=quiz('Que mudanças você adotaria?',[
    [True,'Permitir um recurso leve em texto, áudio com transcrição ou vídeo; pedir justificação das escolhas de linguagem.'],
    [False,'Abrir mais aplicações ao mesmo tempo para treinar todos como multitarefadores.'],
    [True,'Separar tempo de leitura e síntese; comparar a fonte original e justificar a confiança.'],
    [True,'Organizar discussão em pares, com feedback sobre os argumentos e revisão do trabalho.'],
    [False,'Manter nome completo e publicação aberta obrigatórios, aumentando o peso dos gostos na nota.'],
    [True,'Oferecer alternativa acessível e participação sem exposição pública obrigatória de dados pessoais.']
],final_feedback,'<p><strong>Há critérios a rever.</strong> Procure medidas que tornem o raciocínio observável e removam barreiras.</p>'+final_feedback)
final['eXeFormInstructions']='<p><strong>Selecione todas as medidas fundamentadas.</strong> Depois, compare com a explicação.</p>'

page_specs=[
 ('O problema',[('A situação','text',textdata(read('01-problema.html'))),('Escolher evidências','form',first),('Crédito da abertura','text',textdata('<div class="red"><details id="creditos-locais"><summary>Fotografia da abertura: origem e direitos</summary><p><i>Two women operating ENIAC</i>, 1946. Betty Jennings e Frances Bilas; fotógrafo não identificado do U.S. Army, arquivos da ARL Technical Library. <a href="https://commons.wikimedia.org/wiki/File:Two_women_operating_ENIAC_(full_resolution).jpg#Licensing">Página do ficheiro e declaração de domínio público nos EUA (PD-USGov-Military-Army)</a>.</p></details><p class="source-note">Competência não se deduz da geração. Contraponto: <a href="https://doi.org/10.1016/j.tate.2017.06.001">Kirschner &amp; De Bruyckere (2017)</a>. Referências completas na etapa 5.</p></div>'))]),
 ('Conceitos e crítica',[('Distinguir conceitos e evidências','text',textdata(read('02-conceitos.html')))]),
 ('Aprender em rede',[('Laboratório de conexões','text',textdata(read('03-rede.html')))]),
 ('Práticas 1 a 3',[('Criar, colaborar e experimentar','text',textdata(read('04-praticas.html'))),('Transferir a ideia','text',textdata(read('04-sintese.html'),'<div class="red"><p><strong>Dividir tarefas não garante construção conjunta.</strong> Peça que cada participante confronte um argumento de outro colega com uma fonte e que o grupo registre uma revisão. O indicador é a mudança fundamentada na síntese, não o número de mensagens ou de edições.</p></div>'))]),
 ('Práticas 4 a 6',[('Refletir, avaliar e incluir','text',textdata(read('05-transferencia.html'))),('Aplicar os critérios','form',final),('Referências e créditos','text',textdata(read('05-referencias.html')))])]

template=ROOT/'tmp/modelo-oficial.elpx'
if not template.exists():template=ROOT/'editavel/nao-basta-estar-ligado.elpx'
with ZipFile(template) as z:
    original={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
root=E.Element(tag('ode'),nsmap={None:NS},version='2.0')
props(root,'userPreferences','userPreference',{'theme':'base'})
props(root,'odeResources','odeResource',{'odeId':idof('R',1),'odeVersionId':idof('V',1),'exe_version':'3.0'})
css=read('estilo.css');js=read('interacoes.js')
metadata={'pp_title':'Não basta estar ligado','pp_subtitle':'Uma experiência sobre gerações, redes e aprendizagem digital.','pp_author':'Fabio Eidi Ara','pp_description':'Microexperiência sobre nativos e imigrantes digitais, conectivismo e seis práticas educativas. ELFD 2026/2027, METD, IE, Universidade de Lisboa.','pp_lang':'pt','pp_license':'creative commons: attribution - share alike 4.0','pp_licenseUrl':'https://creativecommons.org/licenses/by-sa/4.0/','pp_theme':'base','pp_exelearning_version':'4.0.5','pp_addExeLink':True,'pp_addPagination':False,'pp_addSearchBox':False,'pp_addAccessibilityToolbar':False,'pp_addMathJax':False,'exportSource':True,'pp_extraHeadContent':'<style id="red-editorial">\n'+css+'\n</style>\n<script>\n'+js+'\n</script>','footer':'<p>Fabio Eidi Ara · ELFD 2026/2027 · Universidade de Lisboa<br>Texto CC BY-SA 4.0 · fotografias de domínio público · eXeLearning 4.0.5</p>'}
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
                html+='<div class="iDevice_buttons feedback-button js-required"><input type="button" class="feedbacktooglebutton" value="Comparar com uma resposta fundamentada"></div><div class="feedback js-feedback js-hidden" style="display:none">'+data['textFeedbackTextarea']+'</div>'
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
    for p in (ROOT/'recursos').rglob('*'):
        if p.is_file():z.write(p,'content/resources/'+p.relative_to(ROOT/'recursos').as_posix())
print(f'ELPX de entrada: {out.name}; {len(page_specs)} páginas; {count} componentes; DTD válido. Importar e reexportar no editor para os artefactos finais.')
