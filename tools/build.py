"""Gera todas as páginas do Ciência Para Iniciantes. Uso: python tools/build.py"""
import hashlib, json, os, re, sys, unicodedata
from html import escape as e
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from licoes_iniciante import INICIANTE
from licoes_intermediario import INTERMEDIARIO
from licoes_avancado import AVANCADO
from extras import TEMAS, ORDEM_GRUPOS
from correntes import C_ as COR, FAMILIAS, FOCO_FAM
from nao_e import NAO_E
from pseudo import PSEUDO, TEMAS_P, SINAIS, STATUS
from pessoas import P as PES, AREAS
from debates import DEBATES, ROT_PESO, TEMAS_DB
from glossario import GLOSSARIO, GRUPOS_G
from biblioteca import LIVROS, SECOES_L, SITES, GRUPOS_S, NAC
from ferramentas import FERR, JOGOS, DETECTOR
from trilhas import TRILHAS
from licoes_novas import NOVAS_INICIANTE, NOVAS_INTERMEDIARIO, NOVAS_AVANCADO, POSICAO
from correntes_novas import C_NOVAS, NAO_E_NOVAS
from casos_novos import PSEUDO_NOVAS, DEBATES_NOVOS, P_NOVOS
from licoes_novas2 import NOVAS2_INICIANTE, NOVAS2_INTERMEDIARIO, NOVAS2_AVANCADO, POSICAO2
from casos_novos2 import C_NOVAS2, NAO_E_NOVAS2, PSEUDO_NOVAS2, DEBATES_NOVOS2, P_NOVOS2
from licoes_novas3 import NOVAS3_INICIANTE, NOVAS3_INTERMEDIARIO, NOVAS3_AVANCADO, POSICAO3
from casos_novos3 import DEBATES_NOVOS3, P_NOVOS3, JOGO_CONSENSO, JOGO_CONSENSO_DADOS, GLOSSARIO_NOVOS
from licoes_novas4 import NOVAS4_INICIANTE, NOVAS4_INTERMEDIARIO, NOVAS4_AVANCADO, POSICAO4
from licoes_novas5 import NOVAS5_INICIANTE, NOVAS5_INTERMEDIARIO, NOVAS5_AVANCADO, POSICAO5
from casos_novos4 import PSEUDO_NOVAS3, DEBATES_NOVOS4
from licoes_novas6 import NOVAS6_AVANCADO, POSICAO6
from casos_novos5 import P_NOVOS4
from licoes_novas7 import NOVAS7_INTERMEDIARIO, POSICAO7
from casos_novos6 import DEBATES_NOVOS6
from licoes_novas8 import NOVAS8_INICIANTE, POSICAO8
FERR.insert(4, JOGO_CONSENSO); JOGOS[JOGO_CONSENSO[0]] = JOGO_CONSENSO_DADOS; GLOSSARIO.extend(GLOSSARIO_NOVOS)
from crossover import caixa_ciencia  # ponte com os sites irmãos (tools/crossover.py, igual nos três sites)
import arte

# segunda leva (2026-11-06): lições entram depois da indicada em POSICAO; o resto é reordenado de forma estável pelo grupo
def _apos(ls, slug, nova): ls.insert(next(i for i, l in enumerate(ls) if l['slug'] == slug) + 1, nova)
for _ls, _novas in ((INICIANTE, NOVAS_INICIANTE), (INTERMEDIARIO, NOVAS_INTERMEDIARIO), (AVANCADO, NOVAS_AVANCADO)):
    for _l in _novas: _apos(_ls, POSICAO[_l['slug']], _l)
for _ls, _novas in ((INICIANTE, NOVAS2_INICIANTE), (INTERMEDIARIO, NOVAS2_INTERMEDIARIO), (AVANCADO, NOVAS2_AVANCADO)):
    for _l in _novas: _apos(_ls, POSICAO2[_l['slug']], _l)
for _ls, _novas in ((INICIANTE, NOVAS3_INICIANTE), (INTERMEDIARIO, NOVAS3_INTERMEDIARIO), (AVANCADO, NOVAS3_AVANCADO)):
    for _l in _novas: _apos(_ls, POSICAO3[_l['slug']], _l)
DEBATES_NOVOS2.extend(DEBATES_NOVOS3); P_NOVOS2.extend(P_NOVOS3)
PSEUDO_NOVAS2.extend(PSEUDO_NOVAS3); DEBATES_NOVOS2.extend(DEBATES_NOVOS4)
for _l in NOVAS6_AVANCADO: _apos(AVANCADO, POSICAO6[_l['slug']], _l)
P_NOVOS2.extend(P_NOVOS4)
DEBATES_NOVOS2.extend(DEBATES_NOVOS6)
for _ls, _novas in ((INICIANTE, NOVAS4_INICIANTE), (INTERMEDIARIO, NOVAS4_INTERMEDIARIO), (AVANCADO, NOVAS4_AVANCADO)):
    for _l in _novas: _apos(_ls, POSICAO4[_l['slug']], _l)
for _ls, _novas in ((INICIANTE, NOVAS5_INICIANTE), (INTERMEDIARIO, NOVAS5_INTERMEDIARIO), (AVANCADO, NOVAS5_AVANCADO)):
    for _l in _novas: _apos(_ls, POSICAO5[_l['slug']], _l)
C_NOVAS.extend(C_NOVAS2); NAO_E_NOVAS.update(NAO_E_NOVAS2); PSEUDO_NOVAS.extend(PSEUDO_NOVAS2); DEBATES_NOVOS.extend(DEBATES_NOVOS2); P_NOVOS.extend(P_NOVOS2)
COR.extend(C_NOVAS); NAO_E.update(NAO_E_NOVAS); COR.sort(key=lambda c: FAMILIAS.index(c['f']))
PSEUDO.extend(PSEUDO_NOVAS); PSEUDO.sort(key=lambda p: TEMAS_P.index(p['t']))
DEBATES.extend(DEBATES_NOVOS); DEBATES.sort(key=lambda d: TEMAS_DB.index(d['t']))
PES.extend(P_NOVOS); PES.sort(key=lambda p: AREAS.index(p['area']))

# bibliotecas irmãs da BiblioVerse e onde cada uma ajuda
BV = {'thinking': ('Biblioteca da Racionalidade', 'https://thinking.biblioverse.org/', 'catálogo pesquisável de pensamento crítico, racionalidade e evidências'),
      'conspiracy': ('Biblioteca de Conspirações', 'https://conspiracy.biblioverse.org/', 'catálogo pesquisável de teorias da conspiração, pseudociências, fraudes e crenças falsas, e de como desmenti-las'),
      'data': ('Biblioteca de Dados', 'https://data.biblioverse.org/', 'catálogo pesquisável das melhores fontes de dados e estatísticas')}
BV_LICAO = {'postura-cientifica': ['thinking'], 'vieses-e-metodo': ['thinking'], 'falacias-e-argumentos': ['thinking'], 'opiniao-crenca-e-conhecimento': ['thinking'],
            'o-que-e-pseudociencia': ['conspiracy'], 'negacionismo-e-desinformacao': ['conspiracy', 'thinking'], 'criterio-da-demarcacao': ['conspiracy'], 'como-ler-noticia-de-ciencia': ['thinking', 'data'],
            'estatistica-para-entender-ciencia': ['data'], 'risco-e-probabilidade': ['data'], 'correlacao-e-causalidade': ['data'], 'niveis-de-evidencia': ['data'], 'confianca-e-especialistas': ['thinking'], 'interpretacoes-da-probabilidade': ['data'], 'experimentos-naturais': ['data'], 'grandes-consensos-cientificos': ['conspiracy'], 'ceticismo-responsavel': [], 'pesquisas-de-opiniao': ['data'], 'como-funciona-a-checagem': ['conspiracy', 'thinking'], 'avaliacao-de-politicas-publicas': ['data'], 'divulgacao-cientifica': ['thinking'], 'ma-ciencia': ['conspiracy'], 'postura-cientifica-etica-e-politica': ['thinking'], 'fora-da-media': ['data'], 'como-achar-e-julgar-artigos': ['data', 'thinking'], 'letramento-cientifico-no-brasil': ['thinking', 'data']}
def bv_nota(chaves, pre=''):
    return '<div class="nota"><strong>Na BiblioVerse:</strong> ' + '; '.join(f'<a href="{BV[k][1]}" target="_blank" rel="noopener">{BV[k][0]}</a>, {BV[k][2]}' for k in chaves) + '.</div>'

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://cienciaparainiciantes.biblioverse.org'
NOME = 'Ciência Para Iniciantes'
EXT = 'target="_blank" rel="noopener"'
ATUALIZADO = '2026-11-07'
CAMPOS = ('slug', 'grupo', 'titulo', 'temas', 'resumo', 'corpo', 'fontes', 'quiz', 'analogia', 'crianca', 'obj', 'caso', 'erro', 'ferr', 'pre', 'guardar', 'pensar')

# ---------- validação e montagem das lições ----------
# as lições da sétima leva entram depois de lições de levas anteriores, por isso vêm por último
for _l in NOVAS7_INTERMEDIARIO: _apos(INTERMEDIARIO, POSICAO7[_l['slug']], _l)
for _l in NOVAS8_INICIANTE: _apos(INICIANTE, POSICAO8[_l['slug']], _l)
for _n, _ls in (('iniciante', INICIANTE), ('intermediario', INTERMEDIARIO), ('avancado', AVANCADO)):
    _o = ORDEM_GRUPOS[_n]; assert all(_l['grupo'] in _o for _l in _ls), [_l['slug'] for _l in _ls if _l['grupo'] not in _o]
    _ls.sort(key=lambda l: _o.index(l['grupo']))
NIVEIS = [('iniciante', 'Iniciante', INICIANTE, 'Ciência para iniciantes', 'O que é ciência, seus valores e áreas, o método, a evidência, os consensos, o ceticismo responsável e como reconhecer pseudociência.', 'v'),
          ('intermediario', 'Intermediário', INTERMEDIARIO, 'Ciência intermediária', 'Epistemologia, indução, positivismo, Popper, Kuhn, probabilidade, ética na pesquisa, ciência usada para o mal, má ciência e fraudes.', ''),
          ('avancado', 'Avançado', AVANCADO, 'Ciência avançada', 'Realismo, leis da natureza, física quântica, teorias unificadas, o incognoscível, bayesianismo, valores e negacionismo.', 'a')]
FERR_S = {f[0] for f in FERR}
for slug, rot, ls, *_ in NIVEIS:
    for i, l in enumerate(ls):
        for k in CAMPOS: assert k in l, (l['slug'], k)
        assert len(l['quiz']) == 3 and len(l['obj']) == 3 and len(l['guardar']) == 3, l['slug']
        assert all(t in TEMAS for t in l['temas']), l['slug']
        assert l['ferr'] is None or l['ferr'] in FERR_S, (l['slug'], l['ferr'])
        l.update(nivel=slug, nivel_rot=rot, i=i)
TODAS = INICIANTE + INTERMEDIARIO + AVANCADO
L_S = {l['slug']: l for l in TODAS}
assert len(L_S) == len(TODAS)
for l in TODAS:
    for p in l['pre']: assert p in L_S, (l['slug'], p)
    blocos = f'<div class="ajuda"><section class="analogia"><h3>Uma analogia</h3><p>{e(l["analogia"])}</p></section><section class="crianca"><h3>Explicando para uma criança</h3><p>{e(l["crianca"])}</p></section></div>'
    fim = l['corpo'].index('</p>') + 4
    l['corpo'] = l['corpo'][:fim] + blocos + l['corpo'][fim:]

COR_S = {c['s']: c for c in COR}; PES_S = {p['slug']: p for p in PES}; PS_S = {p['s']: p for p in PSEUDO}
assert len(COR_S) == len(COR) and len(PES_S) == len(PES) and len(PS_S) == len(PSEUDO)
assert all(c['f'] in FAMILIAS for c in COR)
assert set(NAO_E) == set(COR_S), set(NAO_E) ^ set(COR_S)
for c in COR:
    for p in c['pes']: assert p in PES_S, (c['s'], p)
