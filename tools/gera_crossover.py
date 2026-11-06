"""Gera tools/crossover.py (igual nos três sites) a partir dos pares antigos Política–Ética mais os grupos novos com o Ciência."""
import html, os, re, sys
B = r'C:\Users\julio\Documents\biblioverse'
P = {'pol': os.path.join(B, 'politicaparainiciantes'), 'eti': os.path.join(B, 'eticaparainiciantes'), 'cie': os.path.join(B, 'cienciaparainiciantes')}
sys.path.insert(0, os.path.join(P['eti'], 'tools'))
import crossover as velho

# grupos novos: (páginas do Ciência, páginas do Ética, páginas do Política). Um grupo liga cada página listada às dos outros dois sites.
G = [
 (['opiniao-crenca-e-conhecimento.html', 'cientificismo-e-limites-da-ciencia.html'], ['fatos-e-valores.html'], ['valores-e-decisoes.html']),
 (['ferramentas/opiniao-crenca-ou-conhecimento.html'], ['ferramentas/fato-ou-valor.html'], ['ferramentas/valor-ou-fato.html']),
 (['opiniao-crenca-e-conhecimento.html', 'ceticismo-responsavel.html'], ['etica-da-crenca.html'], ['respeitar-crencas.html']),
 (['vieses-e-metodo.html'], ['vieses-morais.html'], ['vieses-cognitivos.html', 'vieses/confirmation-bias.html', 'vieses/apophenia.html']),
 (['risco-e-probabilidade.html'], [], ['vieses/availability-heuristic.html', 'vieses/gamblers-fallacy.html', 'vieses/neglect-of-probability.html']),
 (['estatistica-para-entender-ciencia.html'], [], ['vieses/survivorship-bias.html', 'vieses/insensitivity-to-sample-size.html', 'vieses/illusory-correlation.html']),
 (['pseudociencias/astrologia.html'], [], ['vieses/barnum-effect.html']),
 (['confianca-e-especialistas.html'], ['debates/humildade-intelectual.html'], ['vieses/authority-bias.html', 'vieses/dunning-kruger-effect.html', 'direta-ou-epistocracia.html']),
 (['postura-cientifica.html', 'ceticismo-responsavel.html'], ['abertura-moral.html'], ['mudar-de-ideia.html', 'inteligencia-nao-protege.html']),
 (['o-que-e-pseudociencia.html', 'pseudociencias.html'], ['debates/pseudociencias.html'], ['debates/pseudociencias.html']),
 (['criterio-da-demarcacao.html', 'debates/psicanalise-e-ciencia.html'], ['debates/pseudociencia-nas-universidades.html'], []),
 (['negacionismo-e-desinformacao.html'], ['debates/bolhas-e-camaras-de-eco.html', 'debates/tornar-ignorantes-famosos.html'], ['camaras-de-eco.html', 'perigo-dos-grupos-de-mensagem.html', 'perigo-dos-bots.html', 'debates/fake-news.html']),
 (['debates/desinformacao-nas-redes.html'], ['debates/censura.html'], ['debates/regulamentacao-redes.html', 'debates/bigtechs.html']),
 (['como-ler-noticia-de-ciencia.html', 'como-funciona-a-checagem.html'], [], ['checagem-de-fatos.html', 'como-ler-a-midia-tradicional.html', 'perigo-da-midia-alternativa.html']),
 (['pratica-baseada-em-evidencias.html', 'avaliacao-de-politicas-publicas.html', 'debates/siga-a-ciencia.html'], ['da-etica-a-politica.html'], ['politicas-baseadas-em-evidencias.html', 'debates/evidencias-debate.html', 'pragmatismo-politico.html']),
 (['pesquisas-de-opiniao.html'], [], ['pesquisas-eleitorais.html']),
 (['falacias-e-argumentos.html'], ['como-discutir-etica.html', 'argumentos-morais.html'], ['sofismo.html', 'ferramentas/que-truque-e-esse.html']),
 (['ciencia-religiao-e-filosofia.html', 'pseudociencias/design-inteligente.html', 'debates/ensinar-os-dois-lados.html'], ['etica-e-religiao.html', 'moralidade-sem-religiao.html'], ['religiao-e-estado.html', 'debates/religiao-estado.html']),
 (['etica-na-pesquisa.html'], ['bioetica.html'], []),
 (['debates/testes-em-animais.html'], ['debates/experimentacao-animal.html', 'etica-animal-na-pratica.html'], ['direito-animal.html']),
 (['ciencia-da-consciencia.html'], ['senciencia.html', 'mentes-artificiais.html', 'gradualismo.html'], ['sencientismo.html', 'politica-baseada-na-senciencia.html']),
 (['pseudociencias/negacionismo-climatico.html', 'debates/energia-nuclear.html'], ['etica-climatica.html'], ['debates/clima.html', 'debates/petroleo-margem-equatorial.html']),
 (['debates/ia-na-ciencia.html'], ['etica-da-inteligencia-artificial.html', 'problema-do-alinhamento.html'], ['debates/inteligencia-artificial.html', 'debates/ia-no-governo.html']),
 (['ciencia-a-servico-do-mal.html'], ['situacionismo-e-experimentos.html', 'catastrofes-morais.html'], ['vertentes/nazismo.html', 'vertentes/totalitarismo.html', 'vertentes/marxismo-leninismo.html', 'vertentes/maoismo.html']),
 (['pseudociencias/racismo-cientifico.html', 'pseudociencias/lisenkoismo.html'], [], ['vertentes/nazismo.html', 'vertentes/marxismo-leninismo.html']),
 (['genetica-ambiente-e-comportamento.html', 'filosofia-da-biologia.html'], ['evolucao-e-moral.html'], ['genetica-e-politica.html']),
 (['psicologia-como-ciencia.html'], ['situacionismo-e-experimentos.html', 'psicologia-moral.html'], ['mente-moralista.html']),
 (['fraudes-cientificas.html'], ['debates/plagio.html'], ['golpes-e-fraudes.html']),
 (['risco-e-probabilidade.html', 'debates/ganho-de-funcao.html'], ['riscos-s-e-riscos-x.html', 'teoria-da-decisao-e-etica.html'], ['riscos-s-e-x.html', 'debates/armas-nucleares.html']),
 (['bayesianismo.html', 'interpretacoes-da-probabilidade.html'], ['probabilidade-e-etica.html'], []),
 (['positivismo.html'], [], ['historia.html']),
 (['naturalismo-epistemologico.html', 'realismo-e-antirrealismo.html'], ['evolucao-e-moral.html', 'realismo-moral.html', 'debates/existe-verdade-moral.html'], []),
 (['o-que-e-epistemologia.html', 'como-justificar-uma-crenca.html'], ['epistemologia-moral.html'], []),
 (['correntes/relativismo-epistemico.html'], ['relativismo-e-quietismo.html', 'debates/relativismo-moral.html'], ['relativismo-e-circulo-moral.html']),
 (['valores-na-ciencia.html', 'os-valores-da-ciencia.html'], ['fatos-e-valores.html', 'da-etica-a-politica.html'], ['valores-e-decisoes.html']),
 (['debates/responsabilidade-dos-cientistas.html'], ['debates/poder-e-responsabilidade.html', 'responsabilidade-coletiva.html'], ['debates/armas-nucleares.html']),
 (['debates/vacinacao-obrigatoria.html', 'pseudociencias/movimento-antivacina.html'], ['debates/vacinacao-obrigatoria.html'], ['debates/pseudociencias.html']),
 (['debates/transgenicos.html', 'debates/ciencia-da-nutricao.html'], [], ['debates/saude.html']),
 (['debates/pics-no-sus.html', 'pseudociencias/homeopatia.html'], ['debates/pseudociencias.html'], ['debates/pseudociencias.html', 'debates/saude.html']),
 (['debates/economia-e-ciencia.html'], ['economia-politica-e-etica.html'], ['economia-para-entender-politica.html']),
 (['debates/conhecimento-tradicional.html'], ['debates/relativismo-moral.html'], ['debates/terras-indigenas.html']),
 (['quem-faz-ciencia.html'], ['etica-feminista.html'], ['estereotipo-preconceito-discriminacao.html']),
 (['tipos-de-ciencia.html', 'experimentos-naturais.html'], [], ['teoria-dos-jogos.html', 'politicas-publicas.html']),
 (['perguntas-em-aberto.html', 'o-incognoscivel.html'], ['sentido-da-vida.html'], []),
 (['divulgacao-cientifica.html'], ['debates/tornar-ignorantes-famosos.html'], ['como-ler-a-midia-tradicional.html', 'perigo-da-midia-alternativa.html']),
 (['ma-ciencia.html', 'debates/financiamento-privado.html'], ['debates/pseudociencia-nas-universidades.html', 'debates/empresas-e-lucro.html'], ['debates/bigtechs.html', 'poder-paralelo.html']),
 (['e-ciencia-ou-nao.html'], ['o-que-e-etica.html'], ['o-que-e-politica.html']),
 (['debates/modificar-genes-e-seres.html'], ['debates/edicao-genetica.html', 'filosofos/pearce.html', 'filosofos/bostrom.html', 'debates/explorar-animais.html'], ['genetica-e-politica.html', 'vertentes/nazismo.html', 'direito-animal.html']),
 (['pseudociencias/psicanalise.html'], ['debates/pseudociencia-nas-universidades.html'], []),
 (['pseudociencias/respiracionismo.html', 'pseudociencias/detox.html', 'pseudociencias/cura-quantica.html'], ['debates/pseudociencias.html'], ['debates/pseudociencias.html']),
 (['pseudociencias/dieta-carnivora.html', 'pseudociencias/dieta-frugivora.html'], ['debates/explorar-animais.html'], []),
 (['debates/meditacao-yoga-mindfulness.html', 'debates/pics-no-sus.html'], ['debates/pseudociencias.html'], ['debates/saude.html', 'debates/pseudociencias.html']),
 (['postura-cientifica-etica-e-politica.html'], ['abertura-moral.html', 'fraqueza-de-vontade.html', 'especismo.html', 'debates/humildade-intelectual.html'], ['mudar-de-ideia.html', 'testar-visao-moral.html', 'inteligencia-nao-protege.html', 'politica-baseada-na-senciencia.html']),
 (['pensadores/stephen-jay-gould.html', 'pensadores/richard-dawkins.html'], ['evolucao-e-moral.html'], []),
 (['pensadores/frans-de-waal.html'], ['senciencia.html', 'emocoes-morais.html'], []),
 (['pensadores/hans-rosling.html', 'pensadores/steven-pinker.html'], ['progresso-moral.html'], ['progresso-moral-e-politico.html']),
 (['pensadores/marcelo-gleiser.html'], ['filosofos/gleiser.html'], []),
 (['fora-da-media.html'], ['deficiencia-e-etica.html'], ['desigualdade-social.html', 'um-sistema-para-todos.html']),
 (['como-achar-e-julgar-artigos.html', 'debates/piramide-de-evidencias.html'], ['debates/pseudociencia-nas-universidades.html'], ['politicas-baseadas-em-evidencias.html']),
 (['letramento-cientifico-no-brasil.html', 'divulgacao-cientifica.html'], ['educacao-moral.html'], ['escola-publica-e-universidade.html', 'checagem-de-fatos.html']),
 (['debates/conhecimento-nao-cientifico.html', 'debates/conhecimento-tradicional.html'], ['epistemologia-moral.html', 'debates/existe-verdade-moral.html'], ['respeitar-crencas.html']),
 (['pensadores/hume.html'], ['filosofos/hume.html'], []),
 (['pensadores/kant.html'], ['filosofos/kant.html'], []),
 (['pensadores/john-stuart-mill.html'], ['filosofos/mill.html'], []),
 (['pensadores/dewey.html'], ['filosofos/dewey.html'], []),
 (['pensadores/aristoteles.html'], ['filosofos/aristoteles.html'], []),
 (['pensadores/kahneman.html'], ['filosofos/haidt.html', 'psicologia-moral.html'], ['vieses-cognitivos.html']),
 (['pensadores/popper.html'], ['dilemas/paradoxo-da-tolerancia.html'], ['perigo-de-questionar-a-democracia.html']),
]

