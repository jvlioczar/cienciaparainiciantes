"""Lições acrescentadas em 2026-11-06 (segunda leva). NOVAS_<NIVEL>: listas de lições no formato de sempre;
POSICAO[slug] = slug da lição depois da qual a nova entra (antes da ordenação por grupo, que é estável)."""
SEP = 'https://plato.stanford.edu/entries/'
IEP = 'https://iep.utm.edu/'
WP = 'https://pt.wikipedia.org/wiki/'
WE = 'https://en.wikipedia.org/wiki/'

POSICAO = {
 'uma-breve-historia-da-ciencia': 'o-que-e-ciencia', 'falacias-e-argumentos': 'o-que-e-pseudociencia', 'risco-e-probabilidade': 'como-ler-noticia-de-ciencia', 'ciencia-no-brasil': 'risco-e-probabilidade',
 'a-revolucao-cientifica': 'positivismo', 'modelos-e-simulacoes': 'tipos-de-ciencia', 'etica-na-pesquisa': 'vieses-e-metodo',
 'leis-da-natureza': 'explicacao-cientifica', 'reducionismo-e-emergencia': 'leis-da-natureza', 'interpretacoes-da-mecanica-quantica': 'reducionismo-e-emergencia',
}

NOVAS_INICIANTE = [
dict(slug='uma-breve-historia-da-ciencia', grupo='O básico', titulo='Uma breve história da ciência', temas=['fundamentos'],
resumo='Da astronomia babilônica aos laboratórios de hoje: como o jeito de investigar a natureza foi inventado, perdido, reencontrado e aperfeiçoado.',
corpo='''
<p class="abre">A ciência não nasceu pronta num dia. É uma invenção humana lenta, com contribuições de muitas culturas, longos períodos de estagnação e viradas rápidas. Conhecer essa história ajuda a entender por que o método é como é.</p>
<h2>Raízes antigas</h2>
<p>Babilônios registraram posições de astros por séculos e preveram eclipses. Egípcios desenvolveram geometria prática e medicina com receitas escritas. Na Grécia, a partir do século VI a.C., filósofos como Tales e Anaximandro tentaram explicar a natureza por causas naturais, sem recorrer a deuses; Aristóteles observou e classificou animais; Eratóstenes estimou o tamanho da Terra; Arquimedes uniu matemática e física.</p>
<h2>Um mundo maior que a Europa</h2>
<p>Entre os séculos VIII e XIII, o mundo islâmico preservou e ampliou o saber grego. Ibn al-Haytham (Alhazen) estudou a luz com experimentos controlados e defendeu testar hipóteses; al-Khwarizmi deu nome à álgebra e ao algoritmo. A China desenvolveu o papel, a bússola e a pólvora; a Índia, o sistema de numeração com o zero que usamos hoje.</p>
<h2>A Revolução Científica</h2>
<p>Entre 1543 (Copérnico) e 1687 (Newton), a Europa viveu uma mudança profunda: o Sol no centro, a física matemática de Galileu, as leis de Kepler, o método experimental defendido por Bacon, a gravitação universal de Newton. Surgiram as primeiras sociedades científicas e revistas, como a Royal Society, em Londres, que publicava resultados para outros conferirem. Há uma lição no nível Intermediário só sobre esse período.</p>
<h2>Os séculos XIX e XX</h2>
<ul><li><strong>Química e biologia:</strong> tabela periódica, teoria atômica, evolução por seleção natural, teoria dos germes, genética.</li><li><strong>Física:</strong> eletromagnetismo, relatividade, mecânica quântica.</li><li><strong>Medicina:</strong> vacinas, antibióticos, ensaios clínicos randomizados (o primeiro grande, com a estreptomicina, em 1948).</li><li><strong>Ciência como profissão:</strong> universidades de pesquisa, laboratórios industriais, financiamento público.</li></ul>
<h2>A ciência de hoje</h2>
<p>A ciência atual é coletiva, internacional e cara: o Grande Colisor de Hádrons envolve milhares de pesquisadores de dezenas de países. Computadores, grandes bases de dados e inteligência artificial mudaram a forma de pesquisar. Ao mesmo tempo, a crise de replicação e a desinformação mostram que o sistema continua precisando se corrigir.</p>
<div class="nota"><strong>Cuidado com a história de heróis:</strong> a imagem do gênio solitário esconde o trabalho coletivo, as instituições e as pessoas esquecidas, como mulheres e cientistas de fora da Europa. Rosalind Franklin, cujas imagens de raios X foram essenciais para a descoberta da estrutura do DNA, é um exemplo famoso.</div>''',
fontes=[('History of science (Wikipédia)', WE + 'History_of_science'), ('Ibn al-Haytham (Wikipédia)', WP + 'Alhazen'), ('Revolução científica (Wikipédia)', WP + 'Revolu%C3%A7%C3%A3o_cient%C3%ADfica')],
quiz=[('O que os primeiros filósofos gregos da natureza tinham de novo?', ['Usavam computadores', 'Buscavam explicar a natureza por causas naturais, sem recorrer a deuses', 'Faziam ensaios randomizados', 'Rejeitavam a matemática'], 1, 'Tales e Anaximandro procuravam explicações naturais.'),
 ('Que contribuição veio do mundo islâmico medieval?', ['A teoria da evolução', 'Experimentos de óptica de Ibn al-Haytham e a álgebra de al-Khwarizmi', 'A relatividade', 'Nenhuma'], 1, 'O mundo islâmico preservou e ampliou o saber antigo.'),
 ('Um filme mostra um cientista que descobre tudo sozinho, num porão. O que a lição diria dessa imagem?', ['Que é fiel à história', 'Que esconde o caráter coletivo e institucional da ciência', 'Que cientistas nunca trabalham sozinhos', 'Que porões são ruins para a ciência'], 1, 'A história de heróis apaga equipes, instituições e pessoas esquecidas.')],
analogia='A história da ciência é como a construção de uma catedral que durou séculos. Cada geração assentou algumas pedras, às vezes derrubou paredes mal feitas, e ninguém viu a obra inteira.',
crianca='Há muito tempo, as pessoas achavam que os raios eram raiva dos deuses. Aos poucos, foram observando, medindo e testando, até entender a eletricidade. A ciência foi sendo construída por muita gente, em muitos lugares.',
obj=['Descrever as grandes etapas da história da ciência.', 'Reconhecer contribuições de culturas não europeias.', 'Criticar a imagem do gênio solitário.'],
caso=('Alguém diz que “a ciência foi inventada pelos europeus no século XVII”.', 'O que essa frase esquece?', 'As raízes babilônicas, gregas, indianas, chinesas e islâmicas, e o fato de que a Revolução Científica se apoiou nelas.'),
erro=('“A ciência sempre avançou em linha reta.”', 'Houve longos períodos de estagnação, ideias perdidas e reencontradas, e erros que duraram séculos.'),
ferr=None, pre=['o-que-e-ciencia'],
guardar=['A ciência é uma invenção lenta, coletiva e de muitas culturas.', 'A Revolução Científica criou instituições para publicar e conferir resultados.', 'A imagem do gênio solitário esconde equipes e pessoas esquecidas.'],
pensar='Que descoberta científica mudou mais a sua vida, e quantas pessoas foram necessárias para chegar a ela?'),

dict(slug='falacias-e-argumentos', grupo='Ciência no dia a dia', titulo='Falácias que aparecem em discussões sobre ciência', temas=['mente', 'demarcacao'],
resumo='Apelo à natureza, à autoridade, à antiguidade, falsa dicotomia e espantalho: os erros de raciocínio mais comuns quando o assunto é ciência.',
corpo='''
<p class="abre">Uma falácia é um argumento que parece bom mas não sustenta a conclusão. Em discussões sobre saúde, clima e tecnologia, algumas falácias aparecem tanto que vale conhecê-las pelo nome.</p>
<h2>As mais comuns</h2>
<div class="tabela"><table><thead><tr><th>Falácia</th><th>Como aparece</th><th>Por que falha</th></tr></thead><tbody>
<tr><td><strong>Apelo à natureza</strong></td><td>“É natural, então é seguro.”</td><td>Arsênico e cicuta são naturais; muitos remédios sintéticos salvam vidas.</td></tr>
<tr><td><strong>Apelo à antiguidade</strong></td><td>“É usado há milênios.”</td><td>A sangria também foi usada por milênios e matou muita gente.</td></tr>
<tr><td><strong>Apelo à autoridade indevida</strong></td><td>“Um médico famoso disse.”</td><td>Conta a evidência e o consenso da área, não um nome isolado, muito menos fora da sua especialidade.</td></tr>
<tr><td><strong>Anedota</strong></td><td>“Meu avô fumou a vida toda e viveu até 95.”</td><td>Casos isolados não refutam riscos estatísticos.</td></tr>
<tr><td><strong>Falsa dicotomia</strong></td><td>“Ou a ciência sabe tudo, ou não sabe nada.”</td><td>Há graus de certeza.</td></tr>
<tr><td><strong>Espantalho</strong></td><td>“Os cientistas dizem que o clima nunca mudou antes.”</td><td>Ninguém diz isso; ataca-se uma versão distorcida.</td></tr>
<tr><td><strong>Depois disso, logo por causa disso</strong></td><td>“Tomei e melhorei.”</td><td>A melhora pode ter outras causas (veja grupo controle).</td></tr>
<tr><td><strong>Ataque à pessoa</strong></td><td>“Esse estudo é de quem odeia agricultores.”</td><td>Ataca o autor em vez dos métodos e dados.</td></tr>
<tr><td><strong>Apelo à ignorância</strong></td><td>“Ninguém provou que não funciona.”</td><td>O ônus da prova é de quem afirma.</td></tr>
<tr><td><strong>Galileu</strong></td><td>“Também riram de Galileu.”</td><td>Ser contestado não torna ninguém certo; Galileu venceu pela evidência.</td></tr>
</tbody></table></div>
<h2>A falácia da falácia</h2>
<p>Apontar uma falácia num argumento não prova que a conclusão é falsa. Alguém pode defender a vacinação com um argumento ruim, e a vacinação continua sendo eficaz. O nome certo da falácia é uma ferramenta para pensar melhor, não um troféu para vencer discussões.</p>
<h2>Nem todo apelo à autoridade é falácia</h2>
<p>Confiar no consenso de especialistas de uma área, quando não somos especialistas, é racional. O erro está em apelar a uma autoridade fora da sua área, isolada, ou com interesse na conclusão.</p>
<div class="nota"><strong>Para ir além:</strong> o <a href="https://guiadeargumentacao.biblioverse.org/" target="_blank" rel="noopener">Guia de Argumentação</a> da BiblioVerse tem dezenas de falácias explicadas com exemplos.</div>''',
fontes=[('Fallacies (Internet Encyclopedia of Philosophy)', IEP + 'fallacy/'), ('Falácia (Wikipédia)', WP + 'Fal%C3%A1cia'), ('Appeal to nature (Wikipédia)', WE + 'Appeal_to_nature')],
quiz=[('“Esse remédio é natural, então não faz mal.” Que falácia é essa?', ['Espantalho', 'Apelo à natureza', 'Falsa dicotomia', 'Ataque à pessoa'], 1, 'Natural não é sinônimo de seguro.'),
 ('Apontar uma falácia num argumento prova que a conclusão é falsa?', ['Sim', 'Não: a conclusão pode ser verdadeira por outras razões', 'Só se for apelo à autoridade', 'Só em ciência'], 1, 'É a falácia da falácia.'),
 ('“Meu tio nunca usou cinto de segurança e nunca se machucou.” O problema é:', ['Anedota contra um risco estatístico', 'Apelo à natureza', 'Espantalho', 'Nenhum'], 0, 'Um caso isolado não refuta dados de milhões de acidentes.')],
analogia='Falácias são como ilusões de óptica do raciocínio. O argumento parece levar à conclusão, como as linhas parecem ter tamanhos diferentes. Saber o nome da ilusão ajuda a não cair nela.',
crianca='Às vezes alguém diz uma coisa que parece certa, mas o motivo não serve. Por exemplo: “é natural, então é bom”. Mas cogumelo venenoso também é natural!',
obj=['Reconhecer falácias comuns em discussões sobre ciência.', 'Explicar por que cada uma falha.', 'Evitar a falácia da falácia e distinguir apelos legítimos à autoridade.'],
caso=('Num grupo, alguém diz: “chá de ervas é usado há três mil anos, então funciona”.', 'O que está errado no argumento?', 'É um apelo à antiguidade: tempo de uso não é teste. A sangria também foi usada por milênios.'),
erro=('“Todo apelo à autoridade é falácia.”', 'Confiar no consenso de especialistas da área é racional. O erro é apelar a alguém fora da área, isolado ou interessado.'),
ferr='ciencia-ou-pseudociencia', pre=['o-que-e-pseudociencia'],
guardar=['Natural, antigo e famoso não são evidências.', 'Anedotas não refutam riscos estatísticos.', 'Apontar uma falácia não prova que a conclusão é falsa.'],
pensar='Qual dessas falácias você já usou para defender algo de que gostava?'),

dict(slug='risco-e-probabilidade', grupo='Ciência no dia a dia', titulo='Risco e probabilidade no dia a dia', temas=['estatistica', 'mente'],
resumo='Por que temos mais medo de avião do que de carro, o que significa “50% de chance” e como comparar riscos sem se assustar à toa.',
corpo='''
<p class="abre">Somos muito ruins em avaliar riscos. Tememos tubarões e aviões e subestimamos o trânsito e o sedentarismo. Entender a probabilidade não é só matemática: é uma ferramenta para decidir melhor sobre saúde, dinheiro e segurança.</p>
<h2>Por que erramos</h2>
<ul><li><strong>Disponibilidade:</strong> o que é noticiado parece comum. Um acidente aéreo vira manchete mundial; milhares de mortes no trânsito, não.</li><li><strong>Controle:</strong> riscos que sentimos controlar (dirigir) parecem menores do que os que não controlamos (voar).</li><li><strong>Medo do novo e do invisível:</strong> radiação e “química” assustam mais do que o sol ou o álcool, mesmo quando o risco é menor.</li><li><strong>Números grandes:</strong> “mil casos” assusta sem dizer em quantas pessoas.</li></ul>
<h2>Ferramentas simples</h2>
<ul class="lista-forte"><li><strong>Pergunte “de quantos?”:</strong> 100 casos em 200 milhões é muito diferente de 100 em mil.</li><li><strong>Prefira o risco absoluto:</strong> “dobra o risco” pode significar passar de 1 em 1 milhão para 2 em 1 milhão.</li><li><strong>Use frequências naturais:</strong> “de cada 100 pessoas como você, 3 terão o problema” é mais fácil de entender do que “3%”.</li><li><strong>Compare com riscos conhecidos:</strong> o micromorte (uma chance em um milhão de morrer) permite comparar atividades.</li><li><strong>Considere o risco de não fazer:</strong> a vacina tem riscos raros; a doença, riscos muito maiores.</li></ul>
<h2>O que “70% de chance de chuva” quer dizer</h2>
<p>Quer dizer que, em dias com condições parecidas, chove em cerca de 70% deles. Se não chover, a previsão não “errou”: 30% dos dias assim são secos. Previsões probabilísticas se avaliam pela <strong>calibração</strong>: das vezes em que se disse 70%, choveu em cerca de 70%?</p>
<h2>A falácia do apostador</h2>
<p>Depois de cinco caras seguidas numa moeda honesta, a chance de coroa continua 50%. A moeda não tem memória. Loterias, roletas e apostas online exploram essa e outras ilusões.</p>
<div class="nota"><strong>Exercício:</strong> antes de reagir a uma manchete de risco, reescreva o número como “X em cada Y pessoas” e compare com algo que você já faz sem medo.</div>''',
fontes=[('Risk perception (Wikipédia)', WE + 'Risk_perception'), ('Micromorte (Wikipédia)', WE + 'Micromort'), ('Gambler\'s fallacy (Wikipédia)', WE + 'Gambler%27s_fallacy'), ('Our World in Data: Causes of death', 'https://ourworldindata.org/causes-of-death')],
quiz=[('Por que acidentes de avião parecem mais frequentes do que são?', ['Porque são muito comuns', 'Pelo viés de disponibilidade: são muito noticiados', 'Porque aviões são inseguros', 'Por causa da gravidade'], 1, 'O que é lembrado com facilidade parece mais provável.'),
 ('A previsão dava 70% de chuva e não choveu. A previsão errou?', ['Sim, totalmente', 'Não necessariamente: em 30% dos dias assim não chove; o que conta é a calibração', 'Sim, deveria ser 100%', 'A meteorologia é pseudociência'], 1, 'Previsões probabilísticas se avaliam ao longo de muitos casos.'),
 ('Depois de 6 números pares seguidos na roleta, alguém aposta tudo no ímpar “porque agora tem que dar”. Isso é:', ['Estratégia correta', 'A falácia do apostador: a roleta não tem memória', 'Regressão à média garantida', 'Bayesianismo'], 1, 'Cada giro é independente dos anteriores.')],
analogia='Avaliar riscos pelo medo é como estimar o tamanho de uma cidade pelo número de vezes que ela aparece no jornal. As cidades das manchetes parecem enormes; as tranquilas parecem não existir.',
crianca='Muita gente tem medo de tubarão, mas é muito mais raro ser mordido por um tubarão do que cair da bicicleta. Às vezes temos medo das coisas erradas.',
obj=['Explicar por que nossa percepção de risco falha.', 'Usar frequências naturais, risco absoluto e comparações.', 'Interpretar previsões probabilísticas e reconhecer a falácia do apostador.'],
caso=('Uma notícia diz que um adoçante “aumenta em 50% o risco” de uma doença rara.', 'Que pergunta você faz primeiro?', 'Qual o risco absoluto: se passa de 2 em 100 mil para 3 em 100 mil, o aumento real é muito pequeno.'),
erro=('“Se a chance era de 90% e não aconteceu, a previsão estava errada.”', 'Eventos de 10% acontecem uma vez em cada dez. Avalia-se a previsão pela calibração em muitos casos.'),
ferr='nivel-de-evidencia', pre=['como-ler-noticia-de-ciencia'],
guardar=['Disponibilidade e sensação de controle distorcem o medo.', 'Pergunte “de quantos?” e prefira frequências naturais e risco absoluto.', 'Probabilidades se avaliam por calibração, e acaso não tem memória.'],
pensar='De que risco você tem mais medo do que deveria, e de qual tem menos?'),

dict(slug='ciencia-no-brasil', grupo='Ciência no dia a dia', titulo='A ciência no Brasil', temas=['sociedade'],
resumo='De Oswaldo Cruz à Embrapa e ao SUS: o que a ciência brasileira já fez, como é financiada e quais são seus desafios.',
corpo='''
<p class="abre">O Brasil produz ciência de impacto mundial, embora isso apareça pouco no noticiário. Quase toda essa ciência é feita em universidades públicas e institutos de pesquisa, com dinheiro público.</p>
<h2>Algumas conquistas</h2>
<ul><li><strong>Saúde pública:</strong> Oswaldo Cruz liderou o combate à febre amarela e à varíola no Rio de Janeiro no começo do século XX. Carlos Chagas descreveu, sozinho, uma doença inteira em 1909, do parasita ao inseto transmissor e aos sintomas: a doença de Chagas.</li>
<li><strong>Vacinas:</strong> o Instituto Butantan e a Fiocruz (Bio-Manguinhos) produzem vacinas para o SUS. O Programa Nacional de Imunizações, de 1973, é referência mundial.</li>
<li><strong>Agricultura:</strong> a Embrapa, criada em 1973, desenvolveu técnicas que transformaram o Cerrado em região produtiva, como a correção da acidez do solo e a fixação biológica de nitrogênio na soja, pesquisada por Johanna Döbereiner.</li>
<li><strong>Zika:</strong> em 2015 e 2016, pesquisadores brasileiros foram os primeiros a associar o vírus zika aos casos de microcefalia, e depois a confirmar a relação.</li>
<li><strong>Física:</strong> César Lattes participou da descoberta do méson pi em 1947. O Sirius, em Campinas, é um dos aceleradores de luz síncrotron mais avançados do mundo.</li></ul>
<h2>Como é financiada</h2>
<p>A maior parte vem de agências federais, como o CNPq e a Capes, e estaduais, como a Fapesp em São Paulo. Universidades públicas concentram a maior parte das publicações. O investimento em pesquisa e desenvolvimento gira em torno de 1% do PIB, abaixo de países como Coreia do Sul, EUA e Alemanha, e oscila muito com cortes orçamentários.</p>
<h2>Desafios</h2>
<ul class="lista-contra"><li>Orçamento instável, com cortes que interrompem projetos de longo prazo.</li><li>Fuga de cérebros: pesquisadores formados aqui vão trabalhar no exterior.</li><li>Pouca pesquisa em empresas, em comparação com outros países.</li><li>Desigualdade regional na distribuição de verbas e instituições.</li><li>Desinformação e queda de confiança em vacinas.</li></ul>
<div class="nota"><strong>Para acompanhar:</strong> a revista <em>Pesquisa FAPESP</em>, a <em>Ciência Hoje</em> (da SBPC) e as agências de notícias das universidades divulgam a pesquisa brasileira em linguagem acessível.</div>''',
fontes=[('Ciência e tecnologia no Brasil (Wikipédia)', WP + 'Ci%C3%AAncia_e_tecnologia_no_Brasil'), ('Fiocruz', 'https://portal.fiocruz.br/'), ('Embrapa', 'https://www.embrapa.br/'), ('Pesquisa FAPESP', 'https://revistapesquisa.fapesp.br/')],
quiz=[('O que tornou a descoberta de Carlos Chagas única?', ['Ele descobriu a penicilina', 'Descreveu sozinho uma doença inteira: parasita, transmissor e sintomas', 'Inventou a vacina da gripe', 'Foi o primeiro a ir ao espaço'], 1, 'A doença de Chagas foi descrita por completo em 1909.'),
 ('Onde se faz a maior parte da pesquisa no Brasil?', ['Em empresas privadas', 'Em universidades públicas e institutos de pesquisa', 'Em ONGs', 'No exterior'], 1, 'A ciência brasileira é majoritariamente pública.'),
 ('Um governo corta pela metade o orçamento de uma agência de fomento por dois anos. Que efeito a lição sugere?', ['Nenhum', 'Interrupção de projetos de longo prazo e estímulo à fuga de cérebros', 'Mais publicações', 'Mais pesquisa em empresas'], 1, 'Pesquisa depende de continuidade.')],
analogia='A ciência de um país é como uma floresta: leva décadas para crescer e pode ser destruída em poucos anos de seca de recursos. Replantar custa muito mais do que manter.',
crianca='Cientistas brasileiros descobriram doenças, fizeram vacinas e ensinaram a plantar em terras que pareciam ruins. Muitas dessas descobertas ajudam você todos os dias, mesmo sem perceber.',
obj=['Citar conquistas da ciência brasileira.', 'Descrever como a pesquisa é financiada no Brasil.', 'Identificar os principais desafios.'],
caso=('Alguém diz que “o Brasil não produz ciência, só copia”.', 'Que exemplos contradizem isso?', 'Carlos Chagas, a Embrapa no Cerrado, a ligação entre zika e microcefalia, as vacinas do Butantan e da Fiocruz, o Sirius.'),
erro=('“Ciência é coisa de país rico; o Brasil não precisa disso.”', 'Agricultura, vacinas e saúde pública brasileiras dependem de pesquisa feita aqui, adaptada a problemas daqui.'),
ferr=None, pre=['o-que-e-ciencia'],
guardar=['A ciência brasileira tem conquistas mundiais, sobretudo em saúde e agricultura.', 'É feita principalmente em instituições públicas.', 'Orçamento instável e fuga de cérebros são os grandes desafios.'],
pensar='Que problema da sua cidade ou região a ciência brasileira poderia ajudar a resolver?'),
]

