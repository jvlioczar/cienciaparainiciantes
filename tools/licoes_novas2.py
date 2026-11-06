"""Terceira leva de lições (2026-11-06). Mesmo formato de licoes_novas.py: NOVAS2_<NIVEL> e POSICAO2."""
SEP = 'https://plato.stanford.edu/entries/'
WP = 'https://pt.wikipedia.org/wiki/'
WE = 'https://en.wikipedia.org/wiki/'

POSICAO2 = {
 'ciencia-e-tecnologia': 'uma-breve-historia-da-ciencia', 'quem-faz-ciencia': 'ciencia-no-brasil',
 'interpretacoes-da-probabilidade': 'estatistica-para-entender-ciencia', 'experimentos-naturais': 'interpretacoes-da-probabilidade',
 'filosofia-da-biologia': 'reducionismo-e-emergencia', 'ciencia-da-consciencia': 'filosofia-da-biologia',
}

NOVAS2_INICIANTE = [
dict(slug='ciencia-e-tecnologia', grupo='O básico', titulo='Ciência e tecnologia: qual a diferença?', temas=['fundamentos', 'sociedade'],
resumo='Ciência busca entender; tecnologia busca fazer funcionar. As duas se alimentam, mas não são a mesma coisa, e confundi-las gera erros.',
corpo='''
<p class="abre">Celular, vacina, avião: costumamos chamar tudo isso de “ciência”. Mas são produtos da <strong>tecnologia</strong>, que usa conhecimento (científico ou não) para resolver problemas práticos. A ciência pergunta “como o mundo funciona?”; a tecnologia pergunta “como fazer isto funcionar?”.</p>
<h2>Uma relação de mão dupla</h2>
<ul><li><strong>Ciência que vira tecnologia:</strong> a mecânica quântica tornou possíveis o transistor e o laser; a genética, os testes de DNA e as vacinas de RNA mensageiro.</li>
<li><strong>Tecnologia que vira ciência:</strong> a máquina a vapor funcionou antes de existir a termodinâmica, que nasceu em parte para explicá-la. O telescópio e o microscópio abriram áreas inteiras de pesquisa.</li>
<li><strong>Tecnologia sem ciência:</strong> por milênios, pessoas fizeram pão, cerveja, aço e pontes com conhecimento prático, por tentativa e erro, sem teorias científicas.</li></ul>
<h2>Pesquisa básica e aplicada</h2>
<p>A <strong>pesquisa básica</strong> busca entender, sem um uso definido: estudar como bactérias se defendem de vírus parecia curiosidade pura, até virar a ferramenta de edição genética CRISPR. A <strong>pesquisa aplicada</strong> mira um problema específico, como uma vacina. Cortar a pesquisa básica porque “não serve para nada” costuma secar as aplicações do futuro.</p>
<h2>Por que a distinção importa</h2>
<ul><li><strong>Critérios diferentes:</strong> uma teoria científica é boa se é verdadeira ou bem testada; uma tecnologia é boa se funciona, é segura e vale o custo.</li>
<li><strong>Valores:</strong> se devemos usar uma tecnologia (reconhecimento facial, armas, agrotóxicos) é uma questão ética e política, não só científica.</li>
<li><strong>Culpa mal distribuída:</strong> danos de uma tecnologia, como a poluição, não mostram que a ciência por trás dela estava errada; mostram escolhas sobre como usá-la.</li></ul>
<h2>O modelo linear e suas críticas</h2>
<p>Depois da Segunda Guerra, popularizou-se o <strong>modelo linear</strong>: pesquisa básica gera pesquisa aplicada, que gera desenvolvimento, que gera produtos. É uma simplificação. Na prática, a inovação vai e volta: problemas práticos inspiram pesquisa básica (Pasteur estudou fermentação para ajudar a indústria de vinho e cerveja e acabou fundando a microbiologia), e empresas, usuários e governos influenciam o que se pesquisa.</p>
<h2>Tecnociência</h2>
<p>Em muitas áreas atuais, ciência e tecnologia se tornaram inseparáveis. A física de partículas depende de aceleradores gigantes; a genômica, de sequenciadores e computadores; a inteligência artificial é ao mesmo tempo ciência e produto. Alguns estudiosos chamam isso de <strong>tecnociência</strong>. Isso traz novas questões: quem controla os instrumentos controla parte da pesquisa, e interesses comerciais passam a influenciar o que se descobre.</p>
<h2>Riscos e benefícios</h2>
<p>A mesma descoberta pode ter usos opostos: a química que produz fertilizantes também produz explosivos; a biologia que faz vacinas pode fazer armas biológicas. Por isso tecnologias costumam ser reguladas, testadas e debatidas publicamente. Veja a lição sobre <a href="ciencia-a-servico-do-mal.html">ciência a serviço do mal</a> e o debate sobre a <a href="debates/responsabilidade-dos-cientistas.html">responsabilidade dos cientistas</a>.</p>
<div class="nota"><strong>Exemplo:</strong> a física da fissão nuclear é ciência; a bomba e a usina são tecnologias, com usos e riscos muito diferentes. A decisão de construir uma ou outra não está nas equações.</div>''',
fontes=[('Philosophy of Technology (Stanford Encyclopedia)', SEP + 'technology/'), ('Linear model of innovation (Wikipédia)', WE + 'Linear_model_of_innovation'), ('Technoscience (Wikipédia)', WE + 'Technoscience'), ('Pesquisa básica (Wikipédia)', WE + 'Basic_research'), ('CRISPR (Wikipédia)', WP + 'CRISPR')],
quiz=[('Qual a diferença central entre ciência e tecnologia?', ['Nenhuma', 'A ciência busca entender o mundo; a tecnologia busca fazer coisas funcionarem', 'A tecnologia é mais antiga e por isso mais certa', 'A ciência só existe em laboratórios'], 1, 'São atividades ligadas, com objetivos diferentes.'),
 ('O que o caso do CRISPR mostra?', ['Que pesquisa básica é inútil', 'Que pesquisa básica, sem uso definido, pode gerar aplicações enormes', 'Que tecnologia vem sempre antes', 'Que bactérias são perigosas'], 1, 'Estudar a defesa das bactérias levou à edição genética.'),
 ('Alguém diz: “a ciência criou a poluição, então não dá para confiar nela”. O que a lição responde?', ['Concorda', 'Danos de tecnologias refletem escolhas de uso, não erro do conhecimento científico', 'A poluição é inventada', 'A ciência nunca erra'], 1, 'Uso de tecnologia é questão de valores e política.')],
analogia='A ciência é como o mapa e a tecnologia é como a viagem. Um bom mapa ajuda a viajar, e viagens às vezes revelam erros no mapa. Mas para onde ir não está escrito em nenhum dos dois.',
crianca='Ciência é descobrir por que as coisas acontecem, como entender por que o ímã gruda. Tecnologia é usar isso para fazer algo útil, como o ímã que fecha a porta da geladeira.',
obj=['Distinguir ciência de tecnologia.', 'Dar exemplos da relação de mão dupla entre as duas.', 'Explicar a importância da pesquisa básica.'],
caso=('Um político diz que o país deve financiar só pesquisas com aplicação imediata.', 'O que essa política arrisca perder?', 'As aplicações do futuro, que muitas vezes vêm de pesquisa básica sem uso previsto, como o CRISPR e o GPS (que depende da relatividade).'),
erro=('“Tecnologia é só ciência aplicada.”', 'Muitas tecnologias vieram antes da ciência que as explica, e tecnologias também geram ciência.'),
ferr=None, pre=['o-que-e-ciencia'],
guardar=['Ciência entende; tecnologia faz funcionar.', 'Uma alimenta a outra, nos dois sentidos.', 'Usar ou não uma tecnologia é questão de valores, não só de ciência.'],
pensar='Que tecnologia que você usa todo dia depende de uma descoberta que parecia inútil?'),

dict(slug='quem-faz-ciencia', grupo='Ciência no dia a dia', titulo='Quem faz ciência: diversidade e exclusão', temas=['sociedade'],
resumo='Mulheres, pessoas negras e cientistas fora dos centros ricos foram excluídos ou esquecidos. Por que isso importa para a justiça e para a própria qualidade da ciência.',
corpo='''
<p class="abre">A imagem típica do cientista ainda é a de um homem branco e velho de jaleco. Essa imagem não é só um estereótipo: reflete séculos de exclusão de quem podia estudar, publicar e ser reconhecido.</p>
<h2>Os esquecidos</h2>
<ul><li><strong>Rosalind Franklin</strong> produziu a imagem de raios X decisiva para a estrutura do DNA e ficou de fora do Nobel de 1962.</li>
<li><strong>Lise Meitner</strong> explicou a fissão nuclear; o Nobel foi só para seu colega Otto Hahn.</li>
<li><strong>Katherine Johnson</strong> e outras matemáticas negras calcularam trajetórias da NASA, numa época de segregação.</li>
<li><strong>Henrietta Lacks</strong>, mulher negra, teve células tiradas sem consentimento em 1951; as células HeLa foram usadas em pesquisas no mundo todo por décadas, sem benefício para sua família.</li></ul>
<p>Historiadoras da ciência chamam de <strong>efeito Matilda</strong> a tendência de atribuir a homens o trabalho de mulheres.</p>
<h2>Por que diversidade melhora a ciência</h2>
<p>Além da questão de justiça, há uma questão de conhecimento:</p>
<ul class="lista-forte"><li>Ensaios clínicos feitos quase só com homens deixaram passar efeitos adversos em mulheres.</li><li>Oxímetros de pulso tendem a superestimar a oxigenação em pessoas de pele escura, o que só ganhou atenção recentemente.</li><li>Na primatologia, pesquisadoras mudaram a visão sobre o comportamento das fêmeas.</li><li>Equipes com perspectivas diferentes fazem perguntas diferentes e notam vieses que equipes homogêneas não veem (veja a lição sobre valores na ciência).</li></ul>
<h2>No Brasil</h2>
<p>Mulheres já são maioria entre os doutores formados no país, mas continuam minoria nos postos mais altos e em áreas como física e engenharia. Pessoas negras seguem sub-representadas na pós-graduação, apesar do avanço trazido pelas políticas de ação afirmativa nas universidades. A ciência produzida fora dos países ricos também recebe menos citações, mesmo quando tem qualidade parecida.</p>
<div class="nota"><strong>Diversidade não é relativismo:</strong> dizer que perspectivas diferentes melhoram a ciência não quer dizer que cada grupo tem sua verdade. Quer dizer que mais olhos críticos, com experiências diferentes, encontram mais erros.</div>''',
fontes=[('Matilda effect (Wikipédia)', WE + 'Matilda_effect'), ('Henrietta Lacks (Wikipédia)', WP + 'Henrietta_Lacks'), ('Racial Bias in Pulse Oximetry Measurement (NEJM)', 'https://www.nejm.org/doi/full/10.1056/NEJMc2029240'), ('Lise Meitner (Wikipédia)', WP + 'Lise_Meitner')],
quiz=[('O que é o efeito Matilda?', ['Um efeito colateral de remédios', 'A tendência de atribuir a homens o trabalho de mulheres cientistas', 'Um viés estatístico', 'Uma lei da física'], 1, 'O nome homenageia a sufragista Matilda Joslyn Gage.'),
 ('Por que o caso dos oxímetros importa?', ['Mostra que oxímetros são inúteis', 'Mostra como falta de diversidade nos testes pode gerar erros que afetam a saúde de grupos', 'Mostra que a tecnologia é racista por natureza', 'Não importa'], 1, 'Quem não é incluído nos testes pode ser mal atendido depois.'),
 ('Alguém diz que defender diversidade na ciência é dizer que “cada grupo tem sua verdade”. O que a lição responde?', ['Concorda', 'Diversidade amplia a crítica e encontra mais erros; não implica relativismo', 'Diversidade piora a ciência', 'A verdade não existe'], 1, 'Mais perspectivas, mais chances de achar vieses.')],
analogia='Uma equipe homogênea é como olhar uma escultura sempre do mesmo ângulo: algumas falhas nunca aparecem. Gente vendo de lados diferentes enxerga o que estava escondido.',
crianca='Por muito tempo, só alguns tipos de pessoas podiam ser cientistas, e muitas descobertas de mulheres foram esquecidas. Quando gente diferente faz ciência junta, cada um nota coisas que os outros não notariam.',
obj=['Reconhecer casos de exclusão e apagamento na história da ciência.', 'Explicar por que diversidade melhora a qualidade da pesquisa.', 'Descrever a situação no Brasil e separar diversidade de relativismo.'],
caso=('Um remédio foi aprovado depois de testes quase só com homens jovens.', 'Que problema pode aparecer depois?', 'Efeitos diferentes em mulheres e idosos podem ter passado despercebidos, porque não estavam na amostra.'),
erro=('“Ciência é neutra, então quem a faz não importa.”', 'Quem pesquisa influencia as perguntas e o que passa despercebido. A crítica coletiva e diversa é o que torna a ciência mais objetiva.'),
ferr=None, pre=['ciencia-no-brasil'],
guardar=['Mulheres, pessoas negras e cientistas fora dos centros ricos foram excluídos ou esquecidos.', 'Amostras e equipes homogêneas deixam passar erros reais.', 'Diversidade amplia a crítica; não significa que cada grupo tenha sua verdade.'],
pensar='Que cientista de um grupo pouco lembrado você conhece? Se não conhece nenhum, por quê?'),
]

