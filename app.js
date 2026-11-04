'use strict';
let base;
const conversation = document.querySelector('#conversation');
const query = document.querySelector('#query');
const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9\s]/g, ' ').replace(/\s+/g, ' ').trim();

function button(label, action, full = false) {
  const element = document.createElement('button');
  element.type = 'button';
  element.className = `choice${full ? ' question-choice' : ''}`;
  element.textContent = label;
  element.addEventListener('click', action);
  return element;
}
function message(text, user = false) {
  const row = document.createElement('div');
  row.className = `message${user ? ' user' : ''}`;
  if (!user) {
    const avatar = document.createElement('div');
    avatar.className = 'mini-avatar';
    const img = document.createElement('img');
    img.src = 'assets/ajudante.jpg'; img.alt = '';
    avatar.append(img); row.append(avatar);
  }
  const bubble = document.createElement('div');
  bubble.className = 'bubble'; bubble.textContent = text;
  row.append(bubble); conversation.append(row);
  return bubble;
}
function choices(bubble, items) {
  const group = document.createElement('div'); group.className = 'choices';
  items.forEach(item => group.append(button(item.label, item.action, item.full)));
  bubble.append(group); scrollChat();
}
function scrollChat() { conversation.scrollTop = conversation.scrollHeight; }
function menu() {
  choices(message(base.messages.menu), base.categories.map(category => ({label: category.label, action: () => showCategory(category.id)})));
}
function showCategory(id) {
  const category = base.categories.find(item => item.id === id);
  message(category.label, true);
  const items = base.questions.filter(item => item.category === id);
  choices(message(base.messages.choose), items.map(item => ({label:item.question, action: () => answer(item.id), full:true})));
}
function sourceLink(source) {
  const link = document.createElement('a');
  link.href = source.url; link.target = '_blank'; link.rel = 'noopener noreferrer';
  link.textContent = `${source.title} ↗`; return link;
}
function answer(id) {
  const item = base.questions.find(entry => entry.id === id);
  if (!item) return;
  message(item.question, true);
  const bubble = message(item.answer);
  const source = document.createElement('div'); source.className = 'source-link';
  source.append('Fonte: ', sourceLink(base.sources[item.source]));
  bubble.append(source);
  choices(bubble, [{label: 'Ver outra dúvida', action: menu}]);
}
function search(text) {
  const terms = [...new Set(normalize(text).split(' ').filter(term => term.length > 2 && !['que','qual','como','posso','para','uma','enem','quero','sobre','das','dos','tem','sao','com','por','nao'].includes(term)))];
  if (!terms.length) return [];
  return base.questions.map(item => {
    const corpus = normalize(`${item.question} ${item.keywords.join(' ')}`);
    const words = corpus.split(' ');
    const score = terms.filter(term => words.some(word => word === term || (term.length >= 4 && word.startsWith(term)))).length;
    return {item,score};
  }).filter(result => result.score > 0).sort((a,b) => b.score-a.score).slice(0,5).map(result => result.item);
}
function restart() {
  if (!base) return;
  conversation.replaceChildren();
  const label = document.createElement('p'); label.className = 'day-label'; label.textContent = 'SEU GUIA PARA O ENEM'; conversation.append(label);
  message(base.messages.welcome); menu(); query.value = '';
}
document.querySelector('#search-form').addEventListener('submit', event => {
  event.preventDefault();
  if (!base || !query.value.trim()) return;
  const text = query.value.trim(); query.value = ''; message(text, true);
  const results = search(text);
  const bubble = message(results.length ? base.messages.results : base.messages.unknown);
  choices(bubble, [...results.map(item => ({label:item.question,action:()=>answer(item.id),full:true})),{label:'Ver todos os assuntos',action:menu}]);
});
document.querySelector('#restart').addEventListener('click', restart);
document.querySelector('#sources').addEventListener('click', () => document.querySelector('#sources-dialog').showModal());
document.querySelector('#close-dialog').addEventListener('click', () => document.querySelector('#sources-dialog').close());

async function init() {
  try {
    const response = await fetch('data/perguntas.json', {cache:'no-cache'});
    if (!response.ok) throw new Error('Não foi possível carregar a base.');
    const data = await response.json();
    if (!Array.isArray(data.questions) || !data.questions.length || !data.messages || !Array.isArray(data.categories) || !data.sources) throw new Error('Base inválida.');
    const ids = new Set();
    for (const item of data.questions) {
      if (ids.has(item.id) || !item.question || !item.answer || !Array.isArray(item.keywords) || !data.categories.some(c=>c.id===item.category) || !data.sources[item.source]) throw new Error('Pergunta inválida.');
      ids.add(item.id);
    }
    for (const source of Object.values(data.sources)) {
      const url = new URL(source.url);
      if (url.protocol !== 'https:' || url.hostname !== 'www.gov.br') throw new Error('Fonte inválida.');
    }
    const today = new Intl.DateTimeFormat('sv-SE',{timeZone:'America/Sao_Paulo'}).format(new Date());
    if (today > data.validUntil) throw new Error('Esta base de 2026 precisa de revisão antes de novas consultas. Acesse as orientações atuais na Página do Participante.');
    base = data;
    query.disabled = false; document.querySelector('#send').disabled = false; document.querySelector('#sources').disabled = false;
    document.querySelector('#review').textContent = `Revisado em ${data.reviewedAt.split('-').reverse().join('/')}`;
    const list = document.querySelector('#source-list');
    Object.values(data.sources).forEach(source=>{const li=document.createElement('li');li.append(sourceLink(source));list.append(li);});
    restart();
  } catch (error) {
    conversation.replaceChildren();
    message(error.message.startsWith('Esta base') ? error.message : 'Não consegui carregar as perguntas. Abra este projeto por um servidor HTTP (veja o README), confira o arquivo data/perguntas.json e recarregue a página.');
    document.querySelector('#review').textContent = 'Consultas indisponíveis';
  }
}
function setupMascot() {
  const character = document.querySelector('.character');
  const characterNote = document.querySelector('.character-note');
  if (!character || !characterNote) return;

  const cheers = [
    'Vamos nessa!',
    'Foco nos estudos! 🎯',
    'Tô na torcida! 🎓',
    'Uma questão de cada vez! 📝',
    'Bora detonar no Enem! 🚀',
    'Você vai se sair bem! ✨'
  ];
  let cheerIndex = 0;

  character.setAttribute('role', 'button');
  character.setAttribute('tabindex', '0');
  character.setAttribute('aria-label', 'Clique para receber incentivo do mascote');

  const cheer = () => {
    cheerIndex = (cheerIndex + 1) % cheers.length;
    characterNote.textContent = cheers[cheerIndex];
    const img = character.querySelector('img');
    if (img) {
      img.classList.remove('mascot-cheer');
      void img.offsetWidth;
      img.classList.add('mascot-cheer');
    }
  };

  character.addEventListener('click', cheer);
  character.addEventListener('keydown', event => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      cheer();
    }
  });
}

setupMascot();
init();
