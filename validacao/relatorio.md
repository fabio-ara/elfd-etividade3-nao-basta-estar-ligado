# Relatório de validação

Recurso: **Não basta estar ligado**, Fabio Eidi Ara. Verificação em 23/10/2026, concluída após a publicação da revisão `3d36672` (cerca de 14h53 UTC). Endereço público: https://fabio-ara.github.io/elfd-etividade3-nao-basta-estar-ligado/.

## Resultado

Os requisitos funcionais do RED foram verificados. Há exatamente cinco páginas principais, seis práticas explícitas e atividades com feedback. O site público carrega sem login, com navegação direta e após recarregamento. O projeto foi importado, editado, exportado e reaberto no eXeLearning online 4.0.5.

| Verificação executada | Evidência e resultado |
|---|---|
| Publicação efetiva | GitHub Actions com sucesso; execução https://github.com/fabio-ara/elfd-etividade3-nao-basta-estar-ligado/actions/runs/39973160240. A URL pública foi aberta no Chrome em contexto isolado `red-publico-sem-login`. |
| Integridade HTTP | `scripts/validar-publicacao.py`: 89 arquivos públicos retornaram HTTP 200 e coincidiram com a exportação local (normalizando somente finais de linha em texto). Dados em `http-e-integridade.json`. |
| Cinco etapas | Cinco páginas no XML e no website, cinco ligações na navegação; referências e créditos estão dentro da etapa 5. |
| Etapa 1 | Escolha baseada em idade produziu retorno de revisão; selecionar origem, comparação independente e revisão fundamentada produziu retorno correto. O botão Reconsiderar reiniciou as escolhas. |
| Etapa 2 | Foram exercitadas as nove combinações de três frases e três categorias; todos os retornos explicativos apareceram conforme a categoria escolhida. A seleção também foi operada por Home, seta e Enter. |
| Etapa 3 | Testados limite inicial de três conexões, ausência de conexões suficientes, rede somente humana, atualização da evidência e necessidade de contexto. Justificações vazia, popularidade e novidade automática produziram orientação. Inclusão de base de dados, perspectiva humana e justificação adequada produziram revisão fundamentada. Space alternou um botão com `aria-pressed`. |
| Revisão da rede | Corrigido e retestado o descarte do feedback anterior após mudança das ligações. Teste final público confirmou o comportamento e o retorno da revisão, após atualização sem cache. |
| Etapa 4 | Três práticas com ação, finalidade e indicador; fotografia carregada. Botão nativo de feedback revelou a explicação sobre divisão de tarefas e construção conjunta. |
| Etapa 5 | Três práticas complementares; alternativa de multitarefa produziu retorno de revisão, medidas fundamentadas produziram explicação correta. Painéis de referências e créditos foram abertos. O formulário também foi testado após a correção de semântica acessível. |
| Conteúdo científico | Leitura das fontes e confronto com identificação editorial. DOIs de Prensky e Kirschner/De Bruyckere confirmados por Crossref (`identificacao-fontes.json`); texto primário de Siemens consultado na revista. Propostas, extrapolações e crítica estão distinguidas; os documentos da rede são explicitamente fictícios. |
| Imagens | Duas fotografias autênticas. Declarações individuais Commons e metadados preservados em `licenca-eniac.json` e `licenca-catalogo.json`; proveniência, direitos, cópias locais e textos alternativos em `../creditos-imagens.md`. Nenhuma imagem de IA. |
| Desktop e móvel | Inspeção visual pelo retorno nativo de screenshots do Chrome DevTools; 1365×900 e 390×844, além da capa a 1280×720. As cinco páginas foram examinadas; nenhuma rolagem horizontal no tamanho móvel. Formulários, imagem e rede mantiveram legibilidade. Dados complementares em `layout-mobile.json`. |
| Acessibilidade básica | Rótulos de campos, grupos nomeados, feedback anunciado, foco visível, seleção e botões por teclado. Auditoria Lighthouse em snapshot móvel da etapa 5: acessibilidade **100**, boas práticas **100**, nenhum audit falho. Report em `lighthouse-mobile-etapa5.json`. |
| Correções de acessibilidade | A primeira auditoria identificou contraste insuficiente do crédito nativo do eXe e grupo aplicado a um item de lista. O contraste foi reforçado e o grupo movido para o contêiner interno; nova auditoria não repetiu os problemas. |
| Console | Sem erros ou avisos nas consultas das páginas públicas feitas durante o percurso e na revisão final da rede. |
| Atualização da página | Recarregamento da página de práticas 4–6 preservou o carregamento do formulário com seis alternativas. Atualização sem cache da rede carregou a revisão publicada e as escolhas de sessão compatíveis. |
| Editabilidade | ELPX de entrada com DTD válido; importação real, edição do primeiro Texto e salvamento do iDevice. ELPX exportado foi reimportado e seu editor TinyMCE aberto, editável, com fotografia e texto preservados. Cinco páginas e dez componentes permaneceram no pacote. As últimas alterações foram no código personalizado, exportado pela mesma API oficial do editor. |
| Pacote final | DTD validado novamente; duas fotografias incorporadas com bytes idênticos aos originais locais; `screenshot.png` idêntico à captura real `capa1280.png`. O último ELPX foi reimportado novamente: título, autor, cinco páginas e ambas as correções no código personalizado foram confirmados. |
| PDF | Cinco páginas geradas com ReportLab, renderizadas com PyMuPDF e todas inspecionadas visualmente. Sem sobreposição ou conteúdo cortado. Contém síntese, retornos das atividades, seis práticas, referências e créditos; é consulta estática. |