for p in PES:
    assert p['area'] in AREAS, p['slug']
    for c in p['correntes']: assert c in COR_S, (p['slug'], c)
for p in PSEUDO:
    assert p['t'] in TEMAS_P and p['status'] in STATUS, p['s']
    for x in p['sinais']: assert x in SINAIS, (p['s'], x)
assert len({d['s'] for d in DEBATES}) == len(DEBATES)
for d in DEBATES:
    assert d['t'] in TEMAS_DB and d['p'][0] in ROT_PESO, d['s']
    for s in d['licoes']: assert s in L_S, (d['s'], s)
    for s, _ in d['visoes']: assert s in COR_S, (d['s'], s)

PAGINAS = []
SECOES = {'correntes': ('correntes.html', 'Correntes', 'O que cada corrente põe no centro, forças, objeções e referências.'), 'debates': ('debates.html', 'Debates', 'Os lados, por que é complexo e para onde a evidência aponta.'), 'pseudociencias': ('pseudociencias.html', 'Pseudociências', 'O que alega, o que a evidência diz e por que atrai tanta gente.'), 'pensadores': ('pensadores.html', 'Pensadores', 'Quem foi, o que defendeu e o que dizem os críticos.'), 'ferramentas': ('ferramentas.html', 'Ferramentas', 'Ferramenta interativa e gratuita, sem cadastro.')}
PAIS_NIVEL = {'iniciante.html': 'Iniciante', 'intermediario.html': 'Intermediário', 'avancado.html': 'Avançado'}
HUBS = {'catalogo.html', 'iniciante.html', 'intermediario.html', 'avancado.html', 'correntes.html', 'debates.html', 'pseudociencias.html', 'pensadores.html', 'ferramentas.html', 'biblioteca.html', 'sites.html', 'glossario.html', 'trilhas.html'}
DESC_CURTA = {}

def desc_seo(path, desc):
    d = re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', desc)).strip()
    if d and d[-1] not in '.!?…': d += '.'
    if len(d) < 70:
        sec = SECOES.get(path.split('/')[0]) if '/' in path else None
        d += ' ' + (sec[2] if sec else 'Explicação simples e com fontes, do básico ao avançado.')
    if len(d) > 160 and path in DESC_CURTA: d = DESC_CURTA[path]
    if len(d) > 160:
        fim = max(d.rfind(x, 0, 160) for x in ('. ', '? ', '! '))
        d = d[:fim + 1] if fim >= 69 else d[:157].rsplit(' ', 1)[0].rstrip(' ,;:') + '…'
    return d

def dados(path, title, desc, url, atual, home):
    org = {'@type': 'Organization', 'name': 'BiblioVerse', 'url': 'https://biblioverse.org'}
    site = {'@type': 'WebSite', '@id': SITE + '/#site', 'name': NOME, 'url': SITE + '/', 'inLanguage': 'pt-BR', 'publisher': org}
    if home: return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': [site]}, ensure_ascii=False) + '</script>'
    pasta = path.split('/')[0] if '/' in path else ''
    pai = (SECOES[pasta][0], SECOES[pasta][1]) if pasta in SECOES else ((atual, PAIS_NIVEL[atual]) if atual in PAIS_NIVEL else None)
    trilha = [('Início', SITE + '/')] + ([(pai[1], f'{SITE}/{pai[0]}')] if pai else []) + [(title, url)]
    migalhas = {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(trilha)]}
    base = {'name': title, 'description': desc, 'url': url, 'inLanguage': 'pt-BR', 'isPartOf': {'@id': SITE + '/#site'}, 'dateModified': ATUALIZADO, 'image': SITE + '/assets/share.png'}
    if atual in PAIS_NIVEL or pasta in ('correntes', 'pseudociencias', 'debates'):
        pagina = {'@type': 'Article', 'headline': title[:110], 'datePublished': ATUALIZADO, 'author': {'@type': 'Organization', 'name': NOME, 'url': SITE + '/sobre.html'}, 'publisher': org, 'mainEntityOfPage': url, **base}
    elif pasta == 'pensadores':
        pagina = {'@type': 'WebPage', 'about': {'@type': 'Person', 'name': title}, **base}
    elif pasta == 'ferramentas':
        pagina = {'@type': 'WebApplication', 'applicationCategory': 'EducationalApplication', 'operatingSystem': 'Web', 'isAccessibleForFree': True, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'BRL'}, **base}
    elif path in HUBS:
        pagina = {'@type': 'CollectionPage', **base}
    else:
        pagina = {'@type': 'WebPage', **base}
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': [site, pagina, migalhas]}, ensure_ascii=False).replace('</', '<\\/') + '</script>'

def titulos_ok(corpo):
    corpo = re.sub(r'(<section class="(?:analogia|crianca)">)<h3>(.*?)</h3>', r'\1<p class="ti">\2</p>', corpo)
    m = re.search(r'</h1>.*?<h([2-6])[\s>]', corpo, re.S)
    fim = corpo.find('</section>', corpo.find('</h1>'))
    if m and m.group(1) == '3' and fim > 0:
        fim += len('</section>')
        return corpo[:fim] + '<h2 class="so-leitor">Nesta página</h2>' + corpo[fim:]
    return corpo

def barra_leitura(path, title, url):
    ano = ATUALIZADO[:4]
    abnt = f'{NOME.upper()}. {e(title)}. BiblioVerse, {ano}. Disponível em: {url}. Acesso em: {{ACESSO}}.'
    apa = f'{NOME}. ({ano}). <em>{e(title)}</em>. BiblioVerse. {url}'
    return (f'<div class="acoes-cap" data-abnt="{e(abnt)}" data-apa="{e(apa)}">'
            '<button type="button" data-acao="ouvir" aria-pressed="false"><span aria-hidden="true">▶</span> Ouvir</button>'
            '<button type="button" data-acao="citar"><span aria-hidden="true">❝</span> Como citar</button>'
            '<button type="button" data-acao="imprimir"><span aria-hidden="true">⎙</span> Imprimir ou PDF</button></div>')

