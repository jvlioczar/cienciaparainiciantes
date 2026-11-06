"""Quarta leva (2026-11-07): debate sobre a responsabilidade dos cientistas, pensadores, jogo de consensos e termos do glossário."""
from debates import D
from pessoas import P_, FIL, CIE

DEBATES_NOVOS3 = [
D('responsabilidade-dos-cientistas', 'Cientistas são responsáveis pelo uso de suas descobertas?', 'Ética na pesquisa', 'Da bomba atômica à edição genética: o cientista só descobre, ou responde também pelo que fazem com o que ele descobre?',
  'Depois de Hiroshima, Robert Oppenheimer disse que os físicos “conheceram o pecado”. Outros cientistas acham que seu papel é produzir conhecimento, e que o uso cabe à sociedade. A pergunta voltou com a edição genética, a inteligência artificial e a pesquisa com vírus.',
  [('Sim, têm responsabilidade', ['Quem sabe mais sobre os riscos de uma descoberta tem o dever de alertar.', 'Há pesquisas cujo uso nocivo é previsível, como armas biológicas.', 'Cientistas já se autorregularam com sucesso: a conferência de Asilomar (1975) criou regras para o DNA recombinante.', 'O Manifesto Russell-Einstein (1955) e as Conferências Pugwash, Nobel da Paz de 1995, mostram cientistas assumindo esse papel.']),
   ('A responsabilidade é sobretudo de quem usa', ['Conhecimento básico raramente tem uso previsível; a mesma química faz remédios e venenos.', 'Proibir pesquisa por medo do uso pode impedir benefícios enormes.', 'Decisões sobre usos são políticas e devem ser tomadas democraticamente, não só por cientistas.'])],
  [('pragmatismo', 'Dewey diria que o conhecimento é inseparável de suas consequências práticas.'), ('empirismo-contextual', 'Lembraria que a comunidade científica, e não só o indivíduo, deve debater os usos.')],
  ['A responsabilidade pode ser individual (não participar), coletiva (regras da comunidade) ou pública (leis).', 'O grau de previsibilidade do uso nocivo varia muito entre áreas.', 'Pesquisas financiadas por militares ou empresas trazem pressões específicas.'],
  ('aberto', 'Há amplo acordo de que cientistas devem alertar sobre riscos previsíveis e recusar participar de abusos, e de que a comunidade pode criar regras próprias, como em Asilomar. Até onde vai a responsabilidade por usos imprevisíveis, e quem deve decidir sobre pesquisas de duplo uso, segue em debate.'),
  ['ciencia-a-servico-do-mal', 'ciencia-e-tecnologia', 'etica-na-pesquisa'],
  [('Russell–Einstein Manifesto (Wikipédia)', 'https://en.wikipedia.org/wiki/Russell%E2%80%93Einstein_Manifesto'), ('Asilomar Conference on Recombinant DNA (Wikipédia)', 'https://en.wikipedia.org/wiki/Asilomar_Conference_on_Recombinant_DNA'), ('Pugwash Conferences on Science and World Affairs', 'https://pugwash.org/')]),
]

P_NOVOS3 = [
P_('kurt-godel', 'Kurt Gödel', '1906–1978', 'Áustria / EUA', CIE, 'Lógico que provou que todo sistema matemático suficientemente rico tem verdades que não pode provar.',
   ['Provou os teoremas da incompletude (1931).', 'Provou a consistência relativa da hipótese do contínuo.', 'Encontrou soluções da relatividade geral que permitiriam viagens no tempo.'],
   ['Sobre proposições formalmente indecidíveis dos Principia Mathematica e sistemas relacionados'],
   'Seus teoremas são frequentemente mal usados para afirmar que “nada pode ser provado” ou que a mente supera qualquer máquina, conclusões que não decorrem deles.', [], 'Kurt_G%C3%B6del'),
P_('alan-turing', 'Alan Turing', '1912–1954', 'Reino Unido', CIE, 'Matemático que fundou a ciência da computação e provou que há problemas que nenhum computador resolve.',
   ['Definiu a máquina de Turing, modelo teórico do computador.', 'Provou a indecidibilidade do problema da parada.', 'Ajudou a decifrar o código Enigma na Segunda Guerra.', 'Propôs o teste de Turing para a inteligência das máquinas.'],
   ['Sobre números computáveis', 'Computação e inteligência'],
   'O teste de Turing é criticado como medida de imitação, não de inteligência ou consciência. Turing foi condenado em 1952 por ser homossexual e submetido a castração química; o governo britânico pediu desculpas em 2009.', [], 'Alan_Turing'),
P_('oppenheimer', 'J. Robert Oppenheimer', '1904–1967', 'Estados Unidos', CIE, 'Físico que dirigiu o laboratório de Los Alamos no Projeto Manhattan e depois defendeu o controle das armas nucleares.',
   ['Dirigiu o desenvolvimento da primeira bomba atômica.', 'Fez contribuições à física quântica e à astrofísica de buracos negros.', 'Defendeu o controle internacional da energia atômica e se opôs à bomba de hidrogênio.'],
   ['Artigos sobre física teórica', 'Ciência e o Entendimento Comum'],
   'Críticos o responsabilizam por ter liderado a criação da bomba; em 1954, teve a autorização de segurança cassada num processo marcado pelo macarthismo, que o governo dos EUA anulou em 2022.', [], 'J._Robert_Oppenheimer'),
P_('fritz-haber', 'Fritz Haber', '1868–1934', 'Alemanha', CIE, 'Químico cuja síntese da amônia alimenta bilhões de pessoas, e que comandou o uso de gás venenoso na Primeira Guerra.',
   ['Desenvolveu a síntese da amônia (processo Haber-Bosch), base dos fertilizantes nitrogenados.', 'Ganhou o Nobel de Química de 1918.', 'Organizou o primeiro grande ataque com gás cloro, em Ypres, em 1915.'],
   ['Trabalhos sobre a síntese da amônia'],
   'É o exemplo clássico do duplo uso da ciência. Sua esposa, a química Clara Immerwahr, opôs-se ao uso de armas químicas. Judeu, Haber teve de deixar a Alemanha nazista em 1933.', [], 'Fritz_Haber'),
]

