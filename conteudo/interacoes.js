/* Extensões didáticas locais: classificação e revisão de uma rede. Sem serviços externos. */
(() => {
  'use strict';
  const get = key => {try{return JSON.parse(sessionStorage.getItem('red-'+key));}catch{return null;}};
  const put = (key,value) => {try{sessionStorage.setItem('red-'+key,JSON.stringify(value));}catch{/* A experiência funciona também sem armazenamento. */}};
  const show = (id,html) => {const target=document.getElementById(id);if(target){target.hidden=false;target.innerHTML=html;}};
  function init(){
    document.documentElement.lang='pt-BR';
    const skip=document.getElementById('skipNav');if(skip)skip.textContent='Ir para o conteúdo';
    const nav=document.getElementById('siteNav');
    const restoreNav=()=>{if(nav?.inert)nav.inert=false;};
    if(nav)new MutationObserver(restoreNav).observe(nav,{attributes:true,attributeFilter:['inert']});
    window.addEventListener('load',restoreNav);restoreNav();
    const active=document.querySelector('#siteNav a.active');
    active?.setAttribute('aria-current','page');
    document.querySelector('#siteNav')?.setAttribute('aria-label','As cinco etapas da experiência');
    document.querySelector('.nav-button-left:not([aria-hidden])')?.setAttribute('aria-label','Etapa anterior');
    document.querySelector('.nav-button-right:not([aria-hidden])')?.setAttribute('aria-label','Próxima etapa');
    const classifications={
      a:{correct:'proposta',text:'É uma proposta pedagógica de Prensky (2001): aproximar o ensino das experiências digitais, com jogos digitais. Uma proposta não demonstra eficácia para todos os estudantes; a adequação ao objetivo e o efeito na aprendizagem precisam de avaliação.'},
      b:{correct:'hipotese',text:'É uma extrapolação que requer evidência. Prensky argumenta a favor de diferenças associadas à experiência, mas reconhece não ter observado diretamente os cérebros dos nativos para confirmar diferenças físicas. Isso não estabelece dois tipos de cérebro nem prova a superioridade da multitarefa. A frase transforma uma inferência em certeza e generaliza para toda uma geração.'},
      c:{correct:'critica',text:'É a conclusão crítica de Kirschner e De Bruyckere (2017). A investigação revista pelos autores não sustenta uma geração homogênea de especialistas digitais ou de multitarefadores eficazes. Isso não significa que nenhum jovem tenha competências: significa que é preciso observá-las, sem as deduzir da idade.'}
    };
    document.querySelectorAll('[data-classify]').forEach(select=>{
      const update=()=>{if(!select.value){document.getElementById('feedback-'+select.dataset.classify).hidden=true;return;}const item=classifications[select.dataset.classify];show('feedback-'+select.dataset.classify,`<strong>${select.value===item.correct?'Classificação fundamentada.':'Reveja o nível da afirmação.'}</strong> ${item.text}`);put('class-'+select.dataset.classify,select.value);};
      const saved=get('class-'+select.dataset.classify);if(saved){select.value=saved;update();}select.addEventListener('change',update);
    });
    if(document.querySelector('.network')){
      const notes={professor:'Professor: ajuda a definir a pergunta e os critérios de comparação. Limite: a sua autoridade não substitui evidência e pode deixar de fora experiências de estudantes.',colegas:'Colegas: revelam dificuldades e interpretações diferentes. Limite: experiências próximas podem repetir a mesma opinião; é preciso procurar contrapontos.',artigo:'Artigo científico: permite examinar método e resultados de um estudo. Limite: a amostra, a data e o contexto delimitam o que se pode concluir. Publicação científica não dispensa leitura crítica.',comunidade:'Comunidade de prática: reúne experiências de aplicação e condições de acesso. Limite: relatos úteis para o contexto não provam, por si só, um efeito geral.',base:'Base de dados: permite localizar outros estudos e atualizar a pesquisa. Limite: indexação e data recente não garantem qualidade; é necessário examinar cada trabalho.'};
      const selected=new Set(get('network')||[]);let examined=!!get('network-examined');
      const sync=()=>{document.querySelectorAll('[data-node]').forEach(button=>{const on=selected.has(button.dataset.node);button.setAttribute('aria-pressed',String(on));document.querySelector(`[data-edge="${button.dataset.node}"]`)?.classList.toggle('selected',on);});document.getElementById('network-count').textContent=examined?`${selected.size} conexões nesta revisão`:`${selected.size} de 3 conexões selecionadas`;put('network',[...selected]);};
      document.querySelectorAll('[data-node]').forEach(button=>button.addEventListener('click',()=>{const key=button.dataset.node;if(selected.has(key))selected.delete(key);else if(!examined&&selected.size>=3){show('node-insight','Para examinar a primeira decisão, mantenha três ligações. Desligue uma antes de escolher outra. '+notes[key]);return;}else selected.add(key);document.getElementById('node-insight').textContent=notes[key];document.getElementById('network-feedback').hidden=true;document.getElementById('revision-feedback').hidden=true;sync();}));
      const reveal=()=>{document.getElementById('network-update').hidden=false;document.getElementById('network-phase').textContent='Revisão da decisão';};
      document.getElementById('evaluate-network').addEventListener('click',()=>{
        if(!examined&&selected.size!==3){show('network-feedback','Escolha três conexões para poder comparar as suas funções. O número limita esta primeira exploração; não é uma medida de qualidade.');return;}
        if(selected.size===0){show('network-feedback','Estabeleça pelo menos uma conexão para examinar as suas possibilidades e os seus limites.');return;}
        const human=['professor','colegas','comunidade'].some(k=>selected.has(k));const research=selected.has('artigo')||selected.has('base');
        show('network-feedback',`<p><strong>${human&&research?'A rede combina investigação e perspectivas humanas.':human?'A rede reúne perspectivas humanas, mas falta confrontá-las com investigação.':'A rede permite procurar evidência, mas precisa de escutar o contexto de quem aprende.'}</strong> ${selected.has('base')?'A base permite atualizar a busca; cada resultado ainda precisa de avaliação.':'Uma nova busca pode revelar informação que as ligações atuais não trazem.'}</p><p>Esta escolha não prova que vídeos sejam melhores. É necessário comparar objetivos, métodos, limites e condições de acesso. Agora examine o que mudou.</p>`);
        examined=true;put('network-examined',true);reveal();sync();
      });
      document.getElementById('revise-network').addEventListener('click',()=>{
        const reason=document.getElementById('network-reason').value;put('network-reason',reason);
        if(!reason){show('revision-feedback','Escolha uma justificação para a sua revisão. Não basta alterar o desenho da rede.');return;}
        if(reason!=='atualizar'){show('revision-feedback',reason==='popular'?'Uma fonte muito partilhada pode repetir um erro. Compare evidências e condições da turma antes de decidir.':'Uma data recente não basta. Examine a qualidade e a pertinência da revisão antes de a usar. Atualizar é avaliar, não substituir automaticamente.');return;}
        if(!selected.has('base')||!['professor','colegas','comunidade'].some(k=>selected.has(k))){show('revision-feedback','A justificação é pertinente. Ajuste também as ligações: nesta simulação, a base permite atualizar a evidência; professor, colegas ou comunidade ajudam a confrontá-la com o contexto. Uma única fonte não cobre ambas as funções.');return;}
        show('revision-feedback','<strong>A revisão está fundamentada.</strong> Você combinou atualização da evidência com uma perspectiva humana e recusou uma regra universal. Uma decisão possível é combinar leituras e vídeos conforme o objetivo, testar uma alternativa acessível e rever a escolha com o grupo. Isso concretiza uma ideia de Siemens: manter conexões e decidir perante informação nova. Não há garantia automática de aprendizagem por ter mais ligações.');
      });
      const savedReason=get('network-reason');if(savedReason)document.getElementById('network-reason').value=savedReason;
      if(examined)reveal();sync();
    }
    // Complementa os formulários nativos com grupos nomeados e anúncios de feedback.
    // Observa apenas esta página; não transmite escolhas a qualquer serviço.
    function enhanceForms(){
      document.querySelectorAll('.FormView_question').forEach((question,i)=>{
        question.removeAttribute('draggable');question.setAttribute('role','group');
        const base=question.querySelector('.FormViewContainer');if(base){const p=base.querySelector('p');if(p){p.id=p.id||'pergunta-'+i;question.setAttribute('aria-labelledby',p.id);}}
      });
      document.querySelectorAll('.FormViewContainer_selection [title], .FormView_question .help-icon[title]').forEach(e=>e.setAttribute('title','Seleção com várias respostas possíveis'));
      document.querySelectorAll('.form-feedback-message').forEach(f=>{f.setAttribute('role','status');f.setAttribute('aria-live','polite');});
    }
    const observer=new MutationObserver(enhanceForms);observer.observe(document.querySelector('.page-content')||document.body,{childList:true,subtree:true});enhanceForms();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