# base: os pares antigos Política–Ética (no arquivo atual, são os grupos sem página do Ciência)
GR = [tuple(list(x) for x in g) for g in velho.GRUPOS if not g[0]] if hasattr(velho, 'GRUPOS') else [([], [b], [a]) for a, b in velho.PARES]
GR += G
erros = 0
def titulo(site, path):
    f = os.path.join(P[site], path)
    if not os.path.exists(f):
        global erros; erros += 1; print('FALTA', site, path); return None
    t = open(f, encoding='utf-8').read()
    m = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S)
    return html.unescape(re.sub('<[^>]+>', '', m.group(1))).strip()
T = {'cie': {}, 'eti': {}, 'pol': {}}
for cie, eti, pol in GR:
    for site, ls in (('cie', cie), ('eti', eti), ('pol', pol)):
        for p in ls:
            if p not in T[site]: T[site][p] = titulo(site, p)
if erros: sys.exit(f'{erros} páginas inexistentes')
def rep(d): return '{\n' + ''.join(f' {k!r}: {v!r},\n' for k, v in sorted(d.items())) + '}'
src = f'''"""Ponte entre os três sites irmãos: Política, Ética e Ciência Para Iniciantes (novembro de 2026). Este arquivo é IGUAL nos
três sites (tools/crossover.py): edite num, copie para os outros dois, ou rode o gerador. GRUPOS reúne páginas dos três sites
sobre o mesmo tema: (páginas do Ciência, páginas da Ética, páginas da Política); listas podem ficar vazias. O build de cada
site mostra, em cada página listada, uma caixa com as páginas dos outros dois. Os títulos são copiados dos <h1> das páginas."""
SITES = {{'pol': ('Política Para Iniciantes', 'https://politicaparainiciantes.biblioverse.org'),
         'eti': ('Ética Para Iniciantes', 'https://eticaparainiciantes.biblioverse.org'),
         'cie': ('Ciência Para Iniciantes', 'https://cienciaparainiciantes.biblioverse.org')}}
GRUPOS = [
{''.join(f' {g!r},' + chr(10) for g in GR)}]
TITULOS = {{'cie': {rep(T['cie'])}, 'eti': {rep(T['eti'])}, 'pol': {rep(T['pol'])}}}
INTRO = {{
 'pol': ('Nos sites irmãos', 'Este tema também tem um lado moral e um lado de método e evidência. Veja nos sites irmãos:'),
 'eti': ('Nos sites irmãos', 'Para ver como este tema aparece na política brasileira e o que a ciência diz sobre ele, veja nos sites irmãos:'),
 'cie': ('Nos sites irmãos', 'Este tema também envolve uma pergunta moral e aparece na política. Veja nos sites irmãos:'),
}}
ORDEM = {{'pol': ('eti', 'cie'), 'eti': ('pol', 'cie'), 'cie': ('eti', 'pol')}}

def _caixa(cls, titulo, intro, blocos):
    secs = ''
    for nome, itens in blocos:
        lis = ''.join(f'<li><a href="{{u}}" target="_blank" rel="noopener">{{t}}</a></li>' for u, t in itens)
        secs += f'<p class="ti">{{nome}}</p><ul>{{lis}}</ul>'
    return f'<div class="wrap estreito secao" style="padding-top:0"><aside class="nota cruzada {{cls}}" aria-label="{{titulo}}"><strong>{{titulo}}</strong><p>{{intro}}</p>{{secs}}</aside></div>'

def caixa(site, path, esc):
    """Caixa dos sites irmãos para a página `path` do site `site` ('pol', 'eti' ou 'cie')."""
    ix = {{'cie': 0, 'eti': 1, 'pol': 2}}
    blocos = []
    for outro in ORDEM[site]:
        vistos = []; itens = []
        for g in GRUPOS:
            if path in g[ix[site]]:
                for p in g[ix[outro]]:
                    if p not in vistos:
                        vistos.append(p); itens.append((f'{{SITES[outro][1]}}/{{p}}', esc(TITULOS[outro][p])))
        if itens: blocos.append((SITES[outro][0], itens))
    if not blocos: return ''
    tit, intro = INTRO[site]
    return _caixa('para-' + site, tit, intro, blocos)

def caixa_politica(path, esc): return caixa('pol', path, esc)
def caixa_etica(path, esc): return caixa('eti', path, esc)
def caixa_ciencia(path, esc): return caixa('cie', path, esc)
'''
for site in P:
    open(os.path.join(P[site], 'tools', 'crossover.py'), 'w', encoding='utf-8', newline='\n').write(src)
print('grupos', len(GR), 'títulos', {k: len(v) for k, v in T.items()})