JOGO_CONSENSO = ('consenso-ou-em-aberto', 'Consenso, em aberto ou refutado?', 'Doze afirmações. Diga se a ciência considera cada uma estabelecida, ainda em aberto ou já refutada.', 'arvore')
CON, ABE, REF = 'Consenso científico', 'Em aberto', 'Refutado'
JOGO_CONSENSO_DADOS = dict(ops=[CON, ABE, REF], lede='Doze afirmações. Diga se a ciência considera cada uma estabelecida, ainda em aberto ou já refutada.', nota='Classificações resumidas, com base nas academias de ciência, revisões sistemáticas e órgãos de saúde. <a href="../grandes-consensos-cientificos.html">Leia sobre os grandes consensos</a> e as <a href="../perguntas-em-aberto.html">perguntas em aberto</a>.', itens=[
 ('A atividade humana é a principal causa do aquecimento global atual.', CON, 'É a conclusão do IPCC e de praticamente todas as academias de ciência.'),
 ('A matéria escura é formada por partículas ainda não detectadas.', ABE, 'É a hipótese principal, mas a natureza da matéria escura segue desconhecida.'),
 ('A vacina tríplice viral causa autismo.', REF, 'Estudos com milhões de crianças não encontraram relação; o artigo original foi retratado por fraude.'),
 ('Todos os seres vivos têm ancestrais comuns.', CON, 'Sustentado por fósseis, anatomia e genética.'),
 ('A vida na Terra começou num “mundo de RNA”.', ABE, 'É uma hipótese forte, mas a origem da vida segue em aberto.'),
 ('A homeopatia funciona melhor que o placebo.', REF, 'Revisões amplas não encontraram efeito além do placebo.'),
 ('O universo tem cerca de 13,8 bilhões de anos.', CON, 'Estimativa sustentada por várias observações independentes.'),
 ('Existe vida em outros planetas.', ABE, 'Não há evidência a favor nem contra; a pergunta está em aberto.'),
 ('Fumar causa câncer de pulmão.', CON, 'Uma das conclusões mais bem estabelecidas da epidemiologia.'),
 ('A posição dos astros no nascimento define a personalidade.', REF, 'Testes cegos não mostraram efeito.'),
 ('É possível unir a gravidade e a mecânica quântica numa só teoria.', ABE, 'É a busca da gravidade quântica, sem confirmação experimental até agora.'),
 ('Muitos animais, como mamíferos e aves, têm experiências conscientes.', CON, 'Reconhecido pelas Declarações de Cambridge (2012) e de Nova York (2024).'),
])

GLOSSARIO_NOVOS = [
 ('Fundamentos', 'Incognoscível', 'O que não pode ser conhecido, em princípio ou na prática.', 'o-incognoscivel.html'),
 ('Fundamentos', 'Agnosticismo', 'Posição de que certas questões, como a existência de Deus, estão além do que podemos saber.', 'o-incognoscivel.html'),
 ('Método e evidência', 'Fraude científica', 'Fabricação, falsificação de dados ou plágio na pesquisa.', 'fraudes-cientificas.html'),
 ('Método e evidência', 'Retratação', 'Retirada formal de um artigo publicado por erro grave ou má conduta.', 'fraudes-cientificas.html'),
 ('Filosofia da ciência', 'Teoria de tudo', 'Teoria hipotética que uniria todas as forças e partículas fundamentais numa só descrição.', 'teorias-unificadas.html'),
 ('Filosofia da ciência', 'Unificação', 'Mostrar que fenômenos aparentemente diferentes têm a mesma explicação, como fez Maxwell com eletricidade, magnetismo e luz.', 'teorias-unificadas.html'),
 ('Mente e sociedade', 'Duplo uso', 'Característica de conhecimentos e tecnologias que podem servir tanto ao bem quanto ao mal.', 'ciencia-a-servico-do-mal.html'),
 ('Mente e sociedade', 'Ceticismo responsável', 'Dúvida proporcional à evidência, coerente e aplicada também às próprias crenças.', 'ceticismo-responsavel.html'),
]