NOVAS_INTERMEDIARIO = [
dict(slug='a-revolucao-cientifica', grupo='Filosofia da ciência clássica', titulo='A Revolução Científica', temas=['filosofia', 'fundamentos'],
resumo='Copérnico, Galileu, Kepler, Bacon, Descartes e Newton: como, entre 1543 e 1687, nasceu o modo moderno de investigar a natureza.',
corpo='''
<p class="abre">Entre 1543, ano em que Copérnico publicou que a Terra gira em torno do Sol, e 1687, quando Newton publicou os <em>Principia</em>, a forma de entender a natureza mudou na Europa. Historiadores chamam esse período de <strong>Revolução Científica</strong>, embora discutam o quanto ela foi uma ruptura.</p>
<h2>O mundo antes</h2>
<p>A física de Aristóteles, adaptada à teologia cristã, explicava o movimento pelas naturezas dos corpos: pedras caem porque seu lugar natural é o centro da Terra; o céu, feito de éter, gira em círculos perfeitos. A astronomia de Ptolomeu previa os movimentos dos planetas com epiciclos. Era um sistema coerente e, em muitos aspectos, bem-sucedido.</p>
<h2>As grandes mudanças</h2>
<ul><li><strong>Copérnico</strong> pôs o Sol no centro, por razões de simplicidade e harmonia, mas manteve órbitas circulares.</li>
<li><strong>Tycho Brahe</strong> fez as observações a olho nu mais precisas da época.</li>
<li><strong>Kepler</strong>, usando os dados de Tycho, descobriu que as órbitas são elípticas.</li>
<li><strong>Galileu</strong> apontou o telescópio para o céu (luas de Júpiter, fases de Vênus) e estudou o movimento com experimentos e matemática.</li>
<li><strong>Bacon</strong> e <strong>Descartes</strong> propuseram novos métodos, um experimental e indutivo, o outro dedutivo e matemático.</li>
<li><strong>Newton</strong> uniu tudo: as mesmas leis explicam a queda de uma maçã e a órbita da Lua.</li></ul>
<h2>O que mudou de fato</h2>
<ul class="lista-forte"><li><strong>Matematização da natureza:</strong> leis expressas em equações.</li><li><strong>Experimento:</strong> provocar a natureza em condições controladas, não só observá-la.</li><li><strong>Instrumentos:</strong> telescópio, microscópio, bomba de vácuo, relógio de pêndulo.</li><li><strong>Instituições:</strong> sociedades científicas e revistas que publicavam resultados para que outros os conferissem.</li><li><strong>Mecanicismo:</strong> a natureza como máquina, sem propósitos internos.</li></ul>
<h2>Revolução ou evolução?</h2>
<p>Historiadores como Alexandre Koyré enfatizaram a ruptura; outros, como Pierre Duhem, mostraram raízes medievais (a teoria do ímpeto, os calculadores de Oxford). Steven Shapin abriu um livro dizendo: “Não houve tal coisa como a Revolução Científica, e este é um livro sobre ela”. Os protagonistas também misturavam o novo e o antigo: Kepler fazia horóscopos e Newton dedicou anos à alquimia.</p>
<div class="nota"><strong>Galileu e a Igreja:</strong> o julgamento de 1633 envolveu ciência, teologia, política e personalidade. Galileu tinha razão sobre o movimento da Terra, mas ainda não tinha uma prova decisiva, que só veio depois, com a aberração da luz estelar (1729) e a paralaxe (1838).</div>''',
fontes=[('Scientific Revolution (Wikipédia)', WE + 'Scientific_Revolution'), ('Copernicus (Stanford Encyclopedia)', SEP + 'copernicus/'), ('Galileo Galilei (Stanford Encyclopedia)', SEP + 'galileo/'), ('A Revolução Científica', 'https://www.google.com/search?tbm=bks&q=A+Revolu%C3%A7%C3%A3o+Cient%C3%ADfica+Shapin')],
quiz=[('Quem descobriu que as órbitas dos planetas são elípticas?', ['Copérnico', 'Kepler', 'Aristóteles', 'Bacon'], 1, 'Kepler usou os dados precisos de Tycho Brahe.'),
 ('Qual foi a grande unificação de Newton?', ['Unir química e biologia', 'Mostrar que as mesmas leis explicam a queda dos corpos e as órbitas', 'Provar o geocentrismo', 'Criar o telescópio'], 1, 'A gravitação universal uniu céu e Terra.'),
 ('Um historiador mostra que ideias medievais sobre o movimento anteciparam Galileu. Isso afeta qual debate?', ['Se a Revolução Científica foi ruptura ou continuidade', 'Se a Terra gira', 'Se Newton existiu', 'Nenhum'], 0, 'Duhem e outros mostraram raízes medievais da física moderna.')],
analogia='A Revolução Científica foi como trocar o sistema operacional de um computador. Muitos programas antigos continuaram rodando por um tempo, alguns foram adaptados, mas a base passou a funcionar com outra lógica: matemática, experimento e mecanismo.',
crianca='Por muito tempo, as pessoas acharam que a Terra ficava parada no meio do universo. Alguns cientistas olharam o céu com cuidado, usaram telescópios e contas, e descobriram que a Terra gira em volta do Sol.',
obj=['Descrever as mudanças entre Copérnico e Newton.', 'Identificar o que a Revolução Científica trouxe de novo.', 'Discutir se foi ruptura ou continuidade.'],
caso=('Alguém diz que Galileu foi condenado só porque a Igreja odiava a ciência.', 'O que a história mostra?', 'O caso envolveu política, teologia, personalidade e o fato de que a prova decisiva do movimento da Terra ainda não existia.'),
erro=('“Os pioneiros da ciência moderna eram racionalistas puros, livres de crenças antigas.”', 'Kepler fazia horóscopos e Newton estudava alquimia. O novo conviveu com o antigo.'),
ferr='quem-disse', pre=['uma-breve-historia-da-ciencia'],
guardar=['Entre 1543 e 1687, a natureza passou a ser explicada com matemática, experimentos e mecanismos.', 'Sociedades científicas e revistas institucionalizaram a crítica.', 'Historiadores debatem quanto houve de ruptura e quanto de continuidade.'],
pensar='Que ideia do seu tempo, hoje evidente, pode parecer tão estranha quanto o geocentrismo daqui a 300 anos?'),

dict(slug='modelos-e-simulacoes', grupo='Ciência na prática', titulo='Modelos e simulações', temas=['metodo', 'filosofia'],
resumo='Mapas, maquetes, equações e simulações de computador: por que a ciência usa representações simplificadas e como avaliar se são confiáveis.',
corpo='''
<p class="abre">“Todos os modelos estão errados, mas alguns são úteis.” A frase do estatístico George Box resume um ponto central da ciência: quase nunca estudamos o mundo diretamente, e sim por meio de <strong>modelos</strong>, representações simplificadas que capturam o que importa para uma pergunta.</p>
<h2>Tipos de modelo</h2>
<ul><li><strong>Físicos:</strong> maquetes de aviões em túneis de vento, o modelo de dupla hélice de arame de Watson e Crick.</li><li><strong>Matemáticos:</strong> equações que descrevem crescimento populacional, epidemias ou órbitas.</li><li><strong>Computacionais:</strong> simulações do clima, de galáxias, do trânsito, de proteínas.</li><li><strong>Organismos-modelo:</strong> moscas, camundongos, leveduras, estudados para entender processos gerais (com limites sérios, como mostra a dificuldade de transferir resultados de animais para humanos).</li></ul>
<h2>Por que simplificar</h2>
<p>Um mapa do tamanho do território seria inútil, como na história de Borges. Modelos idealizam de propósito: o plano sem atrito, o gás de partículas pontuais, o consumidor perfeitamente racional. A pergunta não é se o modelo é realista em tudo, mas se é realista <strong>no que importa</strong> para o objetivo.</p>
<h2>Como avaliar um modelo</h2>
<ul class="lista-forte"><li><strong>Previsões testadas:</strong> o modelo acertou casos que não foram usados para construí-lo?</li><li><strong>Robustez:</strong> modelos diferentes, com pressupostos diferentes, chegam a conclusões parecidas?</li><li><strong>Sensibilidade:</strong> pequenas mudanças nos pressupostos mudam muito o resultado?</li><li><strong>Transparência:</strong> os pressupostos e o código estão disponíveis?</li><li><strong>Faixa de validade:</strong> o modelo está sendo usado dentro das condições em que foi testado?</li></ul>
<h2>Exemplos</h2>
<p>Os modelos climáticos dos anos 1970 e 1980 previram com boa precisão o aquecimento que viria, como mostrou uma avaliação publicada em 2020. Já modelos epidemiológicos do início da pandemia de Covid-19 variaram muito, porque dependiam de parâmetros ainda desconhecidos e do comportamento das pessoas, que muda em resposta às próprias previsões.</p>
<div class="nota"><strong>Simulação é experimento?</strong> Filósofos debatem se simulações de computador produzem conhecimento novo, como experimentos, ou só calculam consequências do que já pusemos no modelo. A resposta tende a depender de quão bem o modelo foi validado contra o mundo real.</div>''',
fontes=[('Models in Science (Stanford Encyclopedia)', SEP + 'models-science/'), ('Computer Simulations in Science (Stanford Encyclopedia)', SEP + 'simulations-science/'), ('Evaluating the performance of past climate model projections (Geophysical Research Letters)', 'https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GL085378')],
quiz=[('O que significa “todos os modelos estão errados, mas alguns são úteis”?', ['Que modelos não servem', 'Que modelos simplificam de propósito e valem pelo que capturam bem', 'Que só modelos físicos funcionam', 'Que a ciência é falsa'], 1, 'Simplificar é a função de um modelo.'),
 ('O que é robustez de um modelo?', ['Ser feito de material resistente', 'Modelos diferentes, com pressupostos diferentes, chegarem a resultados parecidos', 'Ter muitas equações', 'Nunca mudar'], 1, 'Convergência entre modelos independentes aumenta a confiança.'),
 ('Um modelo de trânsito calibrado para dias úteis é usado para prever o trânsito no carnaval. Qual o risco?', ['Nenhum', 'Usar o modelo fora da faixa de validade em que foi testado', 'Ser simples demais', 'Ser um modelo físico'], 1, 'Modelos valem nas condições em que foram validados.')],
analogia='Um modelo é como um mapa de metrô. Ele distorce distâncias e ignora ruas, e por isso mesmo é ótimo para saber onde trocar de linha. Mas seria péssimo para ir a pé.',
crianca='Um globo é um modelo da Terra: é muito menor e não tem pessoas nem árvores, mas ajuda a entender onde ficam os países. Cientistas usam modelos assim, às vezes feitos de contas no computador.',
obj=['Distinguir tipos de modelo usados na ciência.', 'Explicar por que modelos idealizam.', 'Aplicar critérios para avaliar a confiabilidade de um modelo.'],
caso=('Alguém diz: “modelos climáticos são só suposições de computador, não dá para confiar”.', 'Como avaliar essa crítica?', 'Verificando se os modelos acertaram previsões passadas (os antigos acertaram bem), se modelos independentes concordam e se os pressupostos são públicos.'),
erro=('“Se o modelo é simplificado, ele é falso e inútil.”', 'Simplificar é o propósito. O modelo vale se for preciso no que importa para a pergunta e for validado.'),
ferr=None, pre=['hipotese-teoria-e-lei', 'tipos-de-ciencia'],
guardar=['Modelos simplificam de propósito; valem pelo que capturam bem.', 'Avalie por previsões testadas, robustez, sensibilidade, transparência e faixa de validade.', 'Modelos antigos do clima acertaram bem; modelos de epidemias novas variam mais.'],
pensar='Que modelo simplificado você usa no dia a dia para decidir algo, como um mapa mental do trânsito?'),

dict(slug='etica-na-pesquisa', grupo='Ciência na prática', titulo='Ética na pesquisa', temas=['sociedade'],
resumo='Do caso Tuskegee ao consentimento informado e aos comitês de ética: por que a ciência precisa de limites morais, e para quem esses limites valem.',
corpo='''
<p class="abre">Saber mais nunca justifica qualquer meio. A ética na pesquisa nasceu de escândalos reais, em que pessoas foram usadas como cobaias sem saber, e continua a se perguntar quem merece proteção e quanto.</p>
<h2>Os casos que mudaram as regras</h2>
<ul><li><strong>Experimentos nazistas:</strong> médicos submeteram prisioneiros de campos de concentração a experimentos brutais. O julgamento de Nuremberg resultou, em 1947, no <strong>Código de Nuremberg</strong>, cujo primeiro princípio é o consentimento voluntário.</li>
<li><strong>Tuskegee (EUA, 1932–1972):</strong> homens negros com sífilis foram acompanhados sem tratamento, mesmo depois de a penicilina se tornar disponível, sem saber o que tinham. O caso levou ao <strong>Relatório Belmont</strong> (1979).</li>
<li><strong>Talidomida (anos 1950–1960):</strong> um remédio para enjoo na gravidez causou malformações em milhares de bebês, inclusive no Brasil, e levou a regras mais rigorosas de testes de medicamentos.</li></ul>
<h2>Os princípios</h2>
<p>O Relatório Belmont resumiu três princípios, ainda usados:</p>
<ol><li><strong>Respeito às pessoas:</strong> consentimento livre e esclarecido; proteção extra para quem tem autonomia reduzida.</li><li><strong>Beneficência:</strong> maximizar benefícios e minimizar danos.</li><li><strong>Justiça:</strong> distribuir com equidade os riscos e os benefícios da pesquisa, sem usar grupos vulneráveis por conveniência.</li></ol>
<h2>No Brasil</h2>
<p>Pesquisas com seres humanos precisam ser aprovadas por um Comitê de Ética em Pesquisa (CEP), dentro do sistema coordenado pela Comissão Nacional de Ética em Pesquisa (Conep). Pesquisas com animais são reguladas pela Lei Arouca (2008) e pelas Comissões de Ética no Uso de Animais (CEUAs).</p>
<h2>Integridade científica</h2>
<p>Ética na pesquisa inclui também a honestidade: não fabricar nem falsificar dados, não plagiar, declarar conflitos de interesse, dar crédito a quem contribuiu. Fraudes, como a do artigo antivacina de Wakefield, causam danos que duram décadas.</p>
<h2>E os animais?</h2>
<p>As proteções dadas a animais em pesquisa são muito menores do que as dadas a humanos, embora a ciência reconheça que vertebrados e alguns invertebrados são sencientes. O princípio dos <strong>3Rs</strong> (substituir, reduzir, refinar) tenta limitar o sofrimento. Para o sencientismo, a diferença de proteção reflete uma escolha moral discutível, não um fato científico. Veja o debate sobre <a href="debates/testes-em-animais.html">testes em animais</a>.</p>
<div class="nota"><strong>Ponte com a ética:</strong> o <a href="https://eticaparainiciantes.biblioverse.org/" target="_blank" rel="noopener">Ética Para Iniciantes</a> discute bioética e o peso moral do sofrimento animal com mais profundidade.</div>''',
fontes=[('Research ethics (Stanford Encyclopedia: Ethics of Clinical Research)', SEP + 'clinical-research/'), ('Código de Nuremberg (Wikipédia)', WP + 'C%C3%B3digo_de_Nuremberg'), ('Tuskegee Syphilis Study (Wikipédia)', WE + 'Tuskegee_Syphilis_Study'), ('The Belmont Report', 'https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html')],
quiz=[('Qual o primeiro princípio do Código de Nuremberg?', ['Publicar rápido', 'Consentimento voluntário do participante', 'Usar só animais', 'Ter financiamento público'], 1, 'Nenhuma pesquisa pode usar pessoas sem consentimento.'),
 ('Quais são os três princípios do Relatório Belmont?', ['Lucro, rapidez e sigilo', 'Respeito às pessoas, beneficência e justiça', 'Indução, dedução e abdução', 'Hipótese, teste e lei'], 1, 'São a base da ética em pesquisa com humanos.'),
 ('Um estudo só recruta pessoas de baixa renda porque elas aceitam pagamentos menores, embora o tratamento depois vá ser vendido caro. Que princípio é violado?', ['Justiça', 'Beneficência', 'Falseabilidade', 'Nenhum'], 0, 'Riscos e benefícios devem ser distribuídos com equidade.')],
analogia='A ética na pesquisa é como as regras de segurança num canteiro de obras. Ninguém duvida de que o prédio é importante, mas isso não autoriza pôr operários em risco sem proteção nem consentimento.',
crianca='Antes de testar um remédio em alguém, os cientistas precisam explicar tudo e perguntar se a pessoa quer participar. E não podem machucar ninguém só para descobrir algo.',
obj=['Conhecer os casos que deram origem às regras de ética em pesquisa.', 'Explicar os princípios do Relatório Belmont.', 'Discutir integridade científica e a diferença de proteção entre humanos e animais.'],
caso=('Um pesquisador quer testar um novo tratamento sem contar aos participantes que eles podem receber placebo, “para não estragar o efeito”.', 'Isso é aceitável?', 'Não. Os participantes devem saber que podem receber placebo; o cegamento é sobre qual grupo, não sobre a existência do placebo. Esconder isso viola o consentimento esclarecido.'),
erro=('“Se a descoberta for importante, os meios se justificam.”', 'Os casos de Nuremberg e Tuskegee mostram aonde isso leva. O consentimento e a proteção contra danos limitam a busca por conhecimento.'),
ferr=None, pre=['experimentos-e-grupo-controle'],
guardar=['As regras nasceram de escândalos: experimentos nazistas, Tuskegee, talidomida.', 'Respeito às pessoas, beneficência e justiça.', 'Animais sencientes têm proteção muito menor, e isso é uma escolha moral discutível.'],
pensar='Você participaria de um ensaio clínico? Que informações exigiria antes?'),
]

