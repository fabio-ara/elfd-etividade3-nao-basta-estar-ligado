# Como aprendemos com a tecnologia?

Recurso educativo de Fabio Eidi Ara para E-learning e Formação a Distância, 2026/2027, Mestrado em Educação e Tecnologias Digitais, Instituto de Educação, Universidade de Lisboa. Módulo 2, Etividade 3.

## Revisão local

Esta revisão atualiza a escrita, as atividades, a rede e a apresentação. **Não foi publicada nem submetida no Moodle.** O endereço público da versão anterior permanece inalterado e não representa esta revisão.

Para abrir a versão revista, execute na raiz:

```powershell
python -m http.server 8768 --bind 127.0.0.1 --directory website
```

Depois abra http://127.0.0.1:8768/. Não é necessário iniciar sessão.

## Objetivo e público

O recurso destina-se a professores, formadores e estudantes adultos. Distingue a proposta de Prensky das hipóteses sobre os efeitos da experiência digital e da crítica posterior. Apresenta o conectivismo de Siemens através da escolha e comparação de fontes. As seis práticas mantêm a divisão do enunciado: três exploram possibilidades da participação digital; três desenvolvem atenção, avaliação crítica e inclusão.

1. **Início:** Ana e Estevão avaliam uma afirmação sobre estudar com várias aplicações abertas.
2. **Gerações digitais:** conceitos de Prensky, plasticidade cerebral, vídeo com Gary Small, investigação e crítica. Classificação de três ideias.
3. **Aprender em rede:** seleção de três fontes, explicações individuais e comparação das suas contribuições.
4. **Criar e colaborar:** produção multimodal, construção em grupo e aprendizagem com feedback.
5. **Atenção e inclusão:** leitura atenta, verificação das fontes e participação acessível. Desafio final, referências e autoria.

## Ficheiros

- `editavel/nao-basta-estar-ligado.elpx`: projeto editável final, com cinco páginas e nove componentes.
- `editavel/website-exportado.zip`: exportação HTML5 efetivamente produzida pelo eXeLearning.
- `website/`: a mesma exportação, descompactada, com os recursos necessários.
- `editavel/content.xml`: XML extraído do projeto final.
- `editavel/estrutura.json`: especificação auxiliar de autoria.
- `conteudo/`: conteúdos HTML e extensões CSS/JavaScript que alimentam a reconstrução.
- `recursos/imagens/computacao.jpg`: fotografia histórica utilizada. O catálogo de fichas da versão anterior deixou de integrar o recurso.
- `output/pdf/nao-basta-estar-ligado-consulta.pdf`: consulta estática das cinco etapas em seis páginas, incluindo explicações e referências.
- `creditos-imagens.md`: proveniência e direitos da fotografia.
- `pesquisa/notas-fontes.md`: registo de conferência das leituras.
- `validacao/relatorio.md`: resultados e limites dos testes desta revisão.

Os nomes dos ficheiros editáveis foram conservados para manter a continuidade do projeto. O título apresentado ao estudante é "Como aprendemos com a tecnologia?".

## Ferramenta e nova exportação

Foi utilizado o **eXeLearning online 4.0.5**, em https://online.exelearning.net/. O projeto foi importado, aberto para edição num iDevice Texto e guardado no editor. Os ficheiros ELPX e HTML5 resultam dos exportadores reais da ferramenta. O ELPX final foi reaberto para confirmar a estrutura.

Os questionários inicial e final usam o iDevice **Formulário**. A resposta do trabalho de grupo usa o feedback do iDevice **Texto**. A classificação e a rede usam HTML, SVG e JavaScript em iDevices Texto. Não foi acrescentada uma biblioteca.

No editor, altere textos e perguntas nos respetivos iDevices. Para a rede e a classificação, preserve os IDs e atributos `data-*` do HTML. O CSS e o JavaScript encontram-se em **Propriedades do projeto, Código personalizado**. Depois de editar, exporte novamente como website e teste.

Para reconstruir a partir dos ficheiros de origem:

1. Execute `python scripts/gerar-projeto.py` (Python e lxml).
2. Importe `tmp/entrada.elpx` no eXeLearning. Este pacote é uma entrada de autoria, não a exportação final.
3. Exporte pelo eXeLearning para atualizar os dois ficheiros finais e descompacte o website.
4. Execute `python scripts/gerar-pdf.py` para atualizar a consulta (ReportLab e fontes Arial/Georgia do Windows).
5. Execute `python scripts/validar-publicacao.py` com o servidor local ativo. Apesar do nome histórico, este verificador usa apenas o endereço local por omissão.

Documentação: [formato ELPX](https://exelearning.github.io/exelearning/elpx-format/) e [guia oficial de geração](https://exelearning.github.io/exelearning/elpx-format/ai-generation/). A entrada usa o contrato ODE 2.0 e um modelo oficial, seguido de importação e exportação no editor.

## Interações e privacidade

Há um único conjunto de fontes selecionadas na rede. Esse conjunto determina os destaques, a contagem, as explicações e a comparação. O limite é sempre três; todas as dez combinações têm uma apreciação específica e uma ação para continuar a pesquisa. As fontes são tipos de documentos e interlocutores, sem estudos ou resultados fictícios.

As escolhas personalizadas podem permanecer em `sessionStorage` durante a sessão. Os formulários nativos reiniciam ao voltar à página. A experiência funciona também sem armazenamento. Não são enviados resultados, não há conta, serviços de IA, base de dados ou dependência dos projetos pessoais do autor. As leituras e o vídeo abrem nos respetivos sites e podem estar sujeitos às condições desses sites.

## Fundamentação e direitos

As referências completas estão no último ecrã. Foram utilizados Prensky (2001), Siemens (2005, texto de 2004), Kirschner e De Bruyckere (2017), o vídeo da CBS com Gary Small (2008) e o estudo de Small e colegas (2009). Os resultados sobre atividade cerebral não são apresentados como prova de melhor aprendizagem ou de diferenças entre gerações. Os exemplos de práticas são propostas deste recurso, com as relações teóricas indicadas junto das passagens relevantes.

Texto sob CC BY-SA 4.0. Fotografia do ENIAC em domínio público nos Estados Unidos (PD-USGov-Military-Army). O software e os recursos de interface do eXeLearning conservam os seus avisos e licenças. Não foram utilizadas imagens geradas por IA. A assistência técnica e editorial foi realizada com Codex; a revisão académica e a submissão ficam a cargo do autor.

Não se declara certificação de acessibilidade nem teste integral com leitores de ecrã. Os testes efetivamente realizados estão descritos no relatório.