def page(path, title, desc, corpo, atual='', home=False):
    PAGINAS.append(path)
    erro = path == '404.html'
    desc = desc_seo(path, desc)
    corpo = titulos_ok(corpo)
    _cx = caixa_ciencia(path, e)  # caixa dos sites irmãos, antes do bloco de páginas relacionadas
    _i = corpo.rfind('<section class="relac"')
    corpo = corpo[:_i] + _cx + corpo[_i:] if _i >= 0 else corpo + _cx
    pre = '../' * path.count('/')
    url = SITE + '/' + ('' if path == 'index.html' else path)
    if not erro and '<section class="cabeca">' in corpo and re.search(r'class="[^"]*\bleitura\b', corpo):
        _ic = corpo.index('<section class="cabeca">'); _fc = corpo.index('</div></section>', _ic)
        corpo = corpo[:_fc] + barra_leitura(path, title, url) + corpo[_fc:]
    full = title if home else f'{title} | {NOME}'
    if len(full) > 60: full = title
    artigo = atual in PAIS_NIVEL or path.split('/')[0] in ('correntes', 'pseudociencias', 'debates')
    pre_tag = '<base href="/"/>\n' if erro else ''
    indexa = '<meta name="robots" content="noindex"/>\n' if erro else f'<link rel="canonical" href="{url}"/>\n' + dados(path, title, desc, url, atual, home) + '\n'
    l = lambda u, t: f'<a href="{pre}{u}">{e(t)}</a>'
    def grupo(nome, itens, cls=''):
        ativo = any(u == atual for u, _ in itens)
        links = ''.join(f'<a href="{pre}{u}"{" aria-current=page" if u == atual else ""}>{e(t)}</a>' for u, t in itens)
        gid = 'm-' + re.sub(r'[^a-z]', '', unicodedata.normalize('NFD', nome.lower()))
        return f'<div class="drop{" ativo" if ativo else ""}"><button type="button" aria-expanded="false" aria-controls="{gid}">{e(nome)} ▾</button><div class="mega{" " + cls if cls else ""}" id="{gid}" hidden>{links}</div></div>'
    menu = grupo('Aprender', [('comece-aqui.html', 'Comece aqui'), ('trilhas.html', 'Trilhas por tema')] + [(f'{s}.html', r) for s, r, *_ in NIVEIS] + [('catalogo.html', 'Todas as lições')])
    menu += grupo('Ideias', [('correntes.html', 'Correntes'), ('pseudociencias.html', 'Pseudociências'), ('debates.html', 'Debates'), ('pensadores.html', 'Pensadores'), ('glossario.html', 'Glossário')])
    menu += grupo('Ferramentas', [(f'ferramentas/{a}.html', b) for a, b, _, _ in FERR] + [('ferramentas.html', 'Todas as ferramentas')])
    menu += grupo('Biblioteca', [('biblioteca.html', 'Livros'), ('sites.html', 'Sites sobre ciência')])
    menu += f'<a href="{pre}sobre.html"{" aria-current=page" if atual == "sobre.html" else ""}>Sobre</a>'
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
{pre_tag}<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}"/>
{indexa}<meta property="og:type" content="{'article' if artigo else 'website'}"/>
<meta property="og:site_name" content="{NOME}"/>
<meta property="og:title" content="{e(full)}"/>
<meta property="og:description" content="{e(desc)}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:locale" content="pt_BR"/>
<meta property="og:image" content="{SITE}/assets/share.png"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:alt" content="{NOME}"/>
{f'<meta property="article:modified_time" content="{ATUALIZADO}"/>' if artigo else ''}
<meta name="twitter:card" content="summary_large_image"/>
<meta name="theme-color" content="#4b2a82"/>
<link rel="icon" href="{pre}assets/icon.svg" type="image/svg+xml"/>
<link rel="apple-touch-icon" href="{pre}assets/icon-180.png"/>
<link rel="manifest" href="{pre}manifest.webmanifest"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Fraunces:ital,opsz,wght,SOFT@0,9..144,400,100;0,9..144,600,100;0,9..144,700,100;1,9..144,500,100&display=swap"/>
<link rel="stylesheet" href="{pre}assets/style.min.css?v={VERSAO}"/>
<script src="https://biblioverse.org/superbar.js" async></script>
</head>
<body data-base="{pre}">
<nav id="bvbar" class="bvbar" data-current="cienciaparainiciantes" data-offset="none" aria-label="BiblioVerse" style="position:relative;height:44px;background:linear-gradient(90deg,#4f7cff,#7a5cff)"><a href="https://biblioverse.org" style="color:#fff;line-height:44px;padding:0 14px;font-weight:700;text-decoration:none">BiblioVerse</a></nav>
<a class="skip" href="#main">Pular para o conteúdo</a>
<header class="topo"><div class="wrap topo-in">
<a class="marca" href="{pre}index.html">{arte.LOGO}<span>Ciência<br/>Para Iniciantes</span></a>
<nav class="menu" aria-label="Principal">{menu}</nav>
<a class="btn cta-topo" href="{pre}comece-aqui.html">Comece aqui</a>
<button class="bbusca" type="button" aria-label="Buscar no site">🔍<span> Buscar</span> <kbd>Ctrl K</kbd></button>
<button class="hamb" type="button" aria-label="Abrir menu" aria-expanded="false">☰</button>
</div></header>
<div id="busca" hidden><div class="bcx" role="dialog" aria-label="Buscar no site"><input id="q" type="search" placeholder="Busque um tema, corrente ou pensador" aria-label="Buscar no site" autocomplete="off"/><div class="res" id="res"></div></div></div>
<main id="main">{corpo}</main>
<footer class="rodape"><div class="wrap rodape-in">
<div><strong>{NOME}</strong><p>Explicações objetivas e simples sobre ciência, método e conhecimento, do básico ao avançado. Com fontes e aberto a correções.</p><p>Parte da <a href="https://biblioverse.org">BiblioVerse</a>.</p><p class="copy">© {ATUALIZADO[:4]} BiblioVerse. Atualizado em {ATUALIZADO[8:10]}/{ATUALIZADO[5:7]}/{ATUALIZADO[:4]}.</p></div>
<div><p class="ti">Aprender</p><ul><li>{l('comece-aqui.html', 'Comece aqui')}</li><li>{l('iniciante.html', 'Iniciante')}</li><li>{l('intermediario.html', 'Intermediário')}</li><li>{l('avancado.html', 'Avançado')}</li><li>{l('trilhas.html', 'Trilhas por tema')}</li><li>{l('catalogo.html', 'Todas as lições')}</li></ul></div>
<div><p class="ti">Ideias</p><ul><li>{l('correntes.html', 'Correntes')}</li><li>{l('pseudociencias.html', 'Pseudociências')}</li><li>{l('debates.html', 'Debates')}</li><li>{l('pensadores.html', 'Pensadores')}</li><li>{l('glossario.html', 'Glossário')}</li></ul></div>
<div><p class="ti">Mais</p><ul><li>{l('ferramentas.html', 'Ferramentas')}</li><li>{l('biblioteca.html', 'Biblioteca')}</li><li>{l('sites.html', 'Sites sobre ciência')}</li><li><a href="https://eticaparainiciantes.biblioverse.org/" {EXT}>Ética Para Iniciantes</a></li><li><a href="https://politicaparainiciantes.biblioverse.org/" {EXT}>Política Para Iniciantes</a></li><li><a href="https://thinking.biblioverse.org/" {EXT}>Biblioteca da Racionalidade</a></li><li><a href="https://conspiracy.biblioverse.org/" {EXT}>Biblioteca de Conspirações</a></li><li><a href="https://data.biblioverse.org/" {EXT}>Biblioteca de Dados</a></li><li>{l('sobre.html', 'Sobre')}</li><li>{l('privacidade.html', 'Política de privacidade')}</li></ul></div>
</div></footer>
<noscript><p class="nojs">A leitura funciona sem JavaScript. A busca, os menus suspensos, os testes e as ferramentas interativas precisam dele; o rodapé tem links para todas as seções.</p></noscript>
<script src="{pre}assets/app.min.js?v={VERSAO}" defer></script>
</body></html>
'''
    html = html.replace('href="index.html"', 'href="./"').replace('href="../index.html"', 'href="../"')
    full_path = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    open(full_path, 'w', encoding='utf-8', newline='\n').write(html)

def cabeca(kicker, titulo, lede='', meta=''):
    return f'<section class="cabeca"><div class="wrap"><p class="trilha">{kicker}</p><h1>{e(titulo)}</h1>' + (f'<p class="lede">{lede}</p>' if lede else '') + meta + '</div></section>'
def fontes(ls):
    return '<aside class="fontes"><h2>Fontes e leituras</h2><ul>' + ''.join(f'<li><a href="{e(u)}" {EXT}>{e(t)}</a></li>' for t, u in ls) + '</ul></aside>'
def tabelas(h): return h.replace('<table>', '<div class="tabela"><table>').replace('</table>', '</table></div>').replace('<div class="tabela"><div class="tabela">', '<div class="tabela">').replace('</table></div></div>', '</table></div>')
def tempo_leitura(h): return max(2, round(len(re.sub('<[^>]+>', ' ', h).split()) / 190))
def cartao_licao(l, pre=''):
    tg = ''.join(f'<span class="tag">{e(TEMAS[t])}</span>' for t in l['temas'])
    return f'<a class="cartao" data-licao="{l["slug"]}" data-temas="{" ".join(l["temas"])}" data-nivel="{l["nivel"]}" href="{pre}{l["slug"]}.html"><span class="linha-cartao"><span class="tipo {l["nivel"]}">{e(l["nivel_rot"])}</span></span><h3>{e(l["titulo"])}</h3><p>{e(l["resumo"])}</p><span class="tags" style="margin-top:auto;padding-top:6px">{tg}</span></a>'
def cartao_ferr(a, b, c, n, pre=''): return f'<a class="cartao" data-temas="ferramenta" data-nivel="ferr" href="{pre}ferramentas/{a}.html">{arte.icone(n)}<h3>{e(b)}</h3><p>{e(c)}</p></a>'
FERR_D = {f[0]: f for f in FERR}
def relacionados(l):
    alvos = [x for x in TODAS if x['slug'] != l['slug'] and set(x['temas']) & set(l['temas'])]
    alvos.sort(key=lambda x: (x['nivel'] != l['nivel'], -len(set(x['temas']) & set(l['temas']))))
    return f'<section class="relac"><div class="wrap"><h2>Continue</h2><div class="grade">{"".join(cartao_licao(x) for x in alvos[:3])}</div></div></section>'
def mistura(q):
    """Embaralha as opções de forma estável (pelo texto da pergunta), para que a resposta certa não caia sempre na mesma posição."""
    p, ops, c, x = q[0], list(q[1]), q[2], q[3]
    h = int(hashlib.md5(p.encode('utf-8')).hexdigest(), 16)
    certa = ops.pop(c)
    k = (h // 7) % len(ops) if ops else 0
    ops = ops[k:] + ops[:k]
    alvo = h % (len(ops) + 1)
    ops.insert(alvo, certa)
    return [p, ops, alvo, x]


def bloco_quiz(q, rot='Teste rápido'):
    q = mistura(q)
    return f'<div class="quiz" data-quiz="{e(json.dumps(q, ensure_ascii=False))}"><p class="k">{e(rot)}</p><div class="alvo"></div></div>'
COR_FAM = {f: i for i, f in enumerate(FAMILIAS)}
COR_AREA = {a: i + 6 for i, a in enumerate(AREAS)}
COR_TP = {t: i + 9 for i, t in enumerate(TEMAS_P)}
def cartao_c(c, pre=''): return f'<a class="cartao item" data-f="{e(c["f"])}" href="{pre}{c["s"]}.html"><span class="tipo fam f{COR_FAM[c["f"]]}">{e(c["f"])}</span><h3>{e(c["n"])}</h3><p>{e(c["r"])}</p></a>'
def cartao_p(p, pre=''): return f'<a class="cartao item" data-c="{e(p["area"])}" href="{pre}{p["slug"]}.html"><span class="linha-cartao"><span class="tipo fam f{COR_AREA[p["area"]]}">{e(p["area"])}</span><span class="tipo">{e(p["anos"])}</span></span><h3>{e(p["nome"])}</h3><p>{e(p["quem"])}</p></a>'
def cartao_ps(p, pre=''): return f'<a class="cartao item" data-t="{e(p["t"])}" data-s="{e(p["status"])}" href="{pre}{p["s"]}.html"><span class="linha-cartao"><span class="peso {STATUS[p["status"]][0]}">{e(p["status"])}</span></span><h3>{e(p["n"])}</h3><p>{e(p["r"])}</p></a>'
def clink(s, pre='', cls=''): return f'<a href="{pre}correntes/{s}.html" class="{cls}">{e(COR_S[s]["n"])}</a>'
def lista_mais(rotulo, links, n=6):
    if not links: return ''
    saida = f'<div class="lista-mais"><strong>{rotulo}:</strong> ' + ', '.join(links[:n])
    if len(links) > n: saida += f' <details class="mais"><summary>e mais {len(links) - n}</summary><span>' + ', '.join(links[n:]) + '</span></details>'
    return saida + '.</div>'

# ---------- glossário em dica ----------
GL_TERMS = sorted(((re.sub(r'\s*\(.*?\)', '', t).strip(), d) for _, t, d, _ in GLOSSARIO if len(t) >= 6 and t not in {'Ciência', 'Teoria'}), key=lambda x: -len(x[0]))
GL_SKIP = {'a', 'h1', 'h2', 'h3', 'h4', 'summary', 'th', 'button', 'script', 'style', 'code'}
def glossa(h, titulo, maximo=6):
    partes = re.split(r'(<[^>]+>)', h); pilha = 0; usados = set(); n = 0; tl = titulo.lower()
    for i, p in enumerate(partes):
        if not p: continue
        if p.startswith('<'):
            m = re.match(r'</?([a-zA-Z0-9]+)', p); nome = m.group(1).lower() if m else ''
            if nome in GL_SKIP and not p.endswith('/>'): pilha = max(0, pilha - 1) if p.startswith('</') else pilha + 1
            continue
        if pilha or n >= maximo: continue
        off = 0; novo = ''
        for termo, d in GL_TERMS:
            if n >= maximo: break
            if termo in usados or termo.lower() in tl: continue
            m = re.search(r'(?<![\w-])' + re.escape(termo) + r'(?![\w-])', p[off:], flags=re.I)
            if not m: continue
            s, f = m.start() + off, m.end() + off
            novo += p[off:s] + f'<span class="gl" tabindex="0" data-def="{e(d)}">{p[s:f]}</span>'; off = f; usados.add(termo); n += 1
        partes[i] = novo + p[off:]
    return ''.join(partes)

# ---------- início ----------
def inicio():
    niv = ''.join(f'<div><h2><span class="grad {g}">{e(r)}</span></h2><p>{e(d)}</p><a class="btn {g}" href="{s}.html">Começar</a><small>{len(ls)} lições</small></div>' for s, r, ls, _, d, g in NIVEIS)
    temas = ''.join(f'<a href="catalogo.html?tema={k}">{e(v)}</a>' for k, v in TEMAS.items())
    secoes = ''.join(f'<a class="cartao" href="{u}">{arte.icone(i)}<h3>{e(t)}</h3><p>{e(d)}</p></a>' for u, i, t, d in [
        ('catalogo.html', 'ficha', 'Aprenda', f'{len(TODAS)} lições em três níveis, com busca por tema.'),
        ('trilhas.html', 'rede', 'Trilhas por tema', f'{len(TRILHAS)} caminhos curtos: o essencial, saúde, pensamento crítico, filosofia da ciência e desinformação.'),
        ('correntes.html', 'arvore', 'Correntes', f'{len(COR)} correntes da epistemologia e da filosofia da ciência: o que cada uma põe no centro.'),
        ('pseudociencias.html', 'lupa', 'Pseudociências', f'{len(PSEUDO)} casos: o que alegam, o que a evidência diz e por que atraem.'),
        ('debates.html', 'valor', 'Debates', f'{len(DEBATES)} debates sobre ciência e sociedade, e para onde a evidência aponta.'),
        ('pensadores.html', 'pessoa', 'Pensadores', f'{len(PES)} cientistas, filósofos e críticos, de Aristóteles a Oreskes.'),
        ('ferramentas.html', 'compara', 'Ferramentas', f'{len(FERR) - 1} jogos e um detector de pseudociência para aprender fazendo.'),
        ('glossario.html', 'livro', 'Glossário', f'{len(GLOSSARIO)} termos explicados em uma frase.'),
        ('biblioteca.html', 'livro', 'Biblioteca', f'{len(LIVROS)} livros por nível e {len(SITES)} sites para ir além.'),
    ])
    destaque = ''.join(f'<a href="correntes/{s}.html">{e(COR_S[s]["n"])}</a>' for s in ['empirismo', 'positivismo-logico', 'falsificacionismo', 'paradigmas', 'bayesianismo', 'realismo-cientifico'])
    corpo = f'''<section class="capa"><div class="wrap capa-in"><div><h1>Entenda a <span class="grifo">ciência</span>, do <span class="grifo v">básico</span> ao <span class="grifo a">avançado</span>, e pense por conta própria.</h1><p class="lede">O que é ciência, como ela sabe o que sabe e como separar conhecimento de opinião e de pseudociência. Explicações simples, com fontes, em três níveis.</p><div class="cta"><a class="btn" href="comece-aqui.html">Comece aqui</a><a class="btn alt" href="correntes.html">Mapa das correntes</a></div></div>{arte.hero()}</div></section>