NOVAS2_INTERMEDIARIO = [
dict(slug='interpretacoes-da-probabilidade', grupo='Ciência na prática', titulo='O que é probabilidade?', temas=['estatistica', 'filosofia'],
resumo='Frequência, grau de crença ou propensão? As interpretações da probabilidade e por que estatísticos discutem há um século.',
corpo='''
<p class="abre">Todos usam a palavra “probabilidade”, mas o que ela significa? Quando dizemos que a chance de dar cara é 50%, falamos de moedas, de frequências ou do que acreditamos? A resposta divide estatísticos e filósofos, com consequências práticas.</p>
<h2>As principais interpretações</h2>
<ul><li><strong>Clássica</strong> (Laplace): número de casos favoráveis dividido pelo de casos possíveis, quando todos são igualmente prováveis. Funciona para dados e moedas, mas não diz o que fazer quando os casos não são iguais.</li>
<li><strong>Frequentista</strong> (Venn, von Mises, Reichenbach): a probabilidade é a frequência relativa de um resultado numa longa série de repetições. Objetiva, mas tem dificuldade com eventos únicos: qual a probabilidade de chover amanhã, se amanhã só acontece uma vez?</li>
<li><strong>Subjetiva ou bayesiana</strong> (Ramsey, De Finetti): probabilidade é o grau de crença de alguém, que deve ser coerente e atualizado pela evidência. Aplica-se a eventos únicos, mas é acusada de subjetividade.</li>
<li><strong>Propensão</strong> (Popper): a probabilidade é uma tendência física da situação, como a propensão de um átomo a decair. Útil na física quântica, mas difícil de definir.</li>
<li><strong>Lógica</strong> (Keynes, Carnap): probabilidade é uma relação lógica entre evidência e hipótese.</li></ul>
<h2>Frequentistas e bayesianos na prática</h2>
<div class="tabela"><table><thead><tr><th></th><th>Frequentista</th><th>Bayesiana</th></tr></thead><tbody>
<tr><td>Pergunta típica</td><td>Se não houvesse efeito, quão raros seriam estes dados?</td><td>Dados estes dados, quão provável é a hipótese?</td></tr>
<tr><td>Ferramentas</td><td>p-valores, intervalos de confiança</td><td>a priori, a posteriori, fatores de Bayes</td></tr>
<tr><td>Força</td><td>Não depende de crenças prévias</td><td>Responde diretamente à pergunta que interessa</td></tr>
<tr><td>Crítica</td><td>Fácil de interpretar errado</td><td>Depende da escolha da priori</td></tr>
</tbody></table></div>
<p>Muitos erros de leitura de estudos vêm de confundir as duas: o p-valor responde à pergunta frequentista, mas é lido como se respondesse à bayesiana.</p>
<h2>Hoje</h2>
<p>A maioria dos estatísticos é pragmática e usa as duas abordagens conforme o problema. Métodos bayesianos cresceram com o poder dos computadores e são muito usados em epidemiologia, aprendizado de máquina e ensaios clínicos adaptativos.</p>
<div class="nota"><strong>Sem a matemática:</strong> sempre que vir uma probabilidade, pergunte se ela fala de frequências (quantas vezes acontece) ou de confiança (o quanto devemos acreditar). As duas são úteis; misturá-las causa confusão.</div>''',
fontes=[('Interpretations of Probability (Stanford Encyclopedia)', SEP + 'probability-interpret/'), ('Frequentist inference (Wikipédia)', WE + 'Frequentist_inference'), ('Bayesian inference (Wikipédia)', WE + 'Bayesian_inference')],
quiz=[('Para a interpretação frequentista, probabilidade é:', ['O grau de crença de alguém', 'A frequência relativa de um resultado em muitas repetições', 'Uma relação lógica', 'Um palpite'], 1, 'É a interpretação por trás dos p-valores.'),
 ('Qual a dificuldade da interpretação frequentista?', ['Não usa matemática', 'Lidar com eventos únicos, que não se repetem', 'Depender de priori', 'Ser subjetiva'], 1, 'Amanhã só acontece uma vez.'),
 ('Uma reportagem diz: “p = 0,03, então há 97% de chance de o remédio funcionar”. Qual a confusão?', ['Nenhuma', 'Ler um p-valor (frequentista) como se fosse a probabilidade da hipótese (bayesiana)', 'Usar porcentagem', 'Confundir propensão e lógica'], 1, 'O p-valor não dá a probabilidade de a hipótese ser verdadeira.')],
analogia='Frequentistas e bayesianos são como dois navegadores. Um confia no registro de milhares de viagens anteriores; o outro começa com uma estimativa e a corrige a cada sinal no horizonte. Ambos chegam, mas falam línguas diferentes.',
crianca='Quando você joga uma moeda muitas vezes, mais ou menos metade dá cara: isso é um jeito de pensar a chance. Outro jeito é pensar no quanto você acredita que vai dar cara na próxima jogada.',
obj=['Descrever as interpretações clássica, frequentista, bayesiana, de propensão e lógica.', 'Comparar as abordagens frequentista e bayesiana na estatística.', 'Evitar a confusão entre p-valor e probabilidade da hipótese.'],
caso=('Um meteorologista diz que há 30% de chance de chover amanhã.', 'Que interpretação da probabilidade ele está usando?', 'Pode ser lida como frequência (em dias parecidos, chove em 30%) ou como grau de confiança calibrado; os serviços meteorológicos costumam usar a primeira leitura.'),
erro=('“Probabilidade é um número objetivo e todo mundo concorda sobre o que significa.”', 'Há pelo menos cinco interpretações, e a disputa entre frequentistas e bayesianos é uma das mais antigas da estatística.'),
ferr=None, pre=['estatistica-para-entender-ciencia'],
guardar=['Probabilidade pode ser frequência, grau de crença, propensão ou relação lógica.', 'Frequentistas perguntam pelos dados; bayesianos, pela hipótese.', 'Muitos erros vêm de ler um p-valor como probabilidade da hipótese.'],
pensar='Quando você diz que algo é “provável”, está pensando em frequência ou em confiança?'),

dict(slug='experimentos-naturais', grupo='Ciência na prática', titulo='Experimentos naturais e causalidade sem laboratório', temas=['metodo', 'estatistica'],
resumo='Quando não dá para sortear pessoas, a ciência procura situações em que o acaso fez o sorteio: experimentos naturais, diferença em diferenças e regressão descontínua.',
corpo='''
<p class="abre">Não se pode sortear quem vai receber mais salário mínimo ou quem vai nascer numa cidade com mais imigrantes. Ainda assim, economistas e epidemiologistas descobriram maneiras engenhosas de estimar causas sem experimentos. O Nobel de Economia de 2021 premiou David Card, Joshua Angrist e Guido Imbens por esse trabalho.</p>
<h2>O que é um experimento natural</h2>
<p>É uma situação em que algum fator, por acaso ou por uma regra arbitrária, divide pessoas parecidas em grupos que recebem ou não algo. A natureza ou a burocracia faz o papel do sorteio.</p>
<h2>Exemplos clássicos</h2>
<ul><li><strong>John Snow e a cólera (1854):</strong> em Londres, duas empresas abasteciam casas vizinhas, misturadas nas mesmas ruas; uma captava água poluída do Tâmisa. As casas da empresa poluída tinham muito mais mortes por cólera, o que apoiou a transmissão pela água.</li>
<li><strong>Salário mínimo:</strong> Card e Alan Krueger compararam restaurantes de fast-food em Nova Jersey, que aumentou o salário mínimo, e na Pensilvânia vizinha, que não aumentou. Não encontraram a queda de empregos que a teoria simples previa, o que gerou um longo debate.</li>
<li><strong>Loterias:</strong> sorteios reais de vagas em escolas, de vistos ou de programas sociais criam grupos comparáveis.</li></ul>
<h2>Técnicas</h2>
<ul><li><strong>Diferença em diferenças:</strong> comparar a mudança ao longo do tempo num grupo afetado com a mudança num grupo parecido não afetado.</li>
<li><strong>Regressão descontínua:</strong> quando uma regra usa um ponto de corte (nota mínima, idade, renda), quem está logo acima e logo abaixo é quase igual; diferenças nos resultados podem ser atribuídas à regra.</li>
<li><strong>Variáveis instrumentais:</strong> usar um fator que afeta a exposição mas não o resultado diretamente, como a distância até uma faculdade para estudar o efeito da educação.</li></ul>
<h2>Limites</h2>
<ul class="lista-contra"><li>Os grupos podem não ser tão parecidos quanto parecem.</li><li>O resultado vale para a situação estudada, nem sempre para outras.</li><li>Pressupostos das técnicas precisam ser defendidos, e às vezes são frágeis.</li></ul>
<div class="nota"><strong>Brasil:</strong> estudos usaram a expansão gradual de programas como o Bolsa Família e o Saúde da Família, em municípios diferentes e em anos diferentes, para estimar efeitos sobre a mortalidade infantil.</div>''',
fontes=[('Natural experiment (Wikipédia)', WE + 'Natural_experiment'), ('The Nobel Prize in Economic Sciences 2021', 'https://www.nobelprize.org/prizes/economic-sciences/2021/summary/'), ('John Snow (Wikipédia)', WP + 'John_Snow')],
quiz=[('O que é um experimento natural?', ['Um experimento feito ao ar livre', 'Uma situação em que o acaso ou uma regra arbitrária divide pessoas parecidas em grupos', 'Um experimento com plantas', 'Um ensaio clínico'], 1, 'A natureza ou a burocracia faz o papel do sorteio.'),
 ('O que John Snow comparou?', ['Remédios contra a cólera', 'Casas vizinhas abastecidas por empresas de água diferentes', 'Cidades de países diferentes', 'Ratos e humanos'], 1, 'A mistura de clientes nas mesmas ruas tornava os grupos comparáveis.'),
 ('Uma bolsa é dada a quem tira nota 700 ou mais num exame. Pesquisadores comparam alunos com 699 e 701. Que técnica é essa?', ['Diferença em diferenças', 'Regressão descontínua', 'Metanálise', 'Duplo-cego'], 1, 'Logo acima e logo abaixo do corte, os alunos são quase iguais.')],
analogia='Um experimento natural é como achar um sorteio já feito. Ninguém pode jogar a moeda de novo, mas às vezes a vida jogou por nós, e cabe ao cientista perceber.',
crianca='Imagine duas ruas iguais, mas uma ganhou um parquinho por sorteio. Se as crianças dessa rua passam a brincar mais, dá para desconfiar que foi por causa do parquinho.',
obj=['Definir experimento natural.', 'Descrever diferença em diferenças, regressão descontínua e variáveis instrumentais.', 'Reconhecer os limites dessas técnicas.'],
caso=('Uma cidade adotou uma política de segurança e a cidade vizinha, parecida, não.', 'Como estimar o efeito da política?', 'Com diferença em diferenças: comparar a mudança na criminalidade das duas cidades antes e depois, supondo que elas teriam evoluído de forma parecida sem a política.'),
erro=('“Sem experimento com sorteio, nunca dá para falar em causa.”', 'Experimentos naturais e técnicas como regressão descontínua permitem estimar causas, com pressupostos que precisam ser defendidos.'),
ferr='correlacao-ou-causa', pre=['correlacao-e-causalidade', 'experimentos-e-grupo-controle'],
guardar=['Experimentos naturais aproveitam sorteios que a vida ou a burocracia já fizeram.', 'Diferença em diferenças, regressão descontínua e variáveis instrumentais são as ferramentas.', 'Os resultados dependem de pressupostos que precisam ser defendidos.'],
pensar='Que regra com ponto de corte na sua vida (idade, nota, renda) poderia servir de experimento natural?'),
]

