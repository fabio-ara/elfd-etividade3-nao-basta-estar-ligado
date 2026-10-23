"""Gera a consulta em PDF a partir dos conteúdos e atividades do projeto editável."""
from pathlib import Path
import json, re
from lxml import html as H, etree
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
OUT.mkdir(parents=True, exist_ok=True)
for name, filename in [('Body','arial.ttf'), ('Body-Bold','arialbd.ttf'), ('Body-Italic','ariali.ttf'), ('Title','georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name, 'C:/Windows/Fonts/' + filename))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Body-Bold',italic='Body-Italic',boldItalic='Body-Bold')
ink = HexColor('#203238')
teal = HexColor('#176761')
styles = {
    'h1': ParagraphStyle('h1', fontName='Title', fontSize=24, leading=28, textColor=ink, spaceAfter=14, keepWithNext=True),
    'h2': ParagraphStyle('h2', fontName='Title', fontSize=14, leading=18, textColor=teal, spaceBefore=11, spaceAfter=7, keepWithNext=True),
    'h3': ParagraphStyle('h3', fontName='Body-Bold', fontSize=10.8, leading=14.7, textColor=ink, spaceBefore=8, spaceAfter=5, keepWithNext=True),
    'p': ParagraphStyle('p', fontName='Body', fontSize=10.8, leading=14.2, textColor=ink, spaceAfter=5),
    'caption': ParagraphStyle('caption', fontName='Body', fontSize=10, leading=13, textColor=ink, spaceAfter=8),
}
story=[]
def inline(node):
    out=escape(node.text or '')
    for child in node:
        content=inline(child)
        if child.tag == 'a':
            href=child.get('href','')
            if href.startswith(('https://','http://')):
                content='<a href="'+escape(href, {'"':'&quot;'})+'" color="#176761">'+content+'</a>'
        elif child.tag in ('strong','b'): content='<b>'+content+'</b>'
        elif child.tag in ('em','i'): content='<i>'+content+'</i>'
        elif child.tag=='br': content='<br/>'
        out += content + escape(child.tail or '')
    return out.replace('–','-')
def paragraph(text, style='p'): story.append(Paragraph(text, styles[style]))
def add_html(content, omit_classification=False):
    root=H.fragment_fromstring(content,create_parent='div')
    for node in root.iter():
        if omit_classification and any('classification-item' in e.get('class','') for e in [node,*node.iterancestors()]): continue
        if node.tag in ('h1','h2','h3','p','figcaption','label'):
            if node.tag=='label': continue
            if node.get('id') in ('network-count','network-limit'): continue
            text=inline(node)
            if text.strip(): paragraph(text.replace(' <a','&#160;<a').replace('</a> ','</a>&#160;'), 'caption' if node.tag=='figcaption' else node.tag)
        elif node.tag=='img':
            image=Image(str(ROOT/'recursos/imagens/computacao.jpg'),width=190,height=130.308)
            image.hAlign='LEFT';story.append(image);story.append(Spacer(1,8))
        elif node.tag=='button' and node.get('id')=='evaluate-network': continue
def quiz(data):
    q=data['questionsData'][0]
    add_html(q['baseText'])
    for expected,text in q['answers']:
        paragraph(escape(text))
    paragraph('Explicação das escolhas','h3')
    add_html(q['feedbackRight'])

spec=json.loads((ROOT/'editavel/estrutura.json').read_text(encoding='utf-8'))
for i,page in enumerate(spec['pages']):
    if i: story.append(PageBreak())
    for block in page['blocks']:
        data=block['properties']
        if block['type']=='form': quiz(data);continue
        add_html(data['textTextarea'],omit_classification=(i==1))
        if data.get('textFeedbackTextarea'):
            paragraph('Uma possibilidade','h3')
            add_html(data['textFeedbackTextarea'])
    if i==1:
        for label,text in [
          ('Jogos digitais adequados aos conteúdos','Sugestão para o ensino. Prensky propôs jogos que envolvessem os estudantes nos conteúdos das aulas. O professor precisa de verificar a adequação das tarefas ao que pretende ensinar.'),
          ('Experiência digital e aprendizagem','Hipótese a investigar. É necessário definir que experiências se comparam e observar como as pessoas aprendem. Prensky não demonstrou as diferenças físicas entre grupos que sugeria.'),
          ('Competências diferentes na mesma idade','Crítica à divisão por gerações. Kirschner e De Bruyckere questionaram a ideia de capacidades digitais uniformes numa geração. As competências devem ser observadas em tarefas concretas.')]:
            paragraph(label,'h3');paragraph(text)
    if i==2:
        paragraph('Comparar fontes','h3')
        paragraph('Por exemplo, o professor ajuda a definir o que se pretende aprender, os colegas descrevem as suas experiências e o artigo permite examinar como uma investigação avaliou a aprendizagem. Compare o conteúdo estudado, as atividades realizadas e a forma de avaliar a compreensão.')
        paragraph('A seguir, procure outra pesquisa sobre a mesma pergunta e verifique se os seus resultados se aplicam às condições descritas pelos colegas.')

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(HexColor('#c4cec9'));canvas.line(48,40,547,40)
    canvas.setFont('Body',9);canvas.setFillColor(ink)
    canvas.drawString(48,26,'Fabio Eidi Ara, Universidade de Lisboa')
    canvas.drawRightString(547,26,str(doc.page))
    canvas.restoreState()

target=OUT/'nao-basta-estar-ligado-consulta.pdf'
doc=SimpleDocTemplate(str(target),pagesize=(595.28,841.89),leftMargin=48,rightMargin=48,topMargin=40,bottomMargin=52,
    title='Como aprendemos com a tecnologia?',author='Fabio Eidi Ara',subject='E-learning e Formação a Distância, Etividade 3')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(target)