<section class="noite"><div class="wrap niveis">{niv}</div></section>
<section class="secao areia"><div class="wrap"><div class="sec-cab"><h2>Explore o site</h2><p>Escolha por onde quer ir.</p></div><div class="grade">{secoes}</div></div></section>
<section class="secao"><div class="wrap numeros"><div><b class="grad">{len(TODAS)}</b><span>lições em três níveis</span></div><div><b class="grad v">{len(COR)}</b><span>correntes de pensamento</span></div><div><b class="grad a">{len(PSEUDO) + len(DEBATES)}</b><span>pseudociências e debates</span></div><div><b class="grad">{len(PES)}</b><span>cientistas e filósofos</span></div></div></section>
<section class="secao areia"><div class="wrap capa-in" style="padding-block:0"><div><h2>Observar, refutar ou atualizar?</h2><p style="font-size:1.1rem">Empiristas, positivistas, popperianos, kuhnianos e bayesianos discordam sobre o que faz a ciência funcionar. Veja o que cada corrente põe no centro, as forças e as objeções.</p><a class="btn" href="correntes.html">Explorar as correntes</a></div><div class="temas">{destaque}</div></div></section>
<section class="secao"><div class="wrap"><div class="sec-cab"><h2>O que você quer entender?</h2></div><div class="temas">{temas}</div></div></section>'''
    page('index.html', 'Ciência Para Iniciantes: do básico ao avançado', 'Guia de ciência em três níveis: método científico, epistemologia, evidências, demarcação, pseudociências e as correntes da filosofia da ciência.', corpo, home=True)

def comece():
    _p1 = ['o-que-e-ciencia', 'opiniao-crenca-e-conhecimento', 'crenca-verdadeira-justificada', 'postura-cientifica', 'o-metodo-cientifico', 'niveis-de-evidencia', 'correlacao-e-causalidade', 'o-que-e-pseudociencia']
    p1 = [L_S[s] for s in _p1]
    corpo = cabeca('Comece aqui', 'Novo em ciência? Comece por aqui', 'Um caminho curto para ter o básico em cerca de uma hora. Depois, siga pelo tema que mais te interessar.')
    corpo += f'''<div class="wrap secao"><h2>1. Entenda o básico</h2><p>Oito lições curtas, nesta ordem: o que é ciência, opinião e conhecimento, a postura científica, o método, a evidência e a pseudociência.</p><div class="grade">{"".join(cartao_licao(l) for l in p1)}</div>
