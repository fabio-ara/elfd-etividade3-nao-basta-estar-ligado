/* Complementos dos iDevices nativos. As escolhas ficam apenas nesta sessão do navegador. */
(() => {
  'use strict';
  const get = key => { try { return JSON.parse(sessionStorage.getItem('red-revisao2-' + key)); } catch { return null; } };
  const put = (key, value) => { try { sessionStorage.setItem('red-revisao2-' + key, JSON.stringify(value)); } catch {} };
  function init() {
    document.documentElement.lang = 'pt-PT';
    const skip = document.getElementById('skipNav');
    if (skip) skip.textContent = 'Ir para o conteúdo';
    const nav = document.getElementById('siteNav');
    const restoreNav = () => { if (nav?.inert) nav.inert = false; };
    if (nav) new MutationObserver(restoreNav).observe(nav, {attributes:true, attributeFilter:['inert']});
    window.addEventListener('load', restoreNav);
    restoreNav();
    nav?.setAttribute('aria-label', 'Páginas do recurso');
    document.querySelector('#siteNav a.active')?.setAttribute('aria-current', 'page');
    const links = [...document.querySelectorAll('#siteNav a')];
    for (const [selector, prefix] of [['.nav-button-left', 'Anterior: '], ['.nav-button-right', 'Seguinte: ']]) {
      document.querySelectorAll(selector + ':not([aria-hidden="true"])').forEach(button => {
        const target = links.find(link => link.href === button.href);
        if (target) { button.textContent = prefix + target.textContent.trim(); button.setAttribute('aria-label', button.textContent); }
      });
    }
    const finalPage = links.at(-1);
    document.querySelectorAll('#siteFooter a[href="https://creativecommons.org/licenses/by-sa/4.0/"]').forEach(link => {
      link.textContent = 'CC BY-SA 4.0';
    });
    if (finalPage) document.querySelectorAll('[data-final-anchor]').forEach(link => {
      const target = new URL(finalPage.href);
      target.hash = link.dataset.finalAnchor;
      link.href = target.href;
    });
    const classifications = {
      a: {correct:'proposta', text:'É uma sugestão para o ensino. Prensky propôs usar jogos digitais para trabalhar os conteúdos das aulas. Ao escolher um jogo, o professor precisa de verificar se as tarefas ajudam os estudantes a compreender esse conteúdo.'},
      b: {correct:'hipotese', text:'É uma hipótese a investigar: sugere uma influência possível da experiência. Para a estudar, é necessário definir que experiências se comparam e observar como as pessoas aprendem. O argumento de Prensky sobre plasticidade cerebral não demonstrou as diferenças físicas que sugeria entre grupos.'},
      c: {correct:'critica', text:'É uma crítica à divisão por gerações. Kirschner e De Bruyckere questionaram a ideia de uma geração com capacidades digitais uniformes. Observar as tarefas que cada pessoa realiza permite conhecer diferenças que a idade não esclarece.'}
    };
    document.querySelectorAll('[data-classify]').forEach(select => {
      const item = classifications[select.dataset.classify];
      const feedback = document.getElementById('feedback-' + select.dataset.classify);
      const update = () => {
        feedback.hidden = !select.value;
        feedback.textContent = select.value ? (select.value === item.correct ? '' : 'Considere o que a frase faz: recomenda uma ação, propõe uma relação a estudar ou questiona uma generalização. ') + item.text : '';
        put('class-' + select.dataset.classify, select.value);
      };
      const saved = get('class-' + select.dataset.classify);
      if ([...select.options].some(option => option.value === saved)) select.value = saved;
      update();
      select.addEventListener('change', update);
    });
    if (document.querySelector('.network')) {
      const order = ['professor', 'colegas', 'artigo', 'base', 'comunidade'];
      const saved = get('network');
      const selected = new Set((Array.isArray(saved) ? saved : []).filter(key => order.includes(key)).slice(0, 3));
      let compared = false;
      const feedback = document.getElementById('network-feedback');
      const limit = document.getElementById('network-limit');
      const comparisons = {
        'professor|colegas|artigo': [
          'O professor ajuda a definir o que se pretende aprender, os colegas descrevem as suas experiências e o artigo permite examinar como uma investigação avaliou a aprendizagem. Compare o conteúdo estudado, as atividades realizadas e a forma de avaliar a compreensão.',
          'A seguir, procure outra pesquisa sobre a mesma pergunta e verifique se os seus resultados se aplicam às condições descritas pelos colegas.'
        ],
        'professor|colegas|base': [
          'O professor ajuda a formular a pergunta, os colegas identificam dificuldades concretas e a base de dados permite procurar pesquisas sobre essas dificuldades. Os relatos ajudam a escolher palavras e situações relevantes para a pesquisa.',
          'Selecione um artigo encontrado na base. Leia o que foi comparado e como se avaliou a aprendizagem antes de decidir quando usar texto ou vídeo.'
        ],
        'professor|colegas|comunidade': [
          'O professor relaciona os materiais com os objetivos, os colegas descrevem o estudo e a comunidade acrescenta experiências de outras aulas. Confronte as condições em que cada relato ocorreu: o conteúdo, a tarefa e a forma de acompanhar a compreensão.',
          'Procure agora uma investigação sobre uma das situações relatadas. Compare os seus resultados com as observações do grupo.'
        ],
        'professor|artigo|base': [
          'O professor ajuda a definir uma tarefa de aprendizagem, o artigo apresenta um estudo e a base permite encontrar pesquisas que o confirmem, completem ou questionem. Compare os métodos e os resultados dos trabalhos encontrados.',
          'Converse também com estudantes sobre as suas condições de acesso e dificuldades. Use essa informação para planear uma atividade que permita observar o que compreenderam.'
        ],
        'professor|artigo|comunidade': [
          'O professor ajuda a escolher o que avaliar, o artigo mostra como uma pesquisa o investigou e a comunidade apresenta experiências de aplicação. Compare a atividade do estudo com as tarefas descritas pelos profissionais.',
          'Procure outras pesquisas e verifique as condições de acesso do grupo. Depois, experimente um material com uma tarefa de compreensão adequada ao objetivo.'
        ],
        'professor|base|comunidade': [
          'O professor ajuda a formular o objetivo, a comunidade apresenta situações de ensino e a base permite localizar investigações relacionadas. Os relatos podem tornar a pergunta de pesquisa mais precisa.',
          'Escolha uma investigação e leia quem participou e como se avaliou a aprendizagem. Confronte esses elementos com as condições das aulas relatadas.'
        ],
        'colegas|artigo|base': [
          'Os colegas descrevem experiências, o artigo permite examinar uma investigação e a base ajuda a encontrar outros trabalhos. Compare as dificuldades relatadas com as tarefas e os participantes de cada estudo.',
          'Peça ao professor que ajude a relacionar o que encontrou com o objetivo de aprendizagem. Definam uma tarefa comum para comparar a compreensão após o texto e o vídeo.'
        ],
        'colegas|artigo|comunidade': [
          'Os colegas e a comunidade trazem experiências de contextos diferentes. O artigo permite confrontar esses relatos com uma investigação. Examine se estudavam conteúdos semelhantes e como acompanharam a aprendizagem.',
          'Pesquise outros estudos sobre a pergunta que ficou em aberto. Registe a data, o contexto e os resultados que justificariam rever a escolha dos materiais.'
        ],
        'colegas|base|comunidade': [
          'Os colegas e a comunidade ajudam a identificar dificuldades e possibilidades de uso. A base de dados permite procurar pesquisas sobre essas situações, em vez de decidir apenas pela frequência dos relatos.',
          'Leia um estudo encontrado e examine como foi avaliada a compreensão. Discuta com o grupo se essa avaliação corresponde ao que pretende aprender.'
        ],
        'artigo|base|comunidade': [
          'O artigo apresenta uma investigação, a base permite acompanhar outras pesquisas e a comunidade acrescenta experiências de aplicação. Compare os resultados publicados com as condições das atividades relatadas.',
          'Escute os estudantes e peça orientação ao professor para definir uma tarefa de compreensão. Use-a para acompanhar o que aprendem com os materiais e rever a decisão.'
        ]
      };
      const compare = () => {
        feedback.hidden = false;
        feedback.replaceChildren();
        const paragraphs = selected.size === 3
          ? comparisons[order.filter(key => selected.has(key)).join('|')]
          : ['Escolha três fontes para comparar as suas contribuições.'];
        for (const text of paragraphs) { const p = document.createElement('p'); p.textContent = text; feedback.append(p); }
      };
      const sync = () => {
        document.querySelectorAll('[data-node]').forEach(button => {
          const on = selected.has(button.dataset.node);
          button.setAttribute('aria-pressed', String(on));
          button.querySelector('.selection-mark').textContent = on ? '✓ Selecionada' : '';
          document.querySelector('[data-edge="' + button.dataset.node + '"]')?.classList.toggle('selected', on);
        });
        document.querySelectorAll('[data-source-note]').forEach(note => { note.hidden = !selected.has(note.dataset.sourceNote); });
        document.getElementById('network-count').textContent = selected.size + ' de 3 fontes escolhidas';
        put('network', order.filter(key => selected.has(key)));
        if (compared) compare();
      };
      document.querySelectorAll('[data-node]').forEach(button => button.addEventListener('click', () => {
        const key = button.dataset.node;
        if (selected.has(key)) selected.delete(key);
        else if (selected.size === 3) {
          limit.textContent = 'Já escolheu três fontes. Retire uma para acrescentar outra.';
          return;
        } else selected.add(key);
        limit.textContent = '';
        sync();
      }));
      document.getElementById('evaluate-network').addEventListener('click', () => { compared = true; compare(); });
      sync();
    }
    function enhanceForms() {
      document.querySelectorAll('.FormView_question').forEach((question, i) => {
        question.removeAttribute('draggable');
        question.removeAttribute('role');
        question.removeAttribute('aria-labelledby');
        const base = question.querySelector('.FormViewContainer');
        const heading = base?.querySelector('h2, p');
        if (heading) {
          heading.id ||= 'pergunta-' + i;
          base.setAttribute('role', 'group');
          base.setAttribute('aria-labelledby', heading.id);
        }
      });
      document.querySelectorAll('.FormViewContainer_selection [title], .FormView_question .help-icon[title]').forEach(e => e.setAttribute('title', 'Seleção com várias respostas possíveis'));
      document.querySelectorAll('.form-feedback-message, .feedback.js-feedback').forEach(f => { f.setAttribute('role', 'status'); f.setAttribute('aria-live', 'polite'); });
    }
    new MutationObserver(enhanceForms).observe(document.querySelector('.page-content') || document.body, {childList:true, subtree:true});
    enhanceForms();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