## Instrumentos e limites

Chrome DevTools MCP foi utilizado para navegação, cliques, teclas, leitura da árvore de acessibilidade, emulação de dimensões, screenshots nativos e Lighthouse. Python fez validação HTTP sem credenciais, comparação dos recursos, verificação XML/DTD e produção/renderização do PDF. A exportação real foi executada pelo exportador oficial carregado no editor eXe; os bytes foram transferidos diretamente por uma ponte temporária de loopback, sem downloads pela interface. Essa ponte não faz parte do RED nem do repositório público.

O Computer Use nativo foi interrompido pelo próprio instrumento, que não conseguiu determinar a URL ativa com confiança para aplicar sua política. Não foi usado novamente. As verificações de navegador foram concluídas com Chrome DevTools, disponível e funcional. Algumas operações de screenshot/arquivo no MCP sofreram restrição de raiz; as capturas preservadas foram obtidas pelo retorno nativo em bytes e gravadas diretamente fora da interface. Não se usaram diálogos Salvar como nem mecanismos de download da UI.

O Lighthouse é um teste automatizado de uma amostra (etapa 5), não certificação WCAG. Não foi realizada auditoria completa com leitor de tela nem teste em todos os navegadores ou dispositivos físicos. A dimensão móvel foi emulada. As atividades exigem JavaScript; o PDF é alternativa de consulta sem interatividade. Os formulários nativos podem reiniciar no recarregamento; isso não impede novas tentativas. Os sites de editoras podem impor controles de acesso: o RED oferece DOIs corretos e caminhos institucionais de leitura, sem prometer acesso universal ao texto integral externo.

## Moodle e revisão do autor

O espaço de entrega foi consultado com a sessão autenticada, somente para verificar instruções, prazo e estado. Foi confirmado **23/10/2026 às 19h59 no fuso São Paulo**, equivalente a **23h59 em Lisboa**, enquanto o enunciado conserva referência anterior a 18/10. O estado observado foi “Ainda não foram submetidos trabalhos”.

O autor determinou expressamente que fará a avaliação e o envio manual. Nenhum arquivo, texto ou rascunho foi salvo no Moodle. `../entrega-moodle.txt` contém material pronto e o endereço correto da submissão. A única etapa de entrega pendente é a revisão e submissão pelo autor; publicar no GitHub não equivale a entregar no Moodle.