<h2 style="margin-top:2.4rem">2. Treine o olhar</h2><div class="grade">{cartao_ferr(*FERR_D['ciencia-ou-pseudociencia'])}{cartao_ferr(*FERR_D['detector-de-pseudociencia'])}{cartao_ferr(*FERR_D['correlacao-ou-causa'])}</div>
<h2 style="margin-top:2.4rem">3. Veja casos reais</h2><div class="grade"><a class="cartao" href="pseudociencias.html">{arte.icone("lupa")}<h3>Pseudociências</h3><p>{len(PSEUDO)} casos analisados, da astrologia à cura quântica.</p></a><a class="cartao" href="debates.html">{arte.icone("valor")}<h3>Debates</h3><p>{len(DEBATES)} discussões sobre ciência e sociedade.</p></a></div>
<h2 style="margin-top:2.4rem">4. Vá mais fundo</h2><div class="grade"><a class="cartao" href="correntes.html">{arte.icone("arvore")}<h3>Correntes</h3><p>{len(COR)} correntes, com forças e objeções.</p></a><a class="cartao" href="pensadores.html">{arte.icone("pessoa")}<h3>Pensadores</h3><p>{len(PES)} cientistas e filósofos.</p></a><a class="cartao" href="biblioteca.html">{arte.icone("livro")}<h3>Biblioteca</h3><p>Livros por nível e sites para continuar.</p></a></div></div>'''
    page('comece-aqui.html', 'Comece aqui', 'Um caminho curto para entender o básico de ciência, método e evidência em cerca de uma hora.', corpo, atual='comece-aqui.html')

def catalogo():
    bt = lambda k, v, t: f'<button type="button" data-k="{k}" data-v="{v}" aria-pressed="false">{e(t)}</button>'
    filt = '<div class="filtros" role="group" aria-label="Nível">' + bt('nivel', '', 'Todos os níveis') + ''.join(bt('nivel', s, r) for s, r, *_ in NIVEIS) + bt('nivel', 'ferr', 'Ferramentas') + '</div><div class="filtros" role="group" aria-label="Tema">' + bt('tema', '', 'Todos os temas') + ''.join(bt('tema', k, v) for k, v in TEMAS.items()) + '</div>'
    itens = ''.join(cartao_licao(l) for l in TODAS) + ''.join(cartao_ferr(*f) for f in FERR)
    corpo = cabeca('Lições', 'Todas as lições', 'Filtre por nível ou por tema.') + f'<div class="wrap secao"><input class="fq" id="fq" type="search" placeholder="Filtrar por palavra" aria-label="Filtrar"/>{filt}<p class="contagem" id="contagem" role="status"></p><div class="grade" id="catalogo">{itens}</div></div>'
    page('catalogo.html', 'Todas as lições', 'Todas as lições e ferramentas de ciência e epistemologia, com filtros por nível e tema.', corpo, atual='catalogo.html')

# ---------- camada didática ----------
def bloco_didatico(l):
    pre = ', '.join(f'<a href="{p}.html">{e(L_S[p]["titulo"])}</a>' for p in l['pre'])
    pre = f'<p class="pre">Ajuda ter lido: {pre}.</p>' if pre else ''
    obj = '<div class="objetivos"><p class="k">Ao fim desta lição, você vai conseguir</p><ul>' + ''.join(f'<li>{e(o)}</li>' for o in l['obj']) + '</ul>' + pre + '</div>'
    caso = f'<div class="caso-abre"><p class="k">Antes de ler: o que você pensa?</p><p>{e(l["caso"][0])}</p><p class="q">{e(l["caso"][1])}</p><details><summary>Ver o que a lição responde</summary><p>{e(l["caso"][2])}</p></details></div>'
    return obj + caso
def erro_pratica(l):
    out = f'<div class="nota erro-comum"><strong>Erro comum:</strong> <em>{e(l["erro"][0])}</em> {e(l["erro"][1])}</div>'
    if l['ferr']:
        f = FERR_D[l['ferr']]
        out += f'<div class="nota"><strong>Pratique:</strong> <a href="ferramentas/{f[0]}.html">{e(f[1])}</a>. {e(f[2])}</div>'
    return out
def quizzes(l):
    q = l['quiz']
    return bloco_quiz(q[0], 'Teste rápido · 1 de 3') + bloco_quiz(q[1], 'Aplique · 2 de 3') + bloco_quiz(q[2], 'Confira · 3 de 3')
def fecho(l):
    return f'<section class="fecho"><h2>Para guardar</h2><ul>{"".join(f"<li>{e(g)}</li>" for g in l["guardar"])}</ul><div class="pensar"><p class="k">Para pensar</p><p>{e(l["pensar"])}</p></div></section>'
def liga_licao(l):
    cs = [c for c in COR if l['slug'] in c['licoes']]
    ps = [p for p in PSEUDO if l['slug'] in p['licoes']]
    dbs = [d for d in DEBATES if l['slug'] in d['licoes']]
    out = ''
    if cs: out += '<div class="nota"><strong>Correntes desta lição:</strong> ' + ', '.join(clink(c['s']) for c in cs) + '.</div>'
    if ps: out += '<div class="nota"><strong>Casos para testar:</strong> ' + ', '.join(f'<a href="pseudociencias/{p["s"]}.html">{e(p["n"])}</a>' for p in ps) + '.</div>'
    if dbs: out += '<div class="nota"><strong>Nos debates:</strong> ' + ', '.join(f'<a href="debates/{d["s"]}.html">{e(d["n"])}</a>' for d in dbs) + '.</div>'
    if BV_LICAO.get(l['slug']): out += bv_nota(BV_LICAO[l['slug']])
    return out

def trilhas():
    secs = ''
    for t in TRILHAS:
        for s in t['licoes']: assert s in L_S, (t['s'], s)
        ls = [L_S[s] for s in t['licoes']]
        prog = f'<div class="barra-prog" id="pg-{t["s"]}" data-prog="{",".join(t["licoes"])}" style="max-width:420px"><i></i></div><small data-prog-t="pg-{t["s"]}"></small>'
        cards = ''.join(f'<div class="trilha-item"><span class="trilha-n">{i + 1}</span>{cartao_licao(l)}</div>' for i, l in enumerate(ls))
        secs += f'<section class="trilha-sec" id="{t["s"]}"><h2 class="grupo">{e(t["n"])} <small>{e(t["tempo"])} · {len(ls)} lições</small></h2><p>{e(t["d"])}</p>{prog}<div class="grade trilha-grade">{cards}</div></section>'
    corpo = cabeca('Aprender', 'Trilhas de estudo', f'{len(TRILHAS)} caminhos curtos por tema, na ordem em que valem ser lidos. O progresso fica salvo no seu navegador.')
    corpo += f'<div class="wrap secao" style="padding-top:18px"><div class="nota" style="margin-top:0"><strong>Como usar:</strong> escolha a trilha que responde à sua pergunta de agora e siga a ordem. As trilhas se cruzam; uma lição lida conta em todas. Para o curso completo, siga os três níveis: <a href="iniciante.html">Iniciante</a>, <a href="intermediario.html">Intermediário</a> e <a href="avancado.html">Avançado</a>.</div>{secs}</div>'
    page('trilhas.html', 'Trilhas de estudo', 'Trilhas curtas de ciência por tema: o essencial, saúde e evidência, filosofia da ciência e desinformação.', corpo, atual='trilhas.html')

def teste_nivel(slug, rot, ls):
    itens = [mistura([q[0], q[1], q[2], q[3] + f' (Lição: {l["titulo"]}.)']) for l in ls for q in l['quiz']]
    dd = json.dumps(dict(itens=itens, n=10), ensure_ascii=False).replace('</', '<\\/')
    corpo = cabeca(f'<a href="{slug}.html">{e(rot)}</a>', f'Teste do nível {rot}', f'Dez perguntas sorteadas entre as {len(itens)} do nível. Cada resposta diz em que lição rever o assunto. Refaça quantas vezes quiser: as perguntas mudam.')
    corpo += f'<div class="wrap estreito secao"><div id="jogo" class="quiz" style="margin-top:0"><div class="placar"><span></span><span></span></div><div class="barra-prog"><i></i></div><div class="alvo" style="margin-top:14px"></div><button class="btn prox-q" type="button" style="margin-top:12px" hidden>Próxima</button></div><script type="application/json" id="dados-teste">{dd}</script><p class="legenda">Acertou 8 ou mais? Você está pronto para o próximo nível. Menos que isso: veja as lições indicadas e tente de novo.</p><p><a class="btn alt" href="{slug}.html">Voltar ao nível {e(rot)}</a></p></div>'
    page(f'teste-{slug}.html', f'Teste do nível {rot}', f'Dez perguntas sorteadas sobre as lições do nível {rot} de ciência, com a lição a rever em cada resposta.', corpo, atual=f'{slug}.html')

def revisao(slug, rot, ls):
    grupos = {}
    for l in ls: grupos.setdefault(l['grupo'], []).append(l)
    cont = f'<div class="nota placar" id="placar-rev" data-total="{len(ls)}" role="status">Responda às perguntas para ver seu placar. Cada uma pede que você aplique a lição a um caso: se errar, o link leva de volta a ela.</div>'
    for gr, its in grupos.items():
        cont += f'<h2 class="grupo">{e(gr)}</h2>'
        for l in its: cont += f'<div class="rev-item"><h3><a href="{l["slug"]}.html">Lição {l["i"] + 1}: {e(l["titulo"])}</a></h3>{bloco_quiz(l["quiz"][2], "Aplique")}</div>'
    ordem = [n[0] for n in NIVEIS]
    if slug != ordem[-1]:
        seg = NIVEIS[ordem.index(slug) + 1]
        cont += f'<div class="fim-nivel"><p class="ti">Pronto para o próximo nível?</p><p>Continue com {len(seg[2])} lições do nível {e(seg[1])}.</p><a class="btn {seg[5]}" href="{seg[0]}.html">Ir para o curso {e(seg[1])} →</a></div>'
    else:
        cont += '<div class="fim-nivel"><p class="ti">Você concluiu o curso</p><p>Siga pelas correntes, pelos debates e pelos casos de pseudociência.</p><a class="btn a" href="correntes.html">Correntes</a> <a class="btn alt" href="debates.html">Debates</a></div>'
    page(f'revisao-{slug}.html', f'Revisão do nível {rot}', f'{len(ls)} perguntas de aplicação, uma por lição do nível {rot}, com placar e link de volta para cada lição.', cabeca(f'<a href="{slug}.html">{e(rot)}</a> / Revisão', f'Revisão do nível {rot}', 'Uma pergunta de aplicação por lição. Responda, veja o placar e volte às lições em que errou.') + f'<div class="wrap secao revisao-pag">{cont}</div>', atual=f'{slug}.html')

def nivel(slug, rot, ls, titulo, desc, g):
    grupos = {}
    for l in ls: grupos.setdefault(l['grupo'], []).append(l)
    cont = ''
    for gr, its in grupos.items():
        cont += f'<h2 class="grupo">{e(gr)}</h2><div class="grade">{"".join(cartao_licao(l) for l in its)}</div>'
    extra = {'iniciante': ['ciencia-ou-pseudociencia', 'opiniao-crenca-ou-conhecimento', 'nivel-de-evidencia'], 'intermediario': ['que-corrente-e-essa', 'detector-de-pseudociencia', 'correlacao-ou-causa'], 'avancado': ['quem-disse', 'que-corrente-e-essa']}[slug]
    cont += '<h2 class="grupo">Experimente</h2><div class="grade">' + ''.join(cartao_ferr(*FERR_D[x]) for x in extra) + '</div>'
    tot = sum(tempo_leitura(l['corpo']) for l in ls); h = round(tot / 60)
    dur = f'cerca de {h} hora{"s" if h > 1 else ""} de leitura' if h >= 1 else f'cerca de {tot} minutos de leitura'
    como = f'<div class="como-estudar"><h2>Como estudar este nível</h2><p>{len(ls)} lições em {len(grupos)} blocos, {dur}, em sessões de 10 a 15 minutos.</p><ol><li><strong>Siga a ordem dos blocos.</strong> Cada lição começa dizendo o que você vai aprender e o que ajuda ter lido antes.</li><li><strong>Responda ao caso de abertura antes de ler:</strong> prever e depois conferir é o que mais fixa, e é também o espírito do método científico.</li><li><strong>Não pule o fim da lição:</strong> os pontos para guardar, a pergunta para pensar, o erro comum e os três testes.</li><li><strong>Marque como lida</strong> para acompanhar o progresso e receber lições para revisar.</li><li><strong>Feche com a <a href="revisao-{slug}.html">revisão do nível</a></strong> (uma pergunta por lição, com placar) e o <a href="teste-{slug}.html">teste do nível</a> (dez sorteadas). Para estudar por tema, use as <a href="trilhas.html">trilhas</a>.</li></ol></div>'
    cont = como + f'<div class="nivel-acoes"><a class="btn alt" href="revisao-{slug}.html">Revisão: {len(ls)} perguntas</a> <a class="btn alt" href="teste-{slug}.html">Teste do nível: 10 sorteadas</a> <a class="btn alt" href="trilhas.html">Trilhas por tema</a></div><section class="revisao" hidden><h2 class="grupo">Revise o que leu há mais tempo</h2><p>A memória precisa de revisão espaçada. Estas são as lições deste nível que você marcou como lidas há mais tempo.</p><div class="grade" id="rev-grade"></div></section>' + cont
    prog = f'<div class="barra-prog" id="pg-{slug}" data-prog="{",".join(l["slug"] for l in ls)}" style="max-width:420px;background:#ffffff33"><i></i></div><small data-prog-t="pg-{slug}" style="color:#fff"></small>'
    page(f'{slug}.html', titulo, desc, cabeca(f'Nível {rot}', titulo, e(desc), meta=f'<div style="margin-top:1.1rem">{prog}</div>') + f'<div class="wrap secao" style="padding-top:18px">{cont}</div>', atual=f'{slug}.html')

def indice(l, ls):
    i = l['i']; n = len(ls)
    def seta(alvo, rel, sim, rot):
        if alvo: return f'<a class="indice-seta" rel="{rel}" href="{alvo["slug"]}.html" aria-label="{rot}: {e(alvo["titulo"])}" title="{rot}: {e(alvo["titulo"])}">{sim}</a>'
        return f'<span class="indice-seta off" aria-hidden="true">{sim}</span>'
    pontos = ''
    for j, x in enumerate(ls):
        rot = f'Lição {j + 1}: {e(x["titulo"])}'
        atual = ' aria-current="page"' if j == i else ''
        pontos += f'<li><a href="{x["slug"]}.html" data-ponto="{x["slug"]}" title="{rot}" aria-label="{rot}"{atual}></a></li>'
    return f'<nav class="indice {l["nivel"]}" aria-label="Lições do nível {e(l["nivel_rot"])}"><div class="wrap"><p class="indice-pos"><a href="{l["nivel"]}.html">{e(l["nivel_rot"])}</a> · Lição {i + 1} de {n}</p><div class="indice-nav">{seta(ls[i - 1] if i else None, "prev", "←", "Lição anterior")}<ol>{pontos}</ol>{seta(ls[i + 1] if i + 1 < n else None, "next", "→", "Próxima lição")}</div></div></nav>'

def licao(l, ls):
    i = l['i']; ant = ls[i - 1] if i else None; prox = ls[i + 1] if i + 1 < len(ls) else None
    pager = '<nav class="pager" aria-label="Lições">'
    if ant: pager += f'<a href="{ant["slug"]}.html"><small>← Anterior</small>{e(ant["titulo"])}</a>'
    if prox: pager += f'<a class="prox" href="{prox["slug"]}.html"><small>Próxima →</small>{e(prox["titulo"])}</a>'
    pager += '</nav>'
    ordem = [n[0] for n in NIVEIS]
    if not prox and l['nivel'] != ordem[-1]:
        seg = NIVEIS[ordem.index(l['nivel']) + 1]
        pager += f'<div class="fim-nivel"><p class="ti">Você chegou ao fim do nível {e(l["nivel_rot"])}</p><p>Faça o teste do nível e continue com {len(seg[2])} lições do nível {e(seg[1])}.</p><a class="btn alt" href="revisao-{l["nivel"]}.html">Revisão do nível</a> <a class="btn alt" href="teste-{l["nivel"]}.html">Teste do nível</a> <a class="btn {seg[5]}" href="{seg[0]}.html">Ir para o curso {e(seg[1])} →</a></div>'
    if not prox and l['nivel'] == ordem[-1]:
        pager += f'<div class="fim-nivel"><p class="ti">Você chegou ao fim do curso</p><p>Faça o teste do nível e siga pelas correntes e pelos debates, ou continue do lado da ética.</p><a class="btn alt" href="revisao-avancado.html">Revisão do nível</a> <a class="btn alt" href="teste-avancado.html">Teste do nível</a> <a class="btn a" href="correntes.html">Correntes</a> <a class="btn" href="https://eticaparainiciantes.biblioverse.org/" {EXT}>Ética Para Iniciantes →</a></div>'
    min_ = tempo_leitura(l['corpo'])
    tg = ''.join(f'<a class="tag" href="catalogo.html?tema={t}">{e(TEMAS[t])}</a>' for t in l['temas'])
    meta = f'<div class="meta"><span class="tipo {l["nivel"]}">{e(l["nivel_rot"])}</span>{tg}<span>{min_} min de leitura</span></div>'
    topo = cabeca(f'<a href="{l["nivel"]}.html">{e(l["nivel_rot"])}</a> / {e(l["grupo"])}', l['titulo'], e(l['resumo']), meta=meta)
    antes = ('<dt>Antes</dt><dd>' + ', '.join(f'<a href="{s}.html">{e(L_S[s]["titulo"])}</a>' for s in l['pre']) + '</dd>') if l['pre'] else ''
    lado = f'''<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Nível</dt><dd>{e(l["nivel_rot"])}</dd><dt>Tempo</dt><dd>{min_} minutos</dd><dt>Temas</dt><dd>{e(", ".join(TEMAS[t] for t in l["temas"]))}</dd>{antes}</dl></div><div class="caixa toc-caixa"><h2>Nesta lição</h2><ul class="toc"></ul></div><button class="marcar" type="button" data-id="{l["slug"]}">Marcar como lida</button></aside>'''
    ct = l['corpo']; k = ct.index('</section></div>', ct.index('class="ajuda"')) + len('</section></div>')
    ct = glossa(ct[:k] + bloco_didatico(l) + ct[k:], l['titulo'])
    corpo = indice(l, ls) + topo + f'<div class="wrap layout"><article class="leitura">{tabelas(ct)}{fecho(l)}{erro_pratica(l)}{liga_licao(l)}{quizzes(l)}{fontes(l["fontes"])}{pager}</article>{lado}</div>' + relacionados(l)
    page(f'{l["slug"]}.html', l['titulo'], l['resumo'], corpo, atual=f'{l["nivel"]}.html')

# ---------- correntes ----------
def nao_e_html(nome, itens):
    li = ''.join(f'<li><p class="nao-e-dito">{e(d)}</p><p>{e(c)}</p></li>' for d, c in itens)
    return f'<h2 id="o-que-nao-e">O que não é {e(nome[0].lower() + nome[1:])}</h2><p class="legenda">Concepções erradas e espantalhos que costumam aparecer em conversas e debates, com a correção.</p><ul class="lista-nao-e">{li}</ul>'
def correntes():
    arvore = ''
    for f in FAMILIAS:
        its = [c for c in COR if c['f'] == f]
        arvore += f'<section class="familia"><h3><span class="tipo fam f{COR_FAM[f]}">{e(f)}</span> <small>{e(FOCO_FAM[f])}</small></h3><div class="fio">' + ''.join(f'<a href="correntes/{c["s"]}.html">{e(c["n"])}</a>' for c in its) + '</div></section>'
    bots = '<button type="button" data-k="f" data-v="" aria-pressed="true">Todas</button>' + ''.join(f'<button type="button" data-k="f" data-v="{e(f)}" aria-pressed="false">{e(f)}</button>' for f in FAMILIAS)
    gr = ''.join(f'<section class="grupo-l"><h2 class="grupo">{e(f)} <small>{e(FOCO_FAM[f])}</small></h2><div class="grade">' + ''.join(cartao_c(c, 'correntes/') for c in COR if c['f'] == f) + '</div></section>' for f in FAMILIAS)
    dados_t = json.dumps([dict(s=c['s'], n=c['n'], f=c['f'], foco=c['foco'], i=re.sub('<[^>]+>', '', c['i']), astro=c['astro'], forte=c['forte'], contra=c['contra'], p=c['p']) for c in COR], ensure_ascii=False).replace('</', '<\\/')
    comp = f'<h2 style="margin:2.2rem 0 .8rem">Compare</h2><div class="grade" style="grid-template-columns:repeat(auto-fit,minmax(170px,1fr));margin-bottom:14px"><label class="campo">Corrente 1<select id="ta"></select></label><label class="campo">Corrente 2<select id="tb"></select></label><label class="campo">Corrente 3<select id="tc"></select></label></div><div class="tabela"><table class="compara" id="tcomp"></table></div><script type="application/json" id="dados-teo">{dados_t}</script>'
    corpo = cabeca('Ideias', 'Correntes da epistemologia e da filosofia da ciência', f'{len(COR)} correntes sobre de onde vem o conhecimento, como se justifica uma crença e o que faz a ciência funcionar: o que cada uma põe no centro, forças e objeções.')
    corpo += f'<div class="wrap secao"><div class="nota" style="margin-top:0"><strong>Como ler:</strong> cada corrente aparece pelo seu <em>ponto focal</em>, o que ela põe no centro da explicação do conhecimento. Quase nenhuma nega o que as outras destacam: o empirista usa a lógica, o racionalista usa a experiência, o popperiano usa observações. A diferença está no que vem primeiro. As famílias vão das fontes do conhecimento até a relação entre ciência e sociedade.</div><div class="sec-cab"><h2>O mapa</h2><p>Clique em uma corrente para abrir.</p></div>{arvore}{comp}<h2 style="margin:2.2rem 0 .8rem">Todas</h2><input class="fq" id="fq" type="search" placeholder="Filtrar por nome ou ideia" aria-label="Filtrar"/><div class="filtros" role="group" aria-label="Família">{bots}</div><p class="contagem" id="contagem" role="status"></p><div id="lista">{gr}</div></div>'
    page('correntes.html', 'Correntes', 'Empirismo, racionalismo, positivismo, falsificacionismo, Kuhn, Lakatos, bayesianismo, realismo e construtivismo: o centro de cada corrente.', corpo, atual='correntes.html')
    for i, c in enumerate(COR):
        wiki = ('https://pt.wikipedia.org/wiki/' + c['w'][3:]) if c['w'].startswith('pt:') else 'https://en.wikipedia.org/wiki/' + c['w']
        pes = ''.join(f'<a href="../pensadores/{p["slug"]}.html" class="tipo ferr">{e(p["nome"])}</a>' for p in PES if c['s'] in p['correntes'] or p['slug'] in c['pes'])
        liga = f'<h2>Pensadores ligados</h2><p class="tags">{pes}</p>' if pes else ''
        ler = lista_mais('Lições', [f'<a href="../{s}.html">{e(L_S[s]["titulo"])}</a>' for s in c['licoes']])
        ler += lista_mais('Nos debates', [f'<a href="../debates/{d["s"]}.html">{e(d["n"])}</a>' for d in DEBATES if any(x[0] == c['s'] for x in d['visoes'])])
        for s in c['licoes']: assert s in L_S, (c['s'], s)
        mesmas = [x for x in COR if x['f'] == c['f'] and x['s'] != c['s']][:3]
        ant, prox = COR[i - 1], COR[(i + 1) % len(COR)]
        lado = f'<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Família</dt><dd>{e(c["f"])}</dd><dt>O que põe no centro</dt><dd>{e(c["foco"])}</dd></dl></div><div class="caixa toc-caixa"><h2>Nesta página</h2><ul class="toc"></ul></div></aside>'
        corpo = cabeca('<a href="../correntes.html">Correntes</a>', c['n'], e(c['r']), meta=f'<div class="meta"><span class="tipo fam f{COR_FAM[c["f"]]}">{e(c["f"])}</span></div>')
        corpo += f'''<div class="wrap layout"><article class="leitura"><div class="nota" style="margin-top:0"><strong>Ponto focal:</strong> {e(c["foco"])} É o que mais pesa para esta corrente, não a única coisa que ela considera.</div><h2>A ideia central</h2><p>{c["i"]}</p>