NOVAS2_AVANCADO = [
dict(slug='filosofia-da-biologia', grupo='Teorias e realidade', titulo='Filosofia da biologia', temas=['filosofia'],
resumo='O que é uma espécie? O que é uma função? A seleção natural age sobre genes, indivíduos ou grupos? As perguntas filosóficas que a biologia levanta.',
corpo='''
<p class="abre">Por muito tempo, a filosofia da ciência usou a física como modelo. Mas a biologia levanta perguntas próprias, que não aparecem na física: o que é estar vivo, o que é uma espécie, o que significa dizer que o coração “serve para” bombear sangue.</p>
<h2>O que é uma espécie?</h2>
<p>Parece simples, mas há mais de vinte definições. A mais conhecida, de Ernst Mayr, diz que espécies são grupos que se reproduzem entre si e estão isolados reprodutivamente de outros. Ela não funciona para bactérias, que trocam genes sem reprodução sexual, nem para fósseis. Outras definições usam a genealogia ou a semelhança. Filósofos discutem se espécies são categorias naturais ou ferramentas úteis de classificação.</p>
<h2>Função e propósito</h2>
<p>Dizemos que o coração existe “para” bombear sangue. Mas a biologia moderna rejeita propósitos na natureza. A solução mais aceita é a <strong>teoria etiológica</strong>: a função de um traço é o efeito pelo qual ele foi selecionado no passado. O coração faz barulho e bombeia sangue, mas só o bombeamento explica por que corações foram selecionados.</p>
<h2>Níveis de seleção</h2>
<p>A seleção natural age sobre o quê? Richard Dawkins popularizou a visão do <strong>gene egoísta</strong>: genes são as unidades que se replicam, e organismos são seus veículos. Outros defendem a seleção de indivíduos e, em certos casos, de grupos (seleção multinível). O debate envolve como explicar o altruísmo, como o das abelhas operárias.</p>
<h2>Adaptacionismo</h2>
<p>Stephen Jay Gould e Richard Lewontin criticaram, em 1979, a tendência de explicar todo traço como adaptação, comparando-a ao Dr. Pangloss de Voltaire, para quem tudo existe para o melhor. Muitos traços podem ser subprodutos, restrições do desenvolvimento ou acaso (deriva genética). A crítica tem implicações também para a psicologia evolucionista.</p>
<h2>Reducionismo na biologia</h2>
<p>A biologia molecular mostrou o poder do reducionismo metodológico. Mas a genética clássica não se deduz da molecular de forma simples: um mesmo traço depende de muitos genes, e um gene afeta muitos traços. É um caso clássico da discussão sobre reducionismo e emergência.</p>
<div class="nota"><strong>E os animais?</strong> A biologia evolutiva mostra a continuidade entre humanos e outros animais, inclusive em capacidades mentais. Isso pesa no debate ético sobre quem merece consideração, tema do Ética Para Iniciantes.</div>''',
fontes=[('Philosophy of Biology (Stanford Encyclopedia)', SEP + 'biology-philosophy/'), ('Species (Stanford Encyclopedia)', SEP + 'species/'), ('Units and Levels of Selection (Stanford Encyclopedia)', SEP + 'selection-units/'), ('The Spandrels of San Marco (Wikipédia)', WE + 'The_Spandrels_of_San_Marco_and_the_Panglossian_Paradigm')],
quiz=[('Por que a definição biológica de espécie de Mayr tem limites?', ['Porque é antiga', 'Porque não funciona para organismos sem reprodução sexual, como bactérias, nem para fósseis', 'Porque ignora genes', 'Porque é religiosa'], 1, 'O isolamento reprodutivo não se aplica a todos os seres vivos.'),
 ('O que diz a teoria etiológica da função?', ['Que tudo tem um propósito divino', 'Que a função de um traço é o efeito pelo qual ele foi selecionado no passado', 'Que função é o que o traço faz agora', 'Que não há funções'], 1, 'Explica a função sem propósitos na natureza.'),
 ('Alguém diz que o queixo humano “existe para” algum benefício que precisamos descobrir. Que crítica a lição sugere?', ['Nenhuma', 'A de Gould e Lewontin: nem todo traço é adaptação; pode ser subproduto', 'A do gene egoísta', 'A do reducionismo'], 1, 'O queixo é um exemplo frequentemente citado de possível subproduto.')],
analogia='Explicar a função de um traço biológico é como explicar por que um guarda-chuva tem cabo curvo. Não foi um plano da natureza: os modelos que funcionavam melhor foram os que continuaram sendo fabricados. Na evolução, “fabricados” quer dizer selecionados.',
crianca='Biólogos se perguntam coisas como: o que faz um cachorro e um lobo serem parecidos ou diferentes? Por que temos coração? Os filósofos ajudam a pensar com cuidado o que essas perguntas querem dizer.',
obj=['Discutir o problema da definição de espécie.', 'Explicar a teoria etiológica da função.', 'Apresentar os debates sobre níveis de seleção e adaptacionismo.'],
caso=('Uma reportagem diz que “o cérebro evoluiu para nos fazer felizes”.', 'O que está errado na frase?', 'Atribui propósito à evolução e supõe que a felicidade foi o efeito selecionado. A seleção favorece o que aumenta a sobrevivência e a reprodução, não a felicidade.'),
erro=('“Todo traço de um ser vivo tem uma função adaptativa.”', 'Muitos traços são subprodutos, restrições ou acaso. Afirmar uma adaptação exige evidência, não só uma história plausível.'),
ferr=None, pre=['reducionismo-e-emergencia'],
guardar=['Não há uma definição única de espécie.', 'Função é o efeito pelo qual o traço foi selecionado, sem propósito na natureza.', 'Nem todo traço é adaptação: Gould e Lewontin contra o adaptacionismo.'],
pensar='Que traço humano você supunha ter uma função e talvez seja só subproduto?'),

dict(slug='ciencia-da-consciencia', grupo='Teorias e realidade', titulo='A ciência da consciência', temas=['filosofia', 'mente'],
resumo='O problema difícil, as teorias científicas da consciência e o que a ciência diz sobre a consciência dos outros animais.',
corpo='''
<p class="abre">Sabemos muito sobre como o cérebro processa informação. Mas por que esse processamento é acompanhado de experiência, de “como é” ver vermelho ou sentir dor? Esse é o <strong>problema difícil da consciência</strong>, nome dado pelo filósofo David Chalmers em 1995.</p>
<h2>Problemas fáceis e o problema difícil</h2>
<p>Os “problemas fáceis” (que não são nada fáceis) são explicar funções: como o cérebro discrimina estímulos, integra informação, controla a atenção e relata estados. O problema difícil é explicar por que tudo isso é <em>sentido</em>. Uma explicação completa do mecanismo parece deixar de fora a experiência. Há quem ache que o problema difícil é real e há quem ache que ele se dissolverá quando os fáceis forem resolvidos (Daniel Dennett).</p>
<h2>Teorias científicas da consciência</h2>
<ul><li><strong>Espaço de trabalho global</strong> (Bernard Baars, Stanislas Dehaene): consciência é a informação que se torna amplamente disponível para muitos sistemas do cérebro.</li>
<li><strong>Informação integrada</strong> (Giulio Tononi): consciência corresponde ao grau de integração de informação de um sistema. Controversa: em 2023, um grupo de pesquisadores a chamou de pseudociência numa carta aberta, o que gerou forte reação de outros cientistas.</li>
<li><strong>Teorias de ordem superior:</strong> um estado é consciente quando há uma representação dele.</li>
<li><strong>Processamento preditivo:</strong> o cérebro como máquina de previsões; a experiência seria o modelo que ele faz do mundo e do corpo.</li></ul>
<p>Em 2023, um experimento de “colaboração adversária” colocou duas teorias rivais para fazer previsões opostas antes dos dados. Nenhuma saiu vitoriosa por completo: um bom exemplo de ciência tentando evitar o viés de confirmação.</p>
<h2>A consciência dos outros animais</h2>
<p>Não temos acesso direto à experiência de ninguém além de nós mesmos; inferimos a dos outros por comportamento, anatomia e evolução. Pelas mesmas razões, a ciência atribui consciência a muitos animais. A <strong>Declaração de Cambridge</strong> (2012) afirmou que mamíferos, aves e outros animais, como os polvos, têm os substratos neurológicos da consciência. A <strong>Declaração de Nova York sobre a Consciência Animal</strong> (2024) disse que há forte apoio científico para a experiência consciente em mamíferos e aves, e pelo menos uma possibilidade realista em todos os vertebrados e em muitos invertebrados, como insetos, crustáceos e moluscos cefalópodes.</p>
<h2>E as máquinas?</h2>
<p>Com modelos de linguagem que conversam de forma fluente, a pergunta sobre consciência artificial deixou de ser só ficção. As teorias acima dão respostas diferentes, e não há consenso. Falar como se tivesse experiências não prova que um sistema as tenha, assim como não falar não prova que um animal não as tenha.</p>
<div class="nota"><strong>Por que importa:</strong> a senciência, a capacidade de ter experiências boas e ruins, é o que faz um ser poder ser prejudicado. Por isso a ciência da consciência é decisiva para a ética, tema do <a href="https://eticaparainiciantes.biblioverse.org/" target="_blank" rel="noopener">Ética Para Iniciantes</a>.</div>''',
fontes=[('Consciousness (Stanford Encyclopedia)', SEP + 'consciousness/'), ('Hard problem of consciousness (Wikipédia)', WE + 'Hard_problem_of_consciousness'), ('The New York Declaration on Animal Consciousness', 'https://sites.google.com/nyu.edu/nydeclaration/declaration'), ('The Cambridge Declaration on Consciousness', 'https://fcmconference.org/img/CambridgeDeclarationOnConsciousness.pdf')],
quiz=[('O que é o problema difícil da consciência?', ['Medir a atividade cerebral', 'Explicar por que o processamento do cérebro é acompanhado de experiência sentida', 'Saber quantos neurônios temos', 'Tratar doenças mentais'], 1, 'É o nome dado por Chalmers à pergunta sobre a experiência.'),
 ('O que disse a Declaração de Nova York (2024)?', ['Que só humanos são conscientes', 'Que há forte apoio para a consciência em mamíferos e aves e possibilidade realista em todos os vertebrados e muitos invertebrados', 'Que máquinas são conscientes', 'Que a consciência não existe'], 1, 'Ampliou o reconhecimento científico da consciência animal.'),
 ('Um chatbot diz “eu sinto tristeza”. O que a lição sugere?', ['Que ele certamente sente', 'Que dizer não prova sentir, e as teorias divergem sobre máquinas', 'Que ele certamente não sente', 'Que a pergunta não faz sentido'], 1, 'Relato verbal não basta, para máquinas ou para qualquer ser.')],
analogia='Explicar o cérebro sem explicar a experiência é como descrever cada pixel e cada circuito de uma TV sem dizer por que alguém está assistindo a um filme. O problema difícil pergunta pelo espectador.',
crianca='Quando você sente o gosto de chocolate, tem uma sensação lá dentro. Os cientistas sabem muito sobre o cérebro, mas ainda tentam entender como essas sensações acontecem, e quais animais também as têm.',
obj=['Explicar a diferença entre os problemas fáceis e o problema difícil.', 'Descrever as principais teorias científicas da consciência.', 'Resumir o que a ciência diz sobre a consciência animal e artificial.'],
caso=('Alguém diz que peixes e camarões não sentem dor porque “não têm cérebro como o nosso”.', 'O que a ciência atual diz?', 'A Declaração de Nova York (2024) considera realista a possibilidade de consciência em todos os vertebrados, inclusive peixes, e em crustáceos. Estruturas diferentes podem realizar funções parecidas.'),
erro=('“Se não podemos provar que um animal é consciente, devemos supor que não é.”', 'Também não podemos provar a consciência de outros humanos; inferimos por comportamento, anatomia e evolução. As mesmas razões se aplicam a muitos animais.'),
ferr=None, pre=['reducionismo-e-emergencia', 'cientificismo-e-limites-da-ciencia'],
guardar=['O problema difícil pergunta por que há experiência, não só processamento.', 'Espaço global, informação integrada, ordem superior e processamento preditivo competem.', 'A ciência reconhece consciência em mamíferos e aves e a considera realista em muitos outros animais.'],
pensar='Que evidência te convenceria de que um animal, ou uma máquina, sente algo?'),
]
