"""Lições do nível Intermediário (mesmo formato do Iniciante)."""
SEP = 'https://plato.stanford.edu/entries/'
IEP = 'https://iep.utm.edu/'
WP = 'https://pt.wikipedia.org/wiki/'
WE = 'https://en.wikipedia.org/wiki/'

INTERMEDIARIO = [
dict(slug='o-que-e-epistemologia', grupo='Epistemologia', titulo='O que é epistemologia?', temas=['epistemologia', 'fundamentos'],
resumo='Epistemologia é a área da filosofia que estuda o conhecimento: o que é saber, de onde vem, como se justifica e quais são seus limites.',
corpo='''
<p class="abre">Epistemologia (do grego <em>episteme</em>, conhecimento, e <em>logos</em>, estudo) é a área da filosofia que pergunta o que é conhecer. Ela não pergunta se a água ferve a 100 °C, e sim o que nos dá o direito de dizer que sabemos disso.</p>
<h2>As grandes perguntas</h2>
<ul><li><strong>O que é conhecimento?</strong> É crença verdadeira justificada, ou falta algo? (Veja o problema de Gettier.)</li>
<li><strong>De onde vem?</strong> Da experiência dos sentidos (empirismo), da razão (racionalismo) ou de uma combinação?</li>
<li><strong>Como uma crença se justifica?</strong> Apoiada em crenças básicas (fundacionalismo), na coerência com outras (coerentismo) ou na confiabilidade do processo que a produziu (confiabilismo)?</li>
<li><strong>Quais os limites?</strong> Podemos saber alguma coisa com certeza? O cético diz que não, ou pelo menos desafia quem diz que sim.</li>
<li><strong>Como devemos formar crenças?</strong> Há deveres epistêmicos, como o de não acreditar sem evidência suficiente?</li></ul>
<h2>Epistemologia e filosofia da ciência</h2>
<p>As duas são vizinhas. A epistemologia trata do conhecimento em geral, inclusive o do dia a dia: saber onde deixei a chave, saber que dois mais dois são quatro. A <strong>filosofia da ciência</strong> trata do conhecimento científico em particular: o que distingue ciência de não ciência, como teorias são testadas, o que é uma explicação, se as teorias descrevem a realidade.</p>
<p>No Brasil e na França, “epistemologia” às vezes é usada como sinônimo de filosofia da ciência, por influência de autores como Gaston Bachelard. No mundo anglófono, <em>epistemology</em> é a teoria geral do conhecimento. Este site usa a palavra no sentido mais amplo e trata a filosofia da ciência como uma parte dela.</p>
<h2>Ramos recentes</h2>
<ul><li><strong>Epistemologia social:</strong> como sabemos coisas por meio dos outros (testemunho, especialistas, instituições, redes sociais).</li>
<li><strong>Epistemologia formal:</strong> usa probabilidade e lógica para modelar graus de crença e como atualizá-los (bayesianismo).</li>
<li><strong>Epistemologia das virtudes:</strong> foca nas qualidades de quem conhece, como honestidade intelectual, humildade e curiosidade.</li>
<li><strong>Epistemologia naturalizada:</strong> propõe estudar o conhecimento com os métodos da própria ciência, como a psicologia cognitiva.</li></ul>
<div class="nota"><strong>Por que importa fora da academia:</strong> desinformação, bolhas de opinião e confiança em especialistas são problemas epistemológicos. Saber como a justificação funciona ajuda a decidir em quem acreditar.</div>''',
fontes=[('Epistemology (Stanford Encyclopedia of Philosophy)', SEP + 'epistemology/'), ('Epistemology (Internet Encyclopedia of Philosophy)', IEP + 'epistemo/'), ('Epistemologia (Wikipédia)', WP + 'Epistemologia')],
quiz=[('O que a epistemologia estuda?', ['A origem do universo', 'O conhecimento: o que é, de onde vem, como se justifica e seus limites', 'Apenas a lógica formal', 'A história das ciências naturais'], 1, 'Epistemologia é a teoria do conhecimento.'),
 ('Qual a relação entre epistemologia e filosofia da ciência?', ['São opostas', 'A filosofia da ciência trata do conhecimento científico em particular; a epistemologia, do conhecimento em geral', 'A filosofia da ciência é mais ampla', 'Não há relação'], 1, 'São vizinhas: uma geral, a outra focada na ciência.'),
 ('Um pesquisador estuda como as pessoas decidem em quais especialistas confiar nas redes sociais. Que ramo é esse?', ['Epistemologia formal', 'Epistemologia social', 'Metafísica', 'Lógica modal'], 1, 'Conhecimento obtido por meio dos outros é o objeto da epistemologia social.')],
analogia='Se a ciência é uma fábrica de conhecimento, a epistemologia é o setor de controle de qualidade. Ela não fabrica os produtos, mas pergunta o que torna um produto bom, como testá-lo e quando uma peça deve ser recolhida.',
crianca='Todo mundo sabe muitas coisas. A epistemologia é a parte da filosofia que pergunta: como você sabe que sabe? Foi porque viu, porque alguém te contou ou porque pensou bastante?',
obj=['Definir epistemologia e suas grandes perguntas.', 'Distinguir epistemologia de filosofia da ciência.', 'Reconhecer ramos recentes, como a epistemologia social e a formal.'],
caso=('Você acredita que a Antártida existe, embora nunca tenha ido lá.', 'O que justifica essa crença?', 'Testemunho: fotos, mapas, relatos de muitas fontes independentes. A epistemologia estuda por que esse tipo de justificação funciona e quando falha.'),
erro=('“Epistemologia é só um nome chique para metodologia científica.”', 'Ela é mais ampla: trata de todo conhecimento, inclusive o cotidiano, o matemático e o obtido por testemunho, e pergunta o que é conhecer, não só como pesquisar.'),
ferr='opiniao-crenca-ou-conhecimento', pre=['crenca-verdadeira-justificada'],
guardar=['Epistemologia é a teoria do conhecimento: o que é, de onde vem, como se justifica, até onde vai.', 'A filosofia da ciência é a parte dela que trata do conhecimento científico.', 'Desinformação e confiança em especialistas são problemas epistemológicos práticos.'],
pensar='Quanto do que você sabe veio de testemunho? Como você decide em que fontes confiar?'),

dict(slug='empirismo-e-racionalismo', grupo='Epistemologia', titulo='Empirismo e racionalismo', temas=['epistemologia', 'filosofia'],
resumo='O conhecimento vem dos sentidos ou da razão? A disputa entre Locke e Hume de um lado, Descartes e Leibniz do outro, e a síntese de Kant.',
corpo='''
<p class="abre">No século XVII, a filosofia se dividiu em torno de uma pergunta: de onde vem o conhecimento? Para os <strong>racionalistas</strong>, a razão pode descobrir verdades sobre o mundo sem depender da experiência. Para os <strong>empiristas</strong>, todo conhecimento sobre o mundo começa nos sentidos.</p>
<h2>Racionalismo</h2>
<p>René Descartes procurava uma base indubitável para o conhecimento. Duvidou de tudo o que podia: dos sentidos, que às vezes enganam, e até de estar acordado. Restou uma certeza: se estou duvidando, estou pensando, e se penso, existo (<em>cogito, ergo sum</em>). A partir daí, pela razão, tentou reconstruir o resto.</p>
<p>Racionalistas como Descartes, Spinoza e Leibniz apontavam a matemática como modelo: sabemos que a soma dos ângulos de um triângulo euclidiano é 180° sem medir triângulos. Defendiam também <strong>ideias inatas</strong>, presentes na mente antes da experiência.</p>
<h2>Empirismo</h2>
<p>John Locke respondeu que a mente nasce como uma “folha em branco” (<em>tabula rasa</em>) e que todas as ideias vêm da experiência. George Berkeley e David Hume levaram o empirismo adiante. Hume distinguiu:</p>
<ul><li><strong>Relações de ideias:</strong> verdades da matemática e da lógica, conhecidas pela razão, mas que não dizem nada sobre o mundo.</li><li><strong>Questões de fato:</strong> tudo o que é sobre o mundo, conhecido só pela experiência.</li></ul>
<p>O empirismo levou Hume a uma conclusão incômoda: não temos justificação racional para a indução, isto é, para esperar que o futuro se pareça com o passado. É o tema da próxima lição.</p>
<h2>A síntese de Kant</h2>
<p>Immanuel Kant tentou unir as duas tradições: “pensamentos sem conteúdo são vazios; intuições sem conceitos são cegas”. Para ele, o conhecimento começa com a experiência, mas não deriva todo dela: a mente organiza o que recebe por estruturas próprias, como espaço, tempo e causalidade. Kant chamou de <strong>sintético a priori</strong> o conhecimento que diz algo sobre o mundo e, ainda assim, não vem da experiência, como (segundo ele) a geometria e o princípio de que todo evento tem causa.</p>
<h2>E a ciência?</h2>
<p>A ciência moderna é filha das duas tradições. Do empirismo herdou a exigência de testar ideias contra observações; do racionalismo, o uso da matemática e da dedução para construir teorias. Galileu dizia que o livro da natureza está escrito em linguagem matemática, e ao mesmo tempo apontava o telescópio para o céu.</p>
<div class="nota"><strong>Debate vivo:</strong> a geometria não euclidiana e a relatividade abalaram a tese de Kant de que a geometria euclidiana é necessária. E a ciência cognitiva reabriu a questão das ideias inatas: bebês parecem nascer com expectativas sobre objetos e números.</div>''',
fontes=[('Rationalism vs. Empiricism (Stanford Encyclopedia of Philosophy)', SEP + 'rationalism-empiricism/'), ('David Hume (Stanford Encyclopedia of Philosophy)', SEP + 'hume/'), ('Kant\'s Critique of Pure Reason (Stanford Encyclopedia)', SEP + 'kant-metaphysics/')],
quiz=[('O que defende o empirismo?', ['O conhecimento sobre o mundo vem da razão pura', 'Todo conhecimento sobre o mundo começa na experiência dos sentidos', 'Nada pode ser conhecido', 'A fé é a fonte do conhecimento'], 1, 'Para empiristas como Locke e Hume, a experiência é a fonte do conhecimento sobre o mundo.'),
 ('Que exemplo os racionalistas usavam como modelo de conhecimento pela razão?', ['A astrologia', 'A matemática', 'A culinária', 'A história'], 1, 'Verdades matemáticas parecem conhecidas sem medir nada.'),
 ('Um estudo mostra que bebês de poucos meses se surpreendem quando um objeto atravessa uma parede. Isso alimenta qual debate?', ['Se há algo inato na mente, como defendiam os racionalistas', 'Se bebês gostam de mágica', 'Se o positivismo está certo', 'Nenhum'], 0, 'Expectativas presentes antes de muita experiência reabrem a questão das ideias inatas.')],
analogia='O racionalista acha que a mente já vem com um mapa desenhado a lápis, que a experiência só confirma. O empirista acha que ela vem com uma folha em branco. Kant achou que ela vem com uma grade quadriculada: sem a grade não dá para desenhar, mas o desenho vem de fora.',
crianca='Algumas pessoas acham que a gente aprende tudo olhando, ouvindo e tocando. Outras acham que a cabeça já nasce sabendo algumas coisas, como contar. Os cientistas usam as duas coisas: observam o mundo e pensam muito.',
obj=['Explicar a diferença entre racionalismo e empirismo.', 'Descrever a distinção de Hume entre relações de ideias e questões de fato.', 'Resumir a síntese de Kant e o que a ciência herdou de cada tradição.'],
caso=('Você sabe que, se todos os gatos são mamíferos e Mingau é gato, Mingau é mamífero. E sabe que Mingau é laranja.', 'Esses dois conhecimentos vêm do mesmo lugar?', 'Não. O primeiro é lógico: vem da razão e vale sem olhar o mundo. O segundo é uma questão de fato: só a experiência diz a cor de Mingau.'),
erro=('“Empiristas desprezam a razão e racionalistas desprezam a experiência.”', 'Ambos usam as duas. A disputa é sobre qual é a fonte última do conhecimento sobre o mundo.'),
ferr='que-corrente-e-essa', pre=['o-que-e-epistemologia'],
guardar=['Racionalistas: a razão descobre verdades sobre o mundo; empiristas: tudo começa nos sentidos.', 'Hume separou relações de ideias (lógica, matemática) de questões de fato (experiência).', 'A ciência moderna combina as duas: teste empírico e construção matemática.'],
pensar='Há algo que você acha que sabe “de nascença”, sem ter aprendido? Como testaria isso?'),

dict(slug='o-problema-da-inducao', grupo='Epistemologia', titulo='O problema da indução', temas=['epistemologia', 'filosofia'],
resumo='Por que esperar que o Sol nasça amanhã? Hume mostrou que não há justificação lógica para generalizar do passado para o futuro. A ciência vive com isso.',
corpo='''
<p class="abre">Você já viu o Sol nascer milhares de vezes e espera que ele nasça amanhã. Mas que razão você tem para isso? Que ele sempre nasceu. E por que o passado garantiria o futuro? Essa pergunta, feita por David Hume no século XVIII, é o <strong>problema da indução</strong>, e até hoje ninguém o resolveu de forma que todos aceitem.</p>
<h2>Dedução e indução</h2>
<ul><li><strong>Dedução:</strong> se as premissas são verdadeiras, a conclusão é necessariamente verdadeira. “Todo humano é mortal; Sócrates é humano; logo, Sócrates é mortal.”</li>
<li><strong>Indução:</strong> as premissas tornam a conclusão provável, mas não garantem. “Todo cisne que vi é branco; logo, todo cisne é branco.” Os europeus pensavam assim até encontrarem cisnes negros na Austrália.</li></ul>
<p>A ciência depende da indução: leis científicas são generalizações a partir de casos observados. Se a indução não tem justificação, que base tem a ciência?</p>
<h2>O argumento de Hume</h2>
<p>Para justificar a indução, precisaríamos de um princípio como “a natureza é uniforme: o futuro se parece com o passado”. Mas como sabemos isso? Não por dedução: não há contradição em imaginar que amanhã a água deixe de matar a sede. Só por experiência: a natureza tem sido uniforme. Mas isso é usar a indução para justificar a indução, um raciocínio circular.</p>
<p>A conclusão de Hume é que nossa confiança na indução é um <strong>hábito</strong> psicológico, não uma conclusão racional. Ele não sugeria abandoná-la: na vida prática, ninguém consegue.</p>
<h2>O peru indutivista</h2>
<p>Bertrand Russell contou a história de uma galinha (a versão popular fala de um peru) que, todo dia, recebia comida às 9h. Depois de meses de observação cuidadosa, em dias de sol e de chuva, concluiu: “sempre sou alimentado às 9h”. Na véspera do Natal, às 9h, foi levado para a ceia.</p>
<h2>Respostas ao problema</h2>
<ul><li><strong>Popper:</strong> a ciência não usa indução. Ela propõe hipóteses e tenta refutá-las, e a refutação é dedutiva. (Críticos dizem que a indução volta pela porta dos fundos quando confiamos em teorias bem testadas.)</li>
<li><strong>Bayesianismo:</strong> não se trata de provar generalizações, mas de atualizar graus de crença com base na evidência, segundo regras da probabilidade.</li>
<li><strong>Pragmatismo (Reichenbach):</strong> se algum método funciona para prever, a indução também funciona; então é a melhor aposta, mesmo sem garantia.</li>
<li><strong>Naturalismo:</strong> a indução é confiável porque fomos moldados pela evolução num mundo com regularidades; a pergunta “por quê” é respondida pela própria ciência.</li></ul>
<h2>O novo enigma da indução</h2>
<p>Em 1955, Nelson Goodman mostrou um problema ainda mais estranho. Defina “verdul” como “verde se observado antes de 2030, azul depois”. Todas as esmeraldas observadas são verdes e também “verdulas”. Por que projetar “verde” e não “verdul”? A indução depende de escolher os conceitos certos, e não está claro o que os torna certos.</p>
<div class="nota"><strong>Na prática:</strong> o problema não torna a ciência irracional. Mostra que o conhecimento científico é falível: sempre pode haver um cisne negro. Por isso a ciência fala em graus de confiança, não em certezas.</div>''',
fontes=[('The Problem of Induction (Stanford Encyclopedia of Philosophy)', SEP + 'induction-problem/'), ('Problema da indução (Wikipédia)', WP + 'Problema_da_indu%C3%A7%C3%A3o'), ('New riddle of induction (Wikipédia)', WE + 'New_riddle_of_induction')],
quiz=[('Qual a diferença entre dedução e indução?', ['Não há diferença', 'Na dedução, premissas verdadeiras garantem a conclusão; na indução, só a tornam provável', 'A indução é sempre mais segura', 'A dedução vai do particular ao geral'], 1, 'A dedução preserva a verdade; a indução amplia o conhecimento com risco.'),
 ('Por que, segundo Hume, não podemos justificar a indução pela experiência?', ['Porque a experiência é sempre falsa', 'Porque seria circular: usaríamos a indução para justificar a indução', 'Porque Deus não permite', 'Porque a matemática proíbe'], 1, 'Justificar a uniformidade da natureza pela experiência passada já supõe a indução.'),
 ('Um investidor diz: “essa ação subiu todos os meses dos últimos três anos, então vai continuar subindo”. Que lição se aplica?', ['O problema da indução: a regularidade passada não garante a futura', 'O falsificacionismo prova que ela vai cair', 'O empirismo garante que vai subir', 'Nenhuma'], 0, 'É o peru indutivista: a série passada não traz garantia lógica sobre o futuro.')],
analogia='A indução é como atravessar uma ponte que você nunca viu cair. Você confia nela porque aguentou até agora, e na prática é a melhor aposta. Mas a experiência passada não é uma garantia: é só um bom motivo para apostar.',
crianca='Se todo dia o seu cachorro late quando a campainha toca, você acha que amanhã ele vai latir de novo. Mas não tem como ter certeza absoluta: é só um palpite muito bom, porque sempre foi assim.',
obj=['Distinguir dedução de indução.', 'Reconstruir o argumento de Hume sobre a circularidade da justificação da indução.', 'Comparar respostas ao problema: Popper, bayesianismo, pragmatismo e naturalismo.'],
caso=('Um cientista testou um remédio em 5 mil pessoas e ele foi seguro em todas.', 'Isso garante que será seguro na pessoa número 5.001?', 'Não garante, por causa do problema da indução, mas torna muito provável. Por isso medicamentos continuam sendo monitorados depois de aprovados (farmacovigilância).'),
erro=('“O problema da indução mostra que a ciência não tem valor.”', 'Mostra que o conhecimento científico é falível, não que é inútil. Nenhuma alternativa prevê melhor, e a ciência já trabalha com graus de confiança.'),
ferr='que-corrente-e-essa', pre=['empirismo-e-racionalismo'],
guardar=['Indução generaliza a partir de casos; nunca garante a conclusão.', 'Hume: justificar a indução pela experiência é circular.', 'Popper, bayesianos e pragmatistas dão respostas diferentes; todas aceitam que a ciência é falível.'],
pensar='Qual crença sua é um “peru indutivista”, baseada só em que sempre foi assim?'),

dict(slug='como-justificar-uma-crenca', grupo='Epistemologia', titulo='Como justificar uma crença', temas=['epistemologia'],
resumo='Fundacionalismo, coerentismo e confiabilismo: três respostas para o que dá apoio às nossas crenças, e o desafio do cético.',
corpo='''
<p class="abre">Se perguntarem por que você acredita em algo, você dá uma razão. E se perguntarem o que justifica essa razão? E a seguinte? Essa cadeia de “por quês” é o <strong>problema do regresso</strong>, e as principais teorias da justificação são respostas a ele.</p>
<h2>As saídas possíveis</h2>
<p>A cadeia de razões pode (1) terminar em crenças que não precisam de outras, (2) dar voltas e se apoiar mutuamente, (3) seguir ao infinito ou (4) parar em algo que não é razão nenhuma. O trilema de Agripa, um cético antigo, dizia que todas as opções são ruins.</p>
<h2>Fundacionalismo</h2>
<p>Algumas crenças são <strong>básicas</strong>: justificadas por si mesmas, sem depender de outras. As demais se apoiam nelas, como um prédio sobre a fundação. Para Descartes, as básicas eram verdades indubitáveis, como “eu penso”. Para empiristas, eram as experiências dos sentidos, como “vejo uma mancha vermelha”.</p>
<p><em>Crítica:</em> o que torna uma crença básica? Se for algo, então ela depende desse algo; se não for nada, a escolha parece arbitrária.</p>
<h2>Coerentismo</h2>
<p>Não há fundação. Uma crença é justificada quando se encaixa num sistema coerente de crenças que se apoiam mutuamente, como os fios de uma teia ou um barco que se conserta em alto-mar, tábua por tábua (a imagem é de Otto Neurath).</p>
<p><em>Crítica:</em> um romance bem escrito também é coerente. Como a coerência se liga ao mundo real?</p>
<h2>Confiabilismo</h2>
<p>Alvin Goldman propôs mudar o foco: uma crença está justificada se foi produzida por um <strong>processo confiável</strong>, isto é, que tende a gerar crenças verdadeiras, como a visão em boas condições ou um termômetro calibrado. Não é preciso que a pessoa saiba que o processo é confiável.</p>
<p><em>Crítica:</em> e se alguém tem um processo confiável mas nenhuma razão para confiar nele, ou um processo não confiável sem ter como saber? Essa disputa entre <strong>internalistas</strong> (a justificação precisa ser acessível à pessoa) e <strong>externalistas</strong> (não precisa) segue viva.</p>
<h2>A ciência como modelo misto</h2>
<p>A filósofa Susan Haack propôs o <strong>fundherentismo</strong>, comparando a justificação a palavras cruzadas: cada resposta é apoiada pela pista (a experiência, como no fundacionalismo) e pelo encaixe com as outras respostas (a coerência). A ciência real parece funcionar assim: observações ancoram as teorias, e teorias ajudam a interpretar observações.</p>
<div class="nota"><strong>E o cético?</strong> O ceticismo radical pergunta como você sabe que não está sonhando ou numa simulação. A maioria dos epistemólogos acha que não precisamos refutar o cético para ter conhecimento no sentido comum, e que exigir certeza absoluta é pôr a barra alta demais.</div>''',
fontes=[('Foundationalist Theories of Epistemic Justification (Stanford Encyclopedia)', SEP + 'justep-foundational/'), ('Coherentist Theories of Epistemic Justification (Stanford Encyclopedia)', SEP + 'justep-coherence/'), ('Reliabilism (Internet Encyclopedia of Philosophy)', IEP + 'reliabil/'), ('Evidence and Inquiry', 'https://www.google.com/search?tbm=bks&q=Evidence+and+Inquiry+Haack')],
quiz=[('O que defende o fundacionalismo?', ['Que crenças se apoiam mutuamente numa teia', 'Que algumas crenças básicas sustentam as demais', 'Que nada pode ser justificado', 'Que só a confiabilidade importa'], 1, 'Fundacionalismo: crenças básicas como alicerce do edifício.'),
 ('Qual a principal crítica ao coerentismo?', ['É circular demais para a lógica', 'Um sistema pode ser coerente e totalmente desligado da realidade, como um romance', 'Exige certeza absoluta', 'Ignora a coerência'], 1, 'Coerência sozinha não garante contato com o mundo.'),
 ('Uma pessoa acredita na hora certa porque olhou um relógio que funciona bem, sem saber nada sobre relógios. Para o confiabilismo, a crença:', ['Não é justificada, pois ela não sabe por que o relógio funciona', 'É justificada, porque foi produzida por um processo confiável', 'É coerente, mas falsa', 'É básica'], 1, 'Para o confiabilismo, basta que o processo tenda a produzir crenças verdadeiras.')],
analogia='Fundacionalismo é um prédio: andares sobre uma fundação. Coerentismo é uma teia de aranha: cada fio é sustentado pelos outros. Confiabilismo é uma fábrica: o que importa é se a máquina costuma produzir peças boas. As palavras cruzadas de Haack misturam pista e encaixe.',
crianca='Quando alguém pergunta “por quê?”, você dá um motivo. Aí a pessoa pergunta “e por quê?” de novo, e de novo. Os filósofos discutem onde essa brincadeira de porquês pode parar.',
obj=['Explicar o problema do regresso da justificação.', 'Comparar fundacionalismo, coerentismo e confiabilismo, com uma crítica a cada um.', 'Descrever o fundherentismo de Haack como modelo para a ciência.'],
caso=('Um detetive tem várias pistas fracas que, juntas, apontam para o mesmo suspeito, e uma impressão digital.', 'O que justifica a conclusão: a pista mais forte ou o encaixe de todas?', 'As duas coisas. A impressão digital ancora (como uma crença básica) e as pistas que se encaixam reforçam (coerência). É o modelo das palavras cruzadas.'),
erro=('“Se não dá para justificar até o fim, nenhuma crença é justificada.”', 'Isso supõe que justificação exige certeza. As teorias da justificação mostram como crenças podem ser bem apoiadas sem ser infalíveis.'),
ferr='que-corrente-e-essa', pre=['o-que-e-epistemologia'],
guardar=['O regresso dos “por quês” precisa terminar em algum lugar, ou dar voltas.', 'Fundacionalismo: base; coerentismo: teia; confiabilismo: processo que costuma acertar.', 'A ciência combina âncoras na observação com coerência entre teorias.'],
pensar='Pense numa crença importante sua. Ela se apoia mais em uma base firme ou no encaixe com outras crenças?'),

dict(slug='o-problema-de-gettier', grupo='Epistemologia', titulo='O problema de Gettier', temas=['epistemologia'],
resumo='Em três páginas, Edmund Gettier mostrou que crença verdadeira e justificada pode não ser conhecimento. As tentativas de consertar a definição.',
corpo='''
<p class="abre">Em 1963, Edmund Gettier publicou um artigo de três páginas chamado “Crença verdadeira justificada é conhecimento?”. A resposta era não, e o artigo virou um dos mais citados da filosofia do século XX.</p>
<h2>Um caso de Gettier</h2>
<p>Smith e Jones concorrem a uma vaga. Smith tem boas razões para acreditar que Jones vai ser contratado (o chefe disse) e que Jones tem dez moedas no bolso (ele contou). Smith conclui: “quem vai ser contratado tem dez moedas no bolso”. No fim, quem é contratado é o próprio Smith, que, sem saber, também tinha dez moedas no bolso.</p>
<p>A crença de Smith era <strong>verdadeira</strong> (o contratado tinha dez moedas), <strong>justificada</strong> (ele tinha boas razões) e ele <strong>acreditava</strong> nela. Mas parece absurdo dizer que ele <em>sabia</em>. Ele acertou por sorte.</p>
<h2>Outros exemplos</h2>
<ul><li><strong>O relógio parado</strong> (de Russell): você olha um relógio que parou ontem exatamente às 14h, e por acaso são 14h.</li>
<li><strong>Os celeiros falsos</strong> (de Goldman): numa região cheia de fachadas falsas de celeiros, você olha para o único celeiro verdadeiro e pensa “isso é um celeiro”. Acertou, mas poderia facilmente ter errado.</li>
<li><strong>A ovelha no campo</strong> (de Chisholm): você vê um cachorro com cara de ovelha e conclui “há uma ovelha no campo”. Há mesmo, escondida atrás de uma pedra.</li></ul>
<h2>Tentativas de conserto</h2>
<ul><li><strong>Sem falsas premissas:</strong> conhecimento exige não ter raciocinado a partir de algo falso. (Mas no caso dos celeiros não há premissa falsa.)</li>
<li><strong>Derrotabilidade:</strong> não pode haver uma verdade que, se você a soubesse, derrubaria sua justificação.</li>
<li><strong>Sensibilidade (Nozick):</strong> se a crença fosse falsa, você não acreditaria nela.</li>
<li><strong>Segurança (Sosa, Williamson):</strong> a crença não poderia facilmente ter sido falsa.</li>
<li><strong>Virtudes (Sosa, Zagzebski):</strong> conhecimento é acertar <em>por causa</em> da competência, não apesar dela.</li>
<li><strong>Conhecimento primeiro (Williamson):</strong> talvez conhecimento não se analise em partes; ele seria o conceito básico.</li></ul>
<h2>Por que isso importa para a ciência</h2>
<p>A ciência quer mais do que acertar: quer acertar <strong>pelas razões certas</strong>. Um modelo que prevê bem os dados por um mecanismo errado é um caso de Gettier em grande escala. A astronomia de Ptolomeu previa eclipses com boa precisão usando um universo com a Terra no centro. Previsão certa não garante explicação certa.</p>
<div class="nota"><strong>Curiosidade:</strong> pesquisas de filosofia experimental indicam que pessoas de culturas muito diferentes tendem a negar conhecimento nos casos de Gettier, o que sugere uma intuição bastante compartilhada.</div>''',
fontes=[('Is Justified True Belief Knowledge?', 'https://www.jstor.org/stable/3326922'), ('The Analysis of Knowledge (Stanford Encyclopedia of Philosophy)', SEP + 'knowledge-analysis/'), ('Gettier Problems (Internet Encyclopedia of Philosophy)', IEP + 'gettier/')],
quiz=[('O que Gettier mostrou?', ['Que o conhecimento é impossível', 'Que uma crença pode ser verdadeira e justificada e ainda assim não ser conhecimento', 'Que a justificação é desnecessária', 'Que Platão estava certo'], 1, 'Os casos de Gettier têm as três condições e ainda parecem acerto por sorte.'),
 ('O que a condição de “segurança” exige?', ['Que a crença seja dita com segurança', 'Que a crença não pudesse facilmente ter sido falsa', 'Que haja uma prova matemática', 'Que muitos concordem'], 1, 'Conhecimento seguro não depende de sorte: em situações parecidas, você ainda acertaria.'),
 ('Um modelo econômico acertou a inflação do ano por um mecanismo que depois se mostrou errado. Isso lembra:', ['Um caso de Gettier: acerto sem as razões certas', 'O problema da indução', 'O efeito placebo', 'A revisão por pares'], 0, 'Previsão certa por razão errada é o padrão dos casos de Gettier.')],
analogia='É como acertar o gol depois de chutar mal: a bola bate na canela do zagueiro e entra. O gol vale no placar, mas ninguém diz que o atacante sabia fazer aquele gol. Conhecimento é o gol de quem chutou certo.',
crianca='Imagine que você diz que tem bolo na geladeira porque viu um bolo ontem. Mas alguém comeu aquele bolo e, sem você saber, sua mãe colocou outro. Você acertou, mas foi por sorte. Os filósofos perguntam: você sabia?',
obj=['Reconstruir um caso de Gettier e explicar por que ele desafia a definição clássica.', 'Citar propostas de conserto: sensibilidade, segurança e virtudes.', 'Relacionar o problema à diferença entre prever e explicar na ciência.'],
caso=('Você vê no painel do aeroporto “voo no horário”. O painel está travado desde ontem, mas, por acaso, o voo está mesmo no horário.', 'Você sabia que o voo estava no horário?', 'É um caso de Gettier: crença verdadeira e justificada (painéis costumam funcionar), mas o acerto foi sorte. A maioria das pessoas diz que você não sabia.'),
erro=('“Gettier é um jogo de palavras sem importância.”', 'O caso aponta algo central: conhecimento exige acertar pelas razões certas, e isso importa na ciência, onde previsões corretas podem vir de modelos errados.'),
ferr=None, pre=['crenca-verdadeira-justificada', 'como-justificar-uma-crenca'],
guardar=['Crença verdadeira justificada pode ser acerto por sorte.', 'Propostas de conserto: sem premissas falsas, sensibilidade, segurança, virtudes.', 'Na ciência, prever certo não basta: é preciso explicar pelas razões certas.'],
pensar='Você já acertou algo importante pelas razões erradas? Como saberia a diferença?'),

dict(slug='positivismo', grupo='Filosofia da ciência clássica', titulo='Positivismo: de Comte ao Círculo de Viena', temas=['filosofia'],
resumo='O positivismo de Comte, que marcou a bandeira do Brasil, e o positivismo lógico do Círculo de Viena: o critério da verificação e por que ele ruiu.',
corpo='''
<p class="abre">“Ordem e Progresso”, na bandeira brasileira, é um lema positivista. A palavra “positivismo” nomeia duas correntes diferentes: a de Auguste Comte, no século XIX, e o positivismo lógico do Círculo de Viena, no século XX. As duas têm em comum a confiança na ciência como modelo de conhecimento.</p>
<h2>O positivismo de Comte</h2>
<p>Auguste Comte (1798–1857) propôs a <strong>lei dos três estados</strong>: o pensamento humano passaria do estado teológico (explicar o mundo por deuses), ao metafísico (por forças abstratas, como “essências”) e, por fim, ao positivo (por leis descobertas pela observação). “Positivo” aqui quer dizer o que é dado, observável, real.</p>
<p>Comte organizou as ciências numa hierarquia (matemática, astronomia, física, química, biologia e, no topo, a sociologia, palavra que ele criou) e defendeu que a sociedade fosse reorganizada pela ciência. No fim da vida, fundou uma “Religião da Humanidade”, com templos e calendário próprios. Um desses templos ainda existe no Rio de Janeiro.</p>
<p>No Brasil, o positivismo influenciou militares e republicanos como Benjamin Constant e Miguel Lemos, e daí veio o lema da bandeira, adaptado de “o amor por princípio, a ordem por base, o progresso por fim”.</p>
<h2>O positivismo lógico</h2>
<p>Nos anos 1920, filósofos e cientistas reunidos em Viena (Moritz Schlick, Rudolf Carnap, Otto Neurath, entre outros) e em Berlim (Hans Reichenbach) criaram o <strong>positivismo lógico</strong>, ou empirismo lógico. Inspirados pela lógica moderna e pela física de Einstein, queriam livrar a filosofia da metafísica.</p>
<p>A ferramenta era o <strong>critério de verificabilidade</strong>: uma frase só tem significado se for verificável pela experiência ou verdadeira por definição (como as da lógica e da matemática). “A água ferve a 100 °C” tem sentido. “O Absoluto se desdobra na história” não tem: não é falsa, é sem sentido.</p>
<h2>Por que ruiu</h2>
<ul><li><strong>O critério não passa no próprio teste:</strong> “só é significativo o que é verificável” não é verificável pela experiência nem verdadeiro por definição.</li>
<li><strong>Leis universais não são verificáveis:</strong> “todo metal se dilata com o calor” nunca pode ser verificada por completo, pois fala de infinitos casos.</li>
<li><strong>Quine</strong> atacou a distinção entre verdades por definição e verdades de fato, e mostrou que frases não são testadas uma a uma, mas em conjunto (holismo).</li>
<li><strong>Popper</strong> propôs a falseabilidade como critério de demarcação, não de significado.</li></ul>
<h2>O legado</h2>
<p>O positivismo lógico, apesar de abandonado como programa, criou a filosofia da ciência moderna: a ênfase na clareza, na lógica, na estrutura das teorias e na relação entre teoria e observação. Muitos de seus membros eram progressistas e fugiram do nazismo, levando essas ideias para os Estados Unidos.</p>
<div class="nota"><strong>Cuidado com o uso popular:</strong> hoje “positivista” às vezes vira xingamento para qualquer pessoa que confia em dados. Isso é uma caricatura: defender evidências não é aderir ao critério de verificabilidade nem à Religião da Humanidade.</div>''',
fontes=[('Auguste Comte (Stanford Encyclopedia of Philosophy)', SEP + 'comte/'), ('Logical Empiricism (Stanford Encyclopedia of Philosophy)', SEP + 'logical-empiricism/'), ('Vienna Circle (Stanford Encyclopedia of Philosophy)', SEP + 'vienna-circle/'), ('Igreja Positivista do Brasil (Wikipédia)', WP + 'Igreja_Positivista_do_Brasil')],
quiz=[('O que diz a lei dos três estados de Comte?', ['A matéria tem três estados', 'O pensamento passa do teológico ao metafísico e ao positivo', 'O Brasil passou por três governos', 'A ciência tem três métodos'], 1, 'Para Comte, a humanidade avança de explicações por deuses para explicações por leis observáveis.'),
 ('Qual era o critério do positivismo lógico?', ['Falseabilidade', 'Verificabilidade: só tem significado o que é verificável ou verdadeiro por definição', 'Coerência', 'Autoridade'], 1, 'O critério de verificabilidade separava frases com e sem significado.'),
 ('Alguém chama de “positivista ultrapassado” um colega que pediu dados antes de aceitar uma política pública. O que está errado nisso?', ['Nada, pedir dados é positivismo lógico', 'Confunde valorizar evidências com aderir ao critério de verificabilidade, uma tese específica e abandonada', 'Positivismo é o mesmo que ciência', 'O colega é religioso'], 1, 'Pedir evidência não compromete ninguém com o programa do Círculo de Viena.')],
analogia='O critério de verificabilidade foi como uma peneira feita para separar o ouro (o que tem sentido) da areia (a metafísica). O problema é que a própria regra da peneira, e até as leis da física, também passavam pelos furos.',
crianca='Alguns filósofos acharam que só valia a pena falar do que dá para ver e medir. Era uma boa ideia para deixar as conversas mais claras, mas descobriram que, com essa regra, nem a própria regra dava para medir.',
obj=['Distinguir o positivismo de Comte do positivismo lógico.', 'Explicar o critério de verificabilidade e suas falhas.', 'Reconhecer o legado do positivismo e a caricatura do termo no uso popular.'],
caso=('Num debate, alguém diz que “a bandeira do Brasil prova que o país foi fundado na ciência”.', 'O que o lema “Ordem e Progresso” realmente indica?', 'A influência do positivismo de Comte entre os republicanos, uma doutrina filosófica e até religiosa, não a adoção do método científico pelo Estado.'),
erro=('“Positivismo é acreditar que só a ciência vale.”', 'É uma família de doutrinas históricas específicas. O positivismo lógico tinha uma teoria do significado, e Comte, uma filosofia da história. Confiar na ciência não é ser positivista.'),
ferr='que-corrente-e-essa', pre=['empirismo-e-racionalismo'],
guardar=['Comte: lei dos três estados, sociologia e influência na bandeira do Brasil.', 'Círculo de Viena: só tem sentido o que é verificável ou analítico.', 'O critério ruiu, mas o legado de clareza fundou a filosofia da ciência moderna.'],
pensar='Que frases você ouve no dia a dia que não seriam verificáveis por nenhuma experiência? Elas são sem sentido ou só não são científicas?'),

dict(slug='popper-e-a-falseabilidade', grupo='Filosofia da ciência clássica', titulo='Popper e a falseabilidade', temas=['filosofia', 'demarcacao'],
resumo='Para Karl Popper, uma teoria é científica se pode ser refutada. A ciência avança por conjecturas ousadas e tentativas de derrubá-las.',
corpo='''
<p class="abre">Na Viena de 1919, o jovem Karl Popper notou algo curioso. Os seguidores de Marx, Freud e Adler encontravam confirmações em tudo: qualquer fato parecia apoiar suas teorias. Enquanto isso, Einstein fazia uma previsão arriscada, a de que a luz das estrelas se curvaria perto do Sol, que podia ter falhado no eclipse daquele ano. Para Popper, era essa disposição de arriscar que fazia a ciência.</p>
<h2>A falseabilidade</h2>
<p>Uma teoria é científica se é <strong>falseável</strong>: se existe alguma observação possível que a mostraria falsa. “Todos os cisnes são brancos” é falseável: um cisne negro a derruba. “Amanhã choverá ou não choverá” não é: nenhum fato a contradiz, e por isso não diz nada sobre o mundo.</p>
<p>A ideia resolve, para Popper, o problema da indução. Nenhum número de cisnes brancos prova que todos são brancos, mas um único cisne negro prova, por dedução, que nem todos são. A ciência não verifica teorias; tenta <strong>refutá-las</strong>.</p>
<h2>Conjecturas e refutações</h2>
<p>O cientista popperiano propõe hipóteses ousadas, que dizem muito e por isso arriscam muito, e as submete aos testes mais severos que consegue imaginar. As que sobrevivem são <strong>corroboradas</strong>, nunca provadas. O conhecimento científico é sempre provisório: o melhor que temos até agora.</p>
<p>Popper chamou sua filosofia de <strong>racionalismo crítico</strong>. Ela vale também para a política: uma sociedade aberta é a que permite criticar e corrigir os governos, como a ciência corrige teorias.</p>
<h2>Os alvos de Popper</h2>
<p>Popper acusava a psicanálise de ser irrefutável: qualquer comportamento podia ser explicado por ela. Quanto ao marxismo, dizia que começou falseável (previu revoluções em países industrializados), foi refutado e, em vez de ser abandonado, recebeu hipóteses extras para salvá-lo. Para Popper, esse resgate <strong>ad hoc</strong> transforma ciência em pseudociência.</p>
<h2>As críticas</h2>
<ul><li><strong>Duhem e Quine:</strong> uma previsão nunca testa uma hipótese sozinha, mas junto com instrumentos, teorias auxiliares e condições. Quando o teste falha, não se sabe qual peça culpar. (Tema do nível Avançado.)</li>
<li><strong>Kuhn:</strong> cientistas não abandonam teorias na primeira anomalia; e se abandonassem, nenhuma teoria sobreviveria, porque todas têm anomalias.</li>
<li><strong>A história:</strong> quando a órbita de Urano não batia com Newton, os astrônomos não refutaram Newton; supuseram um planeta desconhecido, e acharam Netuno. Salvar a teoria às vezes é a decisão certa.</li>
<li><strong>Corroboração e confiança:</strong> se teorias nunca ficam mais prováveis, por que confiar numa ponte calculada com elas? Críticos dizem que a indução volta escondida.</li></ul>
<div class="nota"><strong>O que sobreviveu:</strong> mesmo quem rejeita a filosofia completa de Popper usa a pergunta dele no dia a dia: “o que me faria mudar de ideia?”. Uma afirmação que nenhum fato poderia contrariar deve ser vista com desconfiança.</div>''',
fontes=[('Karl Popper (Stanford Encyclopedia of Philosophy)', SEP + 'popper/'), ('Conjecturas e Refutações', 'https://www.google.com/search?tbm=bks&q=Conjecturas+e+Refuta%C3%A7%C3%B5es+Popper'), ('Falseabilidade (Wikipédia)', WP + 'Falseabilidade')],
quiz=[('Para Popper, o que torna uma teoria científica?', ['Ter sido confirmada muitas vezes', 'Poder ser refutada por alguma observação possível', 'Ser aceita pela maioria', 'Usar matemática'], 1, 'Falseabilidade: a teoria proíbe algo que poderia acontecer.'),
 ('Por que, para Popper, a refutação resolve o problema da indução?', ['Porque refutar é dedutivo: um contraexemplo derruba uma generalização', 'Porque refutar é indutivo', 'Porque teorias refutadas viram leis', 'Porque a indução é sempre válida'], 0, 'Mil confirmações não provam; um contraexemplo refuta, por lógica.'),
 ('A órbita de Urano não batia com a teoria de Newton; os astrônomos supuseram um planeta desconhecido e acharam Netuno. Isso é um problema para qual ideia?', ['Para a falseabilidade ingênua: às vezes salvar a teoria com hipótese auxiliar é a decisão certa', 'Para a lei da gravitação', 'Para o empirismo', 'Para nenhuma'], 0, 'Nem toda hipótese auxiliar é um resgate ad hoc; algumas fazem previsões novas e acertam.')],
analogia='Para Popper, uma teoria científica é como um lutador que aceita qualquer desafiante. Ele nunca prova que é invencível, mas cada luta vencida mostra que merece o título por enquanto. A pseudociência é o lutador que só aceita lutar contra quem não pode derrubá-lo.',
crianca='Se você diz “todos os gatos têm rabo”, basta achar um gato sem rabo para mostrar que errou. Popper achava que a ciência boa é aquela que topa ser testada desse jeito.',
obj=['Explicar o critério da falseabilidade.', 'Descrever o método de conjecturas e refutações e a ideia de corroboração.', 'Avaliar críticas: Duhem-Quine, Kuhn e o caso de Netuno.'],
caso=('Um astrólogo diz: “o horóscopo acerta para quem está aberto a ele; quando não acerta, é porque a pessoa resistiu”.', 'Como Popper analisaria essa defesa?', 'Como imunização contra a refutação: qualquer resultado confirma a teoria. Uma ideia assim não arrisca nada e, por isso, não é científica.'),
erro=('“Para Popper, se uma teoria é científica, ela é verdadeira.”', 'Ao contrário: científica é a que pode ser falsa. A falseabilidade separa ciência de não ciência, não verdade de falsidade.'),
ferr='que-corrente-e-essa', pre=['o-problema-da-inducao'],
guardar=['Científico é o que pode ser refutado por alguma observação possível.', 'Teorias nunca são provadas, só corroboradas por testes severos.', 'Críticas: testes envolvem hipóteses auxiliares, e salvar uma teoria às vezes é certo (Netuno).'],
pensar='Que observação faria você abandonar uma das suas crenças mais firmes? Se não consegue imaginar nenhuma, o que isso diz sobre ela?'),

dict(slug='criterio-da-demarcacao', grupo='Filosofia da ciência clássica', titulo='O critério da demarcação', temas=['demarcacao', 'filosofia'],
resumo='Onde termina a ciência e começa a pseudociência? Da verificabilidade a Popper, Kuhn e Laudan, até os critérios múltiplos usados hoje.',
corpo='''
<p class="abre">O <strong>problema da demarcação</strong> é a pergunta: o que separa ciência de não ciência, e em especial de pseudociência? Popper o chamou de problema central da filosofia da ciência. Não é só acadêmico: tribunais, escolas e sistemas de saúde precisam decidir o que ensinar, financiar e aceitar como prova.</p>
<h2>As propostas clássicas</h2>
<div class="tabela"><table><thead><tr><th>Proposta</th><th>Critério</th><th>Problema</th></tr></thead><tbody>
<tr><td>Positivismo lógico</td><td>Verificabilidade</td><td>Leis universais não são verificáveis</td></tr>
<tr><td>Popper</td><td>Falseabilidade</td><td>A astrologia faz previsões falseáveis (e falhou nelas); então seria ciência ruim, não pseudociência</td></tr>
<tr><td>Kuhn</td><td>Existência de pesquisa normal: resolver quebra-cabeças dentro de um paradigma</td><td>Muito permissivo: a astrologia teria problemas a resolver?</td></tr>
<tr><td>Lakatos</td><td>Programa de pesquisa progressivo: faz previsões novas que se confirmam</td><td>Difícil saber quando um programa estagnou de vez</td></tr>
<tr><td>Thagard</td><td>Pseudociência é o que fica menos progressivo que as alternativas e cujos defensores ignoram isso</td><td>Depende de comparação e de atitude da comunidade</td></tr>
</tbody></table></div>
<h2>A “morte” da demarcação</h2>
<p>Em 1983, Larry Laudan publicou “The Demise of the Demarcation Problem”. Argumentou que nenhum critério único separa todas as ciências de todas as não ciências, e que a pergunta certa não é “é ciência?”, mas “essa afirmação é bem apoiada pela evidência?”. Termos como “pseudociência”, dizia ele, são mais retórica do que análise.</p>
<h2>A resposta: critérios múltiplos</h2>
<p>Filósofos como Massimo Pigliucci, Sven Ove Hansson e Mario Bunge aceitaram que não há uma fronteira nítida, mas negaram que isso torne a distinção inútil. Hansson define ciência, no sentido amplo, como a prática que fornece as afirmações mais confiáveis (epistemicamente justificadas) que podem ser feitas, num dado momento, sobre um objeto de estudo; pseudociência é a doutrina que se apresenta como tão confiável quanto a ciência sem ter esse suporte. A definição cobre ciências naturais e humanas e desloca a pergunta da forma lógica das frases para a qualidade da evidência. A ciência seria um conceito de <strong>semelhança de família</strong>: um conjunto de traços que vêm juntos em graus. Ninguém sabe dizer o número exato de fios que torna alguém careca, e ainda assim há carecas.</p>
<p>Traços frequentemente usados:</p>
<ul><li>Testabilidade e disposição a abandonar hipóteses refutadas.</li><li>Progresso: novas previsões e explicações ao longo do tempo.</li><li>Integração com outras áreas do conhecimento (a homeopatia contradiz a química).</li><li>Revisão por pares e crítica aberta.</li><li>Clareza dos conceitos e possibilidade de medir.</li><li>Ausência de apelos à perseguição e de dependência de autoridade fundadora.</li></ul>
<h2>Demarcação na prática</h2>
<p>Em 1982, no caso McLean contra Arkansas, um tribunal dos EUA decidiu que o “criacionismo científico” não podia ser ensinado como ciência nas aulas de biologia, usando critérios como testabilidade e provisoriedade, com apoio do filósofo Michael Ruse. Laudan criticou a decisão pelos critérios, embora concordasse com o resultado. Em 2005, no caso Kitzmiller contra Dover, o mesmo se decidiu sobre o design inteligente.</p>
<div class="nota"><strong>Pseudociência e protociência:</strong> uma área nova, com poucas evidências mas aberta a testes (como a pesquisa sobre a origem da vida), é <em>protociência</em>. O que caracteriza a pseudociência não é estar no começo, e sim se recusar a crescer pelos caminhos da ciência.</div>''',
fontes=[('Science and Pseudo-Science (Stanford Encyclopedia of Philosophy)', SEP + 'pseudo-science/'), ('Philosophy of Pseudoscience: Reconsidering the Demarcation Problem', 'https://press.uchicago.edu/ucp/books/book/chicago/P/bo15996988.html'), ('Definindo Ciência e Pseudociência para Além da Falseabilidade: A Proposta Ampliada de Hansson', 'https://www.academia.edu/71626490/Definindo_Ci%C3%AAncia_e_Pseudoci%C3%AAncia_para_Al%C3%A9m_da_Falseabilidade_A_Proposta_Ampliada_de_Hansson'), ('The Demise of the Demarcation Problem', 'https://link.springer.com/chapter/10.1007/978-94-009-7055-7_6'), ('Kitzmiller v. Dover (Wikipédia)', WE + 'Kitzmiller_v._Dover_Area_School_District')],
quiz=[('O que é o problema da demarcação?', ['Definir as fronteiras entre países', 'Separar ciência de não ciência e de pseudociência', 'Dividir as ciências em áreas', 'Medir o progresso científico'], 1, 'Demarcar é dizer onde termina a ciência.'),
 ('O que Laudan defendeu em 1983?', ['Que a falseabilidade resolve tudo', 'Que nenhum critério único funciona e a pergunta certa é se a afirmação é bem apoiada por evidência', 'Que a astrologia é ciência', 'Que a ciência não existe'], 1, 'Laudan propôs trocar “é ciência?” por “é bem fundamentado?”.'),
 ('Uma terapia contradiz a química básica, não muda há duzentos anos, depende de depoimentos e seus defensores dizem ser perseguidos. Pela abordagem de critérios múltiplos:', ['Não dá para dizer nada, pois não há critério único', 'Ela acumula muitos traços de pseudociência e pode ser assim classificada com segurança', 'É ciência, pois tem defensores', 'É protociência'], 1, 'Sem fronteira nítida, ainda há casos claros, como há carecas sem um número exato de fios.')],
analogia='A diferença entre ciência e pseudociência é como a diferença entre dia e noite. O crepúsculo não tem um minuto exato em que o dia acaba, e mesmo assim ninguém confunde meio-dia com meia-noite.',
crianca='Às vezes é difícil dizer se algo é ciência ou não, como é difícil dizer exatamente quando alguém fica adulto. Mas tem casos bem claros, e os cientistas olham várias pistas juntas para decidir.',
obj=['Formular o problema da demarcação e por que ele importa fora da academia.', 'Comparar as propostas de verificabilidade, Popper, Kuhn e Lakatos.', 'Explicar a crítica de Laudan e a resposta dos critérios múltiplos.'],
caso=('Uma escola quer ensinar o design inteligente nas aulas de biologia “para mostrar os dois lados”.', 'Que critérios ajudam a decidir se ele é ciência?', 'Testabilidade, previsões novas, integração com outras áreas e produção em revistas científicas. Os tribunais dos EUA concluíram que o design inteligente não atende a esses critérios.'),
erro=('“Se não existe critério perfeito, então não dá para chamar nada de pseudociência.”', 'Fronteiras borradas não apagam casos claros. Vários traços juntos permitem classificar com segurança práticas como a homeopatia ou a astrologia.'),
ferr='detector-de-pseudociencia', pre=['popper-e-a-falseabilidade', 'o-que-e-pseudociencia'],
guardar=['Demarcação: onde termina a ciência; importa para escolas, tribunais e saúde pública.', 'Nenhum critério único funciona sozinho; Laudan sugeriu focar na evidência.', 'Critérios múltiplos tratam ciência como semelhança de família, com casos claros e casos de fronteira.'],
pensar='Que área você considera de fronteira entre ciência e não ciência? Que traços a colocam de cada lado?'),

dict(slug='kuhn-e-os-paradigmas', grupo='Filosofia da ciência clássica', titulo='Kuhn e os paradigmas', temas=['filosofia'],
resumo='Ciência normal, anomalias, crise e revolução: como Thomas Kuhn mudou a forma de ver a história da ciência, e o que ele não disse.',
corpo='''
<p class="abre">Em 1962, o físico e historiador Thomas Kuhn publicou <em>A Estrutura das Revoluções Científicas</em>, um dos livros acadêmicos mais citados do século XX. A ideia central: a ciência não avança de forma contínua, acumulando verdades. Ela alterna longos períodos de estabilidade com rupturas, as <strong>revoluções científicas</strong>.</p>
<h2>O ciclo de Kuhn</h2>
<ol><li><strong>Pré-ciência:</strong> várias escolas competem, sem acordo sobre o básico.</li>
<li><strong>Ciência normal:</strong> a comunidade adota um <strong>paradigma</strong>, um conjunto de teorias, métodos, exemplos e valores compartilhados. A pesquisa vira “resolução de quebra-cabeças”: aplicar o paradigma a novos casos.</li>
<li><strong>Anomalias:</strong> aparecem resultados que o paradigma não explica. No começo, são ignorados ou contornados.</li>
<li><strong>Crise:</strong> as anomalias se acumulam e a confiança no paradigma se abala.</li>
<li><strong>Revolução:</strong> um novo paradigma surge e substitui o antigo. Exemplos: Copérnico no lugar de Ptolomeu, Lavoisier no lugar do flogisto, Einstein no lugar de Newton.</li></ol>
<h2>Incomensurabilidade</h2>
<p>A tese mais polêmica de Kuhn é que paradigmas rivais são, em parte, <strong>incomensuráveis</strong>: não há uma medida neutra para compará-los. Os conceitos mudam de sentido (“massa” em Newton e em Einstein não é a mesma coisa), os problemas considerados importantes mudam, e até o que se “vê” numa observação depende do paradigma. Mudar de paradigma seria parecido com uma mudança de <em>Gestalt</em>, como na figura que é pato ou coelho.</p>
<h2>O que Kuhn não disse</h2>
<p>Kuhn foi lido como se dissesse que a ciência é irracional, que a escolha entre teorias é questão de moda ou de poder, ou que não há progresso. Ele rejeitou essas leituras. Em textos posteriores, listou valores que guiam a escolha entre teorias: <strong>precisão, consistência, alcance, simplicidade e fecundidade</strong>. São razões, só que não formam um algoritmo: cientistas competentes podem pesá-las de formas diferentes.</p>
<p>Kuhn também via progresso: paradigmas novos resolvem mais problemas que os antigos. O que ele duvidava é que a ciência caminhe para uma verdade final.</p>
<h2>Impacto e críticas</h2>
<ul><li>A palavra “paradigma” se espalhou para administração, marketing e autoajuda, quase sempre num sentido vago. Uma leitora contou 21 sentidos diferentes do termo no próprio livro.</li>
<li>Popper e seus alunos acusaram Kuhn de tornar a ciência dogmática ao valorizar a ciência normal.</li>
<li>Lakatos tentou unir Popper e Kuhn; Feyerabend levou Kuhn mais longe (próxima lição).</li>
<li>A sociologia da ciência usou Kuhn para estudar fatores sociais na ciência, em direções que ele próprio criticou.</li></ul>
<div class="nota"><strong>Exemplo brasileiro de anomalia:</strong> quando a Covid-19 começou, a ideia de que o vírus se espalhava sobretudo por gotículas grandes foi desafiada por evidências de transmissão por aerossóis. Levou meses para a OMS ajustar suas orientações: um caso pequeno do padrão de resistência a anomalias que Kuhn descreveu.</div>''',
fontes=[('Thomas Kuhn (Stanford Encyclopedia of Philosophy)', SEP + 'thomas-kuhn/'), ('A Estrutura das Revoluções Científicas', 'https://www.google.com/search?tbm=bks&q=A+Estrutura+das+Revolu%C3%A7%C3%B5es+Cient%C3%ADficas'), ('The Incommensurability of Scientific Theories (Stanford Encyclopedia)', SEP + 'incommensurability/')],
quiz=[('O que é “ciência normal” para Kuhn?', ['Ciência sem erros', 'Pesquisa de resolução de quebra-cabeças dentro de um paradigma aceito', 'Ciência feita por pessoas comuns', 'A fase de revolução'], 1, 'Na ciência normal, a comunidade aplica o paradigma, sem questioná-lo.'),
 ('Que valores, segundo Kuhn, guiam a escolha entre teorias?', ['Moda e poder', 'Precisão, consistência, alcance, simplicidade e fecundidade', 'Apenas a falseabilidade', 'Votação da maioria'], 1, 'Kuhn listou razões para escolher teorias; elas só não formam um algoritmo.'),
 ('Um palestrante diz: “Kuhn provou que a ciência é só uma questão de poder, então qualquer teoria vale o mesmo”. O que há de errado?', ['Nada', 'Kuhn rejeitou essa leitura: via razões na escolha de teorias e progresso na resolução de problemas', 'Kuhn era contra a ciência', 'Kuhn defendia a astrologia'], 1, 'É uma leitura relativista que o próprio Kuhn recusou.')],
analogia='Um paradigma é como as regras de um jogo. Durante a ciência normal, todos jogam e resolvem jogadas difíceis dentro das regras. Quando aparecem lances que as regras não resolvem, alguém propõe um jogo novo, e nem todos os conceitos do jogo antigo fazem sentido no novo.',
crianca='Por muito tempo as pessoas acharam que o Sol girava em volta da Terra, e explicavam tudo assim. Aí foram aparecendo coisas que não batiam, até que mudaram a ideia toda: é a Terra que gira em volta do Sol. Kuhn chamou essa mudança grande de revolução.',
obj=['Descrever o ciclo de Kuhn: ciência normal, anomalia, crise e revolução.', 'Explicar a incomensurabilidade e por que ela é polêmica.', 'Separar o que Kuhn disse das leituras relativistas que ele rejeitou.'],
caso=('Uma empresa diz que vai “quebrar paradigmas” com um novo aplicativo de entregas.', 'Esse uso tem a ver com Kuhn?', 'Pouco. Em Kuhn, paradigma é o conjunto de teorias, métodos e exemplos que organiza uma ciência madura; uma revolução muda o que se considera problema e solução, não só um produto.'),
erro=('“Kuhn mostrou que a ciência é irracional.”', 'Kuhn mostrou que a escolha de teorias não é um algoritmo, mas é guiada por razões (precisão, alcance, simplicidade) e produz progresso na resolução de problemas.'),
ferr='que-corrente-e-essa', pre=['popper-e-a-falseabilidade'],
guardar=['Ciência normal dentro de um paradigma; anomalias, crise e revolução.', 'Paradigmas rivais são em parte incomensuráveis: conceitos e problemas mudam.', 'Kuhn via razões e progresso; a leitura “tudo é poder” não é dele.'],
pensar='Em que área da sua vida você resiste a anomalias para manter um “paradigma” pessoal?'),

dict(slug='lakatos-e-feyerabend', grupo='Filosofia da ciência clássica', titulo='Lakatos e Feyerabend', temas=['filosofia'],
resumo='Programas de pesquisa progressivos e degenerativos, e o “vale tudo” de Feyerabend: dois amigos que discordavam sobre o método da ciência.',
corpo='''
<p class="abre">Imre Lakatos e Paul Feyerabend eram amigos e planejavam escrever juntos um livro chamado <em>A favor e contra o método</em>: Lakatos defenderia a racionalidade da ciência, Feyerabend a atacaria. Lakatos morreu em 1974, e Feyerabend publicou só a sua parte, <em>Contra o Método</em>.</p>
<h2>Lakatos: programas de pesquisa</h2>
<p>Lakatos queria salvar a racionalidade de Popper sem ignorar a história de Kuhn. Para ele, a unidade de avaliação não é uma teoria isolada, mas um <strong>programa de pesquisa</strong>, com duas partes:</p>
<ul><li><strong>Núcleo rígido:</strong> as hipóteses centrais, que os cientistas decidem não abandonar (em Newton, as leis do movimento e a gravitação).</li>
<li><strong>Cinturão protetor:</strong> hipóteses auxiliares que podem ser ajustadas para absorver anomalias (por exemplo, supor um planeta desconhecido).</li></ul>
<p>Ajustar o cinturão é legítimo, desde que o programa seja <strong>progressivo</strong>: que os ajustes levem a previsões novas que se confirmam. A hipótese de Netuno previu onde o planeta estaria, e ele estava lá. Um programa é <strong>degenerativo</strong> quando os ajustes só servem para tapar buracos, sem prever nada de novo, sempre correndo atrás dos fatos.</p>
<p>A regra racional é preferir programas progressivos. Mas Lakatos admitia que um programa degenerativo pode se recuperar, e que não há como saber, no momento, se é hora de desistir.</p>
<h2>Feyerabend: contra o método</h2>
<p>Feyerabend estudou episódios históricos, como a defesa do heliocentrismo por Galileu, e concluiu que grandes avanços muitas vezes violaram as regras metodológicas da época. Galileu usou retórica, propaganda e argumentos que hoje pareceriam frágeis. Se tivesse seguido o método “correto”, o heliocentrismo teria perdido.</p>
<p>Daí o famoso “<strong>tudo vale</strong>” (<em>anything goes</em>). Feyerabend explicou que não era uma recomendação, mas uma ironia: se alguém insiste em ter uma regra metodológica universal que nunca atrapalhe o progresso, a única que sobra é essa, vazia. Ele defendia o <strong>pluralismo</strong>: muitas teorias e métodos competindo, inclusive os marginais, para que cada um teste os outros.</p>
<p>Feyerabend também defendia que cidadãos, e não só especialistas, decidissem sobre o papel da ciência na sociedade, e chegou a defender o direito de tradições não científicas, como a medicina tradicional, de competir com a científica.</p>
<h2>Avaliação</h2>
<ul><li>Lakatos é muito usado para avaliar áreas em disputa: programas que só se protegem, sem prever nada novo, perdem credibilidade.</li>
<li>Feyerabend ajudou a mostrar que a história da ciência é mais bagunçada do que os manuais sugerem. Mas sua defesa de igualdade entre ciência e outras tradições é rejeitada pela maioria dos filósofos: a história bagunçada não apaga a diferença de resultados.</li>
<li>Feyerabend é frequentemente usado para justificar pseudociências. Ele próprio gostava de provocar, mas seus argumentos eram sobre pluralismo de métodos, não sobre aceitar qualquer conclusão sem teste.</li></ul>
<div class="nota"><strong>Aplicando Lakatos:</strong> a astrologia ajusta suas explicações para acomodar falhas há séculos sem gerar uma previsão nova confirmada: é o exemplo típico de programa degenerativo.</div>''',
fontes=[('Imre Lakatos (Stanford Encyclopedia of Philosophy)', SEP + 'lakatos/'), ('Paul Feyerabend (Stanford Encyclopedia of Philosophy)', SEP + 'feyerabend/'), ('Contra o Método', 'https://www.google.com/search?tbm=bks&q=Contra+o+M%C3%A9todo+Feyerabend')],
quiz=[('Para Lakatos, quando um programa de pesquisa é progressivo?', ['Quando nunca muda', 'Quando seus ajustes levam a previsões novas que se confirmam', 'Quando tem muitos defensores', 'Quando é antigo'], 1, 'Progresso é prever o que ainda não se sabia, e acertar.'),
 ('O que Feyerabend quis dizer com “tudo vale”?', ['Que qualquer crença é tão boa quanto a ciência', 'Que nenhuma regra metodológica universal sobrevive à história da ciência, exceto essa, que é vazia', 'Que a ciência deve ser abolida', 'Que Galileu estava errado'], 1, 'Era uma ironia contra metodologias rígidas, não um endosso a qualquer ideia.'),
 ('Uma terapia, a cada estudo negativo, ganha uma explicação nova (“a dose era errada”, “o paciente tinha energia bloqueada”), sem nunca prever um resultado novo. Para Lakatos, ela é:', ['Um programa progressivo', 'Um programa degenerativo', 'Ciência normal de Kuhn', 'Protociência promissora'], 1, 'Ajustes que só tapam buracos, sem previsões novas, caracterizam a degeneração.')],
analogia='Para Lakatos, um programa de pesquisa é como um castelo: o núcleo é a torre central e o cinturão são as muralhas. Reconstruir muralhas é normal, desde que o castelo continue conquistando território novo. Se só gasta tempo remendando muros, está perdendo a guerra.',
crianca='Um cientista achava que dava para saber quando uma ideia estava indo bem: quando ela adivinha coisas novas e acerta. Outro dizia que os grandes cientistas muitas vezes quebraram as regras, então não dá para ter uma regra só.',
obj=['Explicar núcleo rígido, cinturão protetor e programas progressivos e degenerativos.', 'Interpretar o “tudo vale” de Feyerabend e seu pluralismo.', 'Avaliar o uso de Feyerabend para defender pseudociências.'],
caso=('Um defensor de uma terapia alternativa cita Feyerabend: “até um filósofo da ciência disse que tudo vale, então minha terapia é tão válida quanto a medicina”.', 'Feyerabend sustenta essa conclusão?', 'Não. O “tudo vale” era uma ironia contra regras metodológicas rígidas. Mesmo com pluralismo de métodos, as terapias precisam mostrar resultados, e a pergunta continua sendo se funcionam.'),
erro=('“Feyerabend provou que a ciência não vale mais que qualquer outra crença.”', 'Ele mostrou que a história da ciência não segue um método único. Isso não apaga a diferença de resultados entre a ciência e outras práticas.'),
ferr='que-corrente-e-essa', pre=['kuhn-e-os-paradigmas'],
guardar=['Lakatos: núcleo rígido protegido por hipóteses auxiliares; progressivo é o programa que prevê o novo.', 'Feyerabend: nenhuma regra universal sobrevive à história; defendia pluralismo.', '“Tudo vale” é ironia, não licença para aceitar qualquer coisa sem teste.'],
pensar='Pense numa explicação que você defende. Ela já previu algo novo, ou só se ajusta depois dos fatos?'),

dict(slug='tipos-de-ciencia', grupo='Ciência na prática', titulo='Ciências formais, naturais e humanas', temas=['fundamentos', 'metodo'],
resumo='Matemática prova, física mede, sociologia interpreta: como cada tipo de ciência produz conhecimento e o debate sobre as ciências humanas.',
corpo='''
<p class="abre">Física, matemática e sociologia são todas chamadas de ciências, mas trabalham de jeitos muito diferentes. Uma divisão comum separa três grandes grupos: as ciências <strong>formais</strong>, as <strong>naturais</strong> e as <strong>sociais e humanas</strong>.</p>
<h2>Ciências formais</h2>
<p>Matemática, lógica, estatística teórica e ciência da computação teórica. Não estudam objetos do mundo, mas estruturas abstratas, e seu método é a <strong>prova</strong>: um teorema demonstrado é verdadeiro para sempre, dados os axiomas. Não há experimento que refute o teorema de Pitágoras na geometria euclidiana. Por isso há quem diga que não são ciências no mesmo sentido, já que não testam hipóteses contra o mundo. Mas são indispensáveis a todas as outras.</p>
<h2>Ciências naturais</h2>
<p>Física, química, biologia, geologia, astronomia. Estudam a natureza e testam hipóteses contra observações e experimentos. Costumam ser chamadas de “duras” por terem objetos mais estáveis, medidas mais precisas e leis mais gerais. Mesmo entre elas há diferenças: a física busca leis universais; a biologia evolutiva e a geologia são em parte <strong>históricas</strong>, reconstruindo eventos únicos do passado.</p>
<h2>Ciências sociais e humanas</h2>
<p>Psicologia, economia, sociologia, antropologia, ciência política, história, linguística. Estudam seres humanos e sociedades, o que traz dificuldades especiais:</p>
<ul><li><strong>Complexidade:</strong> muitas causas ao mesmo tempo, difíceis de isolar.</li><li><strong>Reflexividade:</strong> as pessoas reagem ao que se diz sobre elas. Uma previsão de corrida aos bancos pode causar a corrida.</li><li><strong>Significado:</strong> ações humanas têm intenções e sentidos que precisam ser interpretados, não só medidos.</li><li><strong>Ética:</strong> não se pode sortear pessoas para viver na pobreza.</li></ul>
<h2>Explicar ou compreender?</h2>
<p>Há um debate antigo. Para os <strong>naturalistas</strong> (como o positivismo), as ciências humanas devem usar os mesmos métodos das naturais: buscar leis e testar hipóteses com dados. Para a tradição <strong>interpretativa</strong> (Wilhelm Dilthey, Max Weber), o objetivo é também <em>compreender</em> (<em>Verstehen</em>) o sentido das ações. Weber tentou unir os dois: explicar pela compreensão do sentido, e testar essas explicações com dados.</p>
<p>Hoje, a maior parte das ciências sociais usa as duas abordagens: métodos quantitativos (estatística, experimentos, como os premiados com o Nobel de Economia de 2019 por ensaios randomizados contra a pobreza) e qualitativos (entrevistas, etnografia).</p>
<div class="nota"><strong>“Duras” e “moles”:</strong> a divisão é útil mas enganosa. Prever o comportamento de uma economia é mais difícil do que prever um eclipse, e isso torna a economia mais difícil, não menos científica. O que importa é se a área testa suas ideias com o rigor possível ao seu objeto.</div>''',
fontes=[('Philosophy of social science (Wikipédia)', WE + 'Philosophy_of_social_science'), ('Ciências formais (Wikipédia)', WP + 'Ci%C3%AAncias_formais'), ('Verstehen (Wikipédia)', WE + 'Verstehen'), ('Prêmio Nobel de Economia de 2019', 'https://www.nobelprize.org/prizes/economic-sciences/2019/summary/')],
quiz=[('Qual o método típico das ciências formais?', ['O experimento controlado', 'A prova a partir de axiomas', 'A entrevista', 'A observação de campo'], 1, 'Matemática e lógica trabalham com demonstrações.'),
 ('O que é reflexividade nas ciências sociais?', ['Usar espelhos nos experimentos', 'As pessoas reagem ao que se diz sobre elas, o que pode mudar o próprio fenômeno estudado', 'Repetir o experimento', 'Pensar muito'], 1, 'Uma previsão sobre pessoas pode alterar o comportamento delas.'),
 ('Uma ONG sorteia vilas para receber ou não um programa de transferência de renda e compara os resultados. Que abordagem é essa?', ['Quantitativa, com ensaio randomizado, como na economia do desenvolvimento', 'Formal', 'Puramente interpretativa', 'Pseudociência'], 0, 'Ensaios randomizados chegaram às ciências sociais e renderam um Nobel em 2019.')],
analogia='As ciências são como esportes diferentes. Todos exigem disciplina e regras, mas o xadrez (ciências formais) se vence por raciocínio puro, o atletismo (ciências naturais) se mede com cronômetro, e o futebol (ciências sociais) depende de muitas pessoas que reagem umas às outras, o que torna a previsão muito mais difícil.',
crianca='Tem ciência que estuda números, como a matemática. Tem ciência que estuda a natureza, como a biologia. E tem ciência que estuda as pessoas, como a psicologia. Cada uma descobre coisas de um jeito diferente.',
obj=['Distinguir ciências formais, naturais e sociais e humanas.', 'Explicar as dificuldades específicas das ciências sociais.', 'Descrever o debate entre explicar e compreender.'],
caso=('Alguém diz que economia não é ciência porque economistas erram previsões.', 'Esse argumento é bom?', 'Meteorologistas também erram previsões de longo prazo. O que define uma ciência é testar ideias com rigor, não acertar tudo; e a economia lida com sistemas complexos e reflexivos.'),
erro=('“Ciências humanas são só opinião.”', 'Elas usam dados, experimentos e métodos qualitativos rigorosos. São mais difíceis de prever porque o objeto é complexo e reage, não porque abrem mão de evidências.'),
ferr=None, pre=['o-que-e-ciencia'],
guardar=['Formais provam, naturais testam contra a natureza, sociais estudam pessoas que reagem.', 'Ciências sociais enfrentam complexidade, reflexividade, significado e limites éticos.', 'Explicar e compreender se combinam; “dura” e “mole” falam de dificuldade, não de valor.'],
pensar='Que pergunta sobre pessoas você gostaria de responder? Que método usaria: número, entrevista ou os dois?'),

dict(slug='pratica-baseada-em-evidencias', grupo='Ciência na prática', titulo='Prática Baseada em Evidências (PBE)', temas=['evidencias', 'sociedade'],
resumo='Medicina, educação e políticas públicas baseadas em evidências: integrar a melhor pesquisa, a experiência profissional e os valores de quem é afetado.',
corpo='''
<p class="abre">Em 1992, um grupo de médicos da Universidade McMaster, no Canadá, liderado por Gordon Guyatt e David Sackett, cunhou a expressão <strong>medicina baseada em evidências</strong>. A ideia parece óbvia, mas não era a prática: muitas decisões médicas se baseavam no costume, na autoridade do professor ou no raciocínio fisiológico sem teste.</p>
<h2>A definição</h2>
<p>Sackett definiu a medicina baseada em evidências como o uso consciente, explícito e criterioso da melhor evidência disponível para decidir sobre o cuidado de cada paciente. Ela integra três coisas:</p>
<ol><li><strong>A melhor evidência de pesquisa</strong>, de preferência revisões sistemáticas e ensaios bem feitos.</li><li><strong>A experiência clínica</strong> do profissional, para aplicar a evidência ao caso concreto.</li><li><strong>Os valores e preferências do paciente</strong>, que decide junto.</li></ol>
<p>Não é “seguir o estudo cegamente”. É não ignorar o que os estudos mostram.</p>
<h2>Por que foi necessária</h2>
<p>A história tem muitos tratamentos que pareciam lógicos e faziam mal. Na década de 1980, remédios antiarrítmicos eram dados a pacientes após infarto porque corrigiam batimentos irregulares no eletrocardiograma. O ensaio CAST, em 1989, mostrou que eles <strong>aumentavam</strong> a mortalidade. Por décadas, recomendou-se que bebês dormissem de bruços; quando as evidências mostraram que isso aumentava a morte súbita, campanhas para dormir de barriga para cima reduziram muito os casos.</p>
<h2>A Cochrane</h2>
<p>Em 1993, foi fundada a Colaboração Cochrane (hoje Cochrane), em homenagem ao epidemiologista Archie Cochrane, que criticava a medicina por não organizar suas evidências. A Cochrane produz revisões sistemáticas independentes sobre tratamentos, e tem um centro no Brasil.</p>
<h2>Além da medicina</h2>
<ul><li><strong>Educação:</strong> que métodos de alfabetização funcionam? O que a pesquisa diz sobre tamanho de turma ou tempo integral?</li><li><strong>Políticas públicas:</strong> avaliações de impacto de programas como o Bolsa Família, que estudos associaram à redução da mortalidade infantil.</li><li><strong>Segurança pública:</strong> que intervenções reduzem homicídios?</li></ul>
<h2>Críticas</h2>
<ul><li>A evidência disponível é enviesada para o que a indústria financia e para o que é fácil de medir.</li><li>Ensaios são feitos com populações selecionadas, que podem não representar o paciente real.</li><li>Pode virar receita de bolo burocrática, ignorando o caso individual.</li><li>Em políticas públicas, valores e contexto pesam muito: a evidência informa, mas não decide sozinha.</li></ul>
<h2>O que a PBE não é</h2>
<ul class="lista-contra"><li><strong>“O paciente prefere, então faço.”</strong> As preferências do paciente entram na decisão, mas não a substituem: o profissional deve explicar o que a evidência mostra e não oferecer o que não funciona só porque foi pedido.</li>
<li><strong>“Tenho autonomia profissional, prescrevo o que quiser.”</strong> Autonomia é a liberdade de julgar o caso, não licença para indicar intervenções sem evidência; quem a usa assim transfere o risco ao paciente.</li>
<li><strong>“Sou baseado em evidências, logo sou cientista.”</strong> Usar evidência é consumir ciência; produzir ciência é outra atividade, com outro treino. Um bom clínico baseado em evidências não é, por isso, pesquisador, e vice-versa.</li>
<li><strong>“O paciente melhorou, então a intervenção funcionou.”</strong> Melhora natural, regressão à média, placebo e outros tratamentos simultâneos explicam melhoras sem que a intervenção tenha feito nada; só a comparação controlada separa isso.</li>
<li><strong>“Um estudo de coorte mostrou que funciona.”</strong> Coortes mostram associação em quem escolheu fazer algo; o efeito de uma intervenção se mede em ensaios randomizados (ou em experimentos naturais bem defendidos).</li></ul>
<div class="nota"><strong>Brasil:</strong> o SUS usa avaliações de tecnologias em saúde (pela Conitec) para decidir que remédios e procedimentos incorporar. É a prática baseada em evidências aplicada ao orçamento público.</div>''',
fontes=[('Evidence based medicine: what it is and what it isn\'t (BMJ)', 'https://www.bmj.com/content/312/7023/71'), ('Cochrane Brasil', 'https://brazil.cochrane.org/'), ('Cardiac Arrhythmia Suppression Trial (Wikipédia)', WE + 'Cardiac_Arrhythmia_Suppression_Trial'), ('Conitec', 'https://www.gov.br/conitec/pt-br')],
quiz=[('Quais são os três elementos da medicina baseada em evidências?', ['Preço, prazo e qualidade', 'Melhor evidência, experiência clínica e valores do paciente', 'Tradição, autoridade e fé', 'Teoria, lei e hipótese'], 1, 'A definição de Sackett integra os três.'),
 ('O que o caso dos antiarrítmicos (ensaio CAST) ensinou?', ['Que remédios sempre ajudam', 'Que um tratamento que parece lógico pode aumentar a mortalidade, e só o teste mostra isso', 'Que eletrocardiogramas não servem', 'Que a Cochrane erra'], 1, 'Raciocínio fisiológico plausível não substitui ensaios com desfechos reais.'),
 ('Um gestor quer ampliar um programa escolar porque “todo mundo gosta”, sem nenhuma avaliação. A prática baseada em evidências sugeriria:', ['Ampliar de qualquer jeito', 'Avaliar o impacto, de preferência comparando escolas com e sem o programa, antes de ampliar', 'Cancelar o programa', 'Fazer uma votação'], 1, 'Avaliação de impacto é a evidência aplicada a políticas públicas.')],
analogia='A prática baseada em evidências é como um piloto que usa ao mesmo tempo o GPS (a pesquisa), a própria experiência de estrada (a experiência clínica) e o destino que o passageiro escolheu (os valores do paciente). Ignorar o GPS é arriscado; seguir só o GPS, sem olhar a estrada, também.',
crianca='Antes, alguns médicos faziam as coisas porque sempre foi assim. Hoje eles procuram saber o que os testes mostram que funciona de verdade, e perguntam também o que o paciente prefere.',
obj=['Definir prática baseada em evidências e seus três componentes.', 'Dar exemplos de tratamentos plausíveis que se mostraram prejudiciais.', 'Aplicar a ideia à educação e às políticas públicas, com suas críticas.'],
caso=('Um médico prescreve um suplemento “porque faz sentido fisiologicamente”, embora ensaios não mostrem benefício.', 'O que a prática baseada em evidências diria?', 'Que plausibilidade não basta: vários tratamentos lógicos fizeram mal quando testados. Sem evidência de benefício, a prescrição precisa de outra justificativa, discutida com o paciente.'),
erro=('“Baseado em evidências quer dizer seguir o protocolo sem pensar.”', 'A definição original integra pesquisa, julgamento clínico e valores do paciente. É o contrário de ignorar o caso individual.'),
ferr='nivel-de-evidencia', pre=['niveis-de-evidencia'],
guardar=['Evidência de pesquisa + experiência profissional + valores de quem é afetado.', 'Tratamentos plausíveis já mataram; só testes com desfechos reais mostram.', 'Vale para saúde, educação e políticas públicas, com atenção a vieses e valores.'],
pensar='Que decisão importante na sua área (trabalho, escola, cidade) é tomada só por costume? Como seria avaliá-la?'),

dict(slug='estatistica-para-entender-ciencia', grupo='Ciência na prática', titulo='Estatística para entender ciência', temas=['estatistica', 'evidencias'],
resumo='Amostra, média, margem de erro, p-valor, significância e tamanho de efeito: o mínimo para ler um estudo sem ser enganado.',
corpo='''
<p class="abre">Quase toda ciência empírica passa pela estatística. Você não precisa saber fazer as contas para entender os conceitos, e eles evitam boa parte dos enganos na leitura de estudos e notícias.</p>
<h2>Amostra e população</h2>
<p>Raramente se estuda todo mundo. Estuda-se uma <strong>amostra</strong> e se tenta generalizar para a <strong>população</strong>. Isso funciona se a amostra for representativa, idealmente escolhida por sorteio. Uma pesquisa feita só com quem segue um perfil numa rede social não representa o país, por maior que seja.</p>
<h2>Margem de erro e intervalo de confiança</h2>
<p>Como a amostra é só uma parte, o resultado tem incerteza. Uma pesquisa que dá 40% com margem de erro de 3 pontos indica que o valor real provavelmente está entre 37% e 43%. Na ciência, isso aparece como <strong>intervalo de confiança</strong>. Intervalos largos indicam pouca precisão; quando dois intervalos se sobrepõem muito, a diferença pode não ser real.</p>
<h2>O p-valor e a significância</h2>
<p>O <strong>p-valor</strong> responde: se não houvesse efeito nenhum, qual seria a chance de ver um resultado tão extremo quanto este, ou mais? Por convenção, p menor que 0,05 é chamado de “estatisticamente significativo”.</p>
<p>O p-valor é muito mal entendido. Ele <strong>não</strong> é:</p>
<ul class="lista-contra"><li>A probabilidade de a hipótese ser verdadeira.</li><li>A probabilidade de o resultado ser obra do acaso.</li><li>Uma medida do tamanho ou da importância do efeito.</li></ul>
<p>Em 2016, a Associação Americana de Estatística publicou um alerta: decisões não devem se basear só em p &lt; 0,05.</p>
<h2>Tamanho do efeito</h2>
<p>Com uma amostra enorme, até diferenças minúsculas ficam “significativas”. Um remédio que reduz a pressão em 0,5 mmHg pode ter p = 0,001 e não ter importância clínica nenhuma. Por isso a pergunta mais útil é: <strong>quão grande</strong> é o efeito, e com que precisão foi medido?</p>
<h2>Armadilhas comuns</h2>
<ul><li><strong>Múltiplas comparações:</strong> teste vinte coisas e, por acaso, uma dará p &lt; 0,05. A tirinha da xkcd sobre balas de goma verdes e acne ilustra isso.</li>
<li><strong>Viés de sobrevivência:</strong> olhar só os casos que “sobreviveram” a um filtro. Analisar só empresas de sucesso para descobrir o segredo do sucesso ignora as que fizeram o mesmo e faliram.</li>
<li><strong>Regressão à média:</strong> resultados extremos tendem a ser seguidos por resultados mais próximos da média. O aluno que tirou a pior nota tende a melhorar na prova seguinte, com ou sem castigo.</li>
<li><strong>Média que esconde:</strong> a renda média de um bairro sobe muito se um bilionário se muda para lá; a mediana mostra melhor o morador típico.</li></ul>
<div class="nota"><strong>Base rate (taxa de base):</strong> um exame com 99% de acerto, para uma doença que atinge 1 em 10 mil, dá muito mais falsos positivos do que verdadeiros. Sem a taxa de base, o “99%” engana. O bayesianismo, no nível Avançado, explica por quê.</div>''',
fontes=[('The ASA Statement on p-Values', 'https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108'), ('Significant (xkcd)', 'https://xkcd.com/882/'), ('Regressão à média (Wikipédia)', WP + 'Regress%C3%A3o_%C3%A0_m%C3%A9dia'), ('Survivorship bias (Wikipédia)', WE + 'Survivorship_bias')],
quiz=[('O que o p-valor mede?', ['A probabilidade de a hipótese ser verdadeira', 'A chance de ver um resultado tão extremo se não houvesse efeito', 'O tamanho do efeito', 'A importância prática do resultado'], 1, 'O p-valor supõe que não há efeito e pergunta quão surpreendente seria o dado.'),
 ('Um estudo com 2 milhões de pessoas acha que um hábito reduz o peso em 50 gramas, com p = 0,0001. O que concluir?', ['É um efeito enorme', 'O efeito é real, mas minúsculo: significância estatística não é importância prática', 'O estudo é falso', 'Todos devem adotar o hábito'], 1, 'Amostras gigantes tornam “significativos” efeitos irrelevantes.'),
 ('Um técnico de futebol nota que, depois de broncas em jogadores que tiveram péssima atuação, eles melhoram. Que fenômeno pode explicar isso sem a bronca?', ['Viés de sobrevivência', 'Regressão à média', 'Efeito placebo', 'Múltiplas comparações'], 1, 'Atuações extremas tendem a ser seguidas por atuações mais normais, com ou sem bronca.')],
analogia='Ler um estudo sem estatística é como ler a previsão do tempo sem saber o que significa “70% de chance de chuva”. Os números estão lá, mas só fazem sentido quando você sabe o que eles medem, e o que não medem.',
crianca='Se você quer saber de que sabor de sorvete as crianças da escola gostam mais, não precisa perguntar a todas: pode perguntar a algumas, desde que escolha bem quem, e não só os seus amigos.',
obj=['Explicar amostra, margem de erro e intervalo de confiança.', 'Interpretar corretamente o p-valor e diferenciá-lo do tamanho do efeito.', 'Reconhecer armadilhas: múltiplas comparações, sobrevivência, regressão à média e taxa de base.'],
caso=('Um livro de negócios analisa dez empresas de sucesso e conclui que todas tinham CEOs que acordavam às 5h.', 'Que armadilha estatística aparece aqui?', 'Viés de sobrevivência: faltam as empresas cujos CEOs também acordavam às 5h e faliram. Sem comparação, o hábito não explica nada.'),
erro=('“p < 0,05 quer dizer que há 95% de chance de a hipótese estar certa.”', 'O p-valor não mede a probabilidade da hipótese. Mede quão surpreendente seria o dado se não houvesse efeito.'),
ferr='correlacao-ou-causa', pre=['correlacao-e-causalidade'],
guardar=['Amostra boa é representativa; tamanho não compensa viés.', 'p-valor não é probabilidade da hipótese nem tamanho do efeito.', 'Desconfie de múltiplas comparações, de sobreviventes e de extremos que “melhoram sozinhos”.'],
pensar='Que número você viu esta semana que parecia impressionante? Ele vinha com margem de erro ou tamanho de efeito?'),

dict(slug='vieses-e-metodo', grupo='Ciência na prática', titulo='Vieses cognitivos e o método', temas=['mente', 'metodo'],
resumo='Viés de confirmação, raciocínio motivado e ver padrões no acaso: por que o método científico existe para proteger cientistas de si mesmos.',
corpo='''
<p class="abre">“O primeiro princípio é que você não deve enganar a si mesmo, e você é a pessoa mais fácil de enganar.” A frase do físico Richard Feynman resume por que a ciência precisa de método: cérebros humanos têm atalhos que funcionam bem no dia a dia e falham sistematicamente em certas tarefas.</p>
<h2>Os vieses que mais atrapalham a ciência</h2>
<ul class="lista-contra">
<li><strong>Viés de confirmação:</strong> procurar, notar e lembrar mais o que confirma o que já pensamos. Num experimento clássico de Peter Wason, pessoas testavam uma regra numérica só com exemplos que a confirmavam, nunca com os que poderiam derrubá-la.</li>
<li><strong>Raciocínio motivado:</strong> avaliar a evidência conforme a conclusão que desejamos. Somos exigentes com estudos que nos contrariam e generosos com os que nos agradam.</li>
<li><strong>Apofenia:</strong> ver padrões no acaso, como rostos em nuvens ou “sequências quentes” em jogos de azar.</li>
<li><strong>Viés de disponibilidade:</strong> julgar a frequência pelo que vem fácil à mente. Acidentes de avião parecem mais comuns que de carro porque são mais noticiados.</li>
<li><strong>Efeito do observador:</strong> expectativas do pesquisador influenciam o resultado, por exemplo ao classificar dados ambíguos.</li>
<li><strong>Excesso de confiança:</strong> achar que sabemos mais do que sabemos, inclusive especialistas fora da sua área.</li></ul>
<h2>Cada procedimento é uma vacina contra um viés</h2>
<div class="tabela"><table><thead><tr><th>Procedimento</th><th>Contra qual viés</th></tr></thead><tbody>
<tr><td>Grupo controle</td><td>Atribuir ao tratamento o que é melhora natural</td></tr>
<tr><td>Sorteio</td><td>Escolher, sem perceber, os casos favoráveis</td></tr>
<tr><td>Teste cego e duplo-cego</td><td>Expectativas de participantes e pesquisadores</td></tr>
<tr><td>Pré-registro do estudo</td><td>Mudar a hipótese depois de ver os dados</td></tr>
<tr><td>Estatística e correção para múltiplas comparações</td><td>Ver padrões no acaso</td></tr>
<tr><td>Revisão por pares e replicação</td><td>Raciocínio motivado e erros pessoais</td></tr>
<tr><td>Procurar refutações</td><td>Viés de confirmação</td></tr>
</tbody></table></div>
<h2>O caso de Clever Hans</h2>
<p>No começo do século XX, o cavalo Hans, em Berlim, parecia fazer contas: batia o casco o número certo de vezes. O psicólogo Oskar Pfungst descobriu que Hans só acertava quando quem perguntava sabia a resposta e estava à vista: o cavalo lia sinais involuntários de tensão e alívio no rosto das pessoas. O dono não era fraudador; ele próprio se enganava. Daí vem a importância dos testes cegos.</p>
<h2>Inteligência não protege</h2>
<p>Estudos de Dan Kahan e outros sugerem que, em temas politicamente carregados, pessoas com mais habilidade numérica podem ser <strong>mais</strong> polarizadas: usam a habilidade para defender o lado do seu grupo. O antídoto não é ser mais inteligente, mas adotar procedimentos e hábitos, como a curiosidade e a busca ativa por contraexemplos.</p>
<div class="nota"><strong>Veja também:</strong> o Política Para Iniciantes tem um catálogo de centenas de vieses, com exemplos e como se proteger de cada um.</div>''',
fontes=[('Cargo Cult Science', 'https://calteches.library.caltech.edu/51/2/CargoCult.htm'), ('Confirmation bias (Wikipédia)', WE + 'Confirmation_bias'), ('Clever Hans (Wikipédia)', WP + 'Clever_Hans'), ('Motivated numeracy and enlightened self-government', 'https://doi.org/10.1017/bpp.2016.2')],
quiz=[('O que é o viés de confirmação?', ['Confirmar tudo duas vezes', 'Tendência a procurar e lembrar o que confirma o que já pensamos', 'Confiar demais em especialistas', 'Ver rostos em nuvens'], 1, 'É o viés mais combatido pelo método científico.'),
 ('O que o caso do cavalo Hans mostrou?', ['Que cavalos sabem matemática', 'Que expectativas de quem observa podem produzir o resultado, por isso testes cegos são necessários', 'Que o dono era um fraudador', 'Que a psicologia não é ciência'], 1, 'Hans lia sinais involuntários; só um teste cego revelou isso.'),
 ('Um pesquisador testa 30 alimentos contra dor de cabeça e publica apenas o que deu p < 0,05. Que proteção faltou?', ['Pré-registro e correção para múltiplas comparações', 'Grupo controle', 'Revisão por pares', 'Nada faltou'], 0, 'Com 30 testes, é esperado que algum dê “significativo” por acaso.')],
analogia='O método científico é como o cinto de segurança. Ninguém o usa porque acha que dirige mal; usa porque sabe que todo motorista, mesmo o bom, um dia se distrai. Os procedimentos científicos são cintos de segurança contra os nossos vieses.',
crianca='Nosso cérebro às vezes nos engana, como quando a gente vê uma cara numa nuvem. Os cientistas inventaram truques, como não saber quem tomou o remédio de verdade, para não se enganarem.',
obj=['Descrever vieses que ameaçam a pesquisa: confirmação, raciocínio motivado, apofenia, disponibilidade.', 'Associar cada procedimento metodológico ao viés que ele combate.', 'Explicar por que inteligência sozinha não protege contra vieses.'],
caso=('Um professor está convencido de que um novo método de ensino funciona e decide avaliar ele mesmo as provas dos alunos que usaram o método, sabendo quem são.', 'Que problema há no desenho?', 'Efeito do observador e raciocínio motivado: ele pode corrigir com mais boa vontade os alunos do método. Avaliar às cegas resolveria.'),
erro=('“Cientistas são pessoas mais racionais, imunes a vieses.”', 'Cientistas têm os mesmos vieses. O que os protege é o método: controles, cegamento, pré-registro e crítica dos pares.'),
ferr='correlacao-ou-causa', pre=['postura-cientifica', 'experimentos-e-grupo-controle'],
guardar=['Todo cérebro procura confirmação e vê padrões no acaso.', 'Cada procedimento do método é uma proteção contra um viés específico.', 'Inteligência pode até aumentar a polarização; o que protege são hábitos e procedimentos.'],
pensar='Qual procedimento do método científico você poderia usar numa decisão pessoal importante?'),

dict(slug='ciencia-religiao-e-filosofia', grupo='Ciência na prática', titulo='Ciência, religião e filosofia', temas=['fundamentos', 'sociedade'],
resumo='Conflito, independência, diálogo ou integração? As formas de relacionar ciência e religião e o papel da filosofia nas perguntas que a ciência não responde sozinha.',
corpo='''
<p class="abre">Ciência e religião estão em guerra? A resposta popular costuma ser sim, mas historiadores e filósofos descrevem uma relação mais variada. O teólogo e físico Ian Barbour propôs quatro modelos para pensar essa relação.</p>
<h2>Os quatro modelos de Barbour</h2>
<ul><li><strong>Conflito:</strong> as duas fazem afirmações rivais sobre o mundo, e uma tem de perder. Exemplos: o criacionismo da Terra jovem contra a geologia e a biologia; ou o “novo ateísmo” de Richard Dawkins, que vê a religião como hipótese científica fracassada.</li>
<li><strong>Independência:</strong> tratam de domínios separados. Stephen Jay Gould chamou isso de “magistérios não sobrepostos”: a ciência trata de fatos e mecanismos; a religião, de sentido e valores.</li>
<li><strong>Diálogo:</strong> há perguntas de fronteira em que as duas podem conversar, como a origem do universo ou a ética da pesquisa.</li>
<li><strong>Integração:</strong> tentar unir ciência e teologia num só sistema, como na teologia natural.</li></ul>
<h2>O que a história mostra</h2>
<p>O “mito do conflito” foi popularizado no século XIX. A história real é mais complicada: muitos cientistas pioneiros eram religiosos (Kepler, Newton, Mendel, que era monge, e Georges Lemaître, o padre que propôs o que viria a ser o Big Bang). O caso Galileu envolveu política, personalidade e disputas dentro da própria Igreja, não só ciência contra fé. Ao mesmo tempo, houve conflitos reais, como a condenação de Galileu e a resistência ao ensino da evolução.</p>
<h2>Onde há conflito real</h2>
<p>Quando a religião faz afirmações empíricas sobre o mundo (a idade da Terra, a origem das espécies, curas por oração), elas podem ser testadas, e a ciência pode contradizê-las. Grandes ensaios sobre oração intercessora, como o estudo STEP de 2006, não encontraram benefício para pacientes de cirurgia cardíaca. Por outro lado, a ciência não testa afirmações que não têm consequências observáveis, como a existência de um Deus que não intervém no mundo.</p>
<h2>E a filosofia?</h2>
<p>A filosofia trabalha com perguntas que nem a ciência nem a fé resolvem sozinhas: o que é uma boa razão, o que é conhecimento, o que devemos fazer, o que é a mente. A ciência depende de pressupostos filosóficos (que há regularidades, que a observação é confiável) e levanta perguntas filosóficas (o que é uma lei da natureza, se a física quântica descreve a realidade). Dizer que “a filosofia morreu porque a ciência responde tudo” já é uma tese filosófica.</p>
<div class="nota"><strong>Respeito sem confusão:</strong> é possível respeitar a fé de alguém e, ao mesmo tempo, dizer que uma afirmação empírica feita em nome dela foi testada e não se confirmou. A postura científica avalia afirmações, não pessoas.</div>''',
fontes=[('Religion and Science (Stanford Encyclopedia of Philosophy)', SEP + 'religion-science/'), ('Non-overlapping magisteria (Wikipédia)', WE + 'Non-overlapping_magisteria'), ('Study of the Therapeutic Effects of Intercessory Prayer (STEP)', 'https://pubmed.ncbi.nlm.nih.gov/16569567/'), ('Conflict thesis (Wikipédia)', WE + 'Conflict_thesis')],
quiz=[('O que propõe o modelo da “independência”?', ['Que ciência e religião sempre se contradizem', 'Que tratam de domínios separados: fatos e mecanismos de um lado, sentido e valores de outro', 'Que devem ser unidas', 'Que a religião é uma ciência'], 1, 'É a ideia dos magistérios não sobrepostos de Gould.'),
 ('Quando ciência e religião entram em conflito real?', ['Sempre', 'Quando a religião faz afirmações empíricas testáveis sobre o mundo', 'Nunca', 'Só em países religiosos'], 1, 'Afirmações sobre o mundo observável podem ser testadas, venham de onde vierem.'),
 ('Alguém diz: “a ciência explica tudo, então a filosofia é inútil”. Qual o problema?', ['Nenhum', 'A frase é uma tese filosófica, e a ciência depende de pressupostos filosóficos', 'A ciência não explica nada', 'A filosofia é uma ciência natural'], 1, 'Afirmar o alcance da ciência é fazer filosofia.')],
analogia='Ciência, religião e filosofia são como ferramentas numa caixa. O martelo (ciência) é ótimo para pregos (perguntas sobre o mundo observável). Usá-lo para apertar parafusos é um erro, e usar uma chave de fenda para martelar pregos também.',
crianca='A ciência ajuda a responder como as coisas funcionam, como o arco-íris se forma. Algumas pessoas também se perguntam por que existimos ou o que é certo fazer. Para essas perguntas, as pessoas usam a filosofia, a religião e a ciência de jeitos diferentes.',
obj=['Descrever os quatro modelos de Barbour para a relação entre ciência e religião.', 'Distinguir conflitos reais (afirmações empíricas) de falsos conflitos.', 'Explicar o papel da filosofia nas perguntas que a ciência não resolve sozinha.'],
caso=('Uma pessoa religiosa pergunta se pode aceitar a evolução sem abandonar a fé.', 'O que a história e os modelos de Barbour sugerem?', 'Muitas tradições religiosas aceitam a evolução (a Igreja Católica, por exemplo, a considera compatível com a fé). O conflito aparece quando se exige uma leitura literal com afirmações empíricas, como a idade da Terra.'),
erro=('“Ciência e religião sempre foram inimigas.”', 'A história é variada: há conflitos reais e cooperação, e muitos cientistas pioneiros eram religiosos. O “mito do conflito” simplifica demais.'),
ferr=None, pre=['o-que-e-ciencia'],
guardar=['Conflito, independência, diálogo e integração são modelos diferentes.', 'Afirmações empíricas, venham de onde vierem, podem ser testadas.', 'A filosofia trata do que nenhuma das duas resolve sozinha, inclusive dos limites da ciência.'],
pensar='Que pergunta importante para você não pode ser respondida só por experimento?'),
]