NOVAS_AVANCADO = [
dict(slug='leis-da-natureza', grupo='Teorias e realidade', titulo='O que são leis da natureza?', temas=['filosofia'],
resumo='Regularidades, necessidades ou só bons resumos? Humeanos, necessitaristas e quem acha que as leis “mentem”.',
corpo='''
<p class="abre">“Nenhum objeto viaja mais rápido que a luz” e “nenhuma esfera de ouro tem mais de um quilômetro de diâmetro” podem ser ambas verdadeiras. Mas a primeira parece uma lei da natureza, e a segunda, um acidente. Qual é a diferença? Essa pergunta divide os filósofos.</p>
<h2>Regularidade (humeanismo)</h2>
<p>Para os herdeiros de Hume, não há nada na natureza além de fatos particulares; leis são <strong>regularidades</strong>. A versão mais influente é a de David Lewis, a teoria do <strong>melhor sistema</strong>: leis são os axiomas do sistema que melhor equilibra simplicidade e poder de descrever todos os fatos. A esfera de ouro não entra porque não simplifica nada.</p>
<p><em>Problema:</em> se as leis só resumem o que acontece, elas não <em>explicam</em> por que acontece. Seria circular dizer que a pedra cai por causa de uma lei que só resume que pedras caem.</p>
<h2>Necessitarismo</h2>
<p>David Armstrong, Fred Dretske e Michael Tooley propuseram que leis são <strong>relações de necessidade</strong> entre propriedades: ser massa necessita atrair outra massa. Isso explicaria por que regularidades legais se mantêm e acidentais não.</p>
<p><em>Problema:</em> o que é essa “necessitação”, e como a conhecemos? Críticos dizem que é só um nome para o mistério.</p>
<h2>Disposições e poderes</h2>
<p>Outra família (Alexander Bird, Stephen Mumford) diz que as propriedades têm <strong>poderes</strong> essenciais: carga elétrica é, em parte, a disposição de atrair e repelir. Leis derivam desses poderes.</p>
<h2>As leis “mentem”?</h2>
<p>Nancy Cartwright notou que as leis fundamentais, entendidas como descrições literais, quase nunca são verdadeiras: a lei da gravitação descreve corpos sem cargas elétricas, sem atrito e sem outras forças, o que não existe. Para ela, leis descrevem <strong>capacidades</strong> que se manifestam em condições ideais ou em máquinas construídas para isolá-las.</p>
<h2>E as ciências especiais?</h2>
<p>Biologia, economia e psicologia têm “leis” cheias de exceções e cláusulas <em>ceteris paribus</em> (“mantido o resto igual”). Algumas pessoas acham que só a física tem leis de verdade; outras, que leis vêm em graus de estabilidade.</p>
<div class="nota"><strong>Por que importa:</strong> a resposta afeta o que é explicar, se a indução se justifica (se há necessidade natural, a uniformidade teria fundamento) e até o debate sobre livre-arbítrio.</div>''',
fontes=[('Laws of Nature (Stanford Encyclopedia)', SEP + 'laws-of-nature/'), ('Laws of Nature (Internet Encyclopedia of Philosophy)', IEP + 'lawofnat/'), ('How the Laws of Physics Lie', 'https://www.google.com/search?tbm=bks&q=How+the+Laws+of+Physics+Lie')],
quiz=[('O que diz a teoria do melhor sistema de Lewis?', ['Leis são mandamentos divinos', 'Leis são os axiomas do sistema que melhor equilibra simplicidade e poder descritivo', 'Leis são necessidades misteriosas', 'Não há leis'], 1, 'É a versão mais influente do humeanismo.'),
 ('Qual a crítica ao humeanismo?', ['Ele é complicado demais', 'Se leis só resumem fatos, parecem não explicar por que eles acontecem', 'Ele nega a física', 'Ele exige Deus'], 1, 'Resumo não é explicação, dizem os críticos.'),
 ('Uma economista diz: “a lei da oferta e da procura vale, mantido o resto igual”. Que questão isso levanta?', ['Se as ciências especiais têm leis de verdade, cheias de cláusulas ceteris paribus', 'Se a economia usa matemática', 'Se a física é falsa', 'Nenhuma'], 0, 'Leis com exceções desafiam a ideia de lei universal.')],
analogia='Para o humeano, leis são como a melhor legenda para um álbum enorme de fotos: o resumo mais curto que descreve tudo. Para o necessitarista, são como as regras do jogo que fazem as jogadas acontecerem.',
crianca='Quando você solta uma bola, ela cai. Sempre. Os cientistas chamam isso de lei. Os filósofos perguntam: a bola cai porque existe uma regra obrigando, ou a “lei” é só o nosso jeito de dizer que ela sempre cai?',
obj=['Distinguir regularidades legais de acidentais.', 'Comparar humeanismo, necessitarismo e disposicionalismo.', 'Explicar a tese de Cartwright e o problema das ciências especiais.'],
caso=('Todas as moedas no seu bolso hoje são de 1 real. Todos os metais se dilatam quando aquecidos.', 'Por que só a segunda parece uma lei?', 'A primeira é acidental e não sustenta contrafactuais (“se esta moeda de 50 centavos estivesse no bolso, seria de 1 real” é falso). A segunda sustenta: “se este metal fosse aquecido, dilataria”.'),
erro=('“Lei da natureza é o mesmo que lei científica escrita nos livros.”', 'As leis científicas são nossas formulações, que podem estar erradas. A pergunta filosófica é o que, no mundo, elas tentam descrever.'),
ferr=None, pre=['explicacao-cientifica', 'hipotese-teoria-e-lei'],
guardar=['Leis sustentam contrafactuais; regularidades acidentais, não.', 'Humeanos: leis resumem; necessitaristas: leis obrigam; disposicionalistas: leis vêm dos poderes das propriedades.', 'Cartwright: leis fundamentais valem em condições ideais.'],
pensar='Há “leis” na sua área de interesse que valem só “mantido o resto igual”?'),

dict(slug='reducionismo-e-emergencia', grupo='Teorias e realidade', titulo='Reducionismo e emergência', temas=['filosofia'],
resumo='A biologia é só química, e a química é só física? Ou há propriedades que surgem em níveis mais altos e não se explicam pelas partes?',
corpo='''
<p class="abre">Uma célula é feita de moléculas, moléculas de átomos, átomos de partículas. Isso quer dizer que tudo, em princípio, se explica pela física? Ou existem fenômenos, como a vida, a mente ou os mercados, que <strong>emergem</strong> em níveis mais altos e precisam de explicações próprias?</p>
<h2>Três tipos de reducionismo</h2>
<ul><li><strong>Ontológico:</strong> tudo o que existe é composto pelas entidades da física; não há “força vital” nem substâncias extras. A maioria dos cientistas e filósofos aceita isso.</li><li><strong>Teórico:</strong> as teorias de níveis altos podem ser deduzidas das de níveis baixos, como Ernest Nagel propôs (a termodinâmica a partir da mecânica estatística).</li><li><strong>Metodológico:</strong> a melhor estratégia de pesquisa é estudar as partes. Muito bem-sucedida na biologia molecular.</li></ul>
<h2>Os problemas da redução teórica</h2>
<ul class="lista-contra"><li><strong>Realizabilidade múltipla:</strong> a mesma propriedade de alto nível pode ser realizada por bases muito diferentes. “Ser um relógio” pode ser feito de engrenagens, quartzo ou areia; “sentir dor” talvez possa ocorrer em cérebros muito diferentes. Não há uma única tradução para a física.</li><li><strong>Complexidade:</strong> mesmo sabendo as leis das partes, calcular o todo pode ser impossível na prática.</li><li><strong>Explicações melhores no nível alto:</strong> explicar por que um pino quadrado não passa num buraco redondo pela geometria é melhor do que pela posição de cada átomo (exemplo de Hilary Putnam).</li></ul>
<h2>Emergência</h2>
<ul><li><strong>Emergência fraca:</strong> propriedades do todo são difíceis de prever, mas em princípio derivam das partes. Exemplos: padrões de revoada de pássaros, engarrafamentos, o “jogo da vida” de computador.</li><li><strong>Emergência forte:</strong> propriedades do todo são genuinamente novas e não deriváveis das partes, talvez com poderes causais próprios. É muito mais controversa; a consciência é o candidato mais citado.</li></ul>
<p>O físico Philip Anderson resumiu num artigo famoso de 1972: “Mais é diferente”. Mesmo aceitando que tudo é feito de partículas, cada nível de organização exige conceitos e leis próprios.</p>
<div class="nota"><strong>Cuidado com o uso popular:</strong> “emergência” às vezes é usada como palavra mágica para dispensar explicação (“a consciência simplesmente emerge”). Dizer que algo emerge não é explicar como.</div>''',
fontes=[('Scientific Reduction (Stanford Encyclopedia)', SEP + 'scientific-reduction/'), ('Emergent Properties (Stanford Encyclopedia)', SEP + 'properties-emergent/'), ('More Is Different (Science)', 'https://www.science.org/doi/10.1126/science.177.4047.393')],
quiz=[('O que é reducionismo ontológico?', ['A tese de que tudo é composto pelas entidades da física', 'A tese de que a biologia é inútil', 'Um método estatístico', 'A rejeição da física'], 0, 'É a forma mais aceita de reducionismo.'),
 ('O que é realizabilidade múltipla?', ['Fazer o mesmo experimento várias vezes', 'A mesma propriedade de alto nível poder ser realizada por bases físicas diferentes', 'Ter várias teorias', 'Um tipo de falácia'], 1, 'É o principal argumento contra a redução teórica.'),
 ('Um engarrafamento se forma sem que nenhum motorista queira, só pelas interações. Isso é exemplo de:', ['Emergência fraca', 'Emergência forte', 'Reducionismo teórico', 'Pseudociência'], 0, 'O padrão é difícil de prever, mas deriva das interações das partes.')],
analogia='Uma música é feita de notas, e as notas de vibrações do ar. Mas a melodia, o ritmo e a emoção não aparecem quando se olha uma nota de cada vez. Mais é diferente.',
crianca='Um formigueiro faz coisas incríveis, como construir túneis, mas nenhuma formiga sabe o plano. O que o grupo faz é mais do que cada formiga sozinha.',
obj=['Distinguir reducionismo ontológico, teórico e metodológico.', 'Explicar a realizabilidade múltipla e os limites da redução.', 'Diferenciar emergência fraca e forte, e o mau uso do termo.'],
caso=('Alguém diz que “o amor é só química no cérebro”.', 'Que tipo de reducionismo está em jogo, e o que fica de fora?', 'Pode ser reducionismo ontológico (aceitável: o amor tem base física) ou teórico (mais forte: a explicação química bastaria). O nível psicológico e social do amor pode exigir conceitos próprios.'),
erro=('“Se tudo é feito de átomos, a física explica tudo.”', 'Ser feito de átomos não garante que a melhor explicação esteja no nível dos átomos. Cada nível pode exigir leis e conceitos próprios.'),
ferr=None, pre=['explicacao-cientifica'],
guardar=['Quase todos aceitam o reducionismo ontológico; o teórico é controverso.', 'Realizabilidade múltipla e complexidade limitam a redução.', 'Emergência fraca é comum; a forte é controversa; “emerge” não é explicação.'],
pensar='Que fenômeno da sua vida é mais do que a soma das partes?'),

dict(slug='interpretacoes-da-mecanica-quantica', grupo='Teorias e realidade', titulo='As interpretações da mecânica quântica', temas=['filosofia'],
resumo='A teoria mais precisa da física e ninguém concorda sobre o que ela diz da realidade: Copenhague, muitos mundos, Bohm, colapso e QBismo.',
corpo='''
<p class="abre">A mecânica quântica prevê resultados com precisão espantosa e sustenta lasers, transistores e ressonância magnética. Mas os físicos não concordam sobre o que ela diz sobre a realidade. É o caso mais vivo do debate entre realismo e antirrealismo.</p>
<h2>O problema da medição</h2>
<p>Na teoria, um sistema é descrito por uma <strong>função de onda</strong>, que evolui de forma contínua e pode estar em superposição: um elétron “aqui e ali”. Mas quando medimos, sempre encontramos um resultado definido. O que acontece com a superposição? O gato de Schrödinger, vivo e morto ao mesmo tempo dentro da caixa, foi criado para mostrar o absurdo de levar a superposição para objetos grandes.</p>
<h2>As principais interpretações</h2>
<ul><li><strong>Copenhague</strong> (Bohr, Heisenberg): a teoria descreve o que podemos medir, não uma realidade independente; a medição “colapsa” a função de onda. Pragmática, mas vaga sobre o que é uma medição.</li>
<li><strong>Muitos mundos</strong> (Hugh Everett, 1957): não há colapso; todos os resultados acontecem, cada um num ramo do universo. Elegante matematicamente, mas multiplica mundos e tem dificuldade em explicar probabilidades.</li>
<li><strong>Bohmiana</strong> (David Bohm, 1952): partículas têm posições definidas o tempo todo, guiadas pela função de onda. Recupera o realismo, mas é explicitamente não local.</li>
<li><strong>Colapso objetivo</strong> (GRW, Penrose): a função de onda colapsa espontaneamente, mais rápido em sistemas grandes. Muda a teoria e faz previsões que podem ser testadas.</li>
<li><strong>QBismo e interpretações epistêmicas:</strong> a função de onda representa o conhecimento ou as crenças de um agente, não o mundo. Próxima do bayesianismo.</li></ul>
<h2>O que é consenso</h2>
<p>Os experimentos sobre as desigualdades de Bell, premiados com o Nobel de Física de 2022 (Aspect, Clauser e Zeilinger), mostraram que nenhuma teoria com variáveis ocultas locais reproduz as previsões quânticas. A natureza é, num sentido preciso, não local ou não “realista” à moda clássica. Mas as interpretações acima, em sua maioria, são compatíveis com todos os experimentos feitos até hoje: é um caso de subdeterminação.</p>
<div class="nota"><strong>Contra a cura quântica:</strong> nenhuma interpretação séria diz que a consciência humana cria a realidade ou que pensamentos curam doenças. Usar o mistério interpretativo para vender terapias é pseudociência; veja <a href="pseudociencias/cura-quantica.html">cura quântica</a>.</div>''',
fontes=[('Philosophical Issues in Quantum Theory (Stanford Encyclopedia)', SEP + 'qt-issues/'), ('Interpretations of quantum mechanics (Wikipédia)', WE + 'Interpretations_of_quantum_mechanics'), ('The Nobel Prize in Physics 2022', 'https://www.nobelprize.org/prizes/physics/2022/summary/')],
quiz=[('O que é o problema da medição?', ['Medir com régua errada', 'Explicar por que superposições dão resultados definidos quando medimos', 'Falta de instrumentos', 'Um erro de cálculo'], 1, 'É o núcleo das disputas interpretativas.'),
 ('O que diz a interpretação dos muitos mundos?', ['Que só há um mundo', 'Que não há colapso e todos os resultados ocorrem em ramos diferentes', 'Que a consciência cria a realidade', 'Que partículas têm posições definidas'], 1, 'É a proposta de Everett.'),
 ('Um curso diz que, segundo a física quântica, “seus pensamentos criam a realidade”. O que a lição responde?', ['Que é a interpretação de Copenhague', 'Que nenhuma interpretação séria diz isso', 'Que é a dos muitos mundos', 'Que é consenso'], 1, 'Medição é interação física, não pensamento humano.')],
analogia='As interpretações da mecânica quântica são como várias explicações para um truque de mágica que funciona perfeitamente sempre. Todos veem o mesmo resultado, mas discordam sobre o que acontece por trás da cortina.',
crianca='Coisas muito, muito pequenas, como os elétrons, se comportam de um jeito estranho, diferente de bolas e pedras. Os cientistas sabem fazer as contas certinhas, mas ainda discutem o que está acontecendo de verdade.',
obj=['Explicar o problema da medição.', 'Comparar as principais interpretações.', 'Separar o consenso experimental (Bell) da disputa interpretativa e do mau uso pela pseudociência.'],
caso=('Dois físicos usam as mesmas equações e fazem as mesmas previsões, mas um acredita em muitos mundos e o outro não.', 'Algum experimento atual decide entre eles?', 'Em geral não: é um caso de subdeterminação. Só interpretações que mudam a teoria, como o colapso objetivo, fazem previsões diferentes testáveis.'),
erro=('“A física quântica provou que a realidade não existe.”', 'Mostrou que a realidade não se comporta à moda clássica. Há interpretações realistas, como a bohmiana e a dos muitos mundos.'),
ferr=None, pre=['realismo-e-antirrealismo', 'subdeterminacao-e-duhem-quine'],
guardar=['O problema da medição: superposição na teoria, resultado definido na prática.', 'Copenhague, muitos mundos, Bohm, colapso objetivo e QBismo dão respostas diferentes.', 'Os testes de Bell são consenso; a interpretação segue em aberto; “cura quântica” não tem base em nenhuma.'],
pensar='Se duas interpretações fazem as mesmas previsões, faz sentido perguntar qual é a verdadeira?'),
]
