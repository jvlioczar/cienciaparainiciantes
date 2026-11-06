"""Lições do nível Avançado (mesmo formato do Iniciante)."""
SEP = 'https://plato.stanford.edu/entries/'
IEP = 'https://iep.utm.edu/'
WP = 'https://pt.wikipedia.org/wiki/'
WE = 'https://en.wikipedia.org/wiki/'

AVANCADO = [
dict(slug='realismo-e-antirrealismo', grupo='Teorias e realidade', titulo='Realismo e antirrealismo científico', temas=['filosofia'],
resumo='Elétrons existem ou são só ferramentas de cálculo? O argumento do milagre, a metaindução pessimista e as posições intermediárias.',
corpo='''
<p class="abre">Ninguém nunca viu um elétron. Ainda assim, a física fala deles como coisas reais, com carga e massa. As teorias científicas descrevem o mundo como ele é, inclusive a parte invisível, ou são só instrumentos úteis para prever o que vemos? Esse é o debate entre <strong>realismo</strong> e <strong>antirrealismo</strong> científico.</p>
<h2>Realismo científico</h2>
<p>O realista diz que nossas melhores teorias maduras são aproximadamente verdadeiras, e que as entidades que elas postulam (elétrons, genes, campos) existem de fato. O principal argumento é o <strong>argumento do “nenhum milagre”</strong>, de Hilary Putnam: se as teorias não fossem aproximadamente verdadeiras, o sucesso delas em prever e manipular o mundo seria um milagre. Nós construímos computadores usando a teoria dos elétrons; seria uma coincidência inexplicável se elétrons não existissem.</p>
<h2>A metaindução pessimista</h2>
<p>Larry Laudan respondeu com a história: muitas teorias bem-sucedidas foram abandonadas e hoje são consideradas falsas, como o éter luminífero, o calórico (fluido do calor) e o flogisto. Elas também previam bem. Se o sucesso passado não garantiu a verdade delas, por que garantiria a das atuais? Por indução sobre a história, nossas teorias atuais provavelmente também serão abandonadas.</p>
<h2>Posições antirrealistas</h2>
<ul><li><strong>Instrumentalismo:</strong> teorias são ferramentas de previsão; perguntar se são verdadeiras é como perguntar se um martelo é verdadeiro.</li>
<li><strong>Empirismo construtivo</strong> (Bas van Fraassen): a ciência busca teorias <em>empiricamente adequadas</em>, que acertam sobre o observável. Aceitar uma teoria não exige acreditar no que ela diz sobre o inobservável.</li>
<li><strong>Convencionalismo</strong> (Henri Poincaré): algumas partes das teorias, como a escolha da geometria, são convenções, escolhidas por simplicidade.</li></ul>
<h2>Posições intermediárias</h2>
<ul><li><strong>Realismo estrutural</strong> (John Worrall): o que sobrevive às revoluções é a estrutura matemática. As equações de Fresnel para a luz sobreviveram à queda do éter. Devemos ser realistas sobre a estrutura, não sobre a natureza das entidades.</li>
<li><strong>Realismo de entidades</strong> (Ian Hacking, Nancy Cartwright): acreditamos nas entidades que conseguimos manipular para produzir efeitos. A frase de Hacking: “se você consegue borrifá-los, eles são reais”, sobre os pósitrons usados em experimentos.</li>
<li><strong>Realismo seletivo:</strong> ser realista apenas sobre as partes das teorias que realmente fizeram o trabalho de prever.</li></ul>
<div class="nota"><strong>Por que importa:</strong> o debate não muda como se faz um experimento, mas muda como interpretamos o que a ciência diz. Também aparece na física quântica, em que interpretações diferentes da mesma matemática divergem sobre o que é real.</div>''',
fontes=[('Scientific Realism (Stanford Encyclopedia of Philosophy)', SEP + 'scientific-realism/'), ('Constructive Empiricism (Stanford Encyclopedia of Philosophy)', SEP + 'constructive-empiricism/'), ('Structural Realism (Stanford Encyclopedia of Philosophy)', SEP + 'structural-realism/'), ('A Confutation of Convergent Realism', 'https://www.jstor.org/stable/187066')],
quiz=[('O que diz o argumento do “nenhum milagre”?', ['Que milagres não existem', 'Que o sucesso das teorias seria um milagre se elas não fossem aproximadamente verdadeiras', 'Que a ciência é um milagre', 'Que teorias falsas são inúteis'], 1, 'É o principal argumento a favor do realismo científico.'),
 ('O que é a metaindução pessimista?', ['Uma previsão de crise econômica', 'O argumento de que teorias bem-sucedidas do passado foram abandonadas, então as atuais provavelmente também serão', 'Uma forma de dedução', 'A defesa do realismo'], 1, 'A história da ciência é usada contra a inferência do sucesso à verdade.'),
 ('Uma física diz: “não sei se o elétron é uma partícula ou um campo, mas as equações que o descrevem continuam valendo há um século”. Que posição isso lembra?', ['Instrumentalismo puro', 'Realismo estrutural', 'Relativismo', 'Fundacionalismo'], 1, 'Confiar na estrutura matemática, não na natureza das entidades, é o realismo estrutural.')],
analogia='Teorias científicas são como mapas de um território que só vemos em parte. O realista acha que o mapa retrata até as áreas cobertas de neblina. O antirrealista acha que só podemos confiar no mapa onde já andamos; o resto pode ser invenção útil.',
crianca='Ninguém consegue ver um átomo com os olhos. Alguns filósofos acham que os átomos existem de verdade, porque a ciência funciona muito bem quando fala deles. Outros acham que são só um jeito útil de fazer as contas.',
obj=['Distinguir realismo de antirrealismo científico.', 'Reconstruir o argumento do milagre e a metaindução pessimista.', 'Descrever posições intermediárias: realismo estrutural e de entidades.'],
caso=('No século XIX, a teoria do éter previa muito bem o comportamento da luz. Depois, o éter foi abandonado.', 'Isso derruba o realismo científico?', 'Pressiona, pela metaindução pessimista. Mas o realista estrutural responde que as equações da luz sobreviveram; só a interpretação sobre o éter caiu.'),
erro=('“Antirrealistas acham que a ciência não funciona.”', 'Antirrealistas aceitam o sucesso da ciência. A discordância é sobre se esse sucesso autoriza a crer no inobservável.'),
ferr='que-corrente-e-essa', pre=['kuhn-e-os-paradigmas'],
guardar=['Realismo: as melhores teorias são aproximadamente verdadeiras, inclusive sobre o invisível.', 'Argumento do milagre contra metaindução pessimista.', 'Meios-termos: realismo estrutural (as equações) e de entidades (o que manipulamos).'],
pensar='Há algo em que você acredita sem poder ver, só por causa do que essa coisa permite fazer? Isso é diferente do caso do elétron?'),

dict(slug='subdeterminacao-e-duhem-quine', grupo='Teorias e realidade', titulo='Subdeterminação e a tese Duhem-Quine', temas=['filosofia', 'metodo'],
resumo='Nenhuma hipótese é testada sozinha, e os mesmos dados podem caber em teorias diferentes. O que isso significa para a refutação e a escolha de teorias.',
corpo='''
<p class="abre">Quando um experimento contradiz uma previsão, o que exatamente foi refutado? O físico Pierre Duhem notou, em 1906, que uma previsão nunca vem de uma hipótese sozinha. Ela depende também da teoria dos instrumentos, de hipóteses auxiliares e das condições do experimento. Se a previsão falha, a culpa pode estar em qualquer uma dessas peças.</p>
<h2>A tese Duhem-Quine</h2>
<p>W. V. O. Quine radicalizou a ideia em “Dois dogmas do empirismo” (1951): nossas crenças enfrentam o tribunal da experiência <strong>em conjunto</strong>, como uma teia. Diante de uma experiência contrária, podemos ajustar qualquer parte da teia; em princípio, até leis da lógica. Escolhemos ajustar a periferia (hipóteses específicas) e proteger o centro (lógica, matemática, leis bem estabelecidas) por razões de conservadorismo e simplicidade.</p>
<h2>Exemplos</h2>
<ul><li><strong>Netuno e Vulcano:</strong> as anomalias na órbita de Urano foram atribuídas a um planeta desconhecido, e Netuno foi achado (1846). As anomalias na órbita de Mercúrio foram atribuídas a um planeta chamado Vulcano, que nunca apareceu; a solução veio da relatividade geral, que mudou o núcleo da teoria. Mesma estratégia, resultados opostos.</li>
<li><strong>Neutrinos mais rápidos que a luz (2011):</strong> o experimento OPERA mediu neutrinos aparentemente mais rápidos que a luz. Em vez de abandonar a relatividade, os físicos procuraram um erro nos instrumentos, e acharam: um cabo de fibra óptica mal conectado.</li></ul>
<h2>Subdeterminação das teorias pela evidência</h2>
<p>Uma tese relacionada diz que, para qualquer conjunto de dados, existem várias teorias incompatíveis que os explicam igualmente bem. Há duas versões:</p>
<ul><li><strong>Fraca (transitória):</strong> com a evidência disponível <em>hoje</em>, às vezes mais de uma teoria se encaixa. É comum e se resolve com mais dados.</li>
<li><strong>Forte (permanente):</strong> mesmo com <em>toda</em> evidência possível, teorias rivais empiricamente equivalentes continuariam empatadas. É bem mais controversa: filósofos como Laudan e Leplin argumentam que casos genuínos são raros ou artificiais.</li></ul>
<h2>Consequências</h2>
<ul><li>Refutações não são automáticas: exigem julgamento sobre qual peça culpar. Isso enfraquece o falsificacionismo ingênuo.</li><li>A escolha entre teorias usa critérios além dos dados, como simplicidade, alcance e fecundidade (os valores de Kuhn).</li><li>Alguns sociólogos usaram a subdeterminação para dizer que fatores sociais decidem a escolha. Críticos respondem que critérios epistêmicos bastam na maioria dos casos.</li></ul>
<div class="nota"><strong>Lição prática:</strong> quando um estudo contradiz uma teoria bem estabelecida, a primeira suspeita costuma ser o estudo, não a teoria. Isso não é dogmatismo: é a distribuição racional da culpa entre as peças da teia, como no caso dos neutrinos.</div>''',
fontes=[('Underdetermination of Scientific Theory (Stanford Encyclopedia of Philosophy)', SEP + 'scientific-underdetermination/'), ('Two Dogmas of Empiricism', 'https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf'), ('Faster-than-light neutrino anomaly (Wikipédia)', WE + 'Faster-than-light_neutrino_anomaly')],
quiz=[('O que diz a tese Duhem-Quine?', ['Que toda hipótese é verdadeira', 'Que hipóteses são testadas em conjunto com outras, então uma falha não aponta sozinha qual está errada', 'Que a lógica é imutável', 'Que só há uma teoria possível'], 1, 'O teste envolve um conjunto: hipótese, auxiliares, instrumentos.'),
 ('Qual a diferença entre a subdeterminação fraca e a forte?', ['Nenhuma', 'A fraca é temporária, com a evidência atual; a forte diria que nenhuma evidência possível desempataria', 'A forte é mais aceita', 'A fraca é sobre lógica'], 1, 'A versão fraca é comum; a forte é controversa.'),
 ('Um experimento indica que a energia não se conserva. A maioria dos físicos procura primeiro um erro no equipamento. Isso é:', ['Dogmatismo puro', 'Distribuição racional da culpa: a lei tem enorme apoio, e o experimento é a peça mais provável de falhar', 'Prova de que a lei é falsa', 'Pseudociência'], 1, 'Como no caso dos neutrinos, suspeitar primeiro do elo mais fraco é razoável.')],
analogia='Quando um carro não liga, o defeito pode estar na bateria, no motor de arranque, no combustível ou na chave. O teste “girei a chave e nada” não diz qual peça falhou. Testes científicos também envolvem várias peças, e é preciso julgamento para achar a culpada.',
crianca='Se o seu bolo não cresceu, pode ter sido o fermento, o forno ou a receita. Só olhando o bolo, você não sabe qual foi o problema. Os cientistas também precisam descobrir qual parte da ideia deu errado.',
obj=['Explicar a tese Duhem-Quine e o holismo da confirmação.', 'Distinguir subdeterminação fraca e forte.', 'Avaliar as consequências para o falsificacionismo e a escolha de teorias.'],
caso=('Um estudo pequeno diz que um alimento comum causa câncer, contrariando dezenas de estudos maiores.', 'Onde é mais racional procurar o erro?', 'Na peça mais frágil: o estudo novo (amostra, desenho, análise). A teia de evidências anteriores tem muito mais apoio.'),
erro=('“Se os dados cabem em várias teorias, qualquer teoria vale.”', 'A subdeterminação forte é rara, e mesmo na fraca critérios como simplicidade, alcance e previsões novas desempatam a maioria dos casos.'),
ferr=None, pre=['popper-e-a-falseabilidade'],
guardar=['Hipóteses enfrentam a experiência em conjunto; a culpa por uma falha precisa ser atribuída.', 'Subdeterminação fraca é comum e passageira; a forte é controversa.', 'Desconfiar primeiro do elo mais fraco é razoável, não dogmático.'],
pensar='Quando algo dá errado no seu dia a dia, como você decide qual parte do plano culpar?'),

dict(slug='carga-teorica-da-observacao', grupo='Teorias e realidade', titulo='A carga teórica da observação', temas=['filosofia', 'mente'],
resumo='Observar não é só abrir os olhos: o que vemos depende do que sabemos. Hanson, Kuhn e o problema de usar observações para testar teorias.',
corpo='''
<p class="abre">Um médico experiente olha um raio-X e vê uma pneumonia. Um leigo vê manchas cinzentas. Os dois receberam a mesma luz nos olhos. O filósofo Norwood Russell Hanson chamou isso de <strong>carga teórica da observação</strong>: o que vemos depende do que sabemos, esperamos e dos conceitos que temos.</p>
<h2>A ideia</h2>
<p>O empirismo clássico imaginava a observação como um registro neutro, que serviria de juiz imparcial entre teorias. Hanson (<em>Patterns of Discovery</em>, 1958) e depois Kuhn argumentaram que observar é interpretar. Tycho Brahe e Kepler, olhando o nascer do Sol, “viam” coisas diferentes: um o Sol se movendo, o outro a Terra girando.</p>
<p>Há graus diferentes nessa tese:</p>
<ul><li><strong>Percepção:</strong> a psicologia mostra que expectativas influenciam o que percebemos (como nas figuras ambíguas).</li>
<li><strong>Linguagem:</strong> relatar uma observação usa conceitos (“o termômetro marca 30 °C” supõe uma teoria sobre temperatura).</li>
<li><strong>Instrumentos:</strong> microscópios, telescópios e detectores dependem de teorias sobre como funcionam.</li></ul>
<h2>Por que é um problema</h2>
<p>Se as observações dependem das teorias, como podem testar as teorias de forma imparcial? Um teste não seria circular? Kuhn sugeriu que defensores de paradigmas diferentes, em parte, vivem em “mundos diferentes”.</p>
<h2>Respostas</h2>
<ul><li><strong>Independência relativa:</strong> a teoria que carrega a observação geralmente não é a que está sendo testada. A teoria óptica do telescópio é independente da teoria astronômica que o telescópio testa.</li>
<li><strong>Robustez:</strong> quando métodos diferentes, com teorias de fundo diferentes, chegam ao mesmo resultado, é improvável que todos estejam enviesados da mesma forma. Jean Perrin mediu o número de Avogadro de mais de dez maneiras independentes, e os resultados convergiram; isso convenceu céticos da existência de átomos.</li>
<li><strong>Experimentos têm vida própria</strong> (Ian Hacking): muitas observações são estabilizadas por práticas de laboratório antes de qualquer teoria sofisticada.</li>
<li><strong>Percepção resistente:</strong> Jerry Fodor lembrou que ilusões de óptica continuam enganando mesmo quando sabemos que são ilusões; parte da percepção é encapsulada, imune às crenças.</li></ul>
<div class="nota"><strong>Para o dia a dia:</strong> pessoas de lados políticos opostos assistem ao mesmo vídeo e “veem” agressões diferentes. Saber disso não torna tudo relativo, mas pede cuidado: procurar observações independentes e registros que não dependam de interpretação.</div>''',
fontes=[('Theory and Observation in Science (Stanford Encyclopedia of Philosophy)', SEP + 'science-theory-observation/'), ('Patterns of Discovery', 'https://www.google.com/search?tbm=bks&q=Patterns+of+Discovery+Hanson'), ('Jean Perrin e o número de Avogadro (Wikipédia)', WE + 'Jean_Baptiste_Perrin')],
quiz=[('O que é a carga teórica da observação?', ['A observação é pesada', 'O que observamos depende de conhecimentos, expectativas e conceitos prévios', 'Só teorias observam', 'Observações são sempre falsas'], 1, 'Observar é também interpretar.'),
 ('Como a robustez responde ao problema?', ['Ignorando a observação', 'Métodos independentes, com teorias de fundo diferentes, que convergem tornam improvável um viés comum', 'Usando um só instrumento muito bom', 'Votando'], 1, 'O caso de Perrin e os átomos é o exemplo clássico.'),
 ('Dois torcedores rivais veem o mesmo lance e discordam se foi pênalti. O que ajudaria, segundo a lição?', ['Concluir que tudo é relativo', 'Buscar registros e ângulos independentes, menos dependentes de interpretação', 'Dar razão a quem gritar mais', 'Desistir de saber'], 1, 'A carga teórica pede métodos independentes, não relativismo.')],
analogia='Observar é como ouvir uma língua. Quem não fala o idioma ouve só sons; quem fala ouve frases. O som é o mesmo, mas o que se “ouve” depende do que se sabe. Ainda assim, dois falantes nativos raramente discordam sobre o que foi dito.',
crianca='Um médico olha um raio-X e vê um osso quebrado. Você olha e vê só uma mancha. O que a gente vê depende do que a gente sabe.',
obj=['Explicar a tese da carga teórica da observação e seus graus.', 'Descrever por que ela ameaça a ideia de observação como juiz neutro.', 'Apresentar respostas: independência relativa, robustez e prática experimental.'],
caso=('Um astrônomo usa um telescópio para testar uma teoria sobre galáxias. Um crítico diz: “o telescópio depende de teoria, então o teste é circular”.', 'O teste é circular?', 'Não necessariamente: a teoria óptica do telescópio é independente da teoria sobre galáxias. A circularidade só aparece quando a teoria testada é a mesma que carrega a observação.'),
erro=('“Se toda observação depende de teoria, então não há fatos.”', 'A carga teórica mostra que a observação não é neutra, não que é arbitrária. Métodos independentes que convergem estabelecem fatos com segurança.'),
ferr=None, pre=['kuhn-e-os-paradigmas'],
guardar=['Observar é interpretar: percepção, linguagem e instrumentos carregam teoria.', 'Isso ameaça o ideal de um juiz neutro, mas não torna tudo relativo.', 'Independência relativa e robustez (métodos que convergem) restauram a força dos testes.'],
pensar='Em que situação você e alguém “viram” a mesma coisa de jeitos diferentes? Que registro independente teria resolvido?'),

dict(slug='explicacao-cientifica', grupo='Teorias e realidade', titulo='O que é uma explicação científica?', temas=['filosofia'],
resumo='Do modelo dedutivo-nomológico de Hempel às explicações causais, mecanicistas e por unificação: o que torna uma resposta a um “por quê” científica.',
corpo='''
<p class="abre">A ciência não quer só prever; quer explicar. Mas o que é explicar? A pergunta parece simples e gerou um dos debates mais longos da filosofia da ciência.</p>
<h2>O modelo de Hempel</h2>
<p>Em 1948, Carl Hempel e Paul Oppenheim propuseram o <strong>modelo dedutivo-nomológico</strong> (DN, de <em>nomos</em>, lei): explicar um fenômeno é deduzi-lo de leis gerais mais condições iniciais. Por que o metal dilatou? Porque metais se dilatam quando aquecidos (lei), e este metal foi aquecido (condição). Para fenômenos estatísticos, Hempel propôs um modelo indutivo-estatístico.</p>
<p>Uma consequência do modelo é a <strong>simetria</strong> entre explicação e previsão: uma explicação correta é uma previsão que poderia ter sido feita antes.</p>
<h2>Os contraexemplos</h2>
<ul><li><strong>O mastro e a sombra:</strong> da altura do mastro, da posição do Sol e das leis da óptica deduz-se o comprimento da sombra. Mas também se deduz a altura do mastro a partir da sombra. Só a primeira dedução explica; a sombra não explica o mastro. O modelo DN não vê a diferença: falta a <strong>direção causal</strong>.</li>
<li><strong>O barômetro:</strong> a queda do barômetro permite prever a tempestade, mas não a explica; os dois têm uma causa comum.</li>
<li><strong>A pílula do homem:</strong> “João não engravidou porque tomou anticoncepcional” é deduzível, mas a explicação é irrelevante: homens não engravidam.</li></ul>
<h2>Alternativas</h2>
<ul><li><strong>Explicação causal</strong> (Wesley Salmon, James Woodward): explicar é mostrar as causas. Para Woodward, A explica B quando intervir em A mudaria B; essa ideia de intervenção é hoje muito usada em estatística e IA.</li>
<li><strong>Explicação mecanicista:</strong> na biologia e na neurociência, explicar é mostrar o mecanismo, as partes e atividades que produzem o fenômeno, como a cadeia de reações da fotossíntese.</li>
<li><strong>Explicação por unificação</strong> (Michael Friedman, Philip Kitcher): explicar é reduzir o número de fatos independentes. Newton explicou as marés, as órbitas e a queda dos corpos com uma só lei.</li>
<li><strong>Pragmática</strong> (Bas van Fraassen): uma explicação é a resposta a uma pergunta “por quê” num contexto; o que conta como boa resposta depende do contraste pretendido (“por que Adão comeu a maçã e não a pera?” e “por que Adão e não Eva?”).</li></ul>
<h2>Explicar e prever não são a mesma coisa</h2>
<p>A teoria da evolução explica muito e prevê pouco em detalhe (não diz que espécie surgirá amanhã). Modelos de aprendizado de máquina podem prever muito bem sem explicar nada que entendamos. A separação entre as duas virtudes é um dos temas mais atuais da filosofia da ciência.</p>
<div class="nota"><strong>Inferência à melhor explicação:</strong> muitos filósofos acham que a ciência raciocina escolhendo a hipótese que melhor explicaria os dados (abdução). O detetive que conclui quem é o culpado faz isso. Mas o que é “melhor”? Mais simples? Mais abrangente? Mais provável? A resposta liga este tema ao bayesianismo.</div>''',
fontes=[('Scientific Explanation (Stanford Encyclopedia of Philosophy)', SEP + 'scientific-explanation/'), ('Studies in the Logic of Explanation', 'https://www.jstor.org/stable/185169'), ('Abduction (Stanford Encyclopedia of Philosophy)', SEP + 'abduction/')],
quiz=[('O que propõe o modelo dedutivo-nomológico?', ['Explicar é contar uma história', 'Explicar é deduzir o fenômeno de leis gerais mais condições iniciais', 'Explicar é mostrar sentimentos', 'Explicar é prever ao acaso'], 1, 'É o modelo de Hempel e Oppenheim.'),
 ('O que o exemplo do mastro e da sombra mostra?', ['Que sombras não existem', 'Que o modelo DN não captura a direção causal da explicação', 'Que a óptica está errada', 'Que mastros explicam o Sol'], 1, 'Deduzimos nos dois sentidos, mas só um explica.'),
 ('Um modelo de IA prevê com 95% de acerto quais pacientes vão piorar, mas ninguém sabe por quê. Que distinção isso ilustra?', ['Entre previsão e explicação', 'Entre indução e dedução', 'Entre fato e valor', 'Entre realismo e relativismo'], 0, 'Prever bem não é o mesmo que explicar.')],
analogia='Explicar é como mostrar o caminho, não só o destino. Um GPS que diz “você chegará às 15h” prevê; um mapa que mostra as ruas, o trânsito e por que o caminho demora explica.',
crianca='Saber que vai chover quando o céu fica escuro é prever. Saber que a chuva vem das nuvens cheias de gotinhas de água é explicar.',
obj=['Apresentar o modelo dedutivo-nomológico e seus contraexemplos.', 'Comparar explicações causais, mecanicistas, por unificação e pragmáticas.', 'Distinguir prever de explicar e definir inferência à melhor explicação.'],
caso=('Alguém diz que o galo canta e por isso o Sol nasce, já que sempre que o galo canta o Sol nasce logo depois.', 'Por que isso não é explicação?', 'Falta a direção causal e o mecanismo: o galo canta por causa da luz que antecede o Sol. Regularidade e previsão não bastam para explicar.'),
erro=('“Se prevê bem, explica.”', 'Barômetros preveem tempestades sem explicá-las, e modelos de IA preveem sem que entendamos o mecanismo. Explicação exige causas, mecanismos ou unificação.'),
ferr=None, pre=['hipotese-teoria-e-lei', 'correlacao-e-causalidade'],
guardar=['Hempel: explicar é deduzir de leis; falha em capturar a direção causal.', 'Alternativas: causas e intervenções, mecanismos, unificação, contexto da pergunta.', 'Prever e explicar são virtudes diferentes, e a IA torna essa diferença urgente.'],
pensar='Que coisa você sabe prever mas não sabe explicar?'),

dict(slug='bayesianismo', grupo='Teorias e realidade', titulo='Bayesianismo: atualizar crenças com evidências', temas=['epistemologia', 'estatistica'],
resumo='Graus de crença, probabilidade a priori e a regra de Bayes: como a evidência deve mudar o que pensamos, e por que um exame com 99% de acerto pode enganar.',
corpo='''
<p class="abre">E se, em vez de perguntar se uma teoria é verdadeira ou falsa, perguntássemos <strong>quanto</strong> devemos acreditar nela, e como essa confiança deve mudar com cada nova evidência? Essa é a ideia do <strong>bayesianismo</strong>, hoje uma das abordagens mais influentes da epistemologia e da estatística.</p>
<h2>Graus de crença</h2>
<p>Para o bayesiano, crenças vêm em graus, que podem ser representados como probabilidades entre 0 (certeza de que é falso) e 1 (certeza de que é verdadeiro). Um meteorologista que diz “70% de chance de chuva” expressa um grau de crença. A racionalidade exige que esses graus obedeçam às regras da probabilidade; caso contrário, argumentam os bayesianos, a pessoa aceitaria apostas que perde de qualquer jeito (o argumento do “livro holandês”).</p>
<h2>A regra de Bayes</h2>
<p>O teorema do reverendo Thomas Bayes (século XVIII) diz como atualizar a crença numa hipótese H depois de ver uma evidência E:</p>
<p style="text-align:center;font-size:1.1rem"><strong>P(H|E) = P(E|H) × P(H) / P(E)</strong></p>
<ul><li><strong>P(H)</strong>, a <em>priori</em>: quanto você acreditava em H antes.</li><li><strong>P(E|H)</strong>, a verossimilhança: quão esperada seria a evidência se H fosse verdade.</li><li><strong>P(E)</strong>: quão esperada é a evidência em geral.</li><li><strong>P(H|E)</strong>, a <em>posteriori</em>: quanto você deve acreditar em H depois.</li></ul>
<h2>O exemplo do exame</h2>
<p>Uma doença atinge 1 em cada 1.000 pessoas. Um exame detecta 99% dos doentes e dá falso positivo em 5% dos saudáveis. Seu exame deu positivo. Qual a chance de você ter a doença? A maioria, inclusive muitos médicos em estudos, responde perto de 95%. A resposta certa é <strong>cerca de 2%</strong>. Em 1.000 pessoas, 1 doente dá positivo, mas cerca de 50 saudáveis também. Dos 51 positivos, só 1 está doente. A <em>priori</em> baixa (a raridade da doença) pesa muito.</p>
<h2>O bayesianismo e a ciência</h2>
<ul><li><strong>Explica a confirmação:</strong> uma evidência confirma H quando é mais provável se H for verdadeira do que se for falsa.</li>
<li><strong>Explica por que previsões surpreendentes valem mais:</strong> se E seria improvável sem H, observar E aumenta muito a crença em H.</li>
<li><strong>Explica “afirmações extraordinárias exigem evidências extraordinárias”:</strong> com uma <em>priori</em> muito baixa, é preciso evidência muito forte para chegar a uma crença alta.</li>
<li><strong>Convergência:</strong> pessoas que começam com <em>prioris</em> diferentes tendem a convergir com evidência suficiente.</li></ul>
<h2>Críticas</h2>
<ul><li><strong>Subjetividade das prioris:</strong> de onde vêm? Duas pessoas podem começar muito diferentes. (Resposta: com evidência suficiente, convergem; e há regras para prioris razoáveis.)</li>
<li><strong>Problema da evidência antiga:</strong> a órbita de Mercúrio já era conhecida quando confirmou a relatividade; se P(E) = 1, a regra diz que ela não confirma nada.</li>
<li><strong>Idealização:</strong> ninguém calcula probabilidades para todas as crenças.</li>
<li><strong>Na estatística</strong>, há um debate antigo entre bayesianos e frequentistas (que usam p-valores e intervalos de confiança).</li></ul>
<div class="nota"><strong>Para a vida:</strong> antes de reagir a uma notícia, pergunte qual era a chance de aquilo ser verdade antes da notícia (a priori) e quão provável seria a notícia existir mesmo se fosse falsa.</div>''',
fontes=[('Bayesian Epistemology (Stanford Encyclopedia of Philosophy)', SEP + 'epistemology-bayesian/'), ('Teorema de Bayes (Wikipédia)', WP + 'Teorema_de_Bayes'), ('Base rate fallacy (Wikipédia)', WE + 'Base_rate_fallacy')],
quiz=[('O que é a probabilidade a priori?', ['A probabilidade depois da evidência', 'O grau de crença na hipótese antes de considerar a nova evidência', 'A chance de o exame errar', 'Uma lei da física'], 1, 'A priori é o ponto de partida que a evidência atualiza.'),
 ('Por que, no exemplo, um exame positivo indica só cerca de 2% de chance de doença?', ['Porque o exame é ruim', 'Porque a doença é muito rara: os falsos positivos entre os muitos saudáveis superam os verdadeiros', 'Porque a regra de Bayes está errada', 'Porque 99% é pouco'], 1, 'Ignorar a taxa de base é a falácia mais comum na interpretação de exames.'),
 ('Alguém diz que viu um fantasma. Pelo bayesianismo, por que isso não basta para crer em fantasmas?', ['Porque fantasmas são proibidos', 'Porque a priori é muito baixa e o relato seria bastante provável mesmo sem fantasmas (ilusão, sugestão, sono)', 'Porque relatos nunca contam', 'Porque é preciso votar'], 1, 'Evidência fraca não move muito uma priori muito baixa.')],
analogia='O bayesiano é como um investigador que começa com suspeitas proporcionais (o mordomo é sempre suspeito, mas pouco) e ajusta a cada pista. Uma pista que só faria sentido se o mordomo fosse culpado pesa muito; uma pista que qualquer um deixaria pesa pouco.',
crianca='Se o seu amigo diz que viu um gato na rua, você acredita fácil, porque tem muito gato. Se ele diz que viu um leão, você precisa de muito mais prova, porque leão na rua é raríssimo.',
obj=['Explicar graus de crença e a regra de Bayes em palavras.', 'Resolver o problema do exame com taxa de base baixa.', 'Avaliar forças e críticas do bayesianismo como teoria da confirmação.'],
caso=('Um teste de detector de mentiras acerta 90% das vezes. Numa empresa de 1.000 funcionários, ele é usado para achar 1 ladrão.', 'Se o teste acusar alguém, qual a chance de essa pessoa ser o ladrão?', 'Muito baixa: cerca de 100 inocentes seriam acusados por erro, para 1 culpado. Com taxa de base tão pequena, até um teste bom gera sobretudo falsos positivos.'),
erro=('“Um exame com 99% de acerto deu positivo, então tenho 99% de chance de estar doente.”', 'A chance depende também de quão comum é a doença. Para doenças raras, a maioria dos positivos pode ser falsa.'),
ferr='nivel-de-evidencia', pre=['estatistica-para-entender-ciencia', 'o-problema-da-inducao'],
guardar=['Crença em graus, atualizada pela regra de Bayes.', 'A priori importa: para hipóteses improváveis, só evidência forte muda muito.', 'Críticas: prioris subjetivas, evidência antiga e idealização.'],
pensar='Que crença sua deveria ter uma priori mais baixa do que você dá a ela?'),

dict(slug='filosofia-analitica', grupo='Tradições e métodos filosóficos', titulo='Filosofia analítica e ciência', temas=['filosofia'],
resumo='Clareza, lógica e análise de conceitos: a tradição de Frege, Russell e Wittgenstein, sua relação com a ciência e a divisão com a filosofia continental.',
corpo='''
<p class="abre">A <strong>filosofia analítica</strong> é a tradição dominante nas universidades de língua inglesa e nórdica desde o século XX, e muito presente no Brasil. Ela se caracteriza menos por doutrinas do que por um estilo: clareza, argumentos explícitos, uso da lógica e atenção ao sentido das palavras.</p>
<h2>As origens</h2>
<ul><li><strong>Gottlob Frege</strong> criou a lógica moderna (1879) e distinguiu sentido e referência: “estrela da manhã” e “estrela da tarde” têm sentidos diferentes e se referem ao mesmo objeto, Vênus.</li>
<li><strong>Bertrand Russell</strong> e G. E. Moore romperam com o idealismo britânico. Russell mostrou como a análise lógica dissolve confusões: “o atual rei da França é careca” parece falar de alguém, mas, analisada, afirma que existe exatamente um rei da França e que ele é careca, o que é falso.</li>
<li><strong>Ludwig Wittgenstein</strong>, no <em>Tractatus</em> (1921), tentou mostrar os limites do que pode ser dito com sentido. Mais tarde, nas <em>Investigações Filosóficas</em>, mudou de ideia: o sentido das palavras está no uso, em “jogos de linguagem”.</li>
<li>O <strong>Círculo de Viena</strong> uniu a nova lógica ao empirismo, dando origem ao positivismo lógico.</li></ul>
<h2>Fases</h2>
<ol><li><strong>Análise lógica</strong> (Frege, Russell, primeiro Wittgenstein, positivistas): traduzir frases para a forma lógica.</li>
<li><strong>Filosofia da linguagem comum</strong> (Oxford, anos 1950: Ryle, Austin, segundo Wittgenstein): muitos problemas filosóficos nascem de usos confusos de palavras comuns.</li>
<li><strong>Pós-positivismo e naturalismo</strong> (Quine, Kripke, Putnam, Lewis): retorno da metafísica e aproximação com as ciências.</li></ol>
<h2>Relação com a ciência</h2>
<p>A filosofia analítica sempre foi próxima da ciência: muitos de seus fundadores eram matemáticos ou físicos. Ela deu à filosofia da ciência suas ferramentas: análise de conceitos como “causa”, “lei” e “explicação”, lógica formal, teoria da probabilidade. Hoje, áreas como filosofia da mente, da biologia e da física dialogam diretamente com cientistas.</p>
<h2>Analíticos e continentais</h2>
<p>A tradição “continental” (fenomenologia, hermenêutica, existencialismo, teoria crítica, pós-estruturalismo; nomes como Husserl, Heidegger, Sartre, Foucault, Derrida) desenvolveu-se sobretudo na França e na Alemanha. A divisão é imperfeita (a geografia não bate: Frege era alemão; Wittgenstein, austríaco), mas descreve estilos diferentes: os continentais tendem a enfatizar a história, a interpretação e a crítica cultural; os analíticos, o argumento e a precisão.</p>
<p>A divisão gerou atritos, como o caso Sokal (1996), em que um físico publicou um artigo propositalmente sem sentido numa revista de estudos culturais para criticar o uso de jargão científico por autores pós-modernos. Hoje muitos filósofos trabalham entre as duas tradições.</p>
<div class="nota"><strong>Críticas à filosofia analítica:</strong> excesso de tecnicidade, foco em quebra-cabeças pequenos e pouca atenção à história e à política. Defensores respondem que clareza é condição para discordar de forma produtiva.</div>''',
fontes=[('Analytic Philosophy (Internet Encyclopedia of Philosophy)', IEP + 'analytic/'), ('Gottlob Frege (Stanford Encyclopedia)', SEP + 'frege/'), ('Wittgenstein (Stanford Encyclopedia)', SEP + 'wittgenstein/'), ('Sokal affair (Wikipédia)', WE + 'Sokal_affair')],
quiz=[('O que caracteriza a filosofia analítica?', ['Uma doutrina única sobre Deus', 'Um estilo: clareza, argumentos explícitos, lógica e atenção ao sentido das palavras', 'Rejeição da ciência', 'Foco em poesia'], 1, 'Mais estilo do que doutrina.'),
 ('O que Frege distinguiu com “estrela da manhã” e “estrela da tarde”?', ['Dois planetas', 'Sentido e referência: sentidos diferentes, mesmo objeto (Vênus)', 'Dia e noite', 'Ciência e mito'], 1, 'A distinção entre sentido e referência é um marco da filosofia da linguagem.'),
 ('Num debate, duas pessoas discutem se “a internet é livre” e percebem que uma usa “livre” como gratuita e a outra como sem censura. Que contribuição analítica isso ilustra?', ['Análise conceitual: muitas disputas são confusões sobre o sentido das palavras', 'Hermenêutica', 'Bayesianismo', 'Positivismo de Comte'], 0, 'Esclarecer conceitos é a marca da tradição analítica.')],
analogia='A filosofia analítica é como desmontar um relógio para ver cada engrenagem. Às vezes descobre que um problema enorme era só uma peça mal encaixada, uma palavra usada em dois sentidos.',
crianca='Às vezes duas pessoas brigam porque usam a mesma palavra com significados diferentes. Alguns filósofos gostam de ajudar a deixar as palavras bem claras, para as pessoas discutirem direito.',
obj=['Caracterizar a filosofia analítica pelo estilo e pelos fundadores.', 'Descrever as fases: análise lógica, linguagem comum, naturalismo.', 'Explicar a relação com a ciência e a divisão com a tradição continental.'],
caso=('Num grupo, alguém diz que “a ciência prova que o amor é só química”, e outro diz que isso é absurdo.', 'Como uma análise conceitual ajudaria?', 'Perguntando o que “só” e “é” querem dizer: que o amor tem bases químicas, que se reduz a elas, ou que nada mais importa nele? Cada leitura é uma tese diferente, com evidência diferente.'),
erro=('“Filosofia analítica é só lógica formal.”', 'Lógica é uma ferramenta, mas a tradição inclui filosofia da linguagem comum, ética, metafísica e filosofia da mente, unidas pelo estilo argumentativo.'),
ferr='quem-disse', pre=['positivismo'],
guardar=['Estilo analítico: clareza, argumento, lógica, análise de conceitos.', 'Frege, Russell, Wittgenstein e o Círculo de Viena; depois Quine e o naturalismo.', 'Analíticos e continentais diferem em estilo; a divisão é imperfeita e hoje menos rígida.'],
pensar='Qual discussão recente que você viu era, no fundo, uma confusão sobre o sentido de uma palavra?'),

dict(slug='naturalismo-epistemologico', grupo='Tradições e métodos filosóficos', titulo='Naturalismo e epistemologia naturalizada', temas=['epistemologia', 'filosofia'],
resumo='Para Quine, a epistemologia deve ser parte da ciência. O que isso muda, o problema da circularidade e a influência da ciência cognitiva.',
corpo='''
<p class="abre">Desde Descartes, a epistemologia tentou fundamentar a ciência de fora, a partir de certezas anteriores a ela. Em 1969, Quine propôs abandonar esse projeto. No ensaio “Epistemologia naturalizada”, defendeu que o estudo do conhecimento deveria ser um capítulo da psicologia: estudar, com os métodos da ciência, como seres humanos passam de estímulos sensoriais a teorias sobre o mundo.</p>
<h2>A ideia</h2>
<p>O <strong>naturalismo</strong> filosófico tem duas faces:</p>
<ul><li><strong>Metodológica:</strong> a filosofia não tem um método próprio superior ao da ciência; deve ser contínua com ela.</li>
<li><strong>Ontológica:</strong> o que existe é o que nossas melhores teorias científicas dizem existir, sem entidades sobrenaturais.</li></ul>
<p>Quine usava a imagem do barco de Neurath: somos como marinheiros que precisam consertar o barco em alto-mar, tábua por tábua, sem nunca poder levá-lo a um dique seco. Não há ponto de partida fora da ciência.</p>
<h2>A objeção da normatividade</h2>
<p>Jaegwon Kim criticou: a epistemologia tradicional pergunta como <em>devemos</em> formar crenças (normas), e a psicologia descreve como <em>de fato</em> as formamos. Naturalizar a epistemologia seria mudar de assunto e perder a dimensão normativa.</p>
<p>Respostas naturalistas:</p>
<ul><li><strong>Confiabilismo:</strong> as normas são de tipo instrumental. Devemos usar processos que, como a ciência mostra, tendem a produzir verdades.</li>
<li><strong>Epistemologia melhorativa:</strong> a psicologia dos vieses (Kahneman, Tversky) mostra onde erramos, e isso permite criar normas práticas, como usar taxas de base ou listas de verificação.</li></ul>
<h2>A objeção da circularidade</h2>
<p>Usar a ciência para justificar a ciência não é circular? O naturalista aceita uma circularidade virtuosa: não há alternativa melhor, e uma teoria que explica sua própria confiabilidade é melhor do que uma que se autodestrói. A ciência cognitiva, por exemplo, pode mostrar que nossa percepção é confiável em certas condições e falha em outras (ilusões), e isso corrige o próprio método.</p>
<h2>Naturalismo hoje</h2>
<ul><li><strong>Filosofia experimental:</strong> testar intuições filosóficas com questionários e experimentos, como nos casos de Gettier.</li><li><strong>Epistemologia evolutiva:</strong> nossas capacidades cognitivas foram moldadas pela seleção natural, o que explica tanto acertos quanto vieses.</li><li><strong>Naturalismo na filosofia da ciência:</strong> estudar a ciência real, com história e sociologia, em vez de reconstruções idealizadas.</li></ul>
<div class="nota"><strong>Críticas de outro tipo:</strong> filósofos como Alvin Plantinga argumentaram que, se nossa mente foi moldada só para sobreviver, não para acertar verdades, o naturalismo minaria a confiança na própria razão. Naturalistas respondem que crenças verdadeiras sobre o ambiente geralmente ajudam a sobreviver.</div>''',
fontes=[('Naturalism in Epistemology (Stanford Encyclopedia of Philosophy)', SEP + 'epistemology-naturalized/'), ('Naturalism (Stanford Encyclopedia of Philosophy)', SEP + 'naturalism/'), ('Experimental Philosophy (Stanford Encyclopedia)', SEP + 'experimental-philosophy/')],
quiz=[('O que Quine propôs com a epistemologia naturalizada?', ['Abandonar a ciência', 'Estudar o conhecimento com os métodos da própria ciência, como parte da psicologia', 'Voltar a Descartes', 'Provar a existência de Deus'], 1, 'A epistemologia vira contínua com a ciência.'),
 ('Qual a objeção de Kim?', ['Que a psicologia é falsa', 'Que naturalizar perde a dimensão normativa: descrever como formamos crenças não diz como devemos formá-las', 'Que Quine era cético', 'Que a ciência é circular'], 1, 'É a objeção da normatividade.'),
 ('Pesquisadores aplicam questionários em vários países para ver se as pessoas consideram “conhecimento” os casos de Gettier. Isso é:', ['Filosofia experimental, uma vertente naturalista', 'Fundacionalismo', 'Positivismo de Comte', 'Pseudociência'], 0, 'Testar intuições filosóficas empiricamente é filosofia experimental.')],
analogia='O naturalista é como o marinheiro que conserta o barco em alto-mar. Não há porto seguro para desmontar tudo e reconstruir do zero; trocamos tábua por tábua, usando as tábuas que ainda flutuam.',
crianca='Alguns filósofos acham que, para entender como a gente aprende as coisas, o melhor é estudar o cérebro e o jeito como as pessoas pensam, igual os cientistas estudam qualquer outra coisa.',
obj=['Explicar o naturalismo metodológico e ontológico.', 'Apresentar as objeções da normatividade e da circularidade, com respostas.', 'Citar desenvolvimentos atuais: filosofia experimental e epistemologia evolutiva.'],
caso=('Um estudo mostra que juízes dão sentenças mais duras antes do almoço do que depois.', 'O que um epistemólogo naturalista faria com esse dado?', 'Usaria a descoberta (se confirmada) para propor normas práticas de decisão, como pausas ou revisões cegas. Descrição informa a norma, sem substituí-la.'),
erro=('“Naturalismo é só dizer que a ciência resolve tudo.”', 'É a tese de que a filosofia é contínua com a ciência e usa seus resultados. Naturalistas debatem normas, circularidade e limites, e não dispensam a filosofia.'),
ferr='que-corrente-e-essa', pre=['o-que-e-epistemologia', 'como-justificar-uma-crenca'],
guardar=['Quine: a epistemologia é parte da ciência; o barco se conserta em alto-mar.', 'Objeções: perda da normatividade e circularidade, com respostas instrumentais.', 'Hoje: filosofia experimental, psicologia dos vieses e epistemologia evolutiva.'],
pensar='Que descoberta sobre como o cérebro funciona mudou o modo como você confia nos seus julgamentos?'),

dict(slug='sociologia-do-conhecimento-cientifico', grupo='Tradições e métodos filosóficos', titulo='Sociologia da ciência e construtivismo', temas=['sociedade', 'filosofia'],
resumo='Normas de Merton, o programa forte, a teoria ator-rede de Latour e as “guerras da ciência”: o que a ciência tem de social, e onde o construtivismo exagera.',
corpo='''
<p class="abre">A ciência é feita por pessoas, em instituições, com dinheiro, prestígio e disputas. Estudar esse lado social é o trabalho da sociologia da ciência. A grande questão é até onde vai a influência social: só na escolha de temas e no ritmo da pesquisa, ou no próprio conteúdo das teorias?</p>
<h2>Merton e o ethos da ciência</h2>
<p>Em 1942, Robert Merton descreveu as normas institucionais da ciência, resumidas na sigla CUDOS: <strong>comunalismo</strong> (resultados são de todos), <strong>universalismo</strong> (vale o argumento, não quem o diz), <strong>desinteresse</strong> (a recompensa é o reconhecimento, não o ganho pessoal) e <strong>ceticismo organizado</strong>. Para Merton, o social explicava a organização da ciência, mas não o conteúdo do conhecimento.</p>
<h2>O programa forte</h2>
<p>Nos anos 1970, David Bloor e Barry Barnes, em Edimburgo, propuseram o <strong>programa forte</strong> da sociologia do conhecimento científico. Seu princípio mais polêmico era a <strong>simetria</strong>: crenças verdadeiras e falsas, racionais e irracionais, devem ser explicadas pelo mesmo tipo de causas sociais. Não se pode dizer que os cientistas aceitaram a teoria certa “porque era certa” e a errada “por interesses”.</p>
<h2>Construtivismo e Latour</h2>
<p>Bruno Latour e Steve Woolgar observaram um laboratório como antropólogos (<em>A Vida de Laboratório</em>, 1979) e descreveram como “fatos” são construídos por inscrições, negociações e alianças. Latour desenvolveu depois a <strong>teoria ator-rede</strong>, que trata humanos e não humanos (micróbios, instrumentos) como participantes da rede que estabiliza um fato.</p>
<h2>As guerras da ciência</h2>
<p>Nos anos 1990, cientistas reagiram ao que viam como relativismo. Paul Gross e Norman Levitt publicaram <em>Higher Superstition</em>; Alan Sokal fez sua paródia publicada numa revista de estudos culturais. A crítica central: se fatos são só construções sociais, por que a física funciona e a astrologia não?</p>
<h2>O que ficou</h2>
<ul class="lista-forte"><li>A ciência tem dimensão social real: financiamento, prestígio, conflitos de interesse e quem é ouvido influenciam o que se pesquisa e quando se aceita uma conclusão.</li><li>Estudos de controvérsias mostraram que o encerramento de debates envolve negociação, não só lógica.</li><li>O próprio Latour, em 2004, lamentou que argumentos construtivistas estivessem sendo usados por negacionistas do clima, e pediu uma crítica que fortalecesse fatos, não os dissolvesse.</li></ul>
<ul class="lista-contra"><li>A tese de que o conteúdo das teorias é determinado só por fatores sociais ignora o papel da natureza nos resultados.</li><li>O princípio da simetria, levado ao extremo, impede de explicar por que algumas teorias funcionam.</li></ul>
<div class="nota"><strong>Construção social, em dois sentidos:</strong> dizer que a <em>classificação</em> de doenças mentais tem componentes sociais é razoável e discutido dentro da própria psiquiatria. Dizer que a <em>gravidade</em> é uma construção social é outra coisa. Ian Hacking (<em>The Social Construction of What?</em>) mostrou como separar esses sentidos.</div>''',
fontes=[('Social Dimensions of Scientific Knowledge (Stanford Encyclopedia)', SEP + 'scientific-knowledge-social/'), ('The Normative Structure of Science (Wikipédia: Mertonian norms)', WE + 'Mertonian_norms'), ('Strong programme (Wikipédia)', WE + 'Strong_programme'), ('Why Has Critique Run out of Steam?', 'https://www.journals.uchicago.edu/doi/10.1086/421123')],
quiz=[('O que defendia o princípio da simetria do programa forte?', ['Que só crenças falsas têm causas sociais', 'Que crenças verdadeiras e falsas devem ser explicadas pelo mesmo tipo de causas sociais', 'Que a ciência é simétrica', 'Que a natureza decide tudo'], 1, 'É o princípio mais polêmico do programa forte.'),
 ('Quais são as normas de Merton?', ['Lucro, sigilo, autoridade e fé', 'Comunalismo, universalismo, desinteresse e ceticismo organizado', 'Indução, dedução, abdução e analogia', 'Hipótese, teoria, lei e fato'], 1, 'A sigla CUDOS resume o ethos da ciência para Merton.'),
 ('Um grupo negacionista diz: “até os sociólogos mostraram que fatos científicos são construções sociais, então o aquecimento global é invenção”. Qual a melhor resposta?', ['Concordar', 'A dimensão social da ciência não torna os fatos arbitrários; o próprio Latour criticou esse uso de argumentos construtivistas', 'Dizer que sociologia é pseudociência', 'Ignorar'], 1, 'Reconhecer o social na ciência não equivale a negar a evidência.')],
analogia='Uma ponte é construída por pessoas, com orçamento, política e erros humanos. Isso não quer dizer que a física da carga seja inventada: se os engenheiros errarem as contas, a ponte cai, quaisquer que sejam os acordos sociais. A ciência é construída socialmente e testada pela natureza.',
crianca='Cientistas são pessoas: trabalham juntos, discutem, às vezes brigam. Isso influencia o que eles estudam. Mas no fim, a natureza é que diz se a ideia funciona ou não.',
obj=['Descrever as normas de Merton e o programa forte.', 'Explicar o construtivismo de Latour e as guerras da ciência.', 'Separar o que a sociologia mostrou de real das conclusões relativistas exageradas.'],
caso=('Uma pesquisa mostra que estudos financiados pela indústria do açúcar nos anos 1960 minimizaram o papel do açúcar em doenças cardíacas.', 'Isso mostra que toda ciência é construção social?', 'Mostra que interesses influenciam a pesquisa, e por isso transparência e independência importam. Mas o erro foi descoberto por mais ciência, o que mostra que o sistema também se corrige.'),
erro=('“A sociologia da ciência prova que a ciência é só opinião de um grupo.”', 'Ela mostra a dimensão social da produção do conhecimento. As versões que reduzem o conteúdo a interesses sociais são minoritárias e muito criticadas.'),
ferr='quem-disse', pre=['kuhn-e-os-paradigmas'],
guardar=['Merton: normas institucionais (comunalismo, universalismo, desinteresse, ceticismo).', 'Programa forte e Latour: o social também no conteúdo; as guerras da ciência reagiram.', 'Social não é arbitrário: interesses influenciam, a natureza testa.'],
pensar='Que interesse econômico ou político poderia enviesar pesquisas na área que mais te interessa?'),

dict(slug='valores-na-ciencia', grupo='Ciência e sociedade', titulo='Valores na ciência', temas=['sociedade', 'filosofia'],
resumo='A ciência é neutra? O ideal livre de valores, o argumento do risco indutivo e as epistemologias feministas: onde os valores entram e onde não deveriam entrar.',
corpo='''
<p class="abre">“A ciência é neutra” e “a ciência é ideológica” são frases que se ouve muito. As duas simplificam. A filosofia da ciência distingue os <strong>momentos</strong> da pesquisa e os <strong>tipos</strong> de valores, para perguntar onde valores entram legitimamente e onde distorcem.</p>
<h2>Tipos de valores</h2>
<ul><li><strong>Epistêmicos:</strong> ligados à busca da verdade, como precisão, consistência, simplicidade e poder explicativo.</li><li><strong>Não epistêmicos:</strong> éticos, sociais, políticos, econômicos.</li></ul>
<h2>Onde os valores entram sem problema</h2>
<ul><li><strong>Na escolha do que pesquisar:</strong> financiar pesquisa sobre malária ou sobre calvície é uma escolha de valores.</li><li><strong>Nos limites éticos:</strong> não se fazem experimentos que causam sofrimento grave a humanos sem consentimento; comitês de ética existem para isso. (Para os animais, essa proteção ainda é bem menor; veja o debate sobre testes em animais.)</li><li><strong>Na aplicação:</strong> o que fazer com o conhecimento sobre energia nuclear é uma questão política.</li></ul>
<h2>O ideal da ciência livre de valores</h2>
<p>O ideal tradicional diz que, no momento de <strong>aceitar ou rejeitar uma hipótese</strong>, só valores epistêmicos devem pesar. Desejar que algo seja verdade não pode ser razão para acreditar que é. Esse ideal protege contra a ciência que conclui o que o financiador quer.</p>
<h2>O argumento do risco indutivo</h2>
<p>Richard Rudner (1953) e, mais recentemente, Heather Douglas argumentaram que valores entram também na aceitação. Como a evidência nunca dá certeza, decidir quanta evidência basta depende das consequências de errar. Se a pergunta é se um produto químico causa câncer, um falso negativo (dizer que é seguro quando não é) pode matar pessoas; um falso positivo pode fechar uma fábrica. O nível de exigência depende de quanto pesam esses erros, e isso é um julgamento de valor.</p>
<p>Douglas distingue papéis: valores não podem servir de <em>razão</em> para crer (o papel direto), mas podem legitimamente definir <em>quanta evidência</em> é suficiente (o papel indireto).</p>
<h2>Epistemologias feministas</h2>
<ul><li><strong>Empirismo contextual</strong> (Helen Longino): a objetividade não vem de cientistas individuais sem valores, mas de comunidades com diversidade de perspectivas, crítica mútua e padrões compartilhados.</li>
<li><strong>Teoria do ponto de vista</strong> (Sandra Harding): grupos marginalizados podem notar vieses invisíveis para os grupos dominantes. Exemplos: pesquisas médicas que por décadas testaram remédios quase só em homens; a primatologia, que mudou quando pesquisadoras passaram a observar o comportamento das fêmeas.</li>
<li><strong>Objetividade forte:</strong> examinar criticamente também os pressupostos de quem faz a pesquisa.</li></ul>
<div class="nota"><strong>O equilíbrio:</strong> reconhecer valores na ciência não autoriza escolher conclusões por conveniência política, à esquerda ou à direita. Lisenko, na União Soviética, rejeitou a genética por ideologia, e a agricultura soviética pagou o preço. O objetivo é tornar os valores explícitos e sujeitos a crítica.</div>''',
fontes=[('Science and Values (Stanford Encyclopedia)', SEP + 'scientific-objectivity/'), ('Feminist Epistemology and Philosophy of Science (Stanford Encyclopedia)', SEP + 'feminism-epistemology/'), ('Science, Policy, and the Value-Free Ideal', 'https://www.google.com/search?tbm=bks&q=Science+Policy+and+the+Value-Free+Ideal+Douglas'), ('Lysenkoism (Wikipédia)', WE + 'Lysenkoism')],
quiz=[('Em que momento da pesquisa valores não epistêmicos entram sem controvérsia?', ['Na aceitação de hipóteses por conveniência', 'Na escolha do que pesquisar e nos limites éticos', 'Na leitura dos dados', 'Em nenhum'], 1, 'Escolher temas e impor limites éticos são escolhas de valor aceitas.'),
 ('O que diz o argumento do risco indutivo?', ['Que a indução é arriscada', 'Que decidir quanta evidência basta depende das consequências de errar, um julgamento de valor', 'Que valores devem decidir a verdade', 'Que a ciência é neutra'], 1, 'Valores entram de forma indireta, no nível de exigência.'),
 ('Remédios foram testados por décadas quase só em homens, e efeitos colaterais em mulheres passaram despercebidos. Que ideia isso ilustra?', ['O ideal livre de valores', 'A teoria do ponto de vista: perspectivas ausentes deixam vieses invisíveis', 'O problema da indução', 'O realismo estrutural'], 1, 'A diversidade de perspectivas ajuda a enxergar o que um grupo homogêneo não vê.')],
analogia='Valores na ciência são como a regulagem de um alarme de incêndio. A física da fumaça não depende de valores; mas quão sensível deixar o alarme depende de quanto custa um alarme falso e quanto custa um incêndio não detectado.',
crianca='Cientistas escolhem o que estudar porque acham importante, e isso é normal. Mas na hora de dizer se uma ideia é verdadeira, não vale escolher só porque gostariam que fosse.',
obj=['Distinguir valores epistêmicos e não epistêmicos e os momentos da pesquisa.', 'Explicar o ideal livre de valores e o argumento do risco indutivo.', 'Descrever contribuições das epistemologias feministas à objetividade.'],
caso=('Uma agência precisa decidir se um agrotóxico é seguro com estudos inconclusivos.', 'Os valores devem influenciar a decisão?', 'Não devem decidir o que é verdade, mas influenciam legitimamente quanta evidência exigir antes de liberar: o custo de errar para a saúde pesa diferente do custo de errar para a produção.'),
erro=('“Se há valores na ciência, então ela é só ideologia.”', 'Valores entram em escolhas de temas, limites e níveis de exigência. Isso não autoriza escolher conclusões por conveniência; o objetivo é torná-los explícitos e criticáveis.'),
ferr=None, pre=['sociologia-do-conhecimento-cientifico'],
guardar=['Valores entram legitimamente na escolha de temas, na ética e na aplicação.', 'Risco indutivo: quanta evidência basta depende do custo de errar.', 'Objetividade cresce com diversidade de perspectivas e crítica mútua (Longino, Harding).'],
pensar='Num tema que te importa, qual erro é pior: o falso positivo ou o falso negativo? Isso muda quanta evidência você exige?'),

dict(slug='confianca-e-especialistas', grupo='Ciência e sociedade', titulo='Confiança em especialistas e epistemologia social', temas=['sociedade', 'epistemologia'],
resumo='Quase tudo o que sabemos vem do testemunho. Como leigos podem avaliar especialistas, quando desconfiar e o que fazer quando especialistas discordam.',
corpo='''
<p class="abre">Você sabe que a Terra tem cerca de 4,5 bilhões de anos, que vírus causam gripe e que o DNA tem forma de dupla hélice. Provavelmente não verificou nada disso. Quase todo o nosso conhecimento é <strong>testemunhal</strong>: depende de confiar em outros. A epistemologia social estuda quando essa confiança é racional.</p>
<h2>A dependência epistêmica</h2>
<p>O filósofo John Hardwig argumentou, em 1985, que a dependência de especialistas não é uma fraqueza, mas a condição normal do conhecimento moderno. Mesmo cientistas dependem uns dos outros: um artigo de física de partículas pode ter milhares de autores, e nenhum domina todas as partes.</p>
<h2>O problema do leigo</h2>
<p>Se não sou especialista, como escolher entre dois especialistas que discordam? Alvin Goldman sugeriu fontes de evidência que um leigo pode usar:</p>
<ol><li><strong>Argumentos:</strong> mesmo sem dominar o tema, dá para notar quem responde às objeções e quem foge delas.</li><li><strong>Concordância de outros especialistas:</strong> o consenso conta, se os especialistas chegaram a ele de forma independente.</li><li><strong>Credenciais e avaliação dos pares:</strong> formação e publicações na área específica.</li><li><strong>Interesses e vieses:</strong> o especialista ganha algo com a conclusão?</li><li><strong>Histórico:</strong> as previsões passadas dele se confirmaram?</li></ol>
<h2>Sinais de alerta</h2>
<ul class="lista-contra"><li>Especialista falando fora da sua área (um médico opinando sobre clima, um físico sobre vacinas).</li><li>Fala dirigida ao público, não aos pares: livros e vídeos em vez de artigos.</li><li>Posição muito minoritária apresentada como se fosse metade do debate.</li><li>Ganho financeiro com a conclusão (venda de cursos, suplementos, consultorias).</li></ul>
<h2>Quando desconfiar é razoável</h2>
<p>A confiança não deve ser cega. Houve casos reais de captura de especialistas por interesses, como a indústria do tabaco financiando pesquisas, e de erros de consenso, como a recomendação de dietas pobres em gordura e ricas em açúcar. O ceticismo saudável pergunta por evidência e conflitos de interesse; o negacionismo rejeita a evidência quando ela incomoda.</p>
<h2>Bolhas e câmaras de eco</h2>
<p>C. Thi Nguyen distinguiu: numa <strong>bolha epistêmica</strong>, as pessoas não ouvem o outro lado por falta de exposição; basta mostrar. Numa <strong>câmara de eco</strong>, as pessoas foram ensinadas a desconfiar ativamente de qualquer fonte de fora; mostrar o outro lado só confirma a desconfiança. Sair de uma câmara de eco exige reconstruir a confiança, não só apresentar fatos.</p>
<div class="nota"><strong>Regra prática:</strong> numa área técnica fora da sua, aposte no consenso dos especialistas da área, e desconfie mais de quem só fala com o público do que de quem publica para os pares.</div>''',
fontes=[('Social Epistemology (Stanford Encyclopedia of Philosophy)', SEP + 'epistemology-social/'), ('Experts: Which Ones Should You Trust?', 'https://www.jstor.org/stable/3071090'), ('Epistemic Dependence', 'https://www.jstor.org/stable/2026523'), ('Echo Chambers and Epistemic Bubbles', 'https://doi.org/10.1017/epi.2018.32')],
quiz=[('Por que Hardwig diz que a dependência de especialistas é normal?', ['Porque leigos são ignorantes', 'Porque o conhecimento moderno é dividido: nem cientistas dominam tudo e dependem uns dos outros', 'Porque especialistas nunca erram', 'Porque é mais rápido'], 1, 'A divisão do trabalho cognitivo é a condição do conhecimento moderno.'),
 ('Qual a diferença entre bolha epistêmica e câmara de eco?', ['Nenhuma', 'Na bolha falta exposição; na câmara de eco há desconfiança ativa das fontes de fora', 'Câmara de eco é mais fácil de sair', 'Bolha é sobre música'], 1, 'Na câmara de eco, apresentar fatos não basta.'),
 ('Um engenheiro famoso diz num podcast que uma vacina é perigosa, contra a posição de associações de imunologia. Que sinais de alerta aparecem?', ['Nenhum: ele é especialista', 'Fala fora da sua área e para o público, contra o consenso da área', 'Ele publica demais', 'Ele é muito jovem'], 1, 'Credencial em outra área não dá autoridade no tema.')],
analogia='Confiar em especialistas é como usar um mapa feito por outros. Você não mediu as ruas, mas pode checar se o mapa é recente, quem o fez, se outros mapas concordam e se o cartógrafo ganha algo mandando você por uma rua específica.',
crianca='Ninguém consegue aprender tudo sozinho, então a gente confia em quem estudou o assunto, como o médico ou o professor. Mas é bom ver se outros especialistas concordam com eles.',
obj=['Explicar a dependência epistêmica e o papel do testemunho.', 'Aplicar os critérios de Goldman para avaliar especialistas.', 'Distinguir bolhas de câmaras de eco e ceticismo de negacionismo.'],
caso=('Dois médicos dão opiniões opostas sobre um tratamento para seu pai.', 'Que critérios você usaria para decidir em quem confiar mais?', 'Quem responde melhor às objeções, o que dizem as diretrizes e outros especialistas, se algum tem interesse financeiro e qual a especialidade de cada um. Pedir as fontes ajuda.'),
erro=('“Confiar em especialistas é falta de pensamento crítico.”', 'Pensamento crítico inclui reconhecer os próprios limites. Confiar com critérios (consenso, área, interesses) é mais racional do que achar que se pode avaliar tudo sozinho.'),
ferr=None, pre=['consenso-cientifico', 'o-que-e-epistemologia'],
guardar=['Quase todo conhecimento é testemunhal; depender de especialistas é normal.', 'Leigos podem avaliar argumentos, consenso, área, interesses e histórico.', 'Bolhas se furam com informação; câmaras de eco exigem reconstruir confiança.'],
pensar='Em que fonte você confia sem saber por quê? Ela passaria pelos critérios de Goldman?'),

dict(slug='crise-de-replicacao', grupo='Ciência e sociedade', titulo='A crise de replicação', temas=['evidencias', 'estatistica', 'sociedade'],
resumo='Por que tantos resultados famosos não se repetem, o que são p-hacking e viés de publicação, e como a ciência aberta tenta corrigir o problema.',
corpo='''
<p class="abre">Em 2015, um consórcio liderado por Brian Nosek tentou repetir 100 estudos publicados em revistas importantes de psicologia. Só cerca de 36% das replicações encontraram resultados estatisticamente significativos, contra 97% dos originais, e os efeitos replicados eram, em média, metade dos originais. Era a confirmação de um problema que já se suspeitava: a <strong>crise de replicação</strong>.</p>
<h2>O que é replicar</h2>
<p>Replicar é refazer um estudo, de preferência com outra equipe e outra amostra, para ver se o resultado se repete. É o teste mais importante de um achado científico, porque elimina acasos e erros locais. A crise mostrou que esse teste era raro, e que, quando feito, muitos resultados falhavam.</p>
<h2>Onde aconteceu</h2>
<p>A psicologia social foi o epicentro (efeitos como o “ego depletion” e a “pose de poder” perderam força em replicações grandes), mas o problema aparece na medicina, na economia e na biologia. Em 2012, pesquisadores da empresa Amgen relataram ter conseguido confirmar apenas 6 de 53 estudos marcantes de biologia do câncer.</p>
<h2>As causas</h2>
<ul class="lista-contra"><li><strong>Viés de publicação:</strong> revistas preferem resultados positivos e novos. Estudos que não acham nada ficam na gaveta (o “problema da gaveta”), e a literatura fica enviesada para efeitos que não existem.</li>
<li><strong>p-hacking:</strong> testar várias análises, excluir alguns dados, parar a coleta quando dá certo, até chegar a p &lt; 0,05. Muitas vezes sem má-fé: são os “jardins de caminhos que se bifurcam”, de Andrew Gelman.</li>
<li><strong>HARKing:</strong> formular a hipótese depois de ver os resultados e apresentá-la como se fosse prévia.</li>
<li><strong>Amostras pequenas:</strong> com poucos participantes, resultados significativos tendem a exagerar o efeito.</li>
<li><strong>Incentivos:</strong> carreiras dependem de publicar muito e de achados chamativos.</li></ul>
<p>Em 2005, John Ioannidis publicou um artigo com o título provocador “Por que a maioria dos resultados de pesquisa publicados é falsa”, mostrando como esses fatores se combinam.</p>
<h2>As respostas: ciência aberta</h2>
<ul class="lista-forte"><li><strong>Pré-registro:</strong> registrar hipótese e análise antes de coletar os dados.</li><li><strong>Relatórios registrados:</strong> a revista aceita o artigo pelo desenho, antes dos resultados, o que acaba com o viés de publicação.</li><li><strong>Dados e código abertos</strong> para que outros confiram.</li><li><strong>Replicações em larga escala</strong> com muitos laboratórios.</li><li><strong>Amostras maiores</strong> e foco em tamanho de efeito.</li></ul>
<h2>Crise ou autocorreção?</h2>
<p>A crise foi descoberta pela própria ciência, com métodos científicos, e levou a reformas. Para muitos, é o melhor exemplo de que a ciência se corrige. Mas ela também é um alerta: um único estudo, ainda mais com amostra pequena e efeito surpreendente, vale pouco antes de ser replicado.</p>
<div class="nota"><strong>Não é munição para o negacionismo:</strong> resultados centrais e muito replicados, como a eficácia das vacinas ou o aquecimento global, não estão em crise. A crise atinge sobretudo efeitos pequenos, surpreendentes e pouco testados.</div>''',
fontes=[('Estimating the reproducibility of psychological science (Science)', 'https://www.science.org/doi/10.1126/science.aac4716'), ('Why Most Published Research Findings Are False (PLOS Medicine)', 'https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0020124'), ('Reproducibility of Scientific Results (Stanford Encyclopedia)', SEP + 'scientific-reproducibility/'), ('Center for Open Science', 'https://www.cos.io/')],
quiz=[('O que é p-hacking?', ['Invadir computadores de cientistas', 'Testar várias análises e escolhas até obter p < 0,05', 'Publicar só resultados negativos', 'Usar amostras grandes'], 1, 'Flexibilidade na análise infla falsos positivos.'),
 ('Como os relatórios registrados combatem o viés de publicação?', ['Publicando só resultados positivos', 'Aceitando o artigo pelo desenho, antes de se conhecer o resultado', 'Proibindo replicações', 'Aumentando o p-valor'], 1, 'Se a aceitação não depende do resultado, resultados nulos também são publicados.'),
 ('Um livro de autoajuda cita um único estudo com 40 pessoas que achou um efeito enorme de uma postura corporal na confiança. O que a crise de replicação sugere?', ['Acreditar, pois é um estudo', 'Desconfiar até haver replicações: amostra pequena e efeito surpreendente são sinais de alerta', 'Que toda psicologia é falsa', 'Que posturas não existem'], 1, 'Efeitos grandes em amostras pequenas costumam encolher ou sumir nas replicações.')],
analogia='A crise de replicação é como descobrir que muitas receitas famosas só deram certo uma vez, na cozinha do autor. Quando outros cozinheiros tentaram, o bolo não cresceu. A solução foi exigir receitas detalhadas antes de cozinhar e testar em várias cozinhas.',
crianca='Quando um cientista descobre algo, outros cientistas tentam fazer igual para ver se dá o mesmo resultado. Descobriram que muitas descobertas não davam certo de novo, e agora estão mudando o jeito de trabalhar para isso acontecer menos.',
obj=['Explicar o que é replicação e os números da crise.', 'Descrever as causas: viés de publicação, p-hacking, HARKing, amostras pequenas e incentivos.', 'Apresentar as respostas da ciência aberta e por que a crise não justifica o negacionismo.'],
caso=('Um pesquisador coleta dados, testa 15 formas de análise e publica a única que deu significativa, sem mencionar as outras.', 'Ele fraudou? O resultado é confiável?', 'Talvez sem má-fé, mas é p-hacking: com 15 tentativas, um resultado significativo por acaso é esperado. O pré-registro teria evitado o problema.'),
erro=('“A crise de replicação mostra que não dá para confiar em nenhuma ciência.”', 'Ela atinge sobretudo efeitos pequenos e pouco testados. Resultados muito replicados continuam sólidos, e a crise foi descoberta e corrigida pela própria ciência.'),
ferr='nivel-de-evidencia', pre=['estatistica-para-entender-ciencia', 'vieses-e-metodo'],
guardar=['Replicar é o teste mais importante, e foi raro por décadas.', 'Viés de publicação, p-hacking e amostras pequenas inflaram falsos positivos.', 'Pré-registro e ciência aberta são a autocorreção em ação.'],
pensar='Que “fato científico” curioso que você conhece veio de um único estudo? Ele foi replicado?'),

dict(slug='negacionismo-e-desinformacao', grupo='Ciência e sociedade', titulo='Negacionismo e desinformação', temas=['sociedade', 'demarcacao', 'mente'],
resumo='As técnicas do negacionismo (FLICC), a fabricação da dúvida pelos mercadores da dúvida e o que funciona para responder: pré-bunking e reconstruir confiança.',
corpo='''
<p class="abre">Negacionismo científico é a rejeição sistemática de um consenso científico bem estabelecido, geralmente por motivos ideológicos, religiosos ou econômicos, e não por evidência nova. Não é o mesmo que ceticismo: o cético pede evidência e muda com ela; o negacionista rejeita a evidência que contraria a conclusão desejada.</p>
<h2>Os mercadores da dúvida</h2>
<p>As historiadoras da ciência Naomi Oreskes e Erik Conway (<em>Merchants of Doubt</em>, 2010) mostraram como a mesma estratégia foi usada contra o elo entre tabaco e câncer, a chuva ácida, o buraco na camada de ozônio e o aquecimento global. Um memorando interno da indústria do tabaco de 1969 resumia: “a dúvida é o nosso produto”. Não era preciso provar o contrário; bastava parecer que havia um debate.</p>
<h2>As técnicas: FLICC</h2>
<p>O pesquisador John Cook organizou as técnicas mais comuns do negacionismo na sigla FLICC:</p>
<div class="tabela"><table><thead><tr><th>Técnica</th><th>O que é</th><th>Exemplo</th></tr></thead><tbody>
<tr><td><strong>Falsos especialistas</strong></td><td>Apresentar pessoas sem competência na área como autoridades</td><td>Listas de “milhares de cientistas” que não são da área</td></tr>
<tr><td><strong>Lógica falaciosa</strong></td><td>Argumentos com conclusões que não decorrem das premissas</td><td>“O clima sempre mudou, então a mudança atual é natural”</td></tr>
<tr><td><strong>Expectativas impossíveis</strong></td><td>Exigir certeza absoluta antes de agir</td><td>“Enquanto não houver 100% de certeza, nada deve ser feito”</td></tr>
<tr><td><strong>Escolha seletiva</strong> (cherry picking)</td><td>Usar só os dados convenientes</td><td>Escolher um ano excepcionalmente quente como ponto de partida para dizer que o aquecimento parou</td></tr>
<tr><td><strong>Conspiração</strong></td><td>Explicar o consenso como complô</td><td>“Os cientistas inventam o problema para ganhar verbas”</td></tr>
</tbody></table></div>
<h2>Por que funciona</h2>
<ul><li><strong>Identidade:</strong> quando uma crença vira marca de um grupo, rejeitá-la parece traição. A evidência ameaça o pertencimento.</li><li><strong>Raciocínio motivado:</strong> aceitar a conclusão teria custos (mudar hábitos, aceitar regulação).</li><li><strong>Assimetria:</strong> criar dúvida é barato; desfazê-la é caro (a “lei de Brandolini”).</li><li><strong>Algoritmos:</strong> conteúdo indignado e surpreendente se espalha mais.</li></ul>
<h2>O que funciona para responder</h2>
<ul class="lista-forte"><li><strong>Pré-bunking (inoculação):</strong> explicar as técnicas antes de a pessoa encontrá-las. Experimentos de Sander van der Linden e John Roozenbeek mostram que conhecer a técnica reduz a persuasão.</li><li><strong>Verdade antes do mito:</strong> ao desmentir, comece pelo fato correto, explique a falácia e só então mencione o mito.</li><li><strong>Comunicar o consenso:</strong> informar que cerca de 97% ou mais dos climatologistas concordam altera percepções.</li><li><strong>Mensageiros confiáveis:</strong> pessoas do próprio grupo convencem mais.</li><li><strong>Respeito:</strong> humilhar fortalece a câmara de eco.</li></ul>
<div class="nota"><strong>No Brasil:</strong> a queda na cobertura vacinal nos anos 2010 e 2020, com retorno do sarampo em 2018, mostra o custo real da desinformação. Agências de checagem e campanhas de pré-bunking são parte da resposta.</div>''',
fontes=[('Merchants of Doubt', 'https://www.merchantsofdoubt.org/'), ('FLICC (Skeptical Science)', 'https://skepticalscience.com/history-FLICC-5-techniques-science-denial.html'), ('Psychological inoculation against misinformation (Wikipédia: Inoculation theory)', WE + 'Inoculation_theory'), ('The Debunking Handbook 2020', 'https://www.climatechangecommunication.org/debunking-handbook-2020/')],
quiz=[('Qual a diferença entre ceticismo e negacionismo?', ['Nenhuma', 'O cético pede evidência e muda com ela; o negacionista rejeita a evidência que contraria a conclusão desejada', 'O negacionista é mais científico', 'O cético nunca acredita em nada'], 1, 'A diferença está na resposta à evidência.'),
 ('O que significa “a dúvida é o nosso produto”?', ['Que a indústria do tabaco vendia ceticismo saudável', 'Que bastava criar a impressão de debate para atrasar ações, sem provar o contrário', 'Que a ciência produz dúvidas', 'Que o tabaco faz bem'], 1, 'Os mercadores da dúvida fabricavam controvérsia.'),
 ('Um vídeo diz: “o clima já mudou antes sem humanos, então a mudança atual é natural”. Que técnica FLICC é essa?', ['Falsos especialistas', 'Lógica falaciosa: causas naturais no passado não excluem causa humana agora', 'Conspiração', 'Expectativas impossíveis'], 1, 'Incêndios naturais existem e isso não prova que nenhum incêndio é criminoso.')],
analogia='O negacionismo funciona como um advogado que não precisa provar a inocência do cliente, só plantar dúvida razoável no júri. A ciência, porém, não é um tribunal: a pergunta não é se resta alguma dúvida, mas para onde a evidência aponta.',
crianca='Algumas pessoas não querem acreditar numa coisa que os cientistas descobriram, porque ela atrapalha os planos delas. Então espalham dúvidas. Um jeito de se proteger é conhecer os truques que elas usam.',
obj=['Distinguir negacionismo de ceticismo.', 'Reconhecer as técnicas FLICC e a estratégia dos mercadores da dúvida.', 'Explicar por que o negacionismo funciona e quais respostas têm evidência a favor.'],
caso=('Um parente diz: “os cientistas também erraram sobre a gordura na dieta, então por que confiar no que dizem sobre vacinas?”.', 'Como responder sem humilhar?', 'Reconhecer que a ciência erra e se corrige, e mostrar a diferença: a recomendação sobre gordura tinha evidência mais fraca, enquanto a segurança das vacinas aprovadas foi testada em bilhões de doses. Começar pelo fato, explicar a falácia, respeitar a pessoa.'),
erro=('“Basta mostrar os fatos para acabar com o negacionismo.”', 'Quando a crença está ligada à identidade, fatos sozinhos podem não bastar. Pré-bunking, mensageiros confiáveis e respeito funcionam melhor.'),
ferr='detector-de-pseudociencia', pre=['consenso-cientifico', 'vieses-e-metodo'],
guardar=['Negacionismo rejeita consensos por motivos não científicos; ceticismo segue a evidência.', 'FLICC: falsos especialistas, lógica falaciosa, expectativas impossíveis, escolha seletiva, conspiração.', 'Pré-bunking, verdade antes do mito e respeito funcionam melhor do que despejar fatos.'],
pensar='Que técnica FLICC você já usou, sem perceber, para defender algo de que gostava?'),

dict(slug='cientificismo-e-limites-da-ciencia', grupo='Ciência e sociedade', titulo='Cientificismo e os limites da ciência', temas=['filosofia', 'fundamentos'],
resumo='A ciência é o melhor método para conhecer o mundo natural, mas responde a tudo? O que é cientificismo, os limites internos e externos da ciência e o lugar da ética.',
corpo='''
<p class="abre">Se a ciência é tão bem-sucedida, por que não usá-la para responder a todas as perguntas? A tese de que só a ciência produz conhecimento genuíno, ou de que tudo o que vale saber pode ser resolvido por ela, tem nome: <strong>cientificismo</strong>. Há versões fortes e fracas, e muita confusão no uso da palavra.</p>
<h2>Dois sentidos de “cientificismo”</h2>
<ul><li><strong>Como posição filosófica:</strong> a ciência é a única (ou a melhor) fonte de conhecimento. Alguns filósofos naturalistas defendem versões disso, e pensadores como Alex Rosenberg assumem o rótulo.</li>
<li><strong>Como acusação:</strong> uso indevido da autoridade científica fora do seu domínio, como dizer que neurociência resolve questões morais, ou apresentar opiniões políticas como “o que a ciência diz”.</li></ul>
<h2>Limites internos</h2>
<ul><li><strong>Incerteza e falibilidade:</strong> todo conhecimento empírico é revisável (o problema da indução).</li><li><strong>Subdeterminação:</strong> às vezes os dados não decidem entre teorias.</li><li><strong>Limites práticos:</strong> sistemas caóticos, como o tempo atmosférico, são imprevisíveis no longo prazo mesmo com leis conhecidas.</li><li><strong>Limites formais:</strong> os teoremas de incompletude de Gödel mostram que sistemas matemáticos suficientemente ricos têm verdades que não podem provar.</li></ul>
<h2>Limites externos: o que a ciência não responde sozinha</h2>
<ul><li><strong>Valores e normas:</strong> a ciência diz o que acontece se fizermos X, mas não se devemos fazer X. Hume chamou isso de distância entre o “é” e o “deve”. Saber que animais sentem dor é ciência; decidir que isso nos obriga a algo é ética, embora a ética deva levar os fatos a sério.</li>
<li><strong>Pressupostos da própria ciência:</strong> que a natureza é regular, que a lógica é válida, que devemos buscar a verdade. A ciência os usa, não os prova.</li>
<li><strong>Significado e experiência:</strong> a física da luz não diz como é ver vermelho (o “problema difícil da consciência”, de David Chalmers, é tema de muito debate).</li>
<li><strong>Matemática e lógica:</strong> são conhecimento, mas não empírico.</li></ul>
<h2>Os dois erros</h2>
<p>Há dois erros simétricos. O cientificismo ingênuo trata a ciência como resposta para tudo e descarta a filosofia e a ética. O anticientificismo usa os limites da ciência para justificar crenças sem evidência em temas em que a ciência é competente (“a ciência não sabe tudo, então minha terapia pode funcionar”).</p>
<p>A posição equilibrada: a ciência é o método mais confiável para questões sobre o mundo natural, e onde ela é competente, sua palavra deve pesar muito. Em questões de valor, ela informa, mas não decide sozinha. E a filosofia ajuda a traçar onde está cada fronteira.</p>
<div class="nota"><strong>Ponte para a ética:</strong> boa parte dos debates públicos mistura fatos (que a ciência pode esclarecer) e valores (que a ética discute). O <a href="https://eticaparainiciantes.biblioverse.org/" target="_blank" rel="noopener">Ética Para Iniciantes</a> trata da outra metade.</div>''',
fontes=[('Scientism (Internet Encyclopedia of Philosophy)', IEP + 'scientism/'), ('Is-ought problem (Wikipédia)', WE + 'Is%E2%80%93ought_problem'), ('Gödel\'s Incompleteness Theorems (Stanford Encyclopedia)', SEP + 'goedel-incompleteness/'), ('Science Unlimited? The Challenges of Scientism', 'https://www.google.com/search?tbm=bks&q=Science+Unlimited+The+Challenges+of+Scientism')],
quiz=[('O que é cientificismo como posição filosófica?', ['Gostar de ciência', 'A tese de que a ciência é a única ou a melhor fonte de conhecimento genuíno', 'Rejeitar a ciência', 'Fazer experimentos'], 1, 'É uma tese sobre o alcance do conhecimento científico.'),
 ('Qual é um limite externo da ciência, segundo a lição?', ['Não conseguir medir temperatura', 'Não decidir sozinha questões de valor: o que acontece é diferente do que devemos fazer', 'Não ter teorias', 'Não usar matemática'], 1, 'A distância entre “é” e “deve” marca o limite com a ética.'),
 ('Alguém diz: “a ciência não explica a consciência, então minha terapia de energia pode curar câncer”. Que erro é esse?', ['Cientificismo ingênuo', 'Anticientificismo: usar um limite da ciência para defender crença sem evidência num tema em que a ciência é competente', 'Realismo estrutural', 'Nenhum'], 1, 'Testar se uma terapia cura câncer está bem dentro do alcance da ciência.')],
analogia='A ciência é como uma lanterna muito potente. Ela ilumina melhor do que qualquer outra o que está no caminho; mas não diz para onde você quer ir. E apontar para o escuro e dizer “a lanterna não alcança lá, então ali tem um dragão” também não vale.',
crianca='A ciência é ótima para descobrir como as coisas funcionam, como o corpo e as estrelas. Mas para decidir o que é justo, ou o que é certo fazer, a gente precisa também pensar em outras coisas, como os sentimentos e a vida dos outros.',
obj=['Distinguir os dois sentidos de cientificismo.', 'Identificar limites internos e externos da ciência.', 'Evitar os dois erros: cientificismo ingênuo e anticientificismo.'],
caso=('Num debate sobre consumo de carne, alguém diz: “a ciência mostra que humanos são onívoros, então comer carne é certo”.', 'O que está misturado nessa frase?', 'Um fato (anatomia e história alimentar) e uma conclusão de valor (é certo). Do fato não se segue a norma; a ética precisa considerar outros fatos, como a senciência dos animais, e argumentos morais.'),
erro=('“Se a ciência não responde a algo, qualquer resposta vale.”', 'Os limites da ciência não abrem espaço para crenças sem evidência em temas que ela pode testar. E nas questões de valor, há também argumentos melhores e piores.'),
ferr=None, pre=['ciencia-religiao-e-filosofia', 'naturalismo-epistemologico'],
guardar=['Cientificismo: tese de que só a ciência conhece, ou uso indevido da autoridade científica.', 'Limites internos (falibilidade, caos, Gödel) e externos (valores, pressupostos, consciência).', 'Evite os dois erros: ciência para tudo e “a ciência não sabe tudo, então qualquer coisa vale”.'],
pensar='Qual debate público você vê sendo apresentado como “questão científica” quando, no fundo, é sobre valores?'),
]
