# Não basta estar ligado

Uma experiência sobre gerações, redes e aprendizagem digital.

**[Abrir o RED](https://fabio-ara.github.io/elfd-etividade3-nao-basta-estar-ligado/)** · [Projeto editável](editavel/nao-basta-estar-ligado.elpx) · [PDF de consulta](output/pdf/nao-basta-estar-ligado-consulta.pdf)

Fabio Eidi Ara · Mestrado em Educação e Tecnologias Digitais, Universidade de Lisboa · E-learning e Formação a Distância, 2026/2027 · Módulo 2, Etividade 3.

## Objetivo e público

Microexperiência autônoma, de aproximadamente 12 minutos, para professores, formadores e estudantes adultos. A pergunta “Ter crescido rodeado de tecnologia significa saber aprender com ela?” conduz a escolhas sobre evidência, conceitos, conexões e práticas educativas. Não é um curso completo nem uma apresentação dos projetos pessoais do autor.

O participante não recebe uma pontuação: examina justificações, pode rever escolhas e precisa combinar atualização da evidência com perspectivas humanas. A rede inclui documentos fictícios, identificados como simulação; eles não são apresentados como estudos científicos reais.

## Cinco etapas

1. **O problema:** Lia e Rui, de gerações diferentes, precisam verificar uma mensagem. Formulário com seleção de evidências e retorno explicativo.
2. **Conceitos e crítica:** nativos e imigrantes digitais na proposta de Prensky; limites da generalização e classificação de proposta, extrapolação e crítica posterior.
3. **Aprender em rede:** conectivismo de Siemens; selecionar três conexões, examinar contribuições e limites, rever a rede perante informação nova.
4. **Práticas 1 a 3:** produção multimodal, aprendizagem colaborativa em rede, interatividade e feedback. Cada prática apresenta ação do educador, finalidade e indicador observável.
5. **Práticas 4 a 6:** reflexão e atenção sustentada, avaliação crítica das fontes, inclusão e ética digital. Desafio final, referências e créditos em painéis expansíveis, sem sexta página.

## Ferramenta e editabilidade

**Ferramenta efetivamente utilizada: eXeLearning online 4.0.5**, em https://online.exelearning.net/. O conteúdo inicial foi preparado por código conforme o formato oficial ODE 2.0 e um modelo oficial. Em seguida foi importado no editor, editado e salvo como conteúdo, exportado em ELPX e HTML5 e reaberto no editor. O pacote final não é uma simulação de arquivo eXe.

- `editavel/nao-basta-estar-ligado.elpx`: projeto canônico, com cinco páginas, dez componentes e recursos incorporados.
- `editavel/website-exportado.zip`: exportação HTML5 real do editor.
- `editavel/content.xml`: cópia do XML do pacote final, para inspeção.
- `editavel/estrutura.json`: especificação auxiliar de autoria; não substitui o ELPX final.
- `website/`: exportação web descompactada, publicada integralmente pelo GitHub Pages.
- `conteudo/`: textos, CSS e JavaScript autorais em UTF-8.
- `recursos/imagens/`: cópias locais das duas fotografias de domínio público.
- `output/pdf/`: versão estática de consulta, em cinco páginas.
- `validacao/`: relatório e evidências da verificação.

Os formulários das etapas 1 e 5 são iDevices **Formulário** nativos; a resposta da etapa 4 usa o feedback do iDevice **Texto**. A classificação e a rede são componentes funcionais em HTML/SVG/JavaScript, inseridos em iDevices Texto. Os textos e formulários podem ser editados no editor. Estruturas interativas devem ser alteradas pelo código-fonte HTML do iDevice; CSS e comportamento estão em **Propriedades do projeto → Código personalizado**. Evite remover IDs, atributos `data-*` e campos de feedback. Após alterações, exporte novamente e teste as interações.

Guia oficial: https://exelearning.github.io/exelearning/elpx-format/ai-generation/. Modelo: https://github.com/exelearning/exelearning/blob/main/test/fixtures/really-simple-test-project.elpx.

## Funcionamento e privacidade

Website estático, sem conta, backend, serviços dos projetos AraLearn/AraTalk/AraHub, chamadas de IA ou banco de dados. Os arquivos necessários à experiência ficam no próprio website; apenas as leituras externas exigem acesso aos respectivos sites. JavaScript é necessário para as atividades. As escolhas personalizadas usam `sessionStorage`; os formulários nativos podem reiniciar ao recarregar ou mudar a dimensão emulada. Não há envio de respostas nem análise de utilização adicionada pelo autor. O provedor de hospedagem recebe as solicitações usuais de acesso ao site.

Navegação entre cinco páginas HTML com caminhos relativos, acesso direto e atualização de página. Teclado, foco visível, rótulos, avisos de feedback e movimento reduzido foram considerados. Não se declara certificação WCAG nem teste completo com leitores de tela.

Para consulta local: `python -m http.server 8768 --directory website`, depois http://127.0.0.1:8768/. O site público dispensa qualquer instalação.

`scripts/gerar-projeto.py` permite reconstruir uma **entrada** ELPX usando o pacote preservado como base; depende de Python e lxml. Essa entrada ainda deve passar pelo editor e pela exportação oficial. `scripts/gerar-pdf.py` gera a versão de consulta com ReportLab e renderiza com PyMuPDF; usa fontes locais do Windows. Os scripts são auxiliares e não integram o funcionamento público do RED.

## Fundamentação

Prensky é apresentado como autor de uma distinção e de propostas pedagógicas; suas inferências sobre diferenças cerebrais não são convertidas em fatos demonstrados. O contraponto de Kirschner e De Bruyckere contextualiza a generalização geracional. O conectivismo é apresentado como a perspectiva teórica de Siemens, com diversidade, fontes especializadas, manutenção de conexões, atualização e decisão. A quantidade de conexões não é usada como medida de aprendizagem. Casos e seis práticas são elaboração pedagógica deste recurso.

- Prensky, M. (2001). Digital natives, digital immigrants, Part II: Do they really think differently? *On the Horizon, 9*(6), 1–6. https://doi.org/10.1108/10748120110424843
- Siemens, G. (2005). Connectivism: A learning theory for the digital age. *International Journal of Instructional Technology and Distance Learning, 2*(1). https://www.itdl.org/Journal/Jan_05/article01.htm. Texto original de dezembro de 2004; publicação na revista em janeiro de 2005.
- Kirschner, P. A., & De Bruyckere, P. (2017). The myths of the digital native and the multitasker. *Teaching and Teacher Education, 67*, 135–142. https://doi.org/10.1016/j.tate.2017.06.001

O workspace estava vazio no início. As leituras foram obtidas de versões verificáveis; os PDFs protegidos por direitos autorais usados na pesquisa não são redistribuídos neste repositório. As notas de verificação estão em [pesquisa/notas-fontes.md](pesquisa/notas-fontes.md).

## Direitos e autoria

Texto e código autorais: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), Fabio Eidi Ara. Concepção e implementação assistidas pelo Codex; revisão e submissão acadêmica sob responsabilidade do autor. Fotografias: domínio público, com declarações individuais verificadas; [créditos completos](creditos-imagens.md). Nenhuma imagem de IA foi utilizada. Componentes e ícones do software eXeLearning conservam suas licenças originais; ver https://github.com/exelearning/exelearning.

## Publicação e entrega

O workflow publica apenas `website/` no GitHub Pages; fontes, ELPX e PDF permanecem acessíveis neste repositório. O estado dos testes está em [validacao/relatorio.md](validacao/relatorio.md).

A submissão no Moodle é **manual, após revisão do autor**. Não foi enviado nem salvo rascunho no espaço institucional. Veja [entrega-moodle.txt](entrega-moodle.txt) para o texto e os passos preparados.