<h2>Referências</h2><p>{e(c["p"])}</p><h2>De onde veio</h2><p>{c["h"]}</p><h2>Diante da astrologia</h2><p>{e(c["astro"])} <a href="../pseudociencias/astrologia.html">Veja o caso da astrologia</a>.</p>
<h2>Pontos fortes: o que pode estar certo</h2><ul class="lista-forte">{"".join(f"<li>{e(x)}</li>" for x in c["forte"])}</ul><h2>Objeções</h2><ul class="lista-contra">{"".join(f"<li>{e(x)}</li>" for x in c["contra"])}</ul><h2>O que dizem os críticos</h2><p>{e(c["c"])}</p>{nao_e_html(c["n"], NAO_E[c["s"]])}{liga}{ler}
{fontes([("Wikipédia: " + c["n"], wiki)] + c["fx"])}<nav class="pager" aria-label="Correntes"><a href="{ant["s"]}.html"><small>← Anterior</small>{e(ant["n"])}</a><a class="prox" href="{prox["s"]}.html"><small>Próxima →</small>{e(prox["n"])}</a></nav></article>{lado}</div><section class="relac"><div class="wrap"><h2>Na mesma família</h2><div class="grade">{"".join(cartao_c(x) for x in mesmas)}</div></div></section>'''
        page(f'correntes/{c["s"]}.html', c['n'], c['r'], corpo, atual='correntes.html')

# ---------- pseudociências ----------
def pseudociencias():
    bots = '<button type="button" data-k="t" data-v="" aria-pressed="true">Todos</button>' + ''.join(f'<button type="button" data-k="t" data-v="{e(t)}" aria-pressed="false">{e(t)}</button>' for t in TEMAS_P)
    bots_s = '<button type="button" data-k="s" data-v="" aria-pressed="true">Qualquer situação</button>' + ''.join(f'<button type="button" data-k="s" data-v="{e(k)}" aria-pressed="false">{e(k)}</button>' for k in STATUS)
    gr = ''.join(f'<section class="grupo-l"><h2 class="grupo">{e(t)}</h2><div class="grade">' + ''.join(cartao_ps(p, 'pseudociencias/') for p in PSEUDO if p['t'] == t) + '</div></section>' for t in TEMAS_P)
    leg = ''.join(f'<li><span class="peso {v[0]}">{e(k)}</span> {e(v[1])}</li>' for k, v in STATUS.items())
    sin = ''.join(f'<li><strong>{e(v[0])}.</strong> {e(v[1])}</li>' for v in SINAIS.values())
    corpo = cabeca('Ideias', 'Pseudociências', f'{len(PSEUDO)} práticas e crenças que se apresentam como científicas: o que alegam, o que a evidência diz, que sinais de alerta mostram e por que atraem tanta gente.')
    corpo += f'''<div class="wrap secao"><div class="nota" style="margin-top:0"><strong>Como ler:</strong> chamar algo de pseudociência é uma afirmação forte, e cada página diz por quê, com fontes. Não é um julgamento sobre quem acredita: essas ideias exploram vieses que todos temos e muitas vezes oferecem acolhimento que o atendimento convencional não deu. Práticas de bem-estar, como meditação ou massagem, não são pseudociência quando prometem só o que entregam; o problema aparece quando a promessa é curar o que não curam.</div><ul class="leg-peso">{leg}</ul><details class="mais" style="margin:1rem 0"><summary>Os sinais de alerta usados nas páginas</summary><ul>{sin}</ul></details>{bv_nota(['conspiracy'])}<input class="fq" id="fq" type="search" placeholder="Filtrar por nome ou tema" aria-label="Filtrar pseudociências"/><div class="filtros" role="group" aria-label="Tema">{bots}</div><div class="filtros" role="group" aria-label="Situação">{bots_s}</div><p class="contagem" id="contagem" role="status"></p><div id="lista">{gr}</div></div>'''
    page('pseudociencias.html', 'Pseudociências', 'Astrologia, homeopatia, terra plana, constelação familiar, cura quântica, antivacina e outras: o que alegam e o que a evidência diz.', corpo, atual='pseudociencias.html')
    for i, p in enumerate(PSEUDO):
        for s in p['licoes']: assert s in L_S, (p['s'], s)
        sinais = ''.join(f'<li><strong>{e(SINAIS[x][0])}.</strong> {e(SINAIS[x][1])}</li>' for x in p['sinais'])
        ler = ('<p><strong>Lições relacionadas:</strong> ' + ', '.join(f'<a href="../{s}.html">{e(L_S[s]["titulo"])}</a>' for s in p['licoes']) + '.</p>') if p['licoes'] else ''
        mesmos = [x for x in PSEUDO if x['t'] == p['t'] and x['s'] != p['s']][:3]
        ant, prox = PSEUDO[i - 1], PSEUDO[(i + 1) % len(PSEUDO)]
        corpo = cabeca('<a href="../pseudociencias.html">Pseudociências</a> / ' + e(p['t']), p['n'], e(p['r']), meta=f'<div class="meta"><span class="peso {STATUS[p["status"]][0]}">{e(p["status"])}</span></div>')
        corpo += f'''<div class="wrap estreito leitura secao"><p class="legenda"><strong>Origem:</strong> {e(p["o"])}</p><h2>O que alega</h2><p>{p["alega"]}</p><h2>O que a evidência diz</h2><p>{p["evid"]}</p><div class="nota veredito {STATUS[p["status"]][0]}"><strong>{e(p["status"])}</strong><p>{e(STATUS[p["status"]][1])}</p></div><h2>Sinais de alerta</h2><ul class="lista-contra">{sinais}</ul><h2>Por que atrai tanta gente</h2><p>{e(p["atrai"])}</p><h2>Riscos</h2><p>{e(p["risco"])}</p><h2>Perguntas para pensar</h2><ol class="roteiro"><li>Que resultado mostraria que a prática não funciona? Quem a defende aceitaria esse resultado?</li><li>A evidência a favor vem de depoimentos ou de estudos com grupo controle?</li><li>O que eu perderia se trocasse um tratamento eficaz por este?</li></ol>{ler}{fontes(p["fx"])}<nav class="pager" aria-label="Pseudociências"><a href="{ant["s"]}.html"><small>← Anterior</small>{e(ant["n"])}</a><a class="prox" href="{prox["s"]}.html"><small>Próxima →</small>{e(prox["n"])}</a></nav></div><section class="relac"><div class="wrap"><h2>No mesmo tema</h2><div class="grade">{"".join(cartao_ps(x) for x in mesmos)}</div></div></section>'''
        page(f'pseudociencias/{p["s"]}.html', p['n'], p['r'], corpo, atual='pseudociencias.html')

# ---------- debates ----------
def cartao_db(d, pre=''): return f'<a class="cartao item" data-t="{e(d["t"])}" data-p="{d["p"][0]}" href="{pre}{d["s"]}.html"><span class="linha-cartao"><span class="peso {d["p"][0]}">{e(ROT_PESO[d["p"][0]])}</span></span><h3>{e(d["n"])}</h3><p>{e(d["r"])}</p></a>'
def debates_pub():
    bots = '<button type="button" data-k="t" data-v="" aria-pressed="true">Todos</button>' + ''.join(f'<button type="button" data-k="t" data-v="{e(t)}" aria-pressed="false">{e(t)}</button>' for t in TEMAS_DB)
    gr = ''.join(f'<section class="grupo-l"><h2 class="grupo">{e(t)}</h2><div class="grade">' + ''.join(cartao_db(d, 'debates/') for d in DEBATES if d['t'] == t) + '</div></section>' for t in TEMAS_DB)
    leg = ''.join(f'<li><span class="peso {k}">{e(v)}</span></li>' for k, v in ROT_PESO.items())
    botp = '<button type="button" data-k="p" data-v="" aria-pressed="true">Qualquer peso</button>' + ''.join(f'<button type="button" data-k="p" data-v="{k}" aria-pressed="false">{e(v)}</button>' for k, v in ROT_PESO.items())
    corpo = cabeca('Ideias', 'Debates sobre ciência', f'{len(DEBATES)} questões que dividem cientistas, filósofos e o público: os lados, o que as correntes dizem, por que é complexo e para onde a evidência aponta.')
    corpo += f'''<div class="wrap secao"><div class="nota" style="margin-top:0"><strong>Como ler:</strong> quando há posições razoáveis dos dois lados, mostramos as duas. Quando a evidência ou o consenso dos especialistas pesa para um lado, damos a ele mais ênfase e dizemos por quê. Essa avaliação é do site e pode ser contestada; cada página traz as fontes.</div><ul class="leg-peso">{leg}</ul><input class="fq" id="fq" type="search" placeholder="Filtrar por nome ou tema" aria-label="Filtrar debates"/><div class="filtros" role="group" aria-label="Tema">{bots}</div><div class="filtros" role="group" aria-label="Peso">{botp}</div><p class="contagem" id="contagem" role="status"></p><div id="lista">{gr}</div></div>'''
    page('debates.html', 'Debates sobre ciência', 'Psicanálise é ciência? A ciência é neutra? Práticas integrativas no SUS, crise de replicação, testes em animais e mais: os lados e a evidência.', corpo, atual='debates.html')
    for i, d in enumerate(DEBATES):
        lado = lambda x: f'<div><h3>{e(x[0])}</h3><ul>' + ''.join(f'<li>{e(p)}</li>' for p in x[1]) + '</ul></div>'
        lados = f'<div class="dois-lados">{"".join(lado(x) for x in d["lados"])}</div>' if len(d['lados']) > 1 else lado(d['lados'][0]).replace('<div>', '<div class="caso">', 1)
        tab = ''.join(f'<tr><th>{clink(s, "../")}</th><td>{e(x)}</td></tr>' for s, x in d['visoes'])
        tab = f'<h2>O que as correntes tendem a dizer</h2><div class="tabela"><table class="compara"><tbody>{tab}</tbody></table></div>' if tab else ''
        ler = '<p><strong>Lições relacionadas:</strong> ' + ', '.join(f'<a href="../{s}.html">{e(L_S[s]["titulo"])}</a>' for s in d['licoes']) + '.</p>'
        mesmos = [x for x in DEBATES if x['t'] == d['t'] and x['s'] != d['s']][:3]
        ant, prox = DEBATES[i - 1], DEBATES[(i + 1) % len(DEBATES)]
        corpo = cabeca('<a href="../debates.html">Debates</a> / ' + e(d['t']), d['n'], e(d['r']))
        bts = ''.join(f'<button type="button" data-v="{j}" aria-pressed="false">{e(x[0])}</button>' for j, x in enumerate(d['lados'])) + '<button type="button" data-v="ns" aria-pressed="false">Ainda não sei</button>'
        pos1 = f'<div class="posicao" data-deb="{d["s"]}"><p class="k">Antes de ler: para que lado você pende?</p><div class="ops">{bts}</div><p class="fb" role="status"></p></div>' if len(d['lados']) > 1 else ''
        pos2 = f'<div class="posicao depois" data-deb="{d["s"]}"><p class="k">E agora, depois de ler?</p><div class="ops">{bts}</div><p class="fb" role="status"></p></div>' if len(d['lados']) > 1 else ''
        corpo += f'''<div class="wrap estreito leitura secao"><p class="abre">{e(d["v"])}</p>{pos1}<h2>{"Os lados" if len(d["lados"]) > 1 else "A posição"}</h2>{lados}<p class="legenda">Posições gerais. Muita gente concorda em parte com cada lado.</p>{tab}<h2>Por que é complexo</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in d["c"])}</ul><h2>Para onde a evidência aponta</h2><div class="nota veredito {d["p"][0]}"><strong>{e(ROT_PESO[d["p"][0]])}</strong><p>{e(d["p"][1])}</p></div><p class="legenda">Avaliação do site, sujeita a críticas. Evidências e argumentos novos podem mudá-la.</p>{pos2}<h2>Perguntas para pensar</h2><ol class="roteiro"><li>Qual parte da discussão é sobre fatos, e qual é sobre valores?</li><li>Que evidência faria cada lado mudar de ideia?</li><li>Quem ganha e quem perde com cada resposta?</li><li>O que me faria mudar de ideia?</li></ol>{ler}{fontes(d["fx"])}<nav class="pager" aria-label="Debates"><a href="{ant["s"]}.html"><small>← Anterior</small>{e(ant["n"])}</a><a class="prox" href="{prox["s"]}.html"><small>Próximo →</small>{e(prox["n"])}</a></nav></div><section class="relac"><div class="wrap"><h2>No mesmo tema</h2><div class="grade">{"".join(cartao_db(x) for x in mesmos)}</div></div></section>'''
        page(f'debates/{d["s"]}.html', d['n'], d['r'], corpo, atual='debates.html')

# ---------- pensadores ----------
def pensadores():
    bots = '<button type="button" data-k="c" data-v="" aria-pressed="true">Todos</button>' + ''.join(f'<button type="button" data-k="c" data-v="{e(a)}" aria-pressed="false">{e(a)}</button>' for a in AREAS)
    gr = ''.join(f'<section class="grupo-l"><h2 class="grupo">{e(a)}</h2><div class="grade">' + ''.join(cartao_p(p, 'pensadores/') for p in PES if p['area'] == a) + '</div></section>' for a in AREAS)
    corpo = cabeca('Ideias', 'Pensadores', f'{len(PES)} cientistas, filósofos, sociólogos e divulgadores que moldaram a forma como entendemos a ciência: ideias, obras e críticas.')
    corpo += f'''<div class="wrap secao"><div class="nota" style="margin-top:0"><strong>Como ler:</strong> cada perfil é um resumo, não uma biografia. As ideias estão simplificadas, e a seção de críticas mostra onde cada autor é mais contestado. Os erros de grandes pensadores ensinam tanto quanto os acertos.</div><input class="fq" id="fq" type="search" placeholder="Filtrar por nome ou ideia" aria-label="Filtrar pensadores"/><div class="filtros" role="group" aria-label="Área">{bots}</div><p class="contagem" id="contagem" role="status"></p><div id="lista">{gr}</div></div>'''
    page('pensadores.html', 'Pensadores', 'Bacon, Galileu, Hume, Comte, Popper, Kuhn, Lakatos, Feyerabend, Sagan, Haack, Oreskes e outros: ideias, obras e críticas.', corpo, atual='pensadores.html')
    for i, p in enumerate(PES):
        cs = ''.join(clink(s, '../', 'tipo fam f' + str(COR_FAM[COR_S[s]['f']])) for s in p['correntes'])
        liga = f'<h2>Correntes ligadas</h2><p class="tags">{cs}</p>' if cs else ''
        mesmos = [x for x in PES if x['area'] == p['area'] and x['slug'] != p['slug']][:3]
        ant, prox = PES[i - 1], PES[(i + 1) % len(PES)]
        lado = f'<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Viveu</dt><dd>{e(p["anos"])}</dd><dt>Onde</dt><dd>{e(p["pais"])}</dd><dt>Área</dt><dd>{e(p["area"])}</dd></dl></div><div class="caixa toc-caixa"><h2>Nesta página</h2><ul class="toc"></ul></div></aside>'
        corpo = cabeca('<a href="../pensadores.html">Pensadores</a>', p['nome'], e(p['quem']), meta=f'<div class="meta"><span class="tipo fam f{COR_AREA[p["area"]]}">{e(p["area"])}</span><span class="tipo ferr">{e(p["anos"])}</span></div>')
        corpo += f'''<div class="wrap layout"><article class="leitura"><h2>Ideias principais</h2><ul class="lista-forte">{"".join(f"<li>{e(x)}</li>" for x in p["ideias"])}</ul><h2>Obras</h2><ul>{"".join(f"<li><em>{e(x)}</em></li>" for x in p["obras"])}</ul><h2>O que dizem os críticos</h2><p>{e(p["criticas"])}</p>{liga}
{fontes([("Wikipédia: " + p["nome"], "https://en.wikipedia.org/wiki/" + p["w"])] + p["fx"])}<nav class="pager" aria-label="Pensadores"><a href="{ant["slug"]}.html"><small>← Anterior</small>{e(ant["nome"])}</a><a class="prox" href="{prox["slug"]}.html"><small>Próximo →</small>{e(prox["nome"])}</a></nav></article>{lado}</div><section class="relac"><div class="wrap"><h2>Na mesma área</h2><div class="grade">{"".join(cartao_p(x) for x in mesmos)}</div></div></section>'''
        page(f'pensadores/{p["slug"]}.html', p['nome'], p['quem'], corpo, atual='pensadores.html')

# ---------- glossário, ferramentas, biblioteca ----------
def glossario():
    gr = ''
    for g in GRUPOS_G:
        gr += f'<h2 class="grupo">{e(g)}</h2><dl class="glossario">' + ''.join(f'<dt>{e(t)}</dt><dd><p>{e(d)}</p>' + (f'<p class="pol"><a href="{u}">Saiba mais</a></p>' if u else '') + '</dd>' for gg, t, d, u in GLOSSARIO if gg == g) + '</dl>'
    corpo = cabeca('Ideias', 'Glossário de ciência', f'{len(GLOSSARIO)} termos explicados em uma ou duas frases, com link para a lição que os aprofunda.') + f'<div class="wrap estreito leitura secao">{gr}</div>'
    page('glossario.html', 'Glossário de ciência', 'Hipótese, teoria, falseabilidade, paradigma, p-valor, placebo, viés de confirmação, demarcação e outros termos explicados em uma frase.', corpo, atual='glossario.html')

def ferramentas():
    cards = ''.join(cartao_ferr(*f) for f in FERR)
    page('ferramentas.html', 'Ferramentas', 'Jogos e um detector de pseudociência para aprender a pensar cientificamente fazendo.', cabeca('Ferramentas', 'Aprenda fazendo', 'Sem cadastro. Nada do que você responde sai do seu navegador.') + f'<div class="wrap secao"><div class="grade">{cards}</div></div>', atual='ferramentas.html')
    JOGO = '<div id="jogo" class="quiz" style="margin-top:0"><div class="placar"><span></span><span></span></div><div class="barra-prog"><i></i></div><div class="alvo" style="margin-top:14px"></div><button class="btn prox-q" type="button" style="margin-top:12px" hidden>Próxima</button></div>'
    for a, tit, desc, _ in FERR:
        if a in JOGOS:
            j = JOGOS[a]
            dj = json.dumps(dict(tipo='opcoes', ops=j['ops'], itens=[list(x) for x in j['itens']]), ensure_ascii=False).replace('</', '<\\/')
            corpo = JOGO + f'<script type="application/json" id="dados-jogo">{dj}</script><p class="legenda">{j["nota"]}</p>'
            lede = j['lede']
        else:
            dd = json.dumps(DETECTOR, ensure_ascii=False).replace('</', '<\\/')
            corpo = f'<div id="detector" class="quiz" style="margin-top:0"><p class="k">Pense numa prática, produto ou afirmação e marque o que se aplica</p><div class="itens"></div><div class="saida fb" role="status" style="font-size:1.05rem;margin-top:14px"></div></div><script type="application/json" id="dados-detector">{dd}</script><p class="legenda">O detector não dá veredito: conta sinais de alerta. Uma prática com muitos sinais merece desconfiança e uma busca por revisões sistemáticas; uma com poucos ainda precisa de evidência a favor. <a href="../o-que-e-pseudociencia.html">Leia a lição sobre pseudociência</a>.</p>'
            lede = 'Doze perguntas sobre uma afirmação ou prática. Quanto mais sinais de alerta, mais motivos para desconfiar.'
        page(f'ferramentas/{a}.html', tit, desc, cabeca('<a href="../ferramentas.html">Ferramentas</a>', tit, lede) + f'<div class="wrap ferr secao" style="padding-top:28px">{corpo}</div>', atual='ferramentas.html')

def biblioteca():
    n_cls = {'Iniciante': 'iniciante', 'Intermediário': 'intermediario', 'Avançado': 'avancado'}
    cart = lambda t, a, d, n, u: f'<a class="cartao" href="{e(u)}" {EXT}><span class="tipo {n_cls.get(n, "ferr")}">{e(n)}</span><h3 class="ext" style="margin-top:.3rem">{e(t)}</h3><p><em>{e(a)}</em></p><p>{e(d)}</p></a>'
    li = ''.join(f'<h2 class="grupo">{n} <small>({sum(1 for x in LIVROS if x[3] == n)})</small></h2><p>{d}</p><div class="grade">' + ''.join(cart(*x) for x in LIVROS if x[3] == n) + '</div>' for n, d in SECOES_L)
    corpo = cabeca('Fontes', 'Biblioteca', f'{len(LIVROS)} livros para entender ciência, método e conhecimento, do primeiro contato à filosofia da ciência.') + f'<div class="wrap secao">{li}<p class="legenda">Os links levam a uma busca pelo livro. Procura sites em vez de livros? Veja a <a href="sites.html">biblioteca de sites sobre ciência</a>.</p></div>'
    page('biblioteca.html', 'Biblioteca', 'Livros recomendados sobre ciência e filosofia da ciência, por nível: de Sagan e Goldacre a Popper, Kuhn, Chalmers e Haack.', corpo, atual='biblioteca.html')

def sites_pub():
    gr = ''
    for g in GRUPOS_S:
        its = [s for s in SITES if s[3] == g]
        gr += f'<section><h2 class="grupo">{e(g)} <small>({len(its)})</small></h2><div class="grade">' + ''.join(f'<a class="cartao" href="{e(u)}" {EXT}><span class="tipo {"iniciante" if amb == NAC else "ferr"}">{e(amb)}</span><h3 class="ext" style="margin-top:.3rem">{e(n)}</h3><p>{e(dd)}</p></a>' for n, u, dd, _, amb in its) + '</div></section>'
    corpo = cabeca('Fontes', 'Biblioteca de sites sobre ciência', 'Enciclopédias, checagem de fatos, evidência em saúde e divulgação científica para continuar por conta própria.')
    corpo += f'<div class="wrap secao"><div class="nota alerta" style="margin-top:0">Nenhum site é infalível. Enciclopédias revisadas e bases de evidência são o ponto de partida mais seguro; divulgadores e agências de checagem também erram, e corrigem. Cruze fontes.</div>{gr}<p class="legenda">Veja também a <a href="biblioteca.html">biblioteca de livros</a>.</p></div>'
    page('sites.html', 'Biblioteca de sites sobre ciência', 'Enciclopédias de filosofia, Cochrane, agências de checagem, divulgação científica e sites sobre pseudociência, em português e inglês.', corpo, atual='sites.html')

def privacidade():
    corpo = cabeca('Sobre', 'Política de privacidade', 'Em resumo: não há cadastro, não usamos cookies próprios nem ferramentas de análise de visitas.') + '''<div class="wrap estreito leitura secao"><p class="abre">Esta página explica quais dados podem ser tratados quando você usa o Ciência Para Iniciantes, em linha com a Lei Geral de Proteção de Dados (LGPD, Lei 13.709/2018).</p>
