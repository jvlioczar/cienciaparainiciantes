// Interações do site: busca, menu, progresso, testes, filtros e ferramentas.
(function () {
  var base = document.body.dataset.base || '';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var norm = function (s) { return String(s).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); };
  /* busca: o nome vem antes da descrição (0 nome igual, 1 começa, 2 palavra, 3 trecho, 4 só no resto) */
  var pontua = function (titulo, t) {
    var n = norm(titulo).trim();
    if (n === t) return 0;
    if (n.indexOf(t) === 0) return 1;
    if (n.split(/[^a-z0-9]+/).some(function (w) { return w.indexOf(t) === 0; })) return 2;
    return n.indexOf(t) >= 0 ? 3 : 4;
  };
  var ordena = function (raiz, cards, t) {
    t = t.trim();
    cards.forEach(function (c, i) { if (!c._casa) { c._casa = c.parentNode; c._pos = i; } });
    cards.forEach(function (c) { if (c.parentNode !== c._casa) c._casa.appendChild(c); });
    cards.slice().sort(function (a, b) { return a._pos - b._pos; }).forEach(function (c) { c._casa.appendChild(c); });
    var rb = raiz._rb;
    if (rb) rb.hidden = true;
    if (!t) return;
    var vis = cards.filter(function (c) { return !c.hidden; }).map(function (c) { var h = c.querySelector('h3'); return { c: c, p: pontua(h ? h.textContent : c.textContent, t) }; });
    vis.sort(function (a, b) { return a.p - b.p || a.c._pos - b.c._pos; });
    var unica = cards.every(function (c) { return c._casa === cards[0]._casa; });
    if (unica) { vis.forEach(function (x) { x.c._casa.appendChild(x.c); }); return; }
    if (!rb) { rb = raiz._rb = document.createElement('div'); rb.className = 'grade res-busca'; raiz.insertBefore(rb, raiz.firstChild); }
    rb.hidden = false;
    vis.forEach(function (x) { rb.appendChild(x.c); });
  };
  var el = function (t, a, tx) { var e = document.createElement(t); if (a) Object.keys(a).forEach(function (k) { e.setAttribute(k, a[k]); }); if (tx != null) e.textContent = tx; return e; };
  var ler = function (k, d) { try { return JSON.parse(localStorage.getItem(k)) || d; } catch (x) { return d; } };
  var grava = function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (x) {} };

  /* menu */
  var hamb = $('.hamb'), menu = $('.menu');
  if (hamb) hamb.addEventListener('click', function () { menu.classList.toggle('aberto'); hamb.setAttribute('aria-expanded', menu.classList.contains('aberto')); });
  var drops = $$('.drop');
  function fechaMenus(fora) { drops.forEach(function (d) { if (d !== fora) { $('.mega', d).hidden = true; $('button', d).setAttribute('aria-expanded', 'false'); } }); }
  drops.forEach(function (d) {
    var b = $('button', d), m = $('.mega', d);
    b.addEventListener('click', function (e) { e.stopPropagation(); fechaMenus(d); m.hidden = !m.hidden; b.setAttribute('aria-expanded', !m.hidden); });
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.drop')) fechaMenus(); });

  /* busca */
  var ov = $('#busca'), q = $('#q'), res = $('#res'), dados = null;
  function abre() { ov.hidden = false; q.value = ''; res.textContent = ''; q.focus(); if (!dados) fetch(base + 'assets/busca.json').then(function (r) { return r.json(); }).then(function (j) { dados = j; }); }
  function fecha() { ov.hidden = true; }
  $$('.bbusca').forEach(function (b) { b.addEventListener('click', abre); });
  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); abre(); }
    if (e.key === 'Escape') { fecha(); fechaMenus(); }
  });
  if (ov) {
    ov.addEventListener('click', function (e) { if (e.target === ov) fecha(); });
    q.addEventListener('input', function () {
      var t = norm(q.value.trim()); res.textContent = '';
      if (t.length < 2 || !dados) return;
      var a = dados.filter(function (d) { return norm(d.t + ' ' + d.d).indexOf(t) >= 0; }).map(function (d, i) { return { d: d, p: pontua(d.t, t), i: i }; }).sort(function (x, y) { return x.p - y.p || x.i - y.i; }).slice(0, 9).map(function (x) { return x.d; });
      if (!a.length) res.appendChild(el('p', null, 'Nada encontrado.'));
      a.forEach(function (d) { var l = el('a', { href: base + d.u }, d.t); l.appendChild(el('small', null, d.d)); res.appendChild(l); });
    });
    q.addEventListener('keydown', function (e) { if (e.key === 'Enter') { var a = $('a', res); if (a) location.href = a.href; } });
  }

  /* progresso das lições */
  var lidas = ler('cpi-lidas', []);
  var marca = $('.marcar');
  function pinta() {
    $$('[data-licao]').forEach(function (c) { c.classList.toggle('lido', lidas.indexOf(c.dataset.licao) >= 0); });
    $$('[data-ponto]').forEach(function (c) { c.classList.toggle('lida', lidas.indexOf(c.dataset.ponto) >= 0); });
    $$('[data-prog]').forEach(function (p) {
      var ids = p.dataset.prog.split(','), n = ids.filter(function (i) { return lidas.indexOf(i) >= 0; }).length;
      $('i', p).style.width = (n / ids.length * 100) + '%';
      var t = $('[data-prog-t="' + p.id + '"]'); if (t) t.textContent = n + ' de ' + ids.length + ' lições lidas';
    });
  }
  if (marca) {
    var id = marca.dataset.id, est = function () { var on = lidas.indexOf(id) >= 0; marca.setAttribute('aria-pressed', on); marca.textContent = on ? '✓ Lição lida' : 'Marcar como lida'; };
    marca.addEventListener('click', function () { var i = lidas.indexOf(id); if (i >= 0) lidas.splice(i, 1); else lidas.push(id); grava('cpi-lidas', lidas); est(); pinta(); });
    est();
  }
  pinta();

  /* setas do teclado entre as lições */
  if ($('.indice')) document.addEventListener('keydown', function (e) {
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    if (e.ctrlKey || e.metaKey || e.altKey || e.shiftKey) return;
    if (e.target.closest('input,textarea,select,[contenteditable],.tabela')) return;
    var a = $(e.key === 'ArrowLeft' ? '.indice-seta[rel=prev]' : '.indice-seta[rel=next]');
    if (a) location.href = a.href;
  });

  /* sumário */
  var toc = $('.toc');
  if (toc) {
    $$('.leitura h2').forEach(function (h, i) { if (h.closest('.fontes')) return; h.id = h.id || 's' + i; var li = el('li'); li.appendChild(el('a', { href: '#' + h.id }, h.textContent)); toc.appendChild(li); });
    if (!toc.children.length) toc.closest('.caixa').hidden = true;
  }

  /* pergunta com alternativas */
  function pergunta(raiz, texto, ops, certo, expl, depois) {
    raiz.textContent = '';
    raiz.appendChild(el('p', { class: 'q' }, texto));
    var box = el('div', { class: 'ops' }), fb = el('p', { class: 'fb', role: 'status' });
    ops.forEach(function (o, i) {
      var b = el('button', { type: 'button' }, o);
      b.addEventListener('click', function () {
        if (certo < 0) return;
        $$('button', box).forEach(function (x, j) { x.disabled = true; if (j === certo) x.classList.add('certo'); });
        var ok = i === certo; if (!ok) b.classList.add('errado');
        fb.textContent = (ok ? 'Isso! ' : 'Quase. ') + expl;
        if (depois) depois(ok);
      });
      box.appendChild(b);
    });
    raiz.appendChild(box); raiz.appendChild(fb);
  }
  /* placar da página de revisão: conta respondidas e acertos */
  var placar = $('#placar-rev'), respondidas = 0, acertos = 0;
  function somaPlacar(ok) {
    respondidas++; if (ok) acertos++;
    placar.textContent = 'Placar: ' + acertos + ' acerto' + (acertos === 1 ? '' : 's') + ' em ' + respondidas + ' respondida' + (respondidas === 1 ? '' : 's') + ', de ' + placar.dataset.total + ' perguntas.' + (respondidas >= +placar.dataset.total ? (acertos >= .8 * respondidas ? ' Muito bem: você está pronto para o próximo nível.' : ' Volte às lições em que errou e tente de novo.') : '');
  }
  $$('[data-quiz]').forEach(function (z) { var d = JSON.parse(z.dataset.quiz); pergunta($('.alvo', z), d[0], d[1], d[2], d[3], placar ? somaPlacar : null); });
  function jogo(raiz, itens, opsDe, certoDe, textoDe, explDe) {
    var i = 0, pts = 0, alvo = $('.alvo', raiz), plc = $('.placar', raiz), bar = $('.barra-prog i', raiz), prox = $('.prox-q', raiz);
    function mostra() {
      plc.firstChild.textContent = 'Pergunta ' + (i + 1) + ' de ' + itens.length; plc.lastChild.textContent = pts + ' acertos';
      bar.style.width = (i / itens.length * 100) + '%'; prox.hidden = true;
      var it = itens[i], ops = opsDe(it);
      pergunta(alvo, textoDe(it), ops, ops.indexOf(certoDe(it)), explDe(it), function (ok) { if (ok) pts++; plc.lastChild.textContent = pts + ' acertos'; prox.hidden = false; prox.textContent = i + 1 < itens.length ? 'Próxima' : 'Ver resultado'; });
    }
    prox.addEventListener('click', function () {
      i++;
      if (i < itens.length) return mostra();
      bar.style.width = '100%'; prox.hidden = true; alvo.textContent = '';
      alvo.appendChild(el('p', { class: 'q' }, 'Você acertou ' + pts + ' de ' + itens.length + '.'));
      var de = el('button', { class: 'btn', type: 'button' }, 'Jogar de novo'); de.addEventListener('click', function () { i = 0; pts = 0; mostra(); }); alvo.appendChild(de);
    });
    mostra();
  }
  var dj = $('#dados-jogo');
  if (dj) {
    var J = JSON.parse(dj.textContent);
    if (J.tipo === 'opcoes') jogo($('#jogo'), J.itens, function () { return J.ops; }, function (x) { return x[1]; }, function (x) { return x[0]; }, function (x) { return x[2]; });
    if (J.tipo === 'frases') jogo($('#jogo'), J.itens, function () { return ['Fato', 'Valor']; }, function (x) { return x[1]; }, function (x) { return '“' + x[0] + '”'; }, function (x) { return x[2]; });
  }

  /* catálogo */
  var cat = $('#catalogo');
  if (cat) {
    var cs = $$('.cartao', cat), busca = $('#fq'), cont = $('#contagem'), f = { tema: '', nivel: '' }, u = new URLSearchParams(location.search);
    f.tema = u.get('tema') || ''; f.nivel = u.get('nivel') || '';
    var aplicaC = function () {
      var t = norm(busca.value), n = 0;
      cs.forEach(function (c) { var ok = (!f.tema || c.dataset.temas.split(' ').indexOf(f.tema) >= 0) && (!f.nivel || c.dataset.nivel === f.nivel) && norm(c.textContent).indexOf(t) >= 0; c.hidden = !ok; if (ok) n++; });
      ordena(cat, cs, t);
      cont.textContent = n + (n === 1 ? ' item' : ' itens');
      $$('.filtros button').forEach(function (b) { b.setAttribute('aria-pressed', f[b.dataset.k] === b.dataset.v); });
    };
    busca.addEventListener('input', aplicaC);
    $$('.filtros button').forEach(function (b) { b.addEventListener('click', function () { f[b.dataset.k] = b.dataset.v; aplicaC(); }); });
    aplicaC();
  }

  /* listas com filtro por grupo e busca (correntes, pensadores, pseudociências, debates) */
  var lst = $('#lista');
  if (lst) {
    var lc = $$('.item', lst), lg = $$('.grupo-l', lst), lq = $('#fq'), lcnt = $('#contagem'), lf = {};
    var aplicaL = function () {
      var t = norm(lq ? lq.value : ''), n = 0;
      lc.forEach(function (c) { var ok = Object.keys(lf).every(function (k) { return !lf[k] || c.dataset[k] === lf[k]; }) && norm(c.textContent).indexOf(t) >= 0; c.hidden = !ok; if (ok) n++; });
      ordena(lst, lc, t);
      lg.forEach(function (g) { g.hidden = !$$('.item', g).some(function (c) { return !c.hidden; }); });
      if (lcnt) lcnt.textContent = n + (n === 1 ? ' item' : ' itens');
    };
    if (lq) lq.addEventListener('input', aplicaL);
    $$('.filtros button').forEach(function (b) { b.addEventListener('click', function () { lf[b.dataset.k] = b.dataset.v; $$('.filtros button[data-k="' + b.dataset.k + '"]').forEach(function (o) { o.setAttribute('aria-pressed', o === b); }); aplicaL(); }); });
    aplicaL();
  }

  /* comparador de correntes */
  var dt = $('#dados-teo');
  if (dt) {
    var TD = JSON.parse(dt.textContent), ts = [$('#ta'), $('#tb'), $('#tc')], tini = ['empirismo', 'falsificacionismo', 'paradigmas'];
    var compT = function () {
      var ps = ts.map(function (s) { return TD.filter(function (x) { return x.s === s.value; })[0]; }), tb = $('#tcomp'); tb.textContent = '';
      var h = el('thead'), tr = el('tr'); tr.appendChild(el('th')); ps.forEach(function (p) { var th = el('th'); th.appendChild(el('a', { href: 'correntes/' + p.s + '.html' }, p.n)); tr.appendChild(th); }); h.appendChild(tr); tb.appendChild(h);
      var bd = el('tbody');
      [['Família', 'f'], ['O que põe no centro', 'foco'], ['Ideia central', 'i'], ['Diante da astrologia', 'astro'], ['Pontos fortes', 'forte'], ['Objeções', 'contra'], ['Referências', 'p']].forEach(function (c) { var l = el('tr'); l.appendChild(el('td', null, c[0])); ps.forEach(function (p) { var v = p[c[1]]; l.appendChild(el('td', null, Array.isArray(v) ? v.join(' ') : v)); }); bd.appendChild(l); });
      tb.appendChild(bd);
    };
    ts.forEach(function (s, i) { TD.forEach(function (x) { s.appendChild(el('option', { value: x.s }, x.n)); }); s.value = tini[i]; s.addEventListener('change', compT); });
    compT();
  }

  /* teste de troca */
  var tr = $('#troca');
  if (tr) {
    var C = JSON.parse($('#dados-troca').textContent), ct = 0, r1 = null;
    var cena = $('.cena', tr), ops = $('.ops', tr), msg = $('.fb', tr), prox2 = $('.prox-q', tr);
    function etapa(lado) {
      var c = C[ct]; cena.textContent = c[0].replace('{a}', lado === 0 ? c[3] : c[4]);
      ops.textContent = ''; msg.textContent = ''; prox2.hidden = true;
      [c[1], c[2]].forEach(function (o, i) {
        var b = el('button', { type: 'button' }, o);
        b.addEventListener('click', function () {
          if (lado === 0) { r1 = i; etapa(1); return; }
          msg.textContent = r1 === i ? 'Você julgou os dois casos do mesmo jeito. É isso que a imparcialidade pede: a regra vale, não importa quem está nela.' : 'Você julgou o mesmo ato de duas formas. É assim que o raciocínio motivado funciona, e acontece com todo mundo. A pergunta é: qual diferença entre os dois casos justifica a mudança?';
          $$('button', ops).forEach(function (x) { x.disabled = true; }); prox2.hidden = false;
        });
        ops.appendChild(b);
      });
    }
    prox2.addEventListener('click', function () { ct = (ct + 1) % C.length; etapa(0); });
    etapa(0);
  }

  /* o bonde: variantes, escolha e o que cada teoria tende a dizer */
  var bd = $('#bonde');
  if (bd) {
    var B = JSON.parse($('#dados-bonde').textContent), bi = 0, resp = [];
    var bcena = $('.cena', bd), bops = $('.ops', bd), bfb = $('.saida', bd), bprox = $('.prox-q', bd), bplc = $('.placar', bd);
    function mostraB() {
      var v = B[bi]; bplc.firstChild.textContent = 'Caso ' + (bi + 1) + ' de ' + B.length; bplc.lastChild.textContent = v.n;
      bcena.textContent = v.cena; bops.textContent = ''; bfb.textContent = ''; bprox.hidden = true;
      [v.sim, v.nao].forEach(function (o, i) {
        var b = el('button', { type: 'button' }, o);
        b.addEventListener('click', function () {
          resp[bi] = i; $$('button', bops).forEach(function (x) { x.disabled = true; }); b.classList.add('certo');
          bfb.appendChild(el('p', { class: 'q' }, i === 0 ? 'Você agiu. ' + v.pct : 'Você não agiu. ' + v.pct));
          var tb = el('table'), tbody = el('tbody');
          v.teorias.forEach(function (t) { var trr = el('tr'); var td = el('td'); td.appendChild(el('a', { href: base + 'teorias/' + t[0] + '.html' }, t[1])); trr.appendChild(td); trr.appendChild(el('td', null, t[2])); tbody.appendChild(trr); });
          tb.appendChild(tbody); var wrap = el('div', { class: 'tabela' }); wrap.appendChild(tb); bfb.appendChild(wrap);
          bprox.hidden = false; bprox.textContent = bi + 1 < B.length ? 'Próximo caso' : 'Ver o padrão';
        });
        bops.appendChild(b);
      });
    }
    bprox.addEventListener('click', function () {
      bi++;
      if (bi < B.length) return mostraB();
      bcena.textContent = 'O que suas respostas sugerem'; bops.textContent = ''; bfb.textContent = ''; bprox.hidden = true;
      var agiu = resp.filter(function (x) { return x === 0; }).length, lista = el('ul');
      B.forEach(function (v, i) { lista.appendChild(el('li', null, v.n + ': ' + (resp[i] === 0 ? v.sim : v.nao))); });
      var txt = agiu === B.length ? 'Você escolheu agir em todos os casos, mesmo quando o dano era direto e pessoal. É o padrão mais próximo do consequencialismo de ato: o que pesa é o número de vidas, não a forma do ato.' : agiu === 0 ? 'Você escolheu não agir em nenhum caso. É um padrão compatível com uma deontologia forte: há coisas que não se fazem, mesmo para salvar mais vidas. Vale perguntar se deixar morrer é mesmo tão diferente de matar.' : 'Você agiu em alguns casos e não em outros. É o padrão da maioria das pessoas, e é o que torna o bonde interessante: a diferença costuma estar em usar alguém como meio, em causar o dano com as próprias mãos ou em ter certeza do resultado. Qual dessas diferenças você acha que justifica mudar a resposta?';
      bfb.appendChild(el('p', { class: 'q' }, txt)); bfb.appendChild(lista);
      var de = el('button', { class: 'btn', type: 'button' }, 'Recomeçar'); de.addEventListener('click', function () { bi = 0; resp = []; mostraB(); }); bfb.appendChild(de);
    });
    mostraB();
  }

  /* véu da ignorância */
  var veu = $('#veu');
  if (veu) {
    var VD2 = JSON.parse($('#dados-veu').textContent), sel = $('#veu-soc'), esp = $('#veu-esp'), out = $('#veu-res'), hist = $('#veu-hist'), reg = [];
    VD2.sociedades.forEach(function (s, i) { sel.appendChild(el('option', { value: i }, s.n)); });
    var desc = $('#veu-desc'), tab = $('#veu-tab');
    function mostraS() {
      var s = VD2.sociedades[sel.value]; desc.textContent = s.d; tab.textContent = '';
      var soma = 0, pior = 101;
      s.pos.forEach(function (p) { soma += p[1] * p[2] / 100; if (p[1] < pior) pior = p[1]; var tr = el('tr'); tr.appendChild(el('td', null, p[0])); tr.appendChild(el('td', null, p[2] + '%')); var td = el('td'); var b = el('span', { class: 'vtrilho', style: 'display:inline-block;width:120px;vertical-align:middle;margin-right:6px' }); var i = el('i', { class: 'vs', style: 'width:' + p[1] + '%' }); b.appendChild(i); td.appendChild(b); td.appendChild(document.createTextNode(p[1])); tr.appendChild(td); tab.appendChild(tr); });
      $('#veu-media').textContent = soma.toFixed(0); $('#veu-pior').textContent = pior;
    }
    sel.addEventListener('change', mostraS); mostraS();
    $('#veu-nascer').addEventListener('click', function () {
      var s = VD2.sociedades[sel.value], r = Math.random() * 100, acc = 0, pos = s.pos[s.pos.length - 1];
      for (var i = 0; i < s.pos.length; i++) { acc += s.pos[i][2]; if (r < acc) { pos = s.pos[i]; break; } }
      var txt = 'Você nasceu como ' + pos[0].toLowerCase() + ' na ' + s.n.split(':')[0] + ': bem-estar ' + pos[1] + ' de 100.';
      if (esp.checked) {
        var r2 = Math.random() * 100, acc2 = 0, e2 = VD2.especies[0];
        for (var j = 0; j < VD2.especies.length; j++) { acc2 += VD2.especies[j][1]; if (r2 < acc2) { e2 = VD2.especies[j]; break; } }
        if (e2[0] !== 'Humano') { var b2 = VD2.bem_esp[e2[0]]; txt = 'Com a espécie sob o véu, você nasceu como ' + e2[0].toLowerCase() + ': bem-estar ' + b2 + ' de 100, em qualquer das sociedades, porque nenhuma delas conta os animais. Sem saber a espécie, que regras você teria escolhido?'; pos = [e2[0], b2]; }
        else txt = 'Com a espécie sob o véu, você nasceu humano, como ' + pos[0].toLowerCase() + ': bem-estar ' + pos[1] + ' de 100. Desta vez. A maioria dos seres que nascem não é humana.';
      }
      out.textContent = txt; reg.push(pos[1]);
      var m = reg.reduce(function (a, b) { return a + b; }, 0) / reg.length;
      hist.textContent = reg.length + (reg.length === 1 ? ' nascimento' : ' nascimentos') + ' · bem-estar médio ' + m.toFixed(0) + ' · pior ' + Math.min.apply(null, reg) + ' · melhor ' + Math.max.apply(null, reg);
    });
    $('#veu-zera').addEventListener('click', function () { reg = []; out.textContent = ''; hist.textContent = ''; });
  }

  /* equilíbrio reflexivo */
  var er = $('#er');
  if (er) {
    var ERD = JSON.parse($('#dados-er').textContent), juiz = {}, passo = 0, alvoE = $('.alvo', er), proxE = $('.prox-q', er);
    function casoE() {
      var c = ERD.casos[passo];
      pergunta(alvoE, 'Caso ' + (passo + 1) + ' de ' + ERD.casos.length + ': ' + c.t, [c.sim, c.nao], -1, '', null);
      $$('button', alvoE).forEach(function (b, i) { b.addEventListener('click', function () { juiz[c.k] = i === 0 ? 'sim' : 'nao'; $$('button', alvoE).forEach(function (x) { x.disabled = true; }); b.classList.add('certo'); proxE.hidden = false; }); });
      $('.fb', alvoE).textContent = ''; proxE.hidden = true; proxE.textContent = passo + 1 < ERD.casos.length ? 'Próximo caso' : 'Ver o resultado';
    }
    proxE.addEventListener('click', function () {
      passo++;
      if (passo < ERD.casos.length) return casoE();
      proxE.hidden = true; alvoE.textContent = '';
      alvoE.appendChild(el('p', { class: 'q' }, 'Seus juízos e os princípios'));
      var lista = ERD.principios.map(function (p) { var ok = 0, dif = []; ERD.casos.forEach(function (c) { if (p.pred[c.k] === juiz[c.k]) ok++; else dif.push(c.t); }); return { p: p, ok: ok, dif: dif }; }).sort(function (a, b) { return b.ok - a.ok; });
      var ul = el('ul'); lista.forEach(function (x) { var li = el('li'); li.appendChild(el('strong', null, x.p.n + ' ')); li.appendChild(document.createTextNode('concorda com ' + x.ok + ' de ' + ERD.casos.length + ' dos seus juízos.')); if (x.dif.length && x.ok >= ERD.casos.length - 3) { var s = el('small', { style: 'display:block;color:var(--suave)' }, 'Diverge em: ' + x.dif.join(' · ')); li.appendChild(s); } ul.appendChild(li); });
      alvoE.appendChild(ul);
      var ten = []; ERD.pares.forEach(function (pr) { if (juiz[pr[0]] && juiz[pr[1]] && juiz[pr[0]] !== juiz[pr[1]]) ten.push(pr[2]); });
      if (ten.length) { alvoE.appendChild(el('p', { class: 'q', style: 'margin-top:1rem' }, 'Tensões a examinar')); ten.forEach(function (t) { alvoE.appendChild(el('p', { class: 'fb' }, t)); }); }
      else alvoE.appendChild(el('p', { class: 'fb' }, 'Seus juízos nos pares críticos foram coerentes entre si. O próximo passo é ver se o princípio que mais concorda com você também o convence nos casos em que diverge.'));
      alvoE.appendChild(el('p', { class: 'fb' }, 'O equilíbrio reflexivo é ajustar os dois lados: rever um juízo quando o princípio convence, e rever o princípio quando o juízo resiste. Nenhum dos dois manda sozinho.'));
      var de = el('button', { class: 'btn', type: 'button' }, 'Recomeçar'); de.addEventListener('click', function () { passo = 0; juiz = {}; casoE(); }); alvoE.appendChild(de);
    });
    casoE();
  }

  /* monte seu círculo moral */
  var cm = $('#circulo');
  if (cm) {
    var caixas = $$('input[type=checkbox]', cm), rad = $$('input[type=radio]', cm), saida = $('#circulo-res'), anel = $('#circulo-anel');
    var calc = function () {
      var m = {}; caixas.forEach(function (c) { m[c.value] = c.checked; });
      var grad = ($('input[name=grad]:checked', cm) || {}).value, temp = ($('input[name=temp]:checked', cm) || {}).value;
      var nome, expl, nada = !m.humanos && !m.animais && !m.ia && !m.vida && !m.eco;
      if (nada) { nome = 'Nenhuma consideração moral direta'; expl = 'Você não marcou ninguém. Quase ninguém sustenta isso na prática: até o egoísta cuida de si mesmo. Marque ao menos uma opção.'; }
      else if (m.animais) {
        var pleno = grad === 'nao' && temp === 'nao';
        nome = (pleno ? 'Sencientismo pleno' : 'Sencientismo parcial') + (m.ia ? '' : ' (carbonismo)');
        var det = [];
        if (grad === 'sim') det.push('gradualista: a inteligência muda o peso do sofrimento');
        if (temp === 'sim') det.push('temporalista: o presente pesa mais do que o futuro');
        if (!m.ia) det.push('carbonismo: só mentes biológicas contam, mesmo que uma máquina venha a sentir');
        if (m.eco) nome += ' e holismo ecológico';
        expl = 'Quem pode sentir, conta' + (det.length ? ', com ressalvas (' + det.join('; ') + ')' : ', sem ressalvas: a dor conta igual, seja de quem for, agora ou no futuro') + '.' + (m.eco ? ' Ecossistemas também contam por si mesmos, e não só pelos seres que vivem neles.' : '') + (m.vida ? ' Você marcou também a vida orgânica sem senciência, o que puxa a posição para o biocentrismo.' : '');
      }
      else if (m.humanos && !m.vida && !m.eco && !m.ia) { nome = 'Antropocentrismo exclusivo'; expl = 'Só humanos contam de forma direta. Animais só entram na conta pelo efeito sobre pessoas. É a posição de boa parte da tradição ocidental, e a mais contestada hoje: o que há nos humanos, e falta nos outros animais, que justifica a fronteira exatamente na espécie?'; }
      else if (m.humanos && m.vida && !m.eco) { nome = 'Antropocentrismo biocêntrico'; expl = 'Humanos e todo ser vivo contam, mas os animais sencientes não ganham peso especial por sentirem. Uma combinação incomum: ela coloca uma bactéria e um porco no mesmo degrau, abaixo do humano.'; }
      else if (m.vida && !m.humanos && !m.eco) { nome = 'Biocentrismo'; expl = 'Toda vida conta por si mesma, e humanos não são a referência. É a posição de Albert Schweitzer e Paul Taylor. A dificuldade está em dizer o que uma planta tem a perder, e em dar peso igual a seres que sentem e a seres que não sentem.'; }
      else if (m.humanos && m.eco && !m.vida) { nome = 'Antropocentrismo com preocupação ecológica'; expl = 'Humanos contam, e ecossistemas também, mas os animais sencientes só contam como parte do todo. Há uma tensão aqui: um ecossistema não sente nada, e os animais que vivem nele sentem.'; }
      else if (m.eco && !m.humanos && !m.vida) { nome = 'Ecocentrismo / holismo ambiental'; expl = 'Ecossistemas contam por si mesmos, acima dos indivíduos. É a ética da terra de Aldo Leopold. Aviso de tensão: você deu consideração ao todo, mas não a nenhum ser que sente. Quem sofre quando a floresta queima são os animais, e eles ficaram de fora.'; }
      else if (m.ia && !m.humanos && !m.animais) { nome = 'Pluralismo moral atípico'; expl = 'Você incluiu mentes artificiais sem incluir humanos nem animais. Uma combinação rara, que vale revisar: se o critério é poder sentir, por que ele valeria para máquinas e não para quem já sente?'; }
      else { nome = 'Pluralismo moral atípico'; expl = 'Uma combinação pouco comum. Ela pode fazer sentido, mas vale explicar o critério: o que as opções marcadas têm em comum, que as não marcadas não têm?'; }
      saida.textContent = ''; saida.appendChild(el('p', { class: 'q' }, nome)); saida.appendChild(el('p', null, expl));
      if (anel) { var n = [m.humanos || m.animais, m.animais, m.ia, m.vida, m.eco].filter(Boolean).length; $$('i', anel).forEach(function (x, i) { x.style.opacity = i < n ? 1 : .15; }); }
    };
    caixas.concat(rad).forEach(function (i) { i.addEventListener('change', function () { if (this.value === 'animais' && this.checked) { var h = caixas.filter(function (c) { return c.value === 'humanos'; })[0]; if (h) h.checked = true; } $('#circulo-extra').hidden = !caixas.filter(function (c) { return c.value === 'animais'; })[0].checked; calc(); }); });
    calc();
  }

  /* data das marcações (para a revisão espaçada) */
  if (marca) marca.addEventListener('click', function () { var tt = ler('cpi-lidas-t', {}); var id = marca.dataset.id; if (lidas.indexOf(id) >= 0) tt[id] = Date.now(); else delete tt[id]; grava('cpi-lidas-t', tt); });

  /* revisão espaçada nos hubs de nível */
  var rev = $('.revisao');
  if (rev) {
    var tt2 = ler('cpi-lidas-t', {}), todas = $$('.cartao[data-licao]').filter(function (c) { return !c.closest('.revisao'); });
    var lidasAqui = todas.filter(function (c) { return lidas.indexOf(c.dataset.licao) >= 0; });
    if (lidasAqui.length >= 3) {
      lidasAqui.sort(function (a, b) { return (tt2[a.dataset.licao] || 0) - (tt2[b.dataset.licao] || 0); });
      var rg = $('#rev-grade'); lidasAqui.slice(0, 3).forEach(function (c) { rg.appendChild(c.cloneNode(true)); });
      rev.hidden = false;
    }
  }

  /* teste do nível: dez perguntas sorteadas */
  var dtn = $('#dados-teste');
  if (dtn && $('#jogo')) {
    var TN = JSON.parse(dtn.textContent), its = TN.itens.slice().sort(function () { return Math.random() - .5; }).slice(0, TN.n);
    jogo($('#jogo'), its, function (x) { return x[1]; }, function (x) { return x[1][x[2]]; }, function (x) { return x[0]; }, function (x) { return x[3]; });
  }

  /* posição antes e depois, nos debates */
  var posB = $$('.posicao');
  if (posB.length) {
    var PP = ler('cpi-pos', {});
    posB.forEach(function (b) {
      var s = b.dataset.deb, dep = b.classList.contains('depois'), fb = $('.fb', b), bts = $$('button', b), k = dep ? 1 : 0;
      var pinta2 = function () { var cur = PP[s] || [null, null]; bts.forEach(function (x) { x.setAttribute('aria-pressed', String(x.dataset.v === cur[k])); }); };
      bts.forEach(function (x) {
        x.addEventListener('click', function () {
          var cur = PP[s] || [null, null]; cur[k] = x.dataset.v; PP[s] = cur; grava('cpi-pos', PP); pinta2();
          if (!dep) { fb.textContent = 'Registrado. Leia os lados e responda de novo no fim da página.'; return; }
          var a = cur[0];
          if (a === null) fb.textContent = 'Você não registrou a posição antes de ler. Da próxima vez, tente: comparar o antes e o depois é o exercício.';
          else if (a === x.dataset.v) fb.textContent = x.dataset.v === 'ns' ? 'Você continua sem posição. Pode ser que o debate esteja em aberto, ou que falte informação. Anote o que faria você decidir.' : 'Você manteve a posição. Pergunte-se: qual foi o melhor argumento do outro lado, e por que ele não bastou?';
          else fb.textContent = 'Você mudou de posição depois de ler. É o que a abertura moral pede quando o argumento convence; vale checar se mudou por razão ou por cansaço.';
        });
      });
      pinta2();
      if (dep) { var c0 = (PP[s] || [null])[0]; if (c0 !== null) { var r = bts.filter(function (x) { return x.dataset.v === c0; })[0]; if (r) fb.textContent = 'Antes de ler, você pendia para: ' + r.textContent + '.'; } }
    });
  }

  /* minha posição */
  var mpd = $('#dados-mp');
  if (mpd) {
    var MP = JSON.parse(mpd.textContent), sel = {}, salvo = ler('cpi-minha', {});
    var opc = function (id, lista, vazio) { var s = $('#' + id); s.appendChild(el('option', { value: '' }, vazio)); lista.forEach(function (o) { s.appendChild(el('option', { value: o[0] }, o[1])); }); if (salvo[id]) s.value = salvo[id]; sel[id] = s; };
    var porFam = function (fs) { return MP.teo.filter(function (t) { return fs.indexOf(t.f) >= 0; }).map(function (t) { return [t.s, t.n]; }); };
    opc('mp-teoria', porFam(MP.fam.teo), 'Escolha uma teoria normativa');
    opc('mp-circulo', porFam(['Círculo moral']), 'Escolha quem conta');
    opc('mp-padrao', [['universal', 'Sim: há um padrão que vale para todos'], ['egoismo-etico', 'Cada um deve cuidar de si (egoísmo ético)'], ['relativismo-cultural', 'Cada cultura tem o seu (relativismo)'], ['ceticismo-normativo', 'Nenhum juízo é mais justificado (ceticismo)']], 'Há um padrão comum?');
    opc('mp-meta', porFam(MP.fam.met), 'Escolha uma metaética');
    opc('mp-abertura', [['revisa', 'Reavalio com calma e mudo se não achar o erro'], ['resiste', 'Procuro qualquer saída para manter a posição'], ['cede', 'Mudo na hora e volto atrás depois']], 'Como você reage?');
    var saida = $('#mp-saida');
    var teoDe = function (s) { return MP.teo.filter(function (t) { return t.s === s; })[0]; };
    var monta = function () {
      var v = {}; Object.keys(sel).forEach(function (k) { v[k] = sel[k].value; }); grava('cpi-minha', v); saida.textContent = '';
      var p = el('div', { class: 'nota' }); var frag = [];
      var t = teoDe(v['mp-teoria']); if (t) { frag.push('Sobre como agir, você se vê no '); frag.push(el('a', { href: base + 'teorias/' + t.s + '.html' }, t.n)); frag.push(': ' + t.foco.charAt(0).toLowerCase() + t.foco.slice(1) + ' ' ); }
      var c = teoDe(v['mp-circulo']); if (c) { frag.push('Sobre quem conta: '); frag.push(el('a', { href: base + 'teorias/' + c.s + '.html' }, c.n)); frag.push('. '); }
      if (v['mp-padrao']) { if (v['mp-padrao'] === 'universal') frag.push('Você aceita que há um padrão válido para todos, o que torna o desacordo moral um desacordo real, com respostas melhores e piores. '); else { var pd = teoDe(v['mp-padrao']); frag.push('Você duvida de um padrão comum: '); frag.push(el('a', { href: base + 'teorias/' + pd.s + '.html' }, pd.n)); frag.push('. Veja as objeções na página da posição. '); } }
      var m = teoDe(v['mp-meta']); if (m) { frag.push('Sobre o que é um juízo moral: '); frag.push(el('a', { href: base + 'teorias/' + m.s + '.html' }, m.n)); frag.push('. '); }
      if (v['mp-abertura']) frag.push({ revisa: 'Diante de um bom argumento contrário, você revisa: é o perfil que a lição sobre abertura moral descreve como raro e desejável.', resiste: 'Diante de um bom argumento contrário, você resiste: vale ler a lição sobre abertura moral e perguntar o que faria você mudar de ideia.', cede: 'Diante de um bom argumento contrário, você cede na hora: a lição sobre abertura moral sugere revisar com tempo, para que a mudança seja por razão.' }[v['mp-abertura']]);
      if (!frag.length) { p.textContent = 'Escolha as opções acima. O resumo aparece aqui e fica salvo no seu navegador.'; saida.appendChild(p); return; }
      frag.forEach(function (x) { p.appendChild(typeof x === 'string' ? document.createTextNode(x) : x); }); saida.appendChild(p);
      var ds = []; [t, c, m].forEach(function (x) { if (x && MP.deb[x.s]) MP.deb[x.s].forEach(function (d) { if (!ds.some(function (y) { return y[0] === d[0]; })) ds.push(d); }); });
      if (ds.length) { var h = el('p', null, 'Debates que testam essa posição: '); ds.slice(0, 6).forEach(function (d, i) { if (i) h.appendChild(document.createTextNode(', ')); h.appendChild(el('a', { href: base + 'debates/' + d[0] + '.html' }, d[1])); }); h.appendChild(document.createTextNode('.')); saida.appendChild(h); }
      if (t && c && t.s === 'utilitarismo-classico' && c.s === 'antropocentrismo') saida.appendChild(el('p', { class: 'legenda' }, 'Atenção: o utilitarismo conta todo bem-estar, e o antropocentrismo exclui os animais; a combinação é tensa. Veja a lição sobre especismo.'));
    };
    Object.keys(sel).forEach(function (k) { sel[k].addEventListener('change', monta); }); monta();
  }

  /* detector de pseudociência: soma os sinais marcados */
  var ddt = $('#dados-detector');
  if (ddt) {
    var DT = JSON.parse(ddt.textContent), caixaD = $('#detector .itens'), saidaD = $('#detector .saida'), totalD = DT.reduce(function (a, x) { return a + x[1]; }, 0);
    var contaD = function () {
      var pts = 0, n = 0; $$('input', caixaD).forEach(function (c) { if (c.checked) { pts += DT[+c.value][1]; n++; } });
      var p = pts / totalD, msg;
      if (!n) msg = 'Nenhum sinal marcado. Isso não prova que funciona: ainda é preciso evidência a favor, de preferência revisões sistemáticas.';
      else if (p < .2) msg = n + (n > 1 ? ' sinais' : ' sinal') + ' de alerta. Pouco, mas vale procurar estudos com grupo controle antes de confiar.';
      else if (p < .45) msg = n + ' sinais de alerta. Desconfie: procure o que dizem revisões sistemáticas e órgãos de saúde ou de ciência.';
      else msg = n + ' sinais de alerta. É o perfil típico de pseudociência. Antes de gastar dinheiro ou trocar um tratamento, procure uma avaliação independente.';
      saidaD.textContent = msg;
    };
    DT.forEach(function (x, i) { var lb = el('label', { class: 'chk' }); var inp = el('input', { type: 'checkbox', value: String(i) }); lb.appendChild(inp); lb.appendChild(el('span', null, x[0])); caixaD.appendChild(lb); inp.addEventListener('change', contaD); });
    contaD();
  }

  /* glossário: toque abre a definição */
  function posGl(g) { var r = g.getBoundingClientRect(), vw = document.documentElement.clientWidth, w = Math.min(320, vw - 32); g.style.setProperty('--gl-w', w + 'px'); g.style.setProperty('--gl-x', Math.min(0, vw - 16 - r.left - w) + 'px'); }
  function fechaGl() { $$('.gl.ativo').forEach(function (o) { o.classList.remove('ativo'); o.blur(); }); }
  $$('.gl').forEach(function (g) {
    g.addEventListener('mouseenter', function () { posGl(g); });
    g.addEventListener('focus', function () { posGl(g); });
    g.addEventListener('click', function (ev) { ev.stopPropagation(); posGl(g); var on = g.classList.contains('ativo'); fechaGl(); if (!on) g.classList.add('ativo'); });
  });
  document.addEventListener('click', fechaGl);
  document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') fechaGl(); });
})();

