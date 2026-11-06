"""Lições do nível Iniciante. Cada lição traz tudo o que a página usa: corpo (HTML), fontes (só títulos), três testes,
analogia, explicação para criança, objetivos, caso de abertura, erro comum, ferramenta, pré-requisitos e fecho."""
SEP = 'https://plato.stanford.edu/entries/'
WP = 'https://pt.wikipedia.org/wiki/'
WE = 'https://en.wikipedia.org/wiki/'

INICIANTE = [
dict(slug='o-que-e-ciencia', grupo='O básico', titulo='O que é ciência?', temas=['fundamentos'],
resumo='Ciência é um jeito de descobrir como o mundo funciona testando ideias contra a realidade, de forma pública e sempre aberta a correção.',
corpo='''
<p class="abre">Ciência é um modo de conhecer o mundo que submete as ideias a testes. Em vez de aceitar uma explicação porque ela é bonita, antiga ou dita por alguém importante, a ciência pergunta: o que deveríamos observar se essa ideia fosse verdadeira? E depois vai olhar.</p>
<p>A palavra vem do latim <em>scientia</em>, conhecimento. Mas nem todo conhecimento é científico. Você sabe o nome da sua mãe e o caminho de casa sem ter feito nenhum experimento. O que torna um conhecimento científico é o <strong>jeito</strong> como ele foi obtido e como pode ser contestado.</p>
<h2>Três coisas que a palavra “ciência” pode querer dizer</h2>
<ul><li><strong>Um método:</strong> o conjunto de práticas para testar ideias, como observar com cuidado, fazer previsões, comparar com um grupo controle e medir.</li><li><strong>Um corpo de conhecimento:</strong> o que já foi descoberto e está bem estabelecido, como a evolução das espécies, a estrutura do átomo e a origem infecciosa de muitas doenças.</li><li><strong>Uma instituição:</strong> universidades, laboratórios, revistas, agências de fomento e a comunidade de pesquisadores que revisa o trabalho uns dos outros.</li></ul>
<p>As três se misturam no dia a dia, mas convém separá-las. Uma instituição científica pode errar, e o método serve justamente para corrigir esses erros.</p>
<h2>O que a ciência tem de especial</h2>
<p>Nenhum cientista é imune a vieses, vaidade ou pressa. A força da ciência não está na virtude individual, e sim no sistema: as ideias precisam ser <strong>testáveis</strong>, os resultados precisam ser <strong>públicos</strong> e <strong>reproduzíveis</strong>, e qualquer pessoa competente pode tentar derrubá-los. O sociólogo Robert Merton chamou isso de <em>ceticismo organizado</em>.</p>
<p>Por isso a ciência é <strong>autocorretiva</strong>. Teorias foram abandonadas (o éter, o flogisto, a geração espontânea) porque a evidência pesou contra elas. Isso não é fraqueza. É o motivo de confiarmos nela mais do que em qualquer outro método para questões sobre o mundo natural.</p>
<h2>O que a ciência não é</h2>
<ul><li>Não é uma lista de verdades definitivas. Todo conhecimento científico é, em princípio, revisável, embora parte dele seja tão bem testada que revisá-la exigiria uma montanha de evidências.</li><li>Não é só o que se faz de jaleco. Um agricultor que compara duas sementes em canteiros iguais está usando raciocínio científico.</li><li>Não responde sozinha a perguntas de valor. Ela diz o que acontece se fizermos X; se devemos fazer X depende também de ética.</li></ul>
<div class="nota"><strong>Ciências formais, naturais e humanas.</strong> Matemática e lógica (formais) trabalham com provas, não com experimentos. Física, química e biologia (naturais) e psicologia, economia e sociologia (sociais) testam ideias contra observações. O nível Intermediário tem uma lição sobre essa divisão.</div>''',
fontes=[('Science (Stanford Encyclopedia of Philosophy)', SEP + 'scientific-method/'), ('Ciência (Wikipédia)', WP + 'Ci%C3%AAncia'), ('The Normative Structure of Science', WE + 'Mertonian_norms')],
quiz=[('O que torna um conhecimento científico, segundo a lição?', ['Ter sido dito por um cientista famoso', 'O jeito como foi obtido e pode ser testado e contestado', 'Ser antigo e aceito por muita gente', 'Ter sido publicado num livro'], 1, 'A ciência se define pelo método: ideias testáveis, resultados públicos e abertos a contestação.'),
 ('Uma teoria científica foi abandonada depois de novas evidências. Isso mostra que:', ['A ciência não é confiável', 'A ciência se corrige quando a evidência pesa contra uma ideia', 'Os cientistas mentem', 'Toda teoria atual também está errada'], 1, 'A autocorreção é uma virtude da ciência, não uma falha.'),
 ('Uma agricultora planta duas sementes em canteiros iguais, com a mesma água, para ver qual rende mais. Ela está:', ['Fazendo algo sem relação com ciência', 'Usando raciocínio científico: compara com condições controladas', 'Fazendo pseudociência', 'Apenas dando uma opinião'], 1, 'Ciência é um método, não um uniforme. Comparar em condições iguais é a base do teste controlado.')],
analogia='A ciência funciona como um tribunal em que as ideias são as rés e a natureza é a testemunha. Ninguém é condenado ou absolvido porque é simpático ou importante: vale o que as provas mostram. E o caso pode ser reaberto se surgir prova nova.',
crianca='Imagine que você acha que a planta cresce mais com música. Em vez de só acreditar, você coloca duas plantas iguais, uma com música e outra sem, e vê qual cresce mais. Isso é ciência: perguntar e depois conferir.',
obj=['Explicar ciência como um modo de testar ideias contra a realidade.', 'Distinguir ciência como método, como corpo de conhecimento e como instituição.', 'Dizer por que a autocorreção é uma força, e não uma fraqueza.'],
caso=('Seu tio diz: “a ciência muda de ideia toda hora, então não dá pra confiar nela”.', 'Mudar de ideia é motivo para desconfiar ou para confiar?', 'Mudar diante de evidência nova é o que torna a ciência confiável. Um método que nunca muda de ideia não tem como descobrir os próprios erros.'),
erro=('“Científico é o que está provado para sempre.”', 'Conhecimento científico é o mais bem testado que temos, mas continua aberto a revisão. Parte dele é tão sólido que só uma montanha de evidências o mudaria.'),
ferr='ciencia-ou-pseudociencia', pre=[],
guardar=['Ciência é testar ideias contra a realidade, de forma pública e aberta a contestação.', 'Ela é método, conhecimento acumulado e instituição; o método corrige as outras duas.', 'Mudar diante de evidência nova é a força da ciência, não sua fraqueza.'],
pensar='Pense numa crença sua sobre saúde ou alimentação. Que observação mostraria que ela está errada?'),

dict(slug='opiniao-crenca-e-conhecimento', grupo='O básico', titulo='Opinião, crença e conhecimento', temas=['fundamentos', 'epistemologia'],
resumo='Nem toda opinião vale o mesmo. Gosto não se discute, mas afirmações sobre o mundo podem ser verdadeiras ou falsas, e a evidência decide.',
corpo='''
<p class="abre">“É a minha opinião, e eu tenho direito a ela.” A frase é verdadeira no sentido político: ninguém deve ser punido por pensar diferente. Mas é falsa se quiser dizer que toda opinião vale o mesmo. Sobre o formato da Terra, a opinião de quem mediu vale mais do que a de quem chutou.</p>
<h2>Três coisas diferentes</h2>
<div class="tabela"><table><thead><tr><th></th><th>O que é</th><th>Exemplo</th></tr></thead><tbody>
<tr><td><strong>Preferência</strong></td><td>Gosto pessoal; não é verdadeiro nem falso</td><td>“Prefiro chocolate a baunilha.”</td></tr>
<tr><td><strong>Crença</strong></td><td>Tomar algo como verdadeiro sobre o mundo; pode estar certo ou errado</td><td>“Vai chover amanhã.”</td></tr>
<tr><td><strong>Conhecimento</strong></td><td>Crença verdadeira e bem justificada</td><td>“A água ferve a 100 °C ao nível do mar.”</td></tr>
</tbody></table></div>
<p>A palavra “opinião” costuma misturar as duas primeiras. Quando alguém diz “na minha opinião, vacinas causam autismo”, isso não é uma preferência, como gostar de azul. É uma <strong>afirmação sobre o mundo</strong>, e afirmações sobre o mundo podem ser checadas. Neste caso, foram checadas em estudos com milhões de crianças, e são falsas.</p>
<h2>Opinião informada e opinião desinformada</h2>
<p>Há opiniões que se apoiam em evidências e opiniões que não se apoiam em nada. Há também opiniões sobre temas em aberto, em que pessoas bem informadas discordam, e opiniões sobre temas já resolvidos. Ter direito de falar não é o mesmo que ter razão.</p>
<ul><li><strong>Em aberto:</strong> qual a melhor política para reduzir a criminalidade? Há evidências parciais, e valores entram no jogo.</li><li><strong>Bem estabelecido:</strong> a Terra gira em torno do Sol; o tabaco causa câncer; o clima está esquentando por ação humana.</li></ul>
<h2>Graus de confiança</h2>
<p>Pensar cientificamente não é ter certeza de tudo. É ajustar a confiança à força da evidência: muita confiança onde a evidência é forte, pouca onde é fraca, e dizer “não sei” quando não há evidência. Uma pessoa que diz “tenho 90% de certeza” e outra que diz “tenho 50%” estão sendo mais honestas do que alguém que tem 100% de certeza sobre tudo.</p>
<div class="nota"><strong>Fato e valor.</strong> “O imposto X reduziu a desigualdade” é uma afirmação de fato, que dados podem testar. “Devemos reduzir a desigualdade” é uma afirmação de valor, que pede argumentos éticos. Boa parte das brigas fica mais clara quando se separa uma coisa da outra.</div>''',
fontes=[('Belief (Stanford Encyclopedia of Philosophy)', SEP + 'belief/'), ('Fato e valor (Wikipédia)', WE + 'Fact%E2%80%93value_distinction'), ('Credence (Stanford Encyclopedia: Formal Representations of Belief)', SEP + 'formal-belief/')],
quiz=[('Qual destas é uma preferência, e não uma crença sobre o mundo?', ['A Lua tem crateras', 'Prefiro filmes de terror a comédias', 'O açúcar causa cárie', 'Amanhã vai fazer sol'], 1, 'Preferências são gostos; não são verdadeiras nem falsas.'),
 ('“Na minha opinião, a Terra é plana.” Isso é:', ['Uma preferência pessoal que não se discute', 'Uma afirmação sobre o mundo que a evidência contradiz', 'Uma questão de valor', 'Um tema em aberto na ciência'], 1, 'Chamar de opinião não tira o caráter de afirmação factual, e esta foi refutada.'),
 ('Uma pessoa diz “tenho uns 70% de confiança de que esse remédio funciona, os estudos ainda são poucos”. Ela está:', ['Sendo indecisa, o que é ruim', 'Ajustando a confiança à força da evidência', 'Fazendo pseudociência', 'Confundindo fato e valor'], 1, 'Calibrar a confiança é uma virtude científica.')],
analogia='Pense num cardápio e num mapa. O cardápio é sobre o que você gosta, e ninguém pode dizer que sua escolha está errada. O mapa é sobre onde as coisas estão, e um mapa que coloca o rio no lugar errado está errado, por mais que o dono goste dele.',
crianca='Gostar mais de azul do que de vermelho é só seu, ninguém pode dizer que está errado. Mas dizer que o céu é verde dá para conferir olhando para cima. Algumas coisas são gosto, outras dá para checar.',
obj=['Distinguir preferência, crença e conhecimento.', 'Reconhecer quando uma “opinião” é, na verdade, uma afirmação sobre o mundo que pode ser checada.', 'Explicar a ideia de graus de confiança proporcionais à evidência.'],
caso=('Num grupo de família, alguém compartilha que chá de boldo cura câncer e, quando questionado, responde: “cada um tem sua opinião”.', 'Essa resposta encerra a discussão?', 'Não. “Cura câncer” é uma afirmação sobre o mundo, que pode ser testada. Ter direito de dizer algo não torna o algo verdadeiro.'),
erro=('“Toda opinião merece o mesmo respeito.”', 'Toda pessoa merece respeito; nem toda opinião merece o mesmo crédito. Afirmações sobre o mundo valem pelo apoio que têm na evidência.'),
ferr='opiniao-crenca-ou-conhecimento', pre=['o-que-e-ciencia'],
guardar=['Preferências não se discutem; crenças sobre o mundo podem estar certas ou erradas.', 'Chamar algo de “opinião” não o protege da evidência.', 'Pensar bem é ajustar a confiança à força da evidência, inclusive dizendo “não sei”.'],
pensar='Qual crença sua você defende com mais certeza do que a evidência permite?'),

dict(slug='crenca-verdadeira-justificada', grupo='O básico', titulo='Crença verdadeira justificada', temas=['epistemologia'],
resumo='Desde Platão, conhecer algo exige três coisas: acreditar, que seja verdade e ter boas razões. Sem justificação, acertar é sorte.',
corpo='''
<p class="abre">O que é preciso para dizer “eu sei”? No diálogo <em>Teeteto</em>, Platão discute uma resposta que virou clássica: conhecimento é <strong>crença verdadeira justificada</strong>. São três condições, e cada uma tem um papel.</p>
<h2>As três condições</h2>
<ol><li><strong>Crença.</strong> Você precisa acreditar. Não dá para saber que a reunião é às 15h se você acha que é às 16h.</li><li><strong>Verdade.</strong> O que você acredita precisa ser o caso. Ninguém “sabia” que a Terra era o centro do universo; as pessoas acreditavam, e estavam erradas.</li><li><strong>Justificação.</strong> Você precisa ter boas razões. Quem aposta no número 17 da roleta e acerta não <em>sabia</em> que ia dar 17; teve sorte.</li></ol>
<p>A terceira condição é a mais interessante para a ciência. Justificação é o que separa conhecimento de palpite certeiro. E é exatamente o que o método científico tenta produzir: boas razões para acreditar.</p>
<h2>O que conta como justificação?</h2>
<ul><li><strong>Percepção:</strong> vi com os próprios olhos, em boas condições.</li><li><strong>Raciocínio:</strong> deduzi de premissas verdadeiras.</li><li><strong>Memória:</strong> lembro bem, e minha memória costuma ser confiável nisso.</li><li><strong>Testemunho:</strong> uma fonte confiável me disse. A maior parte do que sabemos sobre ciência vem daqui: ninguém refaz todos os experimentos da física.</li><li><strong>Evidência acumulada:</strong> muitos testes independentes apontam na mesma direção.</li></ul>
<p>Cada fonte pode falhar. Olhos se enganam, memórias se distorcem, testemunhas mentem. Por isso a ciência combina várias fontes e prefere as que podem ser conferidas por outras pessoas.</p>
<h2>O problema de Gettier</h2>
<p>Em 1963, o filósofo Edmund Gettier publicou um artigo de três páginas mostrando casos em que alguém tem uma crença verdadeira e justificada, mas parece não saber. Exemplo: você olha para um relógio parado que, por acaso, marca a hora certa. Sua crença é verdadeira e justificada (relógios costumam funcionar), mas acertou por sorte. O debate sobre o que falta continua até hoje, e há uma lição no nível Intermediário sobre ele.</p>
<div class="nota"><strong>Para a vida prática:</strong> antes de dizer “eu sei”, pergunte “como eu sei?”. Se a resposta for “porque li num grupo de mensagens”, a justificação é fraca, mesmo que a crença por acaso seja verdadeira.</div>''',
fontes=[('The Analysis of Knowledge (Stanford Encyclopedia of Philosophy)', SEP + 'knowledge-analysis/'), ('Is Justified True Belief Knowledge?', 'https://www.jstor.org/stable/3326922'), ('Teeteto (Wikipédia)', WP + 'Teeteto')],
quiz=[('Quais são as três condições clássicas do conhecimento?', ['Crença, verdade e justificação', 'Fé, tradição e autoridade', 'Observação, hipótese e lei', 'Dúvida, pesquisa e certeza'], 0, 'Conhecimento, na análise clássica, é crença verdadeira justificada.'),
 ('Alguém chuta a resposta de uma prova e acerta. Por que isso não é conhecimento?', ['Porque a resposta é falsa', 'Porque faltou justificação: acertou por sorte', 'Porque ele não acreditava na resposta', 'Porque provas não medem conhecimento'], 1, 'Sem boas razões, acertar é sorte, não saber.'),
 ('Você olha um relógio parado que, por coincidência, marca a hora certa. Esse caso ficou famoso por quê?', ['Mostra que relógios não são confiáveis', 'Mostra uma crença verdadeira e justificada que parece não ser conhecimento', 'Mostra que a percepção nunca justifica', 'Mostra que a verdade não importa'], 1, 'É um caso de Gettier: as três condições estão presentes e ainda assim falta algo.')],
analogia='Conhecimento é como chegar a um destino. Acreditar é querer ir, a verdade é o lugar existir de fato, e a justificação é ter seguido um mapa confiável. Quem chegou dirigindo de olhos fechados também chegou, mas ninguém diria que sabia o caminho.',
crianca='Se você adivinha quantas balas tem no pote e acerta, foi sorte. Se você contou uma por uma, você sabe. Saber é acertar porque você tem um bom motivo.',
obj=['Enunciar as três condições da análise clássica do conhecimento.', 'Explicar por que a justificação separa conhecimento de palpite certeiro.', 'Descrever em linhas gerais o problema de Gettier.'],
caso=('Uma amiga diz que “sabia” que o time ia ganhar, porque sonhou com o placar, e o placar se confirmou.', 'Ela sabia ou acertou?', 'Ela acreditou e acertou, mas um sonho não é boa razão. Faltou justificação: foi palpite certeiro, não conhecimento.'),
erro=('“Se é verdade e eu acredito, então eu sei.”', 'Falta a terceira condição: boas razões. Sem elas, uma crença verdadeira é sorte.'),
ferr='opiniao-crenca-ou-conhecimento', pre=['opiniao-crenca-e-conhecimento'],
guardar=['Conhecimento clássico = crença + verdade + justificação.', 'A justificação é o que separa saber de acertar por sorte; produzi-la é o trabalho da ciência.', 'Gettier mostrou que talvez as três condições não bastem, e o debate segue aberto.'],
pensar='Escolha algo que você diz saber sobre ciência. De onde vem a sua justificação: percepção, raciocínio, memória ou testemunho?'),

dict(slug='postura-cientifica', grupo='O básico', titulo='A postura científica', temas=['fundamentos', 'mente'],
resumo='Pensar como cientista é um hábito: duvidar com método, pedir evidência proporcional à afirmação e estar disposto a mudar de ideia.',
corpo='''
<p class="abre">Não é preciso trabalhar num laboratório para ter uma postura científica. Trata-se de um conjunto de hábitos mentais que qualquer pessoa pode treinar, e que valem tanto para uma pesquisa sobre câncer quanto para decidir se uma notícia é verdadeira.</p>
<h2>Os hábitos</h2>
<ul class="lista-forte">
<li><strong>Ceticismo, não cinismo.</strong> Duvidar não é rejeitar tudo; é pedir razões antes de aceitar. O cínico diz “é tudo mentira”; o cético pergunta “como sabemos?”.</li>
<li><strong>Evidência proporcional à afirmação.</strong> A frase popularizada por Carl Sagan diz que afirmações extraordinárias exigem evidências extraordinárias. Que seu vizinho tem um cachorro, basta ele dizer. Que tem um dragão na garagem, não.</li>
<li><strong>Procurar o que derrubaria a ideia.</strong> Em vez de colecionar casos a favor, perguntar: o que eu deveria ver se eu estivesse errado? E ir procurar isso.</li>
<li><strong>Separar a ideia da identidade.</strong> Quem se sente atacado quando sua crença é contestada tende a defendê-la a qualquer custo. Quem trata a crença como hipótese consegue trocá-la.</li>
<li><strong>Humildade sobre os próprios vieses.</strong> Todo cérebro tende a ver o que quer ver. A postura científica não presume ser imune a isso; cria procedimentos para se proteger, como testes cegos.</li>
<li><strong>Dizer “não sei”.</strong> É uma das frases mais científicas que existem. Lacunas no conhecimento não são licença para preenchê-las com a primeira explicação disponível.</li>
<li><strong>Mudar de ideia quando a evidência pede.</strong> E não mudar só porque alguém insistiu ou gritou mais alto.</li></ul>
<h2>O que a postura científica não é</h2>
<p>Não é arrogância. Muita gente confunde pensamento científico com desprezo por quem acredita em outra coisa. Mas a postura científica começa por aplicar a dúvida a si mesmo. Também não é aceitar tudo o que um cientista diz: a autoridade de alguém conta como indício, mas o que decide é a evidência que ele apresenta, e o consenso de muitos especialistas vale mais do que a opinião de um só.</p>
<h2>A mentalidade de soldado e a de batedor</h2>
<p>A escritora Julia Galef propôs uma imagem útil. O <em>soldado</em> raciocina para defender uma posição: cada argumento é munição. O <em>batedor</em> (o explorador que vai à frente para mapear o terreno) raciocina para ver as coisas como são, mesmo que o mapa traga notícias ruins. A postura científica é a do batedor.</p>
<div class="nota"><strong>Exercício rápido:</strong> antes de compartilhar uma notícia que confirma o que você já pensava, pergunte se você a aceitaria com a mesma facilidade se ela dissesse o contrário.</div>''',
fontes=[('O Mundo Assombrado pelos Demônios', 'https://www.google.com/search?tbm=bks&q=O+Mundo+Assombrado+pelos+Dem%C3%B4nios'), ('The Scout Mindset', 'https://www.google.com/search?tbm=bks&q=The+Scout+Mindset'), ('Scientific skepticism (Wikipédia)', WE + 'Scientific_skepticism')],
quiz=[('Qual a diferença entre ceticismo e cinismo?', ['Nenhuma, são sinônimos', 'O cético pede razões antes de aceitar; o cínico rejeita tudo de antemão', 'O cínico é mais científico', 'O cético nunca acredita em nada'], 1, 'Ceticismo é dúvida com método; cinismo é rejeição sem exame.'),
 ('Alguém afirma ter sido abduzido por alienígenas. Pela postura científica, você deveria:', ['Acreditar, pois não pode provar o contrário', 'Pedir evidência proporcional a uma afirmação tão extraordinária', 'Zombar da pessoa', 'Ignorar o assunto para sempre'], 1, 'Afirmações extraordinárias exigem evidências extraordinárias, sem desprezo pela pessoa.'),
 ('Você lê uma notícia que confirma exatamente o que você pensa sobre um político. O hábito científico é:', ['Compartilhar logo', 'Perguntar se aceitaria a notícia com a mesma facilidade se dissesse o contrário', 'Descartar, pois toda notícia é falsa', 'Acreditar, porque confirma o que você já sabia'], 1, 'Aplicar o mesmo rigor ao que nos agrada é a parte mais difícil, e a mais importante.')],
analogia='A postura científica é como a de um bom detetive. Ele não decide o culpado e depois procura provas; junta pistas, testa suspeitas e está pronto a descartar o suspeito favorito se uma pista nova apontar para outro lado.',
crianca='Ser cientista é como brincar de detetive: você tem um palpite, mas antes de dizer que é verdade, procura pistas. E se as pistas mostrarem que você errou, tudo bem, você muda o palpite.',
obj=['Listar os hábitos da postura científica.', 'Distinguir ceticismo de cinismo e de arrogância.', 'Aplicar a ideia de evidência proporcional à afirmação a casos do cotidiano.'],
caso=('Um vídeo diz que um famoso cientista “admitiu” que certa vacina é perigosa. Você nunca ouviu falar disso.', 'O que você faz antes de acreditar ou de rejeitar?', 'Procura a fonte original, vê se a fala foi tirada de contexto e checa o que o conjunto dos especialistas diz. A autoridade de um nome não substitui a evidência.'),
erro=('“Ser científico é desconfiar de tudo.”', 'Desconfiar de tudo paralisa e é tão pouco racional quanto acreditar em tudo. O cético distribui a confiança conforme a evidência.'),
ferr='ciencia-ou-pseudociencia', pre=['o-que-e-ciencia'],
guardar=['Ceticismo é pedir razões, não rejeitar tudo.', 'Afirmações extraordinárias exigem evidências extraordinárias.', 'O hábito mais difícil é aplicar a mesma dúvida ao que confirma o que já pensamos.'],
pensar='Qual foi a última vez que você mudou de ideia sobre algo importante por causa de evidência? Se não lembra, por quê?'),

dict(slug='o-metodo-cientifico', grupo='Como a ciência funciona', titulo='O método científico', temas=['metodo'],
resumo='Observar, perguntar, formular uma hipótese, prever, testar e revisar: o ciclo que transforma palpites em conhecimento, e por que ele é menos linear do que parece.',
corpo='''
<p class="abre">Nos livros escolares, o método científico aparece como uma receita de seis passos. Na prática, é mais um ciclo do que uma escada, e cientistas pulam etapas, voltam atrás e trabalham em várias ao mesmo tempo. Mas a lógica por trás é sempre a mesma: <strong>fazer previsões arriscadas e conferir</strong>.</p>
<h2>O ciclo básico</h2>
<ol><li><strong>Observação.</strong> Algo chama a atenção. No século XIX, o médico Ignaz Semmelweis notou que mulheres morriam muito mais de febre puerperal na ala atendida por médicos do que na atendida por parteiras.</li>
<li><strong>Pergunta.</strong> Por que essa diferença?</li>
<li><strong>Hipótese.</strong> Uma explicação possível, que pode estar errada. Semmelweis suspeitou que os médicos, que vinham direto das autópsias, levavam “partículas cadavéricas” nas mãos.</li>
<li><strong>Previsão.</strong> Se a hipótese estiver certa, o que deve acontecer? Se os médicos lavarem as mãos com cloro, as mortes devem cair.</li>
<li><strong>Teste.</strong> Ele instituiu a lavagem das mãos. A mortalidade caiu de cerca de 10% para perto de 1%.</li>
<li><strong>Revisão e comunicação.</strong> O resultado é publicado, criticado, repetido por outros, e a hipótese é aceita, ajustada ou descartada.</li></ol>
<p>O caso tem um final amargo: os colegas de Semmelweis rejeitaram a ideia, em parte porque ofendia os médicos e em parte porque ele não tinha uma teoria do mecanismo. A teoria dos germes, de Pasteur e Koch, veio décadas depois e deu a explicação. A história mostra que o método funciona, mas as pessoas que o usam resistem.</p>
<h2>O coração do método: a previsão arriscada</h2>
<p>Uma boa hipótese diz algo que <strong>poderia dar errado</strong>. “Lavar as mãos reduz as mortes” podia ter falhado no teste. Uma ideia que se encaixa em qualquer resultado não está sendo testada. O filósofo Karl Popper fez disso o centro da sua filosofia da ciência, como você verá no nível Intermediário.</p>
<h2>Não existe um método só</h2>
<p>Astrônomos não podem fazer experimentos com estrelas; observam. Paleontólogos reconstroem o passado a partir de fósseis. Epidemiologistas comparam populações. Matemáticos provam teoremas. O que une essas práticas não é uma receita fixa, mas valores comuns: testar ideias, controlar fontes de erro, tornar o trabalho público e aceitar a crítica.</p>
<div class="nota"><strong>Indução e dedução.</strong> Ir de muitas observações para uma regra geral (todo cisne que vi é branco, logo todos são) é indução. Ir da regra para uma previsão particular (se todos são brancos, o próximo será) é dedução. A ciência usa as duas, e a indução tem um problema famoso, tema de uma lição do nível Intermediário.</div>''',
fontes=[('Scientific Method (Stanford Encyclopedia of Philosophy)', SEP + 'scientific-method/'), ('Ignaz Semmelweis (Wikipédia)', WP + 'Ignaz_Semmelweis'), ('Método científico (Wikipédia)', WP + 'M%C3%A9todo_cient%C3%ADfico')],
quiz=[('Qual é o coração do método científico, segundo a lição?', ['Seguir seis passos sempre na mesma ordem', 'Fazer previsões que poderiam dar errado e conferir', 'Usar equipamentos caros', 'Concordar com a maioria dos cientistas'], 1, 'Uma hipótese testável arrisca uma previsão que a realidade pode desmentir.'),
 ('Por que os colegas de Semmelweis rejeitaram a lavagem das mãos?', ['Porque os dados mostravam o contrário', 'Em parte por ofender os médicos e por falta de um mecanismo explicativo', 'Porque a lavagem aumentou as mortes', 'Porque ele não publicou nada'], 1, 'O caso mostra que o método funciona, mas as pessoas resistem a resultados incômodos.'),
 ('Uma pessoa diz que um amuleto traz sorte: se algo bom acontece, foi o amuleto; se algo ruim acontece, seria pior sem ele. O problema é:', ['O amuleto é caro', 'A ideia se encaixa em qualquer resultado, então não arrisca nenhuma previsão', 'Faltou grupo controle de amuletos', 'Não há problema'], 1, 'Uma ideia que nenhum resultado pode contrariar não está sendo testada.')],
analogia='O método científico é como testar uma receita nova. Você tem um palpite (mais fermento deixa o bolo mais fofo), prevê o resultado, assa dois bolos iguais exceto pelo fermento e compara. Se o bolo murchar, você aprendeu algo, mesmo que não fosse o que esperava.',
crianca='Você acha que o gelo derrete mais rápido no sol. Então coloca um gelo no sol e outro na sombra e espera. Se o do sol derreter primeiro, seu palpite passou no teste.',
obj=['Descrever o ciclo observação, pergunta, hipótese, previsão, teste e revisão.', 'Explicar por que uma boa hipótese precisa poder dar errado.', 'Reconhecer que diferentes ciências usam métodos diferentes com valores comuns.'],
caso=('Você nota que dorme pior nos dias em que toma café à tarde.', 'Como testaria isso de forma mais confiável do que só “reparar”?', 'Defina uma previsão (dormir pior nos dias com café), alterne dias com e sem café de forma planejada, anote a qualidade do sono sem olhar o calendário e compare. É o ciclo do método em miniatura.'),
erro=('“O método científico é uma receita fixa de seis passos.”', 'É um ciclo flexível. Astronomia, paleontologia e epidemiologia testam ideias de jeitos diferentes; o que une todas é testar, controlar o erro e aceitar crítica.'),
ferr='ciencia-ou-pseudociencia', pre=['o-que-e-ciencia'],
guardar=['O método é um ciclo: observar, perguntar, hipotetizar, prever, testar e revisar.', 'Uma boa hipótese arrisca uma previsão que poderia falhar.', 'Não há um método único: há valores comuns de teste, controle do erro e crítica pública.'],
pensar='Que crença do seu dia a dia você poderia testar com um pequeno experimento caseiro?'),

dict(slug='hipotese-teoria-e-lei', grupo='Como a ciência funciona', titulo='Hipótese, teoria e lei', temas=['metodo', 'fundamentos'],
resumo='“É só uma teoria” é um erro de vocabulário. Em ciência, teoria é uma explicação ampla e muito testada, não um palpite.',
corpo='''
<p class="abre">“A evolução é só uma teoria.” A frase usa “teoria” no sentido do dia a dia, de palpite. Em ciência, a palavra quer dizer quase o oposto: uma explicação ampla, apoiada por muitas evidências e que já resistiu a muitos testes.</p>
<h2>Os termos</h2>
<div class="tabela"><table><thead><tr><th>Termo</th><th>O que é</th><th>Exemplo</th></tr></thead><tbody>
<tr><td><strong>Fato / observação</strong></td><td>Algo observado e confirmado</td><td>Objetos soltos caem; espécies fósseis diferem das atuais</td></tr>
<tr><td><strong>Hipótese</strong></td><td>Explicação proposta, ainda em teste</td><td>“Esta bactéria causa esta úlcera”</td></tr>
<tr><td><strong>Lei</strong></td><td>Descrição de uma regularidade, muitas vezes em forma matemática</td><td>Lei da gravitação: a força cai com o quadrado da distância</td></tr>
<tr><td><strong>Teoria</strong></td><td>Explicação ampla e testada que une muitos fatos e leis</td><td>Teoria da evolução, teoria atômica, relatividade, teoria dos germes</td></tr>
</tbody></table></div>
<h2>Lei não é teoria “promovida”</h2>
<p>É comum achar que uma hipótese vira teoria e, se for muito confirmada, vira lei. Não é assim. Leis e teorias fazem trabalhos diferentes: a lei diz <strong>o que</strong> acontece (descreve), a teoria diz <strong>por que</strong> acontece (explica). A lei da gravitação de Newton descreve como os corpos se atraem; a relatividade geral de Einstein explica a gravidade como curvatura do espaço-tempo. Uma teoria nunca “sobe” para lei.</p>
<h2>Por que teorias são valiosas</h2>
<p>Uma boa teoria faz três coisas: <strong>explica</strong> muitos fatos diferentes com poucos princípios, <strong>prevê</strong> fatos ainda não observados e <strong>orienta</strong> novas pesquisas. A teoria da evolução explica a semelhança entre espécies, a distribuição geográfica dos seres vivos, a resistência a antibióticos e o registro fóssil. Previu que encontraríamos formas de transição, como o <em>Tiktaalik</em>, peixe com traços de anfíbio, achado em 2004 nas rochas da idade prevista.</p>
<h2>Teorias são definitivas?</h2>
<p>Não, mas isso não as torna frágeis. A mecânica de Newton foi superada pela relatividade em velocidades altíssimas e campos gravitacionais intensos, e continua valendo, com precisão excelente, para lançar foguetes e construir pontes. Quando uma teoria madura é substituída, a nova costuma incluir a antiga como caso particular.</p>
<div class="nota"><strong>Dica de leitura:</strong> quando ler “cientistas acreditam”, troque mentalmente por “as evidências indicam”. E quando ler “é só uma teoria”, lembre que a gravidade também é explicada por uma.</div>''',
fontes=[('Scientific theory (Wikipédia)', WE + 'Scientific_theory'), ('Teaching About Evolution and the Nature of Science (National Academies)', 'https://nap.nationalacademies.org/catalog/5787/'), ('Tiktaalik (Wikipédia)', WP + 'Tiktaalik')],
quiz=[('Em ciência, uma teoria é:', ['Um palpite sem provas', 'Uma explicação ampla e muito testada que une muitos fatos', 'Uma lei ainda não confirmada', 'Uma opinião de um cientista'], 1, 'Teoria científica é o nível mais alto de explicação, não um chute.'),
 ('Qual a diferença entre lei e teoria?', ['Lei é teoria confirmada', 'A lei descreve o que acontece; a teoria explica por quê', 'Teoria é mais certa que lei', 'Não há diferença'], 1, 'Leis descrevem regularidades; teorias explicam. Uma não vira a outra.'),
 ('Alguém diz que não precisa levar a sério a evolução porque “é só uma teoria”. O melhor contraponto é:', ['Concordar, pois teoria é palpite', 'Explicar que, em ciência, teoria é explicação muito testada, como a teoria dos germes', 'Dizer que a evolução já virou lei', 'Mudar de assunto'], 1, 'O erro é de vocabulário: no sentido científico, teoria é o contrário de palpite.')],
analogia='Pense num quebra-cabeça. Os fatos são as peças, as leis são padrões que você nota (as peças de borda são retas) e a teoria é a imagem da tampa da caixa, que explica por que cada peça tem aquele formato e onde ela vai.',
crianca='Hipótese é quando você acha que sabe por que algo acontece, mas ainda vai conferir. Teoria é quando muita gente conferiu muitas vezes e a explicação continuou funcionando.',
obj=['Distinguir fato, hipótese, lei e teoria.', 'Explicar por que uma teoria não “vira” lei.', 'Responder ao argumento “é só uma teoria”.'],
caso=('Num debate, alguém diz: “nem os cientistas têm certeza, tanto que chamam de teoria”.', 'O que essa frase confunde?', 'Confunde o sentido popular (palpite) com o científico (explicação ampla e testada). Teoria atômica e teoria dos germes também se chamam teorias.'),
erro=('“Hipótese confirmada vira teoria, e teoria confirmada vira lei.”', 'Leis descrevem regularidades, teorias as explicam. São tipos diferentes de conhecimento, não degraus de uma escada.'),
ferr=None, pre=['o-metodo-cientifico'],
guardar=['Teoria científica é explicação ampla e testada, não palpite.', 'Leis descrevem o que acontece; teorias explicam por quê.', 'Teorias substituídas costumam continuar valendo como casos particulares.'],
pensar='Que outra palavra tem um sentido no dia a dia e outro na ciência (por exemplo, “significativo” ou “natural”)?'),

dict(slug='experimentos-e-grupo-controle', grupo='Como a ciência funciona', titulo='Experimentos, grupo controle e placebo', temas=['metodo', 'evidencias'],
resumo='Para saber se algo funciona, é preciso comparar com quem não recebeu. Grupo controle, sorteio e testes cegos protegem o resultado dos nossos vieses.',
corpo='''
<p class="abre">Você tomou um chá e o resfriado passou em cinco dias. O chá funcionou? Não dá para saber: resfriados costumam passar sozinhos em uns cinco dias. Para saber se algo funciona, é preciso perguntar <strong>em comparação com o quê?</strong></p>
<h2>O grupo controle</h2>
<p>Um experimento compara dois grupos que só diferem numa coisa: o que está sendo testado. Um grupo recebe o tratamento; o outro, o <strong>grupo controle</strong>, não recebe. Se o primeiro melhora mais, a diferença pode ser atribuída ao tratamento.</p>
<p>Em 1747, o médico escocês James Lind dividiu doze marinheiros com escorbuto em seis duplas e deu a cada dupla um tratamento: sidra, vinagre, água do mar, laranjas e limões, entre outros. Os que comeram cítricos se recuperaram em dias. É um dos primeiros ensaios comparativos registrados.</p>
<h2>Três proteções contra o erro</h2>
<ul><li><strong>Sorteio (randomização).</strong> Se o médico escolhe quem recebe o remédio, pode, sem perceber, escolher os pacientes menos graves. Sortear distribui as diferenças por acaso entre os grupos.</li>
<li><strong>Cegamento.</strong> Se o paciente sabe que está tomando o remédio, a expectativa já muda como ele se sente. No teste <em>cego</em>, o participante não sabe em que grupo está. No <em>duplo-cego</em>, nem quem aplica e avalia sabe.</li>
<li><strong>Amostra grande o bastante.</strong> Com poucos participantes, o acaso pesa demais. Um resultado com dez pessoas pode sumir quando se testa com mil.</li></ul>
<h2>O efeito placebo</h2>
<p>Placebo é uma substância ou procedimento sem efeito específico, como uma pílula de açúcar. Pessoas que o recebem muitas vezes relatam melhora, principalmente em sintomas subjetivos como dor e náusea. Parte disso é expectativa; parte é a melhora natural da doença e a regressão à média (quem procura tratamento num dia muito ruim tende a estar melhor depois, de qualquer jeito).</p>
<p>Por isso um novo remédio não precisa só funcionar: precisa funcionar <strong>melhor do que o placebo</strong>. Muitos tratamentos populares, quando testados assim, não passam desse teste.</p>
<h2>Quando não dá para fazer experimento</h2>
<p>Não se pode sortear pessoas para fumar por trinta anos. Nesses casos, a ciência usa <strong>estudos observacionais</strong>: acompanha quem já fuma e quem não fuma e compara, tentando controlar outras diferenças (idade, renda, profissão). São mais sujeitos a erro, mas, quando muitos estudos diferentes apontam na mesma direção, como no caso do tabaco e do câncer de pulmão, a conclusão fica muito sólida.</p>
<div class="nota"><strong>Pergunta-chave:</strong> diante de qualquer afirmação “X funciona”, pergunte: comparado com o quê, em quantas pessoas, e quem sabia quem recebeu o quê?</div>''',
fontes=[('Randomized controlled trial (Wikipédia)', WE + 'Randomized_controlled_trial'), ('James Lind (Wikipédia)', WP + 'James_Lind'), ('Placebo (Wikipédia)', WP + 'Placebo'), ('Testing Treatments', 'https://www.testingtreatments.org/')],
quiz=[('Para que serve o grupo controle?', ['Para economizar remédio', 'Para ter com o que comparar e saber se a diferença vem do tratamento', 'Para dar placebo a quem não merece tratamento', 'Para aumentar a amostra'], 1, 'Sem comparação, não há como separar o efeito do tratamento da melhora natural.'),
 ('O que é um teste duplo-cego?', ['Os participantes usam vendas', 'Nem os participantes nem quem aplica e avalia sabem quem recebe o quê', 'Dois grupos tomam placebo', 'O teste é repetido duas vezes'], 1, 'O duplo-cego impede que expectativas de pacientes e pesquisadores contaminem o resultado.'),
 ('Uma clínica diz que 80% dos pacientes melhoraram de dor nas costas com seu tratamento. O que falta saber antes de se impressionar?', ['O preço do tratamento', 'Quantos melhorariam sem tratamento ou com placebo', 'A cor da clínica', 'Nada, 80% é muito'], 1, 'Dor nas costas costuma melhorar sozinha. Sem grupo controle, o número não diz nada sobre o tratamento.')],
analogia='Testar um remédio sem grupo controle é como dizer que seu guarda-chuva mágico fez a chuva parar. A chuva ia parar de qualquer jeito; para saber se o guarda-chuva fez diferença, você precisaria comparar com dias em que não o abriu.',
crianca='Se você quer saber se um adubo faz a plantinha crescer, precisa de duas plantinhas: uma com adubo e outra sem. Se só tiver uma, não dá para saber se ela cresceria igual sem o adubo.',
obj=['Explicar por que um experimento precisa de grupo controle.', 'Descrever o papel do sorteio, do cegamento e do tamanho da amostra.', 'Explicar o efeito placebo e por que tratamentos precisam superá-lo.'],
caso=('Sua avó jura que um xarope caseiro cura gripe: “sempre que tomo, em uma semana estou boa”.', 'O que esse relato não consegue mostrar?', 'Gripe costuma passar em cerca de uma semana. Sem comparar com quem não tomou o xarope, não dá para saber se ele fez alguma diferença.'),
erro=('“Se a pessoa melhorou depois de tomar, o tratamento funcionou.”', 'Depois não é por causa de. A melhora pode ser natural, efeito placebo ou regressão à média. Só a comparação com um grupo controle separa essas causas.'),
ferr='ciencia-ou-pseudociencia', pre=['o-metodo-cientifico'],
guardar=['Sem grupo controle não há como saber se o tratamento fez diferença.', 'Sorteio, cegamento e amostras grandes protegem o resultado dos nossos vieses.', 'Um tratamento precisa funcionar melhor do que o placebo, não só “funcionar”.'],
pensar='Que produto ou tratamento você já usou porque “funcionou comigo”? Como saberia se ele funcionou mesmo?'),

dict(slug='niveis-de-evidencia', grupo='Como a ciência funciona', titulo='Níveis de evidência', temas=['evidencias'],
resumo='Um relato pessoal, um estudo com ratos e uma revisão de cem ensaios clínicos não valem o mesmo. Conheça a pirâmide da evidência.',
corpo='''
<p class="abre">“Um estudo mostrou que…” é uma das frases mais enganosas do jornalismo. Que tipo de estudo? Com quantas pessoas? Em humanos ou em ratos? Nem toda evidência vale o mesmo, e conhecer a hierarquia ajuda a não ser enganado.</p>
<h2>A pirâmide da evidência</h2>
<p>Na área da saúde, é comum organizar os tipos de estudo numa pirâmide, da evidência mais fraca para a mais forte:</p>
<ol><li><strong>Opinião de especialista e relatos de caso.</strong> Úteis para levantar hipóteses, fracos para concluir.</li>
<li><strong>Estudos em laboratório e em animais.</strong> Mostram mecanismos possíveis, mas muita coisa que funciona em células ou ratos falha em humanos.</li>
<li><strong>Estudos observacionais</strong> (caso-controle e coorte). Comparam pessoas que já têm ou não uma exposição. Bons para detectar associações, sujeitos a fatores de confusão.</li>
<li><strong>Ensaios clínicos randomizados.</strong> Sorteiam quem recebe o tratamento. O padrão-ouro para testar intervenções.</li>
<li><strong>Revisões sistemáticas e metanálises.</strong> Reúnem todos os bons estudos sobre uma pergunta e combinam os resultados. Ficam no topo, desde que os estudos reunidos sejam bons.</li></ol>
<h2>Por que o relato pessoal fica embaixo</h2>
<p>“Funcionou comigo” é a forma de evidência mais convincente para nós e uma das menos confiáveis. Uma pessoa não tem grupo controle, não sabe o que teria acontecido sem o tratamento e lembra mais dos acertos do que dos erros. Milhares de relatos também não somam um bom estudo: se forem todos do mesmo tipo, compartilham os mesmos defeitos.</p>
<h2>A pirâmide não é tudo</h2>
<ul><li>Um ensaio randomizado mal feito, pequeno ou financiado sem transparência pode valer menos do que um grande estudo observacional bem feito.</li><li>Algumas perguntas não admitem ensaio: ninguém vai sortear pessoas para pular de avião sem paraquedas. A evidência de que paraquedas funcionam vem de outro lugar.</li><li>O sistema GRADE, usado pela OMS e pela Cochrane, avalia a <strong>certeza</strong> da evidência levando em conta o desenho, a consistência entre estudos, a precisão e o risco de viés.</li></ul>
<h2>Fora da saúde</h2>
<p>A mesma lógica vale em outras áreas: uma única pesquisa de opinião vale menos do que a média de várias; um único experimento de psicologia vale menos do que vários que o repetiram; um dado isolado vale menos do que uma série histórica.</p>
<div class="nota"><strong>Na prática:</strong> quando ler “estudo prova”, procure três coisas: se foi em humanos, quantas pessoas participaram e se o resultado foi confirmado por outros estudos.</div>''',
fontes=[('Levels of evidence (Wikipédia)', WE + 'Levels_of_evidence'), ('GRADE Working Group', 'https://www.gradeworkinggroup.org/'), ('Cochrane: O que são revisões sistemáticas', 'https://www.cochrane.org/pt/about-us'), ('Parachute use to prevent death and major trauma (BMJ)', 'https://www.bmj.com/content/327/7429/1459')],
quiz=[('Qual tipo de evidência costuma ficar no topo da pirâmide?', ['Relato pessoal', 'Estudo em ratos', 'Revisões sistemáticas e metanálises de bons estudos', 'Opinião de um especialista famoso'], 2, 'Revisões sistemáticas reúnem e combinam todos os bons estudos sobre uma pergunta.'),
 ('Uma manchete diz: “Substância de fruta mata células de câncer”. O estudo foi feito em células numa placa. Isso significa que:', ['Comer a fruta cura câncer', 'É um resultado inicial; muitas coisas que funcionam em células falham em humanos', 'O estudo é falso', 'Deve-se parar a quimioterapia'], 1, 'Estudos em laboratório estão na base da pirâmide: levantam hipóteses, não provam tratamentos.'),
 ('Mil pessoas dão depoimentos de que um suplemento curou sua ansiedade. Isso equivale a um bom ensaio clínico?', ['Sim, mil é muita gente', 'Não: depoimentos não têm controle, sorteio nem cegamento, e somar mil deles soma os mesmos defeitos', 'Sim, se forem verdadeiros', 'Depende do preço'], 1, 'Quantidade de relatos não substitui qualidade de desenho.')],
analogia='A pirâmide da evidência é como a confiabilidade de testemunhas num julgamento. Um boato que alguém ouviu vale pouco; uma testemunha ocular vale mais; uma gravação de câmera vale mais ainda; e várias câmeras independentes mostrando a mesma coisa quase encerram o caso.',
crianca='Se um amigo diz que viu um disco voador, é legal, mas pode ter sido um avião. Se cem pessoas filmaram de lugares diferentes e os vídeos batem, aí fica muito mais difícil duvidar.',
obj=['Ordenar os principais tipos de estudo pela força da evidência.', 'Explicar por que relatos pessoais são evidência fraca.', 'Reconhecer limites da pirâmide e a ideia de certeza da evidência (GRADE).'],
caso=('Uma amiga manda um vídeo de um médico dizendo que um suplemento “tem estudos”.', 'Que perguntas você faria antes de acreditar?', 'Que tipo de estudo (em células, animais ou humanos), com quantas pessoas, com grupo controle e se outros estudos confirmaram. “Tem estudos” sozinho não diz nada.'),
erro=('“Tem um estudo que prova.”', 'Um estudo isolado raramente prova algo. O que conta é o tipo de estudo, a qualidade e se o conjunto da evidência aponta na mesma direção.'),
ferr='nivel-de-evidencia', pre=['experimentos-e-grupo-controle'],
guardar=['Nem toda evidência vale o mesmo: relato, laboratório, observação, ensaio e revisão sistemática formam uma escada.', '“Funcionou comigo” é convincente para nós e fraco como prova.', 'A qualidade e a consistência dos estudos importam tanto quanto o tipo.'],
pensar='Qual foi a última notícia de saúde que você leu? Em que degrau da pirâmide estava o estudo?'),

dict(slug='consenso-cientifico', grupo='Como a ciência funciona', titulo='Revisão por pares e consenso científico', temas=['evidencias', 'sociedade'],
resumo='Como a comunidade científica filtra erros e chega a acordos, por que o consenso merece peso e quando um cientista isolado tem razão.',
corpo='''
<p class="abre">Nenhum cientista sozinho é confiável o bastante. O que torna a ciência confiável é a forma como os cientistas se vigiam: publicam, criticam, repetem e, com o tempo, convergem. Esse processo tem nome: <strong>revisão por pares</strong> e formação de <strong>consenso</strong>.</p>
<h2>Revisão por pares</h2>
<p>Antes de um artigo ser publicado numa revista científica, ele é enviado a outros especialistas (os pares), em geral anônimos, que avaliam se os métodos são adequados, se as conclusões seguem dos dados e se algo importante foi ignorado. Muitos artigos são rejeitados ou voltam para correção.</p>
<p>A revisão por pares é um filtro, não um selo de verdade. Revisores não refazem os experimentos e podem deixar passar erros e até fraudes. Por isso um artigo publicado é o começo da conversa, não o fim. O teste real vem depois: outros grupos tentam reproduzir o resultado.</p>
<h2>Consenso científico</h2>
<p>Consenso é quando a grande maioria dos especialistas numa área concorda sobre uma conclusão, porque a evidência acumulada aponta para ela. Exemplos: a evolução das espécies, a segurança das vacinas aprovadas, o aquecimento global causado por humanos, a ligação entre tabaco e câncer.</p>
<p>O consenso não é uma votação nem uma opinião coletiva. É o <strong>resultado</strong> de muitos estudos independentes que convergem. Revisões como as do IPCC (clima) ou das academias nacionais de ciência sintetizam milhares de trabalhos.</p>
<h2>Mas e Galileu?</h2>
<p>Quem rejeita um consenso costuma se comparar a Galileu, que estava certo contra todos. Três observações:</p>
<ul><li>Galileu se opunha principalmente à autoridade religiosa e à tradição aristotélica, não a um consenso formado por testes. Ele venceu porque tinha evidência melhor, e a comunidade acabou aceitando.</li><li>Para cada Galileu, houve milhares de pessoas que se achavam Galileu e estavam erradas.</li><li>Consensos mudam, mas mudam por evidência nova publicada e testada, não por vídeos e postagens.</li></ul>
<h2>Como pesar o consenso no dia a dia</h2>
<p>Para quem não é especialista, apostar no consenso é a estratégia mais racional. Não porque a maioria nunca erra, mas porque a chance de um leigo estar certo contra milhares de especialistas que estudaram o tema por décadas é muito pequena. Divergir do consenso é legítimo para quem traz evidência nova, e o lugar para isso é o debate científico.</p>
<div class="nota"><strong>Cuidado com o falso equilíbrio:</strong> uma reportagem que coloca um climatologista e um negacionista frente a frente, com o mesmo tempo, passa a impressão de um debate meio a meio quando a divisão real entre especialistas é de quase todos contra pouquíssimos.</div>''',
fontes=[('Scientific consensus (Wikipédia)', WE + 'Scientific_consensus'), ('Peer review (Wikipédia)', WE + 'Peer_review'), ('IPCC: Sexto Relatório de Avaliação', 'https://www.ipcc.ch/assessment-report/ar6/'), ('Why Trust Science?', 'https://press.princeton.edu/books/hardcover/9780691179001/why-trust-science')],
quiz=[('A revisão por pares garante que um artigo está correto?', ['Sim, sempre', 'Não: é um filtro que reduz erros, mas o teste real vem com a reprodução por outros', 'Sim, se a revista for famosa', 'Não, ela não serve para nada'], 1, 'A revisão por pares filtra, mas não refaz experimentos. Reprodução independente é o teste de verdade.'),
 ('O que é consenso científico?', ['Uma votação entre cientistas', 'Concordância da maioria dos especialistas resultante de muitas evidências convergentes', 'A opinião do cientista mais famoso', 'O que a maioria da população acredita'], 1, 'Consenso é o resultado da evidência acumulada, não uma eleição.'),
 ('Um influenciador diz que é “como Galileu” por discordar de quase todos os climatologistas. O melhor contraponto é:', ['Ele tem razão por definição', 'Galileu venceu por ter evidência melhor, testada; discordar não basta, é preciso trazer evidência ao debate científico', 'Galileu estava errado', 'Ninguém pode discordar de cientistas'], 1, 'Ser minoria não torna alguém um Galileu. O que tornou Galileu certo foi a evidência.')],
analogia='O consenso científico funciona como o resultado de muitos árbitros independentes revendo a mesma jogada em ângulos diferentes. Um deles pode errar, mas quando quase todos, olhando de lugares diferentes, chegam à mesma conclusão, é muito provável que ela esteja certa.',
crianca='Se você pergunta a hora para uma pessoa, ela pode errar. Se pergunta para vinte pessoas com relógios diferentes e quase todas dizem a mesma hora, você pode confiar bastante.',
obj=['Explicar o que é revisão por pares e o que ela não garante.', 'Definir consenso científico como convergência de evidências.', 'Responder ao argumento “Galileu também estava sozinho”.'],
caso=('Um vídeo mostra “500 cientistas” assinando uma carta contra o consenso sobre o clima.', 'Isso muda o quadro?', 'Depende de quem são (muitos não são climatologistas) e do que eles trazem. Há dezenas de milhares de pesquisadores da área, e o que conta é a evidência publicada, não o número de assinaturas.'),
erro=('“Consenso é só a opinião da maioria; a ciência não se faz por votação.”', 'É verdade que não se faz por votação, e justamente por isso o consenso não é opinião: é o resultado de evidências independentes que convergem.'),
ferr=None, pre=['niveis-de-evidencia'],
guardar=['Revisão por pares é filtro, não garantia; a reprodução independente é o teste real.', 'Consenso é convergência de evidências, não votação.', 'Para leigos, apostar no consenso é a estratégia mais racional; divergir exige trazer evidência.'],
pensar='Sobre que tema você discorda da maioria dos especialistas? Que evidência você tem que eles não teriam considerado?'),

dict(slug='correlacao-e-causalidade', grupo='Como a ciência funciona', titulo='Correlação não é causalidade', temas=['evidencias', 'estatistica'],
resumo='Duas coisas andarem juntas não quer dizer que uma causa a outra. Conheça o terceiro fator, a causalidade reversa e a coincidência.',
corpo='''
<p class="abre">Nos meses em que se vende mais sorvete, também há mais afogamentos. O sorvete causa afogamentos? Não: o calor faz as pessoas tomarem mais sorvete e também irem mais à praia. Essa é a lição mais útil da estatística: <strong>correlação não é causalidade</strong>.</p>
<h2>O que é correlação</h2>
<p>Duas coisas são correlacionadas quando variam juntas: quando uma sobe, a outra tende a subir (correlação positiva) ou a descer (negativa). Correlação é um padrão nos dados. Causalidade é uma afirmação sobre o mundo: mexer em A muda B.</p>
<h2>Quatro explicações para uma correlação</h2>
<ol><li><strong>A causa B.</strong> Fumar causa câncer de pulmão. Às vezes a explicação óbvia é a certa.</li>
<li><strong>B causa A (causalidade reversa).</strong> Pessoas que vão mais ao médico estão mais doentes. Ir ao médico não adoece: estar doente leva ao médico.</li>
<li><strong>Um terceiro fator causa as duas (confusão).</strong> O calor, no caso do sorvete. Cidades com mais bombeiros têm mais incêndios porque cidades grandes têm mais dos dois.</li>
<li><strong>Coincidência.</strong> Com dados suficientes, alguma coisa sempre vai se correlacionar com outra por acaso. O site Spurious Correlations mostra, por exemplo, séries que acompanham o consumo de queijo e mortes por enroscar-se no lençol.</li></ol>
<h2>Como a ciência chega à causalidade</h2>
<ul><li><strong>Experimentos com sorteio:</strong> se A é distribuído por sorteio, terceiros fatores ficam equilibrados entre os grupos.</li><li><strong>Ordem no tempo:</strong> a causa precisa vir antes do efeito.</li><li><strong>Dose-resposta:</strong> mais exposição, mais efeito (quem fuma mais tem mais risco).</li><li><strong>Mecanismo plausível:</strong> saber como A poderia produzir B.</li><li><strong>Consistência:</strong> o mesmo resultado em populações e métodos diferentes.</li></ul>
<p>Esses critérios lembram os propostos pelo epidemiologista Austin Bradford Hill em 1965, usados para concluir que o tabaco causa câncer mesmo sem experimentos em humanos.</p>
<h2>Cuidado com o outro extremo</h2>
<p>“Correlação não é causalidade” não quer dizer que correlação não significa nada. Ela é um indício que merece investigação. Usar a frase para descartar qualquer estudo observacional incômodo, como fez a indústria do tabaco por décadas, é outro erro.</p>
<div class="nota"><strong>Pergunta-chave:</strong> diante de “quem faz X tem mais Y”, pergunte: e se for Y que leva a X? Que terceira coisa poderia causar as duas?</div>''',
fontes=[('Correlation does not imply causation (Wikipédia)', WE + 'Correlation_does_not_imply_causation'), ('Spurious Correlations', 'https://www.tylervigen.com/spurious-correlations'), ('Critérios de Bradford Hill (Wikipédia)', WE + 'Bradford_Hill_criteria')],
quiz=[('Cidades com mais igrejas têm mais crimes. A explicação mais provável é:', ['Igrejas causam crimes', 'Um terceiro fator: cidades maiores têm mais igrejas e mais crimes', 'Crimes causam igrejas', 'Pura coincidência sempre'], 1, 'O tamanho da população causa as duas coisas: é um fator de confusão.'),
 ('“Quem toma vinho tinto vive mais.” Que pergunta sobre causalidade reversa ou confusão vale fazer?', ['Qual a cor do vinho?', 'Quem bebe vinho moderadamente pode ter mais renda e saúde por outros motivos', 'O vinho é caro?', 'Nenhuma, está provado'], 1, 'Renda, hábitos e saúde prévia podem explicar a associação.'),
 ('O que torna mais convincente que uma correlação seja causal?', ['Um único estudo com resultado forte', 'Experimento com sorteio, dose-resposta, mecanismo e consistência entre estudos', 'Uma explicação que pareça lógica', 'Uma celebridade confirmar'], 1, 'Vários critérios juntos, como os de Bradford Hill, sustentam a inferência causal.')],
analogia='Ver dois fenômenos juntos é como ver duas pessoas sempre chegando ao trabalho no mesmo ônibus. Uma não faz a outra chegar: as duas pegam o mesmo ônibus. Antes de concluir que uma causa a outra, procure o ônibus.',
crianca='Quando chove, muita gente abre o guarda-chuva. Mas abrir guarda-chuvas não faz chover! Às vezes duas coisas acontecem juntas, mas uma não causa a outra.',
obj=['Distinguir correlação de causalidade.', 'Identificar causalidade reversa, fatores de confusão e coincidência.', 'Citar critérios que tornam uma inferência causal mais forte.'],
caso=('Uma reportagem diz que crianças que tomam café da manhã tiram notas melhores, e conclui que o café da manhã melhora o aprendizado.', 'Que outras explicações você testaria?', 'Famílias com mais tempo e renda podem oferecer café da manhã e também mais apoio escolar. Para saber se o café da manhã causa a melhora, seria preciso um experimento ou controlar esses fatores.'),
erro=('“Correlação não é causalidade, então esse estudo não vale nada.”', 'Correlação é um indício importante. Com dose-resposta, mecanismo e consistência, estudos observacionais podem sustentar conclusões causais, como no caso do tabaco.'),
ferr='correlacao-ou-causa', pre=['experimentos-e-grupo-controle'],
guardar=['Andar junto não é causar.', 'Pergunte sempre por causalidade reversa, por um terceiro fator e por coincidência.', 'Correlação é indício a investigar, não algo a descartar.'],
pensar='Que “quem faz X tem Y” você ouviu recentemente? Qual terceiro fator poderia explicar os dois?'),

dict(slug='o-que-e-pseudociencia', grupo='Ciência no dia a dia', titulo='O que é pseudociência?', temas=['demarcacao'],
resumo='Pseudociência é o que se apresenta como científico sem seguir os métodos da ciência. Conheça os sinais de alerta mais comuns.',
corpo='''
<p class="abre">Pseudociência é um conjunto de afirmações que se apresenta como científico, usa vocabulário científico e às vezes até jaleco, mas não segue as práticas que tornam a ciência confiável. Não é o mesmo que ciência errada: cientistas erram o tempo todo e corrigem. A pseudociência não se corrige.</p>
<h2>Ciência errada, não ciência e pseudociência</h2>
<ul><li><strong>Ciência errada:</strong> uma hipótese testada que não passou no teste. A teoria do éter luminífero foi ciência e estava errada.</li><li><strong>Não ciência:</strong> áreas que não pretendem ser ciência, como poesia, ética ou teologia. Não são pseudociência; só fazem outro tipo de pergunta.</li><li><strong>Pseudociência:</strong> afirma ser científica, mas evita testes, ignora evidências contrárias e não muda.</li></ul>
<h2>Sinais de alerta</h2>
<ul class="lista-contra">
<li><strong>Não pode ser refutada.</strong> Qualquer resultado confirma: se funcionou, prova; se não funcionou, “a energia estava bloqueada”.</li>
<li><strong>Depende de depoimentos</strong>, e não de estudos controlados.</li>
<li><strong>Não muda há décadas ou séculos</strong>, apesar de novas descobertas.</li>
<li><strong>Usa jargão científico sem sentido:</strong> “quântico”, “frequência vibracional”, “energia”, “detox”, aplicados sem nenhuma definição mensurável.</li>
<li><strong>Foge da revisão por pares</strong> e prefere livros, vídeos e cursos pagos.</li>
<li><strong>Explica críticas como perseguição:</strong> “a indústria farmacêutica esconde a cura”.</li>
<li><strong>Inverte o ônus da prova:</strong> “prove que não funciona”.</li>
<li><strong>Promete demais:</strong> cura para tudo, sem efeitos colaterais.</li></ul>
<h2>Exemplos comuns</h2>
<p>Astrologia, homeopatia, terra plana, criacionismo apresentado como ciência, constelação familiar, cura quântica, numerologia, grafologia para contratar funcionários. A seção <a href="pseudociencias.html">Pseudociências</a> analisa cada uma, com o que a evidência diz e por que elas atraem tanta gente.</p>
<h2>Por que importa</h2>
<p>Pseudociência não é inofensiva. Quem troca um tratamento eficaz por um ineficaz pode morrer: estudos encontraram mortalidade maior entre pacientes com câncer que optaram só por terapias alternativas. Também custa dinheiro público, como quando sistemas de saúde financiam práticas sem evidência, e corrói a confiança na ciência de verdade.</p>
<div class="nota"><strong>Sem desprezo:</strong> quem acredita em pseudociência não é burro. Essas ideias exploram vieses que todos temos, oferecem atenção e esperança, e muitas vezes preenchem lacunas deixadas pelo atendimento convencional. Criticar a ideia não exige ridicularizar a pessoa.</div>''',
fontes=[('Science and Pseudo-Science (Stanford Encyclopedia of Philosophy)', SEP + 'pseudo-science/'), ('Pseudociência (Wikipédia)', WP + 'Pseudoci%C3%AAncia'), ('Definindo Ciência e Pseudociência para Além da Falseabilidade: A Proposta Ampliada de Hansson', 'https://www.academia.edu/71626490/Definindo_Ci%C3%AAncia_e_Pseudoci%C3%AAncia_para_Al%C3%A9m_da_Falseabilidade_A_Proposta_Ampliada_de_Hansson'), ('Use of Alternative Medicine for Cancer and Its Impact on Survival (JNCI)', 'https://academic.oup.com/jnci/article/110/1/121/4064136')],
quiz=[('Qual a diferença entre ciência errada e pseudociência?', ['Nenhuma', 'Ciência errada testa e corrige; pseudociência evita testes e não se corrige', 'Pseudociência é sempre mais antiga', 'Ciência errada é proibida'], 1, 'Errar faz parte da ciência. O problema da pseudociência é fugir do teste.'),
 ('Um terapeuta diz que, se o tratamento não funcionou, é porque o paciente “não estava aberto à energia”. Qual sinal de alerta é esse?', ['Uso de jargão', 'A ideia não pode ser refutada: qualquer resultado a confirma', 'Promessa de cura', 'Revisão por pares'], 1, 'Quando o fracasso também confirma a teoria, ela deixou de ser testável.'),
 ('A poesia é pseudociência?', ['Sim, pois não faz experimentos', 'Não: não pretende ser ciência; faz outro tipo de pergunta', 'Sim, se rimar', 'Depende do poeta'], 1, 'Pseudociência é o que finge ser ciência. Áreas que não pretendem sê-lo são apenas não científicas.')],
analogia='A pseudociência é como uma nota falsa de dinheiro. Ela imita a aparência da verdadeira (a cor, o desenho, o vocabulário), mas não tem o lastro que dá valor à nota real. Para descobrir, é preciso olhar os detalhes de segurança: testes, controles, revisão.',
crianca='Algumas coisas parecem ciência porque usam palavras difíceis, mas ninguém testou direito se funcionam. A ciência de verdade sempre topa ser testada e muda quando o teste mostra que errou.',
obj=['Definir pseudociência e diferenciá-la de ciência errada e de não ciência.', 'Reconhecer os principais sinais de alerta.', 'Explicar por que a pseudociência pode causar danos reais.'],
caso=('Um curso online promete “reprogramar seu DNA com frequências quânticas” para curar ansiedade.', 'Quais sinais de alerta aparecem na frase?', 'Jargão científico sem sentido (DNA, quântico, frequências), promessa ampla de cura e venda de curso em vez de estudos publicados. São três sinais em uma frase.'),
erro=('“Tudo o que não é ciência é pseudociência.”', 'Ética, arte e religião não pretendem ser ciência; não são pseudociência. O termo vale para o que se apresenta como científico sem seguir o método.'),
ferr='ciencia-ou-pseudociencia', pre=['o-metodo-cientifico'],
guardar=['Pseudociência finge ser ciência e foge dos testes.', 'Sinais de alerta: irrefutável, baseada em depoimentos, jargão vazio, teoria da perseguição, ônus da prova invertido.', 'Criticar a ideia não exige desprezar a pessoa.'],
pensar='Alguma prática que você ou sua família usam tem algum desses sinais de alerta?'),

dict(slug='como-ler-noticia-de-ciencia', grupo='Ciência no dia a dia', titulo='Como ler uma notícia de ciência', temas=['evidencias', 'sociedade'],
resumo='Um roteiro de perguntas para não cair em manchetes exageradas: quem fez o estudo, em quem, com quantos, comparado a quê e quem pagou.',
corpo='''
<p class="abre">“Café previne câncer.” Meses depois: “Café causa câncer.” Se você já se sentiu perdido com notícias de ciência, a culpa não é sua. Entre o laboratório e a manchete, há várias etapas em que o resultado pode ser simplificado, exagerado ou distorcido.</p>
<h2>Como uma descoberta chega até você</h2>
<p>Pesquisadores publicam um artigo cheio de ressalvas. A universidade faz um comunicado à imprensa, mais animado. Um site resume o comunicado com uma manchete chamativa. Redes sociais compartilham só a manchete. Um estudo de 2014 no <em>BMJ</em> mostrou que boa parte dos exageros nas notícias de saúde já estava no comunicado das próprias universidades.</p>
<h2>Roteiro de nove perguntas</h2>
<ol class="roteiro">
<li><strong>Qual é a fonte original?</strong> Procure o nome da revista e do estudo. Se a notícia não diz, desconfie.</li>
<li><strong>Foi em humanos?</strong> Resultados em células ou ratos são preliminares.</li>
<li><strong>Quantas pessoas?</strong> Dez participantes é muito diferente de dez mil.</li>
<li><strong>Que tipo de estudo?</strong> Observacional mostra associação; ensaio randomizado testa causa.</li>
<li><strong>Comparado a quê?</strong> “Reduz o risco em 50%” pode ser de 2 em mil para 1 em mil. Pergunte pelo <em>risco absoluto</em>.</li>
<li><strong>O efeito é grande ou só “estatisticamente significativo”?</strong> Um efeito pode ser real e minúsculo.</li>
<li><strong>Quem pagou?</strong> Financiamento não invalida um estudo, mas pede atenção a conflitos de interesse.</li>
<li><strong>O que outros especialistas dizem?</strong> Boas reportagens ouvem cientistas que não participaram do estudo.</li>
<li><strong>Confirma o conjunto da evidência ou contradiz tudo?</strong> Um estudo que derruba décadas de pesquisa precisa de confirmação antes de mudar qualquer coisa.</li></ol>
<h2>Palavras que pedem atenção</h2>
<ul><li><strong>“Pode”, “ligado a”, “associado a”:</strong> indicam correlação, não causa.</li><li><strong>“Revolucionário”, “cura”, “cientistas descobrem”:</strong> quase sempre exagero.</li><li><strong>“Estudo prova”:</strong> um estudo raramente prova algo sozinho.</li></ul>
<h2>Onde checar</h2>
<p>Agências de checagem (Lupa, Aos Fatos, Comprova), divulgadores científicos com formação na área, revisões da Cochrane para saúde e sites de órgãos como a OMS e a Fiocruz. E desconfie de qualquer fonte que só traga notícias que confirmam o que você já pensa.</p>
<div class="nota"><strong>Risco relativo e absoluto:</strong> se um remédio reduz o risco de infarto de 2% para 1%, a manchete pode dizer “corta pela metade” (relativo) ou “reduz 1 ponto percentual” (absoluto). As duas são verdadeiras; só a segunda mostra o tamanho real.</div>''',
fontes=[('The association between exaggeration in health related science news and academic press releases (BMJ)', 'https://www.bmj.com/content/349/bmj.g7015'), ('Agência Lupa', 'https://lupa.uol.com.br/'), ('Cochrane Brasil', 'https://brazil.cochrane.org/'), ('Relative risk vs absolute risk (Wikipédia)', WE + 'Relative_risk')],
quiz=[('Uma manchete diz: “Novo remédio reduz pela metade o risco de AVC”. Que pergunta é mais importante?', ['Qual a cor do comprimido?', 'Qual era o risco absoluto antes e depois?', 'O remédio é importado?', 'Quem é o repórter?'], 1, 'Metade de um risco pequeno pode ser uma diferença mínima. O risco absoluto mostra o tamanho real.'),
 ('“Chocolate ligado a menos infartos.” A palavra “ligado” indica:', ['Que chocolate previne infarto', 'Uma associação, que pode ter outras explicações', 'Que o estudo foi em ratos', 'Que é fake news'], 1, '“Ligado a” e “associado a” indicam correlação, não causa.'),
 ('Um estudo único diz que um alimento comum é altamente cancerígeno, contrariando décadas de pesquisa. O mais sensato é:', ['Cortar o alimento imediatamente', 'Esperar confirmação: um estudo contra o conjunto da evidência precisa ser replicado', 'Ignorar toda pesquisa sobre o tema', 'Compartilhar para alertar todos'], 1, 'Afirmações que contradizem muita evidência pedem confirmação antes de mudar comportamento.')],
analogia='Ler uma notícia de ciência é como receber um recado que passou por várias pessoas num telefone sem fio. A mensagem original (o artigo) é cheia de ressalvas; a cada passagem, perde detalhes e ganha exagero. Vale sempre tentar ouvir quem falou primeiro.',
crianca='Quando alguém conta uma história que ouviu de outra pessoa, que ouviu de outra, a história vai mudando. Com notícias de ciência é parecido: é bom procurar quem fez a descoberta para saber o que realmente descobriu.',
obj=['Descrever o caminho de uma descoberta até a manchete e onde surgem exageros.', 'Aplicar um roteiro de perguntas a uma notícia de ciência.', 'Distinguir risco relativo de risco absoluto.'],
caso=('Você vê: “Cientistas descobrem que comer ovos todo dia aumenta o risco de morte em 30%”.', 'Que três perguntas você faria primeiro?', 'Que tipo de estudo era (provavelmente observacional), qual o risco absoluto por trás dos 30% e se o resultado bate com o conjunto da evidência sobre ovos.'),
erro=('“Se saiu num jornal grande, o estudo é forte.”', 'Jornais grandes também reproduzem comunicados exagerados. A força vem do desenho do estudo e da confirmação por outros, não do veículo.'),
ferr='nivel-de-evidencia', pre=['niveis-de-evidencia', 'correlacao-e-causalidade'],
guardar=['Exageros nascem cedo, muitas vezes no comunicado da própria universidade.', 'Pergunte: em humanos? quantos? que tipo de estudo? comparado a quê? quem pagou?', 'Prefira o risco absoluto ao relativo para ver o tamanho real do efeito.'],
pensar='Pegue a última manchete de saúde que você compartilhou. Ela passa pelo roteiro de nove perguntas?'),
]
