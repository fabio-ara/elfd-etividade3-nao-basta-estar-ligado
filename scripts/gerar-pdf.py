"""Versão estática de consulta, com cinco páginas; não substitui as interações web."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf';OUT.mkdir(parents=True,exist_ok=True)
for name,file in [('Body','arial.ttf'),('Body-Bold','arialbd.ttf'),('Body-Italic','ariali.ttf'),('Title','georgia.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Body-Bold',italic='Body-Italic',boldItalic='Body-Bold')
ink=HexColor('#1e3035');teal=HexColor('#176761');accent=HexColor('#a83e25')
styles={
 'title':ParagraphStyle('title',fontName='Title',fontSize=27,leading=31,textColor=ink,spaceAfter=14),
 'h2':ParagraphStyle('h2',fontName='Title',fontSize=15,leading=19,textColor=teal,spaceBefore=11,spaceAfter=6),
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.4,leading=14.2,textColor=ink,spaceAfter=8),
 'small':ParagraphStyle('small',fontName='Body',fontSize=8.5,leading=11.5,textColor=ink,spaceAfter=6),
 'feedback':ParagraphStyle('feedback',fontName='Body',fontSize=10,leading=14,textColor=ink,backColor=HexColor('#e5ece6'),borderPadding=8,spaceBefore=5,spaceAfter=10),
}
story=[]
def p(s,style='body'):story.append(Paragraph(s,styles[style]))
def title(n,s):
    p(f'{n:02d} / NÃO BASTA ESTAR LIGADO','small');p(s,'title')
def practice(n,name,action,purpose,evidence):
    p(f'{n:02d}. {name}','h2');p('<b>O educador faz:</b> '+action);p('<b>Para quê:</b> '+purpose);p('<b>Observe:</b> '+evidence,'feedback')
url='https://fabio-ara.github.io/elfd-etividade3-nao-basta-estar-ligado/'
title(1,'Quem sabe aprender?')
p('Uma experiência sobre gerações, redes e aprendizagem digital.','h2')
p('Ter crescido rodeado de tecnologia significa saber aprender com ela?')
im=Image(str(ROOT/'recursos/imagens/computacao.jpg'),width=300,height=206);im.hAlign='LEFT';story.append(im)
p('Betty Jennings e Frances Bilas no ENIAC, 1946. Fotógrafo não identificado do U.S. Army; ARL Technical Library. Domínio público nos EUA (PD-USGov-Military-Army). <link href="https://commons.wikimedia.org/wiki/File:Two_women_operating_ENIAC_(full_resolution).jpg#Licensing" color="#176761">Origem e direitos</link>.','small')
p('O caso','h2')
p('Lia, 22 anos, publica vídeos todos os dias. Rui, 57 anos, começou a usar plataformas digitais no trabalho. Ambos encontram: “Quem estuda com várias aplicações abertas aprende mais.” Situação fictícia.')
p('<b>Que evidências você procuraria?</b> A idade? A rapidez de publicação? A localização da fonte original? A comparação com fontes independentes? A justificação da confiança e a revisão perante informação nova?')
p('<b>Retorno:</b> idade, familiaridade e avaliação do conhecimento são dimensões diferentes. Localizar a origem, confrontar evidências pertinentes e justificar uma revisão tornam observável a competência. Publicar rapidamente não prova pensamento crítico. Lia e Rui podem aprender com orientação e prática.','feedback')
p('Público: professores, formadores e estudantes adultos. Cerca de 12 minutos no percurso web. Este PDF oferece consulta estática e explicações; as escolhas e a rede são exploradas no site.','small')
p(f'<link href="{url}" color="#176761">Abrir a experiência interativa</link>','body')
story.append(PageBreak())
title(2,'Uma geração não é um diagnóstico.')
p('Nativos e imigrantes digitais','h2')
p('<b>Nativos digitais:</b> pessoas que cresceram em ambientes de computadores, jogos e tecnologias digitais. Na proposta de Prensky, essas experiências influenciam preferências e modos de processar informação.')
p('<b>Imigrantes digitais:</b> pessoas que conheceram esse ambiente mais tarde e se adaptam, conservando hábitos anteriores, comparados a um “sotaque”. É uma metáfora, não uma medida de competência. O enunciado usa “emigrantes”; aqui adota-se a tradução habitual de <i>digital immigrants</i>.')
p('Na Parte II, Prensky (2001) mobiliza a plasticidade cerebral e defende a aprendizagem por jogos digitais. Argumenta que a experiência tecnológica pode alterar o pensamento, mas reconhece não ter observado diretamente os cérebros dos “nativos” para confirmar diferenças físicas.')
p('<b>Plasticidade não prova dois tipos de cérebro definidos pela geração.</b> Kirschner e De Bruyckere (2017) questionam a ideia de uma geração uniformemente competente e de jovens que realizariam várias tarefas cognitivas simultâneas sem prejuízo. Acesso, prática e orientação precisam ser considerados.','feedback')
p('Classifique e compare','h2')
p('<b>1.</b> Jogos digitais podem aproximar os métodos de ensino das experiências dos estudantes. <b>2.</b> Crescer com tecnologia demonstra cérebros diferentes em toda uma geração e melhor aprendizagem em multitarefa. <b>3.</b> Uso frequente não sustenta uma geração de especialistas digitais ou de multitarefadores eficazes.')
p('<b>1 - Proposta de Prensky:</b> uma proposta pedagógica não demonstra eficácia universal. É preciso avaliar a adequação ao objetivo. <b>2 - Extrapolação que requer evidência:</b> transforma inferências em certeza e generaliza. <b>3 - Conclusão crítica posterior:</b> a revisão de Kirschner e De Bruyckere não sustenta uma geração homogênea; isso não nega a competência de indivíduos.','feedback')
p('Frases em paráfrase didática, não citações literais. Referências completas na página 5.','small')
story.append(PageBreak())
title(3,'Aprender numa rede')
p('O conectivismo de Siemens (2004/2005)','h2')
p('Aprender envolve estabelecer e manter conexões entre pessoas, ideias e fontes especializadas. Parte do conhecimento pode estar distribuída por organizações e dispositivos. A diversidade de perspectivas, a capacidade de encontrar conhecimento, a atualização e a decisão são centrais nessa perspectiva teórica.')
p('A turma deve substituir todas as leituras por vídeos curtos? Escolha mentalmente três ligações para investigar. Pessoas, documentos e datas deste caso são fictícios.','h2')
for s in [
 '<b>Professor:</b> ajuda a definir a pergunta e os critérios; autoridade não substitui evidência.',
 '<b>Colegas:</b> trazem dificuldades e interpretações; podem repetir a mesma opinião.',
 '<b>Artigo científico de 2016:</b> oferece método e resultados; data, amostra e contexto limitam a generalização.',
 '<b>Comunidade de prática:</b> relata aplicações e condições de acesso; relatos não provam um efeito geral.',
 '<b>Base de dados:</b> localiza estudos e atualiza a busca; indexação não garante qualidade.'
]:p(s)
p('Examinar e rever','h2')
p('Uma rede só de pessoas precisa confrontar relatos com investigação; uma rede só de documentos precisa escutar o contexto. Nenhuma combinação prova que vídeos sejam superiores.')
p('A informação mudou: uma revisão fictícia de 2026 encontra resultados diferentes conforme objetivos e acesso. O estudo de 2016 envolvia apenas uma turma com boa ligação à internet. Reveja a rede: como atualizar a evidência e incluir uma perspectiva humana?')
p('<b>Retorno fundamentado:</b> combine busca atualizada e leitura crítica com professor, colegas ou comunidade. Popularidade não é prova; data recente não basta sem examinar método e pertinência. Uma decisão possível é combinar leitura e vídeo, testar uma alternativa acessível e rever com o grupo. Manter conexões e decidir perante informação nova concretiza a perspectiva de Siemens. Mais ligações não garantem mais aprendizagem.','feedback')
story.append(PageBreak())
title(4,'Três práticas para potenciar competências')
p('Propostas pedagógicas deste recurso, em diálogo com as leituras. Não são uma lista prescrita pelos autores.','small')
practice(1,'Produção multimodal','pede um recurso sobre uma informação controversa, combinando texto com áudio, imagem ou diagrama e explicação das escolhas e fontes.','comunicação, criação digital e síntese; cada linguagem deve acrescentar significado.','o estudante explica a função de cada formato, articula argumentos e oferece alternativa acessível, como transcrição.')
practice(2,'Aprendizagem colaborativa em rede','organiza grupos para investigar uma questão, distribuir papéis, consultar fontes diferentes e confrontar interpretações num documento compartilhado.','colaboração, argumentação e negociação de significados.','o histórico mostra contribuições, objeções fundamentadas e revisão da síntese após o debate.')
practice(3,'Interatividade e feedback','propõe simulação ou desafio de fontes com explicação da consequência de cada decisão e nova tentativa.','resolução de problemas e autorregulação: perceber, testar e corrigir.','na segunda tentativa, o estudante muda o critério e explica o erro inicial; acertar ao acaso não basta.')
p('<b>Para transferir:</b> dividir a produção de um vídeo em partes garante colaboração? Não. Peça que cada pessoa confronte um argumento de um colega com uma fonte e que o grupo registre uma revisão. Observe a mudança fundamentada, não o número de mensagens.','feedback')
im=Image(str(ROOT/'recursos/imagens/catalogo.jpg'),width=160,height=120);im.hAlign='LEFT';story.append(im)
p('Catálogo da Sterling Memorial Library, Yale. Henry Trotter, 2005. Domínio público por declaração mundial do titular (PD-self). <link href="https://commons.wikimedia.org/wiki/File:SML-Card-Catalog.jpg#Licensing" color="#176761">Origem e direitos</link>. Localizar informação é uma etapa; interpretar e justificar são outras.','small')
story.append(PageBreak())
title(5,'Três práticas complementares')
practice(4,'Reflexão e atenção sustentada','reserva leitura sem notificações, síntese e revisão de uma decisão.','atenção, compreensão e reflexão sobre a aprendizagem.','a síntese relaciona ideias e justifica o que foi mantido ou alterado.')
practice(5,'Avaliação crítica das fontes','compara informações e fonte original: autoria, data, evidência, finalidade e confirmação independente.','pesquisa, pensamento crítico e literacia da informação.','o estudante justifica confiança e explicita limites; popularidade não serve como prova.')
practice(6,'Inclusão e ética digital','oferece versões leves e acessíveis, modos diversos de participação e dados fictícios.','responsabilidade, empatia e participação equitativa.','o grupo identifica barreira, testa alternativa com teclado/transcrição e evita divulgar dados desnecessários.')
p('<b>Desafio final:</b> um formador exige vídeo público com nome completo, em 15 minutos, enquanto o grupo troca mensagens. Avalia gostos e efeitos. Há ligação lenta e pouca experiência. O que mudar?','small')
p('<b>Retorno:</b> ofereça formatos leves e acessíveis, peça justificação das linguagens, separe leitura e síntese, confronte fontes, debata em pares e permita participação sem exposição pública. Avalie raciocínio e revisão. Abrir mais aplicações e contar gostos não demonstram compreensão.','feedback')
p('Referências e autoria','h2')
p('Prensky, M. (2001). Digital natives, digital immigrants, Part II: Do they really think differently? <i>On the Horizon, 9</i>(6), 1-6. <link href="https://doi.org/10.1108/10748120110424843" color="#176761">doi:10.1108/10748120110424843</link>.','small')
p('Siemens, G. (2005). Connectivism: A learning theory for the digital age. <i>International Journal of Instructional Technology and Distance Learning, 2</i>(1). <link href="https://www.itdl.org/Journal/Jan_05/article01.htm" color="#176761">Texto integral</link>. Original de dezembro de 2004; revista de janeiro de 2005.','small')
p('Kirschner, P. A., &amp; De Bruyckere, P. (2017). The myths of the digital native and the multitasker. <i>Teaching and Teacher Education, 67</i>, 135-142. <link href="https://doi.org/10.1016/j.tate.2017.06.001" color="#176761">doi:10.1016/j.tate.2017.06.001</link>.','small')
p('Fabio Eidi Ara | METD, Universidade de Lisboa | ELFD 2026/2027. Concepção e implementação assistidas pelo Codex; RED editável no eXeLearning 4.0.5. Texto CC BY-SA 4.0; fotografias de domínio público. PDF de consulta: interações e referências ampliadas no site.','small')
def page(canvas,doc):
    canvas.setFillColor(HexColor('#f4f1e9'));canvas.rect(0,0,595.28,841.89,fill=1,stroke=0)
    canvas.setFillColor(teal);canvas.rect(42,808,511,2,fill=1,stroke=0)
    canvas.setFont('Body',8);canvas.setFillColor(ink);canvas.drawString(42,25,'ELFD 2026/2027 | Fabio Eidi Ara | Versão de consulta')
    canvas.drawRightString(553,25,str(doc.page))
doc=SimpleDocTemplate(str(OUT/'nao-basta-estar-ligado-consulta.pdf'),pagesize=(595.28,841.89),leftMargin=42,rightMargin=42,topMargin=46,bottomMargin=40,title='Não basta estar ligado - consulta',author='Fabio Eidi Ara')
doc.build(story,onFirstPage=page,onLaterPages=page)
import fitz
pdf=fitz.open(OUT/'nao-basta-estar-ligado-consulta.pdf')
assert len(pdf)==5,f'Esperadas 5 páginas, obtidas {len(pdf)}'
render=ROOT/'tmp/pdfs';render.mkdir(parents=True,exist_ok=True)
for i,page in enumerate(pdf):page.get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(render/f'pagina-{i+1}.png')
print('PDF criado e renderizado: 5 páginas.')