/* home: mede a altura das barras acima da capa para que ela ocupe a primeira tela (CSS usa --topo-capa) */
(function () {
  var c = document.querySelector('.capa'); if (!c) return;
  function mede() { document.documentElement.style.setProperty('--topo-capa', Math.round(c.getBoundingClientRect().top + window.scrollY) + 'px'); }
  mede(); window.addEventListener('load', mede); window.addEventListener('resize', mede);
})();

/* barra da página: ouvir (voz em pt-BR), como citar e imprimir ou PDF, adaptado do Questão de Ética */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var acoes = $('.acoes-cap'), raiz = $('.leitura');
  if (!acoes || !raiz) return;
  var dlg = null;
  function modal(titulo, html) {
    if (!dlg) {
      dlg = document.createElement('dialog'); dlg.className = 'janela';
      dlg.innerHTML = '<div class="jan-cab"><h2></h2><button type="button" class="jan-x" aria-label="Fechar">×</button></div><div class="jan-corpo"></div>';
      document.body.appendChild(dlg);
      $('.jan-x', dlg).addEventListener('click', function () { dlg.close(); });
      dlg.addEventListener('click', function (ev) { if (ev.target === dlg) dlg.close(); });
    }
    $('h2', dlg).textContent = titulo; $('.jan-corpo', dlg).innerHTML = html;
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', '');
    return $('.jan-corpo', dlg);
  }
  function copiar(txt, btn) {
    var ok = function () { if (btn) { var o = btn.textContent; btn.textContent = 'Copiado ✓'; setTimeout(function () { btn.textContent = o; }, 1600); } };
    if (navigator.clipboard) navigator.clipboard.writeText(txt).then(ok, function () {});
    else { var t = document.createElement('textarea'); t.value = txt; document.body.appendChild(t); t.select(); try { document.execCommand('copy'); ok(); } catch (x) {} t.parentNode.removeChild(t); }
  }

  /* ----- imprimir: abre as gavetas fechadas antes de imprimir e as devolve depois ----- */
  window.addEventListener('beforeprint', function () { $$('details', raiz).forEach(function (d) { d.dataset.antes = d.open ? '1' : ''; d.open = true; }); });
  window.addEventListener('afterprint', function () { $$('details', raiz).forEach(function (d) { d.open = d.dataset.antes === '1'; }); });
  $('[data-acao="imprimir"]', acoes).addEventListener('click', function () { window.print(); });

  /* ----- como citar ----- */
  var MES = ['jan.', 'fev.', 'mar.', 'abr.', 'maio', 'jun.', 'jul.', 'ago.', 'set.', 'out.', 'nov.', 'dez.'];
  $('[data-acao="citar"]', acoes).addEventListener('click', function () {
    var d = new Date(), hoje = d.getDate() + ' ' + MES[d.getMonth()] + ' ' + d.getFullYear();
    var abnt = (acoes.dataset.abnt || '').replace('{ACESSO}', hoje), apa = acoes.dataset.apa || '';
    var limpo = function (h) { var t = document.createElement('div'); t.innerHTML = h; return t.textContent; };
    var c = modal('Como citar esta página', '<p class="fino">Referência da página, com o link e a data de acesso de hoje. Confira as normas exigidas pela sua instituição.</p>' +
      '<div class="cit-bloco"><p class="cit-ti">ABNT</p><p class="cit-txt">' + abnt + '</p><button type="button" class="btn alt" data-c="abnt">Copiar ABNT</button></div>' +
      '<div class="cit-bloco"><p class="cit-ti">APA</p><p class="cit-txt">' + apa + '</p><button type="button" class="btn alt" data-c="apa">Copiar APA</button></div>');
    $('[data-c="abnt"]', c).addEventListener('click', function () { copiar(limpo(abnt), this); });
    $('[data-c="apa"]', c).addEventListener('click', function () { copiar(limpo(apa), this); });
  });

  /* ----- ouvir ----- */
  var bOuvir = $('[data-acao="ouvir"]', acoes);
  if (!('speechSynthesis' in window)) { bOuvir.hidden = true; return; }
  var synth = window.speechSynthesis, fila = [], pos = 0, tocando = false, vel = 1, atual = null;
  var bParar = document.createElement('button'); bParar.type = 'button'; bParar.innerHTML = '<span aria-hidden="true">■</span> Parar'; bParar.hidden = true;
  var bVel = document.createElement('button'); bVel.type = 'button'; bVel.textContent = '1×'; bVel.title = 'Velocidade da leitura'; bVel.hidden = true;
  bOuvir.after(bParar, bVel);
  /* escolhe uma voz em português do Brasil; as vozes chegam depois do carregamento em vários navegadores */
  var vozPt = null;
  var escolheVoz = function () {
    var vs = synth.getVoices(); if (!vs.length) return;
    var nota = function (v) {
      var l = (v.lang || '').replace('_', '-').toLowerCase(), n = (v.name || '').toLowerCase();
      if (l !== 'pt-br' && !/portugu[eê]s.*brasil|brazil/.test(n)) return l.indexOf('pt') === 0 ? 1 : 0;
      return 10 + (/natural|online|neural/.test(n) ? 4 : 0) + (/google/.test(n) ? 3 : 0) + (/microsoft/.test(n) ? 2 : 0) + (v.localService ? 0 : 1);
    };
    var melhor = vs.map(function (v) { return [nota(v), v]; }).filter(function (x) { return x[0] > 0; }).sort(function (a, b) { return b[0] - a[0]; })[0];
    vozPt = melhor ? melhor[1] : null;
  };
  escolheVoz();
  if ('onvoiceschanged' in synth) synth.addEventListener('voiceschanged', escolheVoz);
  var voz = function () { if (!vozPt) escolheVoz(); return vozPt; };
  /* o que é lido: o texto da coluna de leitura, sem quizzes, fontes, índices, enquetes, botões e tabelas */
  var PULA = '.quiz, .fontes, .pager, .nota.cruzada, .marcar, .toc, .toc-caixa, .posicao, .links-d, .legenda, table, button, nav';
  var monta = function () {
    fila = [];
    $$('h2, h3, h4, p, li, blockquote, dt, dd', raiz).forEach(function (b) {
      if (b.closest(PULA)) return;
      if (b.tagName === 'LI' && b.querySelector('p, li')) return; /* evita ler duas vezes */
      var c = b.cloneNode(true); $$('sup, button', c).forEach(function (s) { s.parentNode.removeChild(s); });
      var t = c.textContent.replace(/\s+/g, ' ').trim(); if (!t) return;
      (t.match(/[^.!?;]+[.!?;]*\s*/g) || [t]).reduce(function (acc, f) {
        if (acc.length && (acc[acc.length - 1] + f).length < 220) acc[acc.length - 1] += f; else acc.push(f);
        return acc;
      }, []).forEach(function (pedaco) { fila.push([b, pedaco]); });
    });
  };
  var marca = function (b) {
    if (atual) atual.classList.remove('lendo');
    atual = b; if (!b) return; b.classList.add('lendo');
    var r = b.getBoundingClientRect(); if (r.top < 80 || r.bottom > innerHeight) b.scrollIntoView({ block: 'center', behavior: 'smooth' });
  };
  var fala = function () {
    if (pos >= fila.length) { para(); return; }
    var it = fila[pos], u = new SpeechSynthesisUtterance(it[1]);
    var v = voz(); if (v) { u.voice = v; u.lang = v.lang; } else u.lang = 'pt-BR'; u.rate = vel;
    u.onend = function () { if (!tocando) return; pos++; fala(); };
    marca(it[0]); synth.speak(u);
  };
  var estado = function () {
    bOuvir.setAttribute('aria-pressed', String(tocando));
    bOuvir.innerHTML = tocando ? '<span aria-hidden="true">❚❚</span> Pausar' : '<span aria-hidden="true">▶</span> ' + (pos > 0 ? 'Continuar' : 'Ouvir');
    bParar.hidden = bVel.hidden = !(tocando || pos > 0);
  };
  var para = function () { tocando = false; synth.cancel(); pos = 0; marca(null); estado(); };
  bOuvir.addEventListener('click', function () {
    if (!tocando && !voz() && !bOuvir.dataset.avisou) {
      bOuvir.dataset.avisou = '1';
      modal('Voz em português não encontrada', '<p>Seu navegador ou sistema não tem uma voz em português do Brasil instalada, então a leitura pode sair com sotaque de outra língua.</p><p class="fino">No Windows: Configurações → Hora e idioma → Fala → Adicionar vozes → Português (Brasil). No Android e no iPhone, a voz em português costuma vir nas configurações de acessibilidade ou de texto para fala. O Chrome e o Edge já trazem vozes em português na maioria dos computadores.</p>');
    }
    if (tocando) { tocando = false; synth.cancel(); estado(); return; }
    if (!fila.length) monta();
    tocando = true; estado(); fala();
  });
  bParar.addEventListener('click', para);
  bVel.addEventListener('click', function () {
    var vs = [1, 1.25, 1.5, 0.85]; vel = vs[(vs.indexOf(vel) + 1) % vs.length]; bVel.textContent = String(vel).replace('.', ',') + '×';
    if (tocando) { synth.cancel(); setTimeout(fala, 60); }
  });
  window.addEventListener('pagehide', function () { synth.cancel(); });
})();