<p><em>Última atualização: 6 de novembro de 2026.</em></p>
<h2>O que não fazemos</h2><ul><li>Não pedimos cadastro, login ou pagamento.</li><li>Não há formulário que envie seus dados para nós.</li><li>Não usamos cookies próprios, publicidade ou ferramentas de análise de visitas.</li><li>Não vendemos nem compartilhamos dados pessoais.</li></ul>
<h2>O que fica no seu navegador</h2><p>O recurso “Marcar como lida” e as posições nos debates usam o armazenamento local (<em>localStorage</em>) do seu aparelho. Essa informação não é enviada para nós. As respostas às ferramentas e aos testes rápidos não são guardadas.</p>
<p>Para apagar, limpe os dados deste site nas configurações do navegador.</p>
<h2>Serviços de terceiros</h2><div class="tabela"><table><thead><tr><th>Serviço</th><th>Para quê</th></tr></thead><tbody><tr><td>Hospedagem do site</td><td>Entregar as páginas. O provedor pode manter registros técnicos de acesso</td></tr><tr><td><a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Fonts</a></td><td>Carregar as fontes do site</td></tr><tr><td><a href="https://biblioverse.org">BiblioVerse</a></td><td>Carregar a barra superior com as bibliotecas da BiblioVerse</td></tr></tbody></table></div>
<h2>Links externos</h2><p>Indicamos fontes, livros e sites. Ao acessá-los, valem as regras de privacidade de cada um.</p>
<h2>Seus direitos</h2><p>A LGPD garante direitos como acesso, correção e eliminação de dados pessoais. Como não mantemos cadastro, em geral não temos dados que permitam identificar você.</p></div>'''
    page('privacidade.html', 'Política de privacidade', 'Quais dados podem ser tratados ao usar o Ciência Para Iniciantes, e o que fica só no seu navegador.', corpo)

def sobre():
    corpo = cabeca('Sobre', 'Sobre este projeto') + f'''<div class="wrap estreito leitura secao"><p class="abre">Um guia para quem quer entender o que é ciência, como ela produz conhecimento e como separar evidência de opinião e de pseudociência.</p>
<h2>Posição editorial</h2><p>O site parte de algumas posições: afirmações sobre o mundo podem ser verdadeiras ou falsas e a evidência decide; a confiança deve ser proporcional à evidência; o consenso de especialistas é, para leigos, o melhor guia disponível; e a ciência é falível e autocorretiva ao mesmo tempo. Nas questões em aberto da filosofia da ciência, como realismo ou o papel dos valores, apresentamos as correntes pelos seus pontos fortes antes das objeções.</p>
<h2>Como apresentamos as correntes</h2><p>Cada corrente aparece pelo seu <em>ponto focal</em>: o que ela põe no centro da explicação do conhecimento. Evitamos caricaturas, como “o positivismo diz que só existe o que se vê” ou “Kuhn diz que a ciência é irracional”, e cada página tem uma seção sobre o que a corrente não é.</p>
<h2>Pseudociências</h2><p>Chamar algo de pseudociência é uma afirmação forte. Cada página diz o que a prática alega, o que revisões sistemáticas e órgãos de saúde concluem, quais sinais de alerta aparecem e por que ela atrai pessoas, sem desprezo por quem acredita.</p>
<h2>Como apuramos</h2><p>Usamos a Stanford Encyclopedia of Philosophy, a Internet Encyclopedia of Philosophy, a Wikipédia, revisões Cochrane, documentos da OMS e das academias de ciência e as obras originais, indicadas ao fim de cada página. Ao ver um erro, mande a correção com a fonte.</p>
<h2>Seus dados</h2><p>Não há cadastro. Lições lidas ficam só no seu navegador. Veja a <a href="privacidade.html">política de privacidade</a>.</p>
<h2>Parte da BiblioVerse</h2><p>Este site faz parte da <a href="https://biblioverse.org">BiblioVerse</a>, ao lado do <a href="https://eticaparainiciantes.biblioverse.org/" {EXT}>Ética Para Iniciantes</a>, do <a href="https://politicaparainiciantes.biblioverse.org/" {EXT}>Política Para Iniciantes</a> e do <a href="https://pelosanimais.biblioverse.org/" {EXT}>Guia de Argumentação</a>.</p></div>'''
    corpo += '''<div class="wrap secao" style="padding-top:0"><h2 class="grupo">Os sites irmãos</h2><p>Os três sites se cruzam: cada tema aqui aparece, nos outros dois, pelo seu lado ético, político ou científico.</p><div class="grade"><a class="cartao" href="https://eticaparainiciantes.biblioverse.org/" target="_blank" rel="noopener"><span class="tipo">Site irmão</span><h3 class="ext" style="margin-top:.3rem">Ética Para Iniciantes</h3><p>Teorias éticas, círculo moral, metaética, dilemas e filósofos, do básico ao avançado.</p></a><a class="cartao" href="https://politicaparainiciantes.biblioverse.org/" target="_blank" rel="noopener"><span class="tipo">Site irmão</span><h3 class="ext" style="margin-top:.3rem">Política Para Iniciantes</h3><p>Como a política funciona, vertentes, debates, partidos e figuras do Brasil, do básico ao avançado.</p></a></div></div>'''  # cards dos sites irmãos (pedido de 2026-11-07)
    page('sobre.html', 'Sobre', 'Posição editorial e método do Ciência Para Iniciantes: como as correntes e as pseudociências são apresentadas e de onde vêm as fontes.', corpo, atual='sobre.html')

def arquivos():
    w = lambda n, t: open(os.path.join(ROOT, n), 'w', encoding='utf-8', newline='\n').write(t)
    page('404.html', 'Página não encontrada', 'Esta página não existe.', cabeca('Erro 404', 'Página não encontrada', 'Volte para o <a href="/" style="color:#fff">início</a> ou use a busca.'))
    w('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{SITE}/{"" if u == "index.html" else u}</loc><lastmod>{ATUALIZADO}</lastmod></url>\n' for u in sorted(set(PAGINAS) - {'404.html'})) + '</urlset>\n')
    w('llms.txt', f'# {NOME}\n\n> Guia gratuito de ciência em português, em três níveis, com fontes: o que é ciência, método científico, epistemologia, níveis de evidência, demarcação, pseudociências e as correntes da filosofia da ciência.\n\n## Principais seções\n\n- [Comece aqui]({SITE}/comece-aqui.html)\n- [Catálogo de lições]({SITE}/catalogo.html)\n- [Trilhas por tema]({SITE}/trilhas.html)\n- [Correntes]({SITE}/correntes.html)\n- [Pseudociências]({SITE}/pseudociencias.html)\n- [Debates]({SITE}/debates.html)\n- [Pensadores]({SITE}/pensadores.html)\n- [Glossário]({SITE}/glossario.html)\n- [Ferramentas]({SITE}/ferramentas.html)\n- [Biblioteca]({SITE}/biblioteca.html)\n- [Sobre e método]({SITE}/sobre.html)\n')
    w('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    w('CNAME', 'cienciaparainiciantes.biblioverse.org\n')
    w('.nojekyll', '')
    w('.gitignore', '__pycache__/\n')
    w('manifest.webmanifest', json.dumps(dict(name=NOME, short_name='Ciência', start_url='/', display='standalone', background_color='#fbf9fd', theme_color='#4b2a82', icons=[dict(src='assets/icon.svg', sizes='any', type='image/svg+xml'), dict(src='assets/icon-192.png', sizes='192x192', type='image/png'), dict(src='assets/icon-512.png', sizes='512x512', type='image/png')]), ensure_ascii=False))
    w('assets/icon.svg', arte.LOGO.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"'))
    busca = [dict(t=l['titulo'], d=l['nivel_rot'] + ' · ' + l['resumo'], u=l['slug'] + '.html') for l in TODAS]
    busca += [dict(t=c['n'], d='Corrente · ' + c['r'], u=f'correntes/{c["s"]}.html') for c in COR]
    busca += [dict(t=p['n'], d='Pseudociência · ' + p['r'], u=f'pseudociencias/{p["s"]}.html') for p in PSEUDO]
    busca += [dict(t=d['n'], d='Debate · ' + d['r'], u=f'debates/{d["s"]}.html') for d in DEBATES]
    busca += [dict(t=p['nome'], d=f'{p["anos"]} · {p["quem"]}', u=f'pensadores/{p["slug"]}.html') for p in PES]
    busca += [dict(t=f[1], d='Ferramenta · ' + f[2], u=f'ferramentas/{f[0]}.html') for f in FERR]
    busca += [dict(t=t, d='Glossário · ' + d[:90], u='glossario.html') for _, t, d, _ in GLOSSARIO]
    busca += [dict(t='Trilhas por tema', d='Caminhos curtos de estudo', u='trilhas.html'), dict(t='Correntes', d='O mapa das correntes e o comparador', u='correntes.html'), dict(t='Pseudociências', d='Casos analisados com a evidência', u='pseudociencias.html'), dict(t='Debates', d='Os lados e para onde a evidência aponta', u='debates.html'), dict(t='Pensadores', d='Cientistas e filósofos da ciência', u='pensadores.html'), dict(t='Biblioteca', d='Livros por nível', u='biblioteca.html'), dict(t='Sites sobre ciência', d='Enciclopédias, checagem e evidência', u='sites.html')]
    w('assets/busca.json', json.dumps(busca, ensure_ascii=False))

os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
def minifica():
    import hashlib
    try:
        import rcssmin, rjsmin
        cm, jm = rcssmin.cssmin, rjsmin.jsmin
    except ImportError:
        cm = jm = lambda s: s
    css = open(os.path.join(ROOT, 'assets', 'style.css'), encoding='utf-8').read(); js = open(os.path.join(ROOT, 'assets', 'app.js'), encoding='utf-8').read()
    open(os.path.join(ROOT, 'assets', 'style.min.css'), 'w', encoding='utf-8', newline='\n').write(cm(css))
    open(os.path.join(ROOT, 'assets', 'app.min.js'), 'w', encoding='utf-8', newline='\n').write(jm(js))
    return hashlib.sha1((css + js).encode()).hexdigest()[:8]
VERSAO = minifica()
inicio(); comece(); catalogo(); trilhas()
for s, r, ls, t, d, g in NIVEIS:
    nivel(s, r, ls, t, d, g); teste_nivel(s, r, ls); revisao(s, r, ls)
    for l in ls: licao(l, ls)
correntes(); pseudociencias(); debates_pub(); pensadores(); glossario(); ferramentas(); biblioteca(); sites_pub(); sobre(); privacidade(); arquivos()
print(f'{len(TODAS)} lições, {len(COR)} correntes, {len(PSEUDO)} pseudociências, {len(DEBATES)} debates, {len(PES)} pensadores, {len(FERR)} ferramentas, {len(PAGINAS)} páginas.')
