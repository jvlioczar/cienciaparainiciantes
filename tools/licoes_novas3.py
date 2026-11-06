"""Quarta leva de lições (2026-11-07), pedida por Julio: valores da ciência, ciência usada para o mal, mapa das áreas,
consensos, perguntas em aberto, ceticismo responsável, fraudes, teorias unificadas e o incognoscível. Mesmo formato: NOVAS3_<NIVEL> e POSICAO3."""
SEP = 'https://plato.stanford.edu/entries/'
IEP = 'https://iep.utm.edu/'
WP = 'https://pt.wikipedia.org/wiki/'
WE = 'https://en.wikipedia.org/wiki/'

POSICAO3 = {
 'os-valores-da-ciencia': 'postura-cientifica', 'mapa-das-ciencias': 'ciencia-e-tecnologia',
 'grandes-consensos-cientificos': 'consenso-cientifico', 'perguntas-em-aberto': 'grandes-consensos-cientificos',
 'ceticismo-responsavel': 'falacias-e-argumentos',
 'ciencia-a-servico-do-mal': 'etica-na-pesquisa', 'fraudes-cientificas': 'ciencia-a-servico-do-mal',
 'teorias-unificadas': 'interpretacoes-da-mecanica-quantica', 'o-incognoscivel': 'ciencia-da-consciencia',
}

NOVAS3_INICIANTE = [
dict(slug='os-valores-da-ciencia', grupo='O básico', titulo='Os valores da ciência', temas=['fundamentos', 'sociedade'],
resumo='Honestidade, ceticismo organizado, abertura, universalismo, humildade e rigor: os valores que fazem a ciência funcionar, e o que acontece quando são traídos.',
corpo='''
<p class="abre">A ciência não é só um conjunto de técnicas. Ela depende de valores compartilhados por quem a pratica. Sem honestidade, nenhum dado é confiável; sem abertura à crítica, nenhum erro é corrigido. Esses valores são o que transforma pessoas falíveis e vaidosas numa comunidade que produz conhecimento confiável.</p>
<h2>As normas de Merton</h2>
<p>Em 1942, o sociólogo Robert Merton descreveu quatro normas da ciência, conhecidas pela sigla CUDOS:</p>
<ul><li><strong>Comunalismo:</strong> descobertas pertencem a todos e devem ser publicadas. O cientista recebe reconhecimento, não a propriedade da natureza.</li><li><strong>Universalismo:</strong> uma afirmação vale pelos argumentos e pela evidência, não pela nacionalidade, raça, religião ou fama de quem a faz.</li><li><strong>Desinteresse:</strong> a pesquisa deve buscar a verdade, não vantagens pessoais; por isso conflitos de interesse precisam ser declarados.</li><li><strong>Ceticismo organizado:</strong> toda afirmação passa pelo escrutínio da comunidade antes de ser aceita.</li></ul>
<h2>Virtudes de quem pesquisa</h2>
<ul class="lista-forte"><li><strong>Honestidade:</strong> não fabricar, falsificar nem esconder dados, inclusive os que contrariam a hipótese.</li><li><strong>Transparência:</strong> mostrar métodos, dados e incertezas para que outros possam conferir.</li><li><strong>Humildade:</strong> admitir os limites do que se sabe e a possibilidade de estar errado.</li><li><strong>Curiosidade:</strong> querer saber como as coisas são, e não só confirmar o que se pensa.</li><li><strong>Rigor:</strong> cuidado com medidas, controles e análises.</li><li><strong>Coragem intelectual:</strong> defender um resultado impopular quando a evidência o sustenta, e abandonar uma ideia querida quando não sustenta.</li><li><strong>Respeito:</strong> por quem participa da pesquisa, humano ou animal, e por quem discorda.</li></ul>
<h2>Os valores na escolha entre teorias</h2>
<p>Thomas Kuhn listou os valores usados para escolher entre teorias rivais: <strong>precisão</strong> (concorda com os dados), <strong>consistência</strong> (não se contradiz nem contradiz o que sabemos), <strong>alcance</strong> (explica muitas coisas), <strong>simplicidade</strong> e <strong>fecundidade</strong> (abre caminhos novos). São valores <em>epistêmicos</em>, ligados à busca da verdade.</p>
<h2>Ideal e realidade</h2>
<p>As normas de Merton descrevem um ideal. Na prática há segredo comercial, disputas de prioridade, fraudes e pressão por publicar. Mas o ideal importa: é ele que permite denunciar o desvio. Quando um cientista esconde dados, a comunidade o critica justamente porque reconhece essas normas.</p>
<div class="nota"><strong>Valores da ciência e valores na ciência:</strong> esta lição fala dos valores que fazem a ciência funcionar. A lição do nível Avançado sobre <a href="valores-na-ciencia.html">valores na ciência</a> discute outra questão: como valores éticos e políticos influenciam o que se pesquisa e quanta evidência se exige.</div>''',
fontes=[('The Normative Structure of Science (Wikipédia: Mertonian norms)', WE + 'Mertonian_norms'), ('Virtue Epistemology (Stanford Encyclopedia)', SEP + 'epistemology-virtue/'), ('Objectivity, Value Judgment, and Theory Choice (A Tensão Essencial)', 'https://www.google.com/search?tbm=bks&q=A+Tens%C3%A3o+Essencial+Kuhn')],
quiz=[('O que significa o universalismo, nas normas de Merton?', ['Que a ciência estuda o universo', 'Que uma afirmação vale pela evidência, não por quem a faz', 'Que todos devem concordar', 'Que só cientistas famosos podem publicar'], 1, 'Nacionalidade, fama ou religião não tornam um argumento melhor.'),
 ('Que valor é violado quando um pesquisador deixa de publicar os dados que contrariam sua hipótese?', ['Curiosidade', 'Honestidade e transparência', 'Simplicidade', 'Fecundidade'], 1, 'Esconder dados contrários distorce o conhecimento.'),
 ('Um cientista recusa um resultado porque o autor é de um país rival. Que norma ele viola?', ['Comunalismo', 'Universalismo', 'Desinteresse', 'Fecundidade'], 1, 'Julgar pela origem, e não pela evidência, viola o universalismo.')],
analogia='Os valores da ciência são como as regras de um esporte. Um time pode ter os melhores atletas, mas se os jogadores trapacearem e o juiz aceitar, o placar deixa de dizer quem jogou melhor. Sem honestidade e crítica, os resultados da ciência deixam de dizer como o mundo é.',
crianca='Para a ciência funcionar, os cientistas precisam dizer a verdade sobre o que encontraram, até quando dá errado, deixar os outros conferirem e mudar de ideia quando estiverem errados. É como brincar limpo.',
obj=['Descrever as normas de Merton.', 'Listar virtudes de quem pesquisa e os valores de escolha de teorias de Kuhn.', 'Distinguir o ideal da prática e os valores da ciência dos valores na ciência.'],
caso=('Uma pesquisadora descobre que seu resultado mais famoso tinha um erro de análise.', 'O que os valores da ciência pedem que ela faça?', 'Publicar uma correção ou retratação, mesmo com custo para a reputação. Honestidade e ceticismo organizado valem também contra si mesmo.'),
erro=('“Se cientistas também são vaidosos e interesseiros, os valores da ciência são hipocrisia.”', 'Os valores são um ideal que permite denunciar desvios. A ciência funciona apesar dos defeitos individuais porque a comunidade cobra essas normas.'),
ferr=None, pre=['postura-cientifica'],
guardar=['Comunalismo, universalismo, desinteresse e ceticismo organizado (Merton).', 'Honestidade, transparência, humildade, rigor e coragem intelectual.', 'O ideal não descreve todos os cientistas, mas permite cobrar e corrigir os desvios.'],
pensar='Qual desses valores é mais difícil para você no dia a dia, fora da ciência?'),

dict(slug='mapa-das-ciencias', grupo='O básico', titulo='O mapa das ciências', temas=['fundamentos'],
resumo='Das ciências formais às sociais, passando pela física, pela biologia e pelas áreas aplicadas: o que cada grande área estuda e como as áreas se cruzam.',
corpo='''
<p class="abre">“Ciência” abrange áreas muito diferentes, da matemática à antropologia. Conhecer o mapa ajuda a saber a quem perguntar o quê, e a entender por que um físico não é, só por ser físico, especialista em vacinas.</p>
<h2>As grandes áreas</h2>
<div class="tabela"><table><thead><tr><th>Área</th><th>O que estuda</th><th>Exemplos de perguntas</th></tr></thead><tbody>
<tr><td><strong>Ciências formais</strong>: matemática, lógica, estatística, computação teórica</td><td>Estruturas abstratas, provas e cálculo</td><td>Existem infinitos números primos? Que problemas um computador não consegue resolver?</td></tr>
<tr><td><strong>Física</strong></td><td>Matéria, energia, espaço, tempo e as leis mais gerais</td><td>O que é a gravidade? Do que é feita a matéria escura?</td></tr>
<tr><td><strong>Química</strong></td><td>Substâncias, suas estruturas e transformações</td><td>Como criar um material mais leve e resistente?</td></tr>
<tr><td><strong>Ciências da Terra e do espaço</strong>: geologia, oceanografia, meteorologia, climatologia, astronomia</td><td>O planeta, a atmosfera e o universo</td><td>Por que os continentes se movem? Como o clima vai mudar?</td></tr>
<tr><td><strong>Ciências da vida</strong>: biologia, genética, ecologia, neurociência</td><td>Os seres vivos, da molécula ao ecossistema</td><td>Como surgem as espécies? Como funciona a memória?</td></tr>
<tr><td><strong>Ciências da saúde</strong>: medicina, epidemiologia, farmacologia, nutrição</td><td>Doença, saúde e tratamentos</td><td>Este remédio funciona? Como uma doença se espalha?</td></tr>
<tr><td><strong>Ciências sociais e comportamentais</strong>: psicologia, economia, sociologia, antropologia, ciência política, demografia, linguística</td><td>Pessoas, grupos e sociedades</td><td>Por que países enriquecem? Como decidimos?</td></tr>
<tr><td><strong>Ciências aplicadas e engenharias</strong>: engenharias, agronomia, ciência dos materiais, ciência da computação aplicada</td><td>Usar conhecimento para resolver problemas práticos</td><td>Como construir uma ponte mais segura? Como aumentar a produção de alimentos?</td></tr>
</tbody></table></div>
<h2>As humanidades</h2>
<p>História, filosofia, letras e artes estudam a experiência humana com métodos próprios, como a interpretação de fontes e a análise de argumentos. Em português, às vezes são chamadas de ciências humanas, e a história, por exemplo, usa evidências de forma rigorosa. No sentido mais estrito de testar hipóteses contra observações controladas, a maioria delas não é ciência empírica, o que não as torna menos importantes.</p>
<h2>As áreas que cruzam fronteiras</h2>
<p>Boa parte da pesquisa mais ativa hoje é <strong>interdisciplinar</strong>: neurociência (biologia, psicologia, física, computação), ciência do clima (física, química, biologia, economia), bioinformática, ciência de dados, saúde global, ciência cognitiva. No Brasil, a Capes organiza a pós-graduação em grandes áreas, incluindo uma área multidisciplinar.</p>
<h2>Por que o mapa importa</h2>
<ul><li><strong>Especialidade conta:</strong> um prêmio Nobel de física não torna alguém autoridade em epidemiologia. Desconfie de especialistas falando fora da sua área.</li><li><strong>Métodos diferentes:</strong> não se cobra da economia a precisão da física, nem da paleontologia experimentos de laboratório.</li><li><strong>Consensos são por área:</strong> o consenso sobre o clima é o dos climatologistas, não o de todos os cientistas.</li></ul>
<div class="nota"><strong>Veja também:</strong> a lição <a href="tipos-de-ciencia.html">ciências formais, naturais e humanas</a>, do nível Intermediário, discute as diferenças de método entre esses grupos.</div>''',
fontes=[('Branches of science (Wikipédia)', WE + 'Branches_of_science'), ('Áreas do conhecimento (Capes)', 'https://www.gov.br/capes/pt-br/acesso-a-informacao/acoes-e-programas/avaliacao/instrumentos/documentos-de-apoio/tabela-de-areas-de-conhecimento-avaliacao'), ('Interdisciplinaridade (Wikipédia)', WP + 'Interdisciplinaridade')],
quiz=[('Em que grande área está a climatologia?', ['Ciências formais', 'Ciências da Terra e do espaço', 'Humanidades', 'Engenharias'], 1, 'O clima é estudado junto com a geologia, a oceanografia e a meteorologia.'),
 ('Por que o mapa das ciências importa para avaliar especialistas?', ['Porque todo cientista é especialista em tudo', 'Porque autoridade em uma área não se transfere automaticamente para outra', 'Porque só físicos são confiáveis', 'Não importa'], 1, 'Desconfie de especialistas fora da sua área.'),
 ('Um famoso engenheiro diz que um tratamento contra o câncer funciona. Como pesar a opinião dele?', ['Como decisiva, pois é engenheiro', 'Como opinião fora da área; o que conta é a evidência clínica e o consenso da oncologia', 'Como pseudociência', 'Como consenso'], 1, 'A competência dele está em outra área.')],
analogia='O mapa das ciências é como o mapa de um hospital. Todos ali são profissionais de saúde, mas você não leva um problema no coração ao dermatologista. Cada área tem sua especialidade, e as melhores soluções muitas vezes saem de equipes de várias alas.',
crianca='Tem cientista que estuda estrelas, tem cientista que estuda bichos, tem cientista que estuda como as pessoas pensam e tem cientista que estuda números. Cada um sabe muito sobre a sua parte.',
obj=['Reconhecer as grandes áreas da ciência e o que cada uma estuda.', 'Situar as humanidades e as áreas interdisciplinares.', 'Usar o mapa para avaliar quem é especialista em quê.'],
caso=('Um vídeo apresenta um matemático renomado dando opinião sobre a origem de uma doença.', 'Como pesar essa opinião?', 'A competência dele é em matemática; sobre a doença, valem a evidência e o consenso de virologistas e epidemiologistas.'),
erro=('“Cientista é cientista: entende de ciência em geral.”', 'A ciência é muito especializada. Um especialista fora da sua área tem pouco mais autoridade do que um leigo bem informado.'),
ferr=None, pre=['o-que-e-ciencia'],
guardar=['Formais, físicas, químicas, da Terra, da vida, da saúde, sociais e aplicadas.', 'As humanidades usam métodos próprios; a pesquisa de ponta é muitas vezes interdisciplinar.', 'Autoridade científica vale dentro da área de cada um.'],
pensar='Que área da ciência você mais gostaria de conhecer melhor, e por quê?'),

dict(slug='grandes-consensos-cientificos', grupo='Como a ciência funciona', titulo='Os grandes consensos científicos', temas=['evidencias', 'sociedade'],
resumo='Evolução, idade do universo, causa humana do aquecimento global, segurança das vacinas, tabaco e câncer: o que a ciência considera estabelecido, e com que base.',
corpo='''
<p class="abre">Nem tudo na ciência está em discussão. Algumas conclusões foram testadas por tantos métodos, por tantas equipes, durante tanto tempo, que derrubá-las exigiria uma revolução com evidências gigantescas. Conhecer esses consensos ajuda a não ser enganado por quem os apresenta como “polêmicos”.</p>
<h2>O que é consenso, de novo</h2>
<p>Consenso científico não é votação: é a convergência de muitas linhas de evidência independentes, reconhecida pela grande maioria dos especialistas de uma área, e em geral registrada por academias de ciência e revisões sistemáticas. (Veja a lição sobre <a href="consenso-cientifico.html">revisão por pares e consenso</a>.)</p>
<h2>Alguns consensos sólidos</h2>
<div class="tabela"><table><thead><tr><th>Conclusão</th><th>Base principal</th></tr></thead><tbody>
<tr><td>O universo tem cerca de 13,8 bilhões de anos e se expande desde um estado muito quente e denso (Big Bang)</td><td>Radiação cósmica de fundo, expansão das galáxias, abundância de elementos leves</td></tr>
<tr><td>A Terra tem cerca de 4,5 bilhões de anos e é aproximadamente esférica</td><td>Datação radiométrica por métodos independentes; observações e satélites</td></tr>
<tr><td>Os continentes se movem (tectônica de placas)</td><td>Medidas de GPS, fundo oceânico, sismologia</td></tr>
<tr><td>Todos os seres vivos evoluíram de ancestrais comuns, por seleção natural e outros mecanismos</td><td>Fósseis, anatomia, genética, observação direta</td></tr>
<tr><td>Muitas doenças são causadas por micro-organismos (teoria dos germes)</td><td>Isolamento de patógenos, vacinas, antibióticos</td></tr>
<tr><td>O HIV causa a aids</td><td>Décadas de estudos; os antirretrovirais funcionam</td></tr>
<tr><td>Fumar causa câncer de pulmão e outras doenças</td><td>Grandes estudos de coorte, dose-resposta, mecanismos</td></tr>
<tr><td>As vacinas aprovadas são seguras e eficazes; a tríplice viral não causa autismo</td><td>Ensaios clínicos, farmacovigilância, estudos com milhões de crianças</td></tr>
<tr><td>A Terra está esquentando, e a causa principal é a atividade humana</td><td>Medidas de temperatura, física do efeito estufa, IPCC</td></tr>
<tr><td>Transgênicos aprovados são tão seguros para comer quanto os alimentos convencionais</td><td>Academias de ciência e revisões de centenas de estudos</td></tr>
<tr><td>“Raças” humanas não são subdivisões biológicas nítidas; a variação genética é contínua</td><td>Genômica populacional</td></tr>
<tr><td>Muitos animais, ao menos mamíferos e aves, têm experiências conscientes</td><td>Neurociência e comportamento (Declarações de Cambridge e de Nova York)</td></tr>
</tbody></table></div>
<h2>Consensos negativos</h2>
<p>Também há consenso sobre o que <strong>não</strong> funciona: a homeopatia não tem efeito além do placebo, a astrologia não prevê personalidade, a Terra não é plana. Veja a seção <a href="pseudociencias.html">Pseudociências</a>.</p>
<h2>Consenso não é dogma</h2>
<ul><li>Consensos já mudaram: a deriva continental foi rejeitada por décadas antes de ser aceita, quando a evidência ficou esmagadora.</li><li>O que muda costuma ser o detalhe, não o núcleo: a evolução ganhou a genética, mas a descendência comum continua de pé.</li><li>Quanto mais linhas de evidência independentes sustentam uma conclusão, mais improvável é que todas estejam erradas ao mesmo tempo.</li></ul>
<div class="nota"><strong>Onde ainda não há consenso:</strong> a natureza da matéria escura, a origem da vida, como o cérebro produz a consciência, como unir a relatividade e a física quântica. A próxima lição trata dessas perguntas em aberto.</div>''',
fontes=[('Scientific consensus (Wikipédia)', WE + 'Scientific_consensus'), ('IPCC AR6: Summary for Policymakers', 'https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/'), ('Genetically Engineered Crops (National Academies)', 'https://nap.nationalacademies.org/catalog/23395/'), ('Science, Evolution, and Creationism (National Academies)', 'https://nap.nationalacademies.org/catalog/11876/')],
quiz=[('O que torna um consenso científico muito sólido?', ['O número de cientistas que votaram', 'Muitas linhas de evidência independentes convergindo', 'A antiguidade da ideia', 'O apoio de governos'], 1, 'Linhas independentes tornam improvável que todas errem juntas.'),
 ('Qual destas afirmações é consenso científico?', ['A tríplice viral causa autismo', 'A atividade humana é a principal causa do aquecimento atual', 'A Terra tem seis mil anos', 'A homeopatia cura gripe'], 1, 'É a conclusão do IPCC e das academias de ciência.'),
 ('Alguém diz: “o consenso já mudou antes, então este também deve estar errado”. Qual a resposta?', ['Concordar', 'Consensos mudam com evidência nova e esmagadora; a mudança possível não é motivo para supor que este esteja errado', 'Consensos nunca mudam', 'A ciência é opinião'], 1, 'A possibilidade de mudança não é evidência de erro.')],
analogia='Um consenso científico sólido é como uma ponte apoiada em muitos pilares independentes. Um pilar pode ter uma rachadura, mas para a ponte cair seria preciso que todos falhassem ao mesmo tempo.',
crianca='Algumas coisas os cientistas já testaram tantas vezes, de tantos jeitos, que têm muita segurança: que a Terra é redonda, que os bichos evoluíram, que fumar faz mal. Isso é um consenso.',
obj=['Explicar o que torna um consenso sólido.', 'Citar grandes consensos das ciências naturais, da saúde e da vida.', 'Distinguir consenso de dogma e conhecer os consensos negativos.'],
caso=('Um vídeo apresenta o aquecimento global causado por humanos como “uma das teorias em debate”.', 'Como avaliar essa apresentação?', 'É falso equilíbrio: a causa humana é consenso dos climatologistas e do IPCC. O debate real é sobre ritmos, impactos regionais e políticas.'),
erro=('“Consenso é só a opinião da maioria dos cientistas.”', 'É a convergência de evidências independentes, reconhecida pela maioria dos especialistas da área. A maioria segue a evidência, não o contrário.'),
ferr='consenso-ou-em-aberto', pre=['consenso-cientifico'],
guardar=['Consenso sólido = muitas linhas de evidência independentes convergindo.', 'Idade do universo e da Terra, evolução, germes, tabaco, vacinas, clima, transgênicos, consciência animal.', 'Consensos podem mudar, mas só com evidência esmagadora, e costumam mudar no detalhe.'],
pensar='Qual destes consensos você já viu ser apresentado como “polêmico”? Por quem, e por quê?'),

dict(slug='perguntas-em-aberto', grupo='Como a ciência funciona', titulo='As grandes perguntas em aberto', temas=['fundamentos'],
resumo='Matéria escura, origem da vida, consciência, gravidade quântica, estamos sós? O que a ciência ainda não sabe, e por que admitir isso é uma força.',
corpo='''
<p class="abre">A ciência sabe muito, e sabe também o tamanho do que não sabe. Mapear a própria ignorância é uma das suas forças: as perguntas em aberto orientam a pesquisa e mostram onde desconfiar de quem diz ter todas as respostas.</p>
<h2>Algumas grandes perguntas</h2>
<ul><li><strong>Do que é feito o universo?</strong> A matéria comum é cerca de 5% do conteúdo do universo. O resto seria matéria escura (cerca de 27%) e energia escura (cerca de 68%), cuja natureza é desconhecida.</li>
<li><strong>Por que há mais matéria do que antimatéria?</strong> O Big Bang deveria ter produzido as duas em quantidades iguais.</li>
<li><strong>Como unir a relatividade geral e a mecânica quântica?</strong> As duas teorias funcionam muito bem, mas são incompatíveis em condições extremas, como no centro de buracos negros.</li>
<li><strong>Como surgiu a vida?</strong> Há hipóteses (como o “mundo de RNA”), mas não sabemos como a química virou biologia.</li>
<li><strong>Estamos sós?</strong> Milhares de planetas fora do Sistema Solar foram descobertos, mas nenhuma vida fora da Terra.</li>
<li><strong>Como o cérebro produz a consciência?</strong> Veja a lição sobre <a href="ciencia-da-consciencia.html">a ciência da consciência</a>.</li>
<li><strong>Quais as causas do Alzheimer?</strong> A principal hipótese, a das placas de proteína beta-amiloide, segue em debate, com resultados modestos dos remédios baseados nela.</li>
<li><strong>Problemas matemáticos:</strong> a hipótese de Riemann e o problema “P contra NP” valem um milhão de dólares cada para quem os resolver.</li></ul>
<h2>“Não sabemos” não é “qualquer coisa vale”</h2>
<p>Uma lacuna na ciência não é licença para preenchê-la com a primeira explicação disponível. A falácia do <strong>“deus das lacunas”</strong> usa o que a ciência ainda não explica como prova de uma explicação sobrenatural ou alternativa; a história mostra muitas lacunas sendo preenchidas por explicações naturais. Da mesma forma, “a ciência não sabe a origem da vida” não torna verdadeira uma teoria sem evidência sobre ela.</p>
<h2>Saber o que não se sabe</h2>
<p>Há perguntas em aberto de tipos diferentes: algumas esperam mais dados (matéria escura), outras uma ideia nova (gravidade quântica), outras talvez estejam além do que podemos saber. A lição do nível Avançado sobre <a href="o-incognoscivel.html">o incognoscível</a> discute esse último tipo.</p>
<div class="nota"><strong>Sinal de alerta:</strong> pseudociências raramente dizem “não sabemos”. Quando uma fonte tem resposta pronta para tudo, inclusive para o que os especialistas consideram em aberto, desconfie.</div>''',
fontes=[('Lists of unsolved problems (Wikipédia)', WE + 'Lists_of_unsolved_problems'), ('Dark matter (Wikipédia)', WE + 'Dark_matter'), ('Millennium Prize Problems (Wikipédia)', WE + 'Millennium_Prize_Problems'), ('God of the gaps (Wikipédia)', WE + 'God_of_the_gaps')],
quiz=[('Quanto do universo é feito de matéria comum, segundo os modelos atuais?', ['Quase tudo', 'Cerca de 5%', 'Metade', 'Nada'], 1, 'O resto seria matéria escura e energia escura, ainda desconhecidas.'),
 ('O que é a falácia do “deus das lacunas”?', ['Uma teoria da física', 'Usar o que a ciência ainda não explica como prova de uma explicação alternativa', 'Um método estatístico', 'Uma forma de consenso'], 1, 'Lacuna não é evidência a favor de nenhuma explicação específica.'),
 ('Um curso diz: “a ciência não sabe o que é a consciência, então nossa terapia de energia mental pode curar tudo”. Qual o erro?', ['Nenhum', 'Usar uma pergunta em aberto como licença para uma afirmação sem evidência', 'Dizer que a ciência não sabe tudo', 'Falar de consciência'], 1, 'Não saber uma coisa não torna verdadeira outra coisa.')],
analogia='O conhecimento científico é como uma ilha cercada de mar desconhecido. Quanto maior a ilha, maior a praia: quanto mais se sabe, mais perguntas novas aparecem na fronteira.',
crianca='Os cientistas sabem muita coisa, mas ainda não sabem do que é feita a maior parte do universo, nem como a vida começou. E tudo bem dizer “ainda não sabemos”: é assim que a gente continua descobrindo.',
obj=['Citar grandes perguntas em aberto em várias áreas.', 'Explicar a falácia do deus das lacunas.', 'Distinguir tipos de pergunta em aberto.'],
caso=('Alguém diz: “se os cientistas não sabem o que é a matéria escura, como podem ter certeza sobre o clima?”.', 'O argumento faz sentido?', 'Não. Áreas diferentes têm graus diferentes de conhecimento. Não saber uma coisa não enfraquece o que foi bem estabelecido em outra.'),
erro=('“Se a ciência ainda não sabe, qualquer explicação é tão boa quanto outra.”', 'Na ausência de evidência, a resposta honesta é “não sabemos”. Explicações precisam de apoio próprio, não só de lacunas.'),
ferr='consenso-ou-em-aberto', pre=['grandes-consensos-cientificos'],
guardar=['A ciência mapeia o que não sabe: matéria escura, origem da vida, consciência, gravidade quântica.', 'Lacunas não são evidência para nenhuma explicação específica.', 'Quem tem resposta pronta para tudo merece desconfiança.'],
pensar='Que pergunta em aberto você mais gostaria de ver respondida enquanto estiver vivo?'),

dict(slug='ceticismo-responsavel', grupo='Ciência no dia a dia', titulo='Ceticismo responsável', temas=['mente', 'epistemologia'],
resumo='Duvidar bem é diferente de duvidar de tudo. Proporção, coerência, saber quando parar e não confundir dúvida com negação: como ser cético sem virar cínico nem negacionista.',
corpo='''
<p class="abre">“Faça sua própria pesquisa”, “só estou perguntando”, “não confio em ninguém”. Muito do negacionismo atual se apresenta como ceticismo. Mas há uma diferença entre o ceticismo que ajuda a encontrar a verdade e a dúvida que serve para evitá-la.</p>
<h2>Os princípios do ceticismo responsável</h2>
<ul class="lista-forte"><li><strong>Proporção:</strong> a dúvida deve ser proporcional ao quanto a afirmação é surpreendente e à força da evidência. Duvidar igualmente de que a Terra é redonda e de um estudo pequeno sobre café é falta de proporção.</li>
<li><strong>Coerência:</strong> aplicar o mesmo rigor ao que confirma e ao que contraria o que pensamos. Quem exige provas impossíveis de um lado e aceita um vídeo do outro está fazendo raciocínio motivado, não ceticismo.</li>
<li><strong>Começar por si mesmo:</strong> o primeiro alvo da dúvida são as próprias crenças.</li>
<li><strong>Saber quando parar:</strong> dúvida razoável não é dúvida infinita. Quando muitas linhas de evidência convergem, continuar duvidando deixa de ser cuidado e vira obstinação.</li>
<li><strong>Distinguir duvidar de negar:</strong> “não tenho certeza” é diferente de “é mentira”. O cético suspende o juízo; o negacionista já decidiu.</li>
<li><strong>Caridade:</strong> criticar a melhor versão do argumento contrário, não um espantalho.</li>
<li><strong>Pesar os custos de errar:</strong> duvidar de uma vacina tem consequências diferentes de duvidar de um filme.</li>
<li><strong>Reconhecer os próprios limites:</strong> “fazer a própria pesquisa” em vídeos não equivale a anos de formação numa área. Avaliar especialistas é, muitas vezes, mais realista do que avaliar os dados sozinho.</li></ul>
<h2>Sinais de ceticismo irresponsável</h2>
<ul class="lista-contra"><li><strong>Dúvida seletiva:</strong> só aparece contra conclusões incômodas.</li><li><strong>“Só estou perguntando”:</strong> perguntas insinuantes, sem interesse pelas respostas que já existem.</li><li><strong>Exigência de certeza absoluta:</strong> nenhuma evidência nunca basta.</li><li><strong>Desconfiança total das instituições</strong> combinada com confiança total em fontes alternativas.</li><li><strong>Mover as traves:</strong> quando a evidência pedida aparece, a exigência muda.</li></ul>
<h2>Ceticismo e confiança andam juntos</h2>
<p>O ceticismo organizado da ciência funciona porque é <em>coletivo</em>: cada um duvida dentro de um sistema de crítica, e o resultado é conhecimento confiável. Quem duvida de todo esse sistema e confia apenas em si mesmo fica sem nenhum meio de corrigir os próprios erros.</p>
<div class="nota"><strong>Na BiblioVerse:</strong> a <a href="https://thinking.biblioverse.org/" target="_blank" rel="noopener">Biblioteca da Racionalidade</a> reúne recursos sobre pensamento crítico, e a <a href="https://conspiracy.biblioverse.org/" target="_blank" rel="noopener">Biblioteca de Conspirações</a> mostra como desmentir crenças falsas.</div>''',
fontes=[('Scientific skepticism (Wikipédia)', WE + 'Scientific_skepticism'), ('Just asking questions (Wikipédia)', WE + 'Just_asking_questions'), ('Moving the goalposts (Wikipédia)', WE + 'Moving_the_goalposts')],
quiz=[('Qual a diferença entre duvidar e negar?', ['Nenhuma', 'Quem duvida suspende o juízo; quem nega já decidiu', 'Negar é mais científico', 'Duvidar é sempre errado'], 1, 'O negacionista se apresenta como cético, mas já tem a conclusão.'),
 ('O que é “mover as traves”?', ['Mudar de time', 'Mudar a exigência de evidência quando a evidência pedida aparece', 'Pedir mais dados uma vez', 'Fazer um experimento novo'], 1, 'Nenhuma evidência basta para quem move as traves.'),
 ('Uma pessoa duvida de toda pesquisa feita em universidades, mas aceita sem questionar vídeos de um influenciador. O que falta no ceticismo dela?', ['Proporção e coerência', 'Caridade', 'Curiosidade', 'Nada'], 0, 'O mesmo rigor deve valer para todas as fontes.')],
analogia='O ceticismo responsável é como um bom filtro de água: retém as impurezas e deixa a água passar. Um filtro entupido, que não deixa passar nada, não serve para matar a sede; um furado não filtra nada.',
crianca='Ser cético é perguntar “como você sabe?” antes de acreditar. Mas se você nunca acredita em nada, nem quando todo mundo mostra as provas, aí já não é cuidado, é teimosia.',
obj=['Aplicar princípios do ceticismo responsável.', 'Reconhecer sinais de ceticismo irresponsável.', 'Explicar por que ceticismo e confiança andam juntos.'],
caso=('Um parente diz que “faz a própria pesquisa” e por isso não confia em nenhum médico.', 'Como seria um ceticismo responsável nesse caso?', 'Perguntar pelas evidências, comparar com o que dizem as diretrizes e vários especialistas, e aplicar a mesma dúvida às fontes alternativas. Pesquisar não é só procurar quem concorda.'),
erro=('“Quanto mais eu duvido, mais científico eu sou.”', 'A ciência pede dúvida proporcional à evidência. Duvidar de tudo igualmente é tão pouco racional quanto acreditar em tudo.'),
ferr='detector-de-pseudociencia', pre=['postura-cientifica', 'falacias-e-argumentos'],
guardar=['Dúvida proporcional, coerente e começando por si mesmo.', 'Duvidar não é negar; saber quando parar faz parte.', 'Sinais de alerta: dúvida seletiva, “só estou perguntando”, certeza absoluta, traves que se movem.'],
pensar='Sobre que assunto você duvida mais de um lado do que do outro?'),
]

NOVAS3_INTERMEDIARIO = [
dict(slug='ciencia-a-servico-do-mal', grupo='Ciência na prática', titulo='Ciência a serviço do mal', temas=['sociedade'],
resumo='Experimentos nazistas, a Unidade 731, a psiquiatria punitiva e as armas biológicas soviéticas, o Grande Salto maoísta, e abusos em democracias: quando a ciência serviu à crueldade.',
corpo='''
<p class="abre">A ciência dá poder, e o poder pode ser usado para o mal. Ao longo do século XX, regimes totalitários, e também democracias, usaram cientistas, métodos e prestígio científico para torturar, matar e oprimir. Conhecer esses casos não é desprezar a ciência: é entender por que ela precisa de limites éticos, abertura e controle.</p>
<h2>Alemanha nazista</h2>
<ul><li><strong>Experimentos em campos de concentração:</strong> em Dachau, prisioneiros foram submetidos a congelamento e a baixa pressão extrema para simular grandes altitudes; em Ravensbrück, mulheres tiveram ferimentos infectados para testar remédios; em Auschwitz, Josef Mengele fez experimentos com gêmeos, muitos deles crianças. Milhares morreram ou ficaram mutilados.</li>
<li><strong>Programa T4:</strong> pessoas com deficiência física e mental foram assassinadas por médicos, em nome da “higiene racial”; as técnicas de assassinato em massa por gás foram depois usadas no Holocausto.</li>
<li><strong>Ciência racial:</strong> antropólogos e médicos deram verniz científico ao antissemitismo e ao racismo, apoiados na eugenia que tinha prestígio internacional.</li>
<li>No <strong>Julgamento dos Médicos</strong> em Nuremberg (1946–1947), 16 dos 23 réus foram condenados, 7 deles à morte. Do julgamento saiu o Código de Nuremberg.</li></ul>
<h2>Japão imperial</h2>
<p>A <strong>Unidade 731</strong>, comandada pelo médico Shiro Ishii na Manchúria ocupada, fez vivissecções em prisioneiros, infectou pessoas com peste, cólera e antraz e testou armas biológicas contra cidades chinesas. Depois da guerra, os Estados Unidos concederam imunidade a seus líderes em troca dos dados, e quase ninguém foi julgado.</p>
<h2>União Soviética</h2>
<ul><li><strong>Lisenkoísmo:</strong> a genética foi proibida por ideologia; geneticistas foram presos e mortos, como Nikolai Vavilov, que morreu na prisão em 1943.</li>
<li><strong>Psiquiatria punitiva:</strong> dissidentes políticos foram diagnosticados com doenças inventadas para a ocasião, como a “esquizofrenia lenta”, e internados em hospitais psiquiátricos.</li>
<li><strong>Laboratório de venenos:</strong> a polícia secreta manteve um laboratório que testava venenos em prisioneiros.</li>
<li><strong>Biopreparat:</strong> um enorme programa secreto de armas biológicas continuou mesmo depois de a URSS assinar a convenção que as proibia (1972). Em 1979, um vazamento de antraz de uma instalação militar em Sverdlovsk matou dezenas de pessoas; o governo atribuiu as mortes a carne contaminada.</li>
<li><strong>Cientistas prisioneiros:</strong> engenheiros como Andrei Tupolev e Sergei Korolev trabalharam presos em laboratórios do sistema dos gulags.</li></ul>
<h2>China maoísta</h2>
<p>Durante o Grande Salto Adiante (1958–1962), técnicas agrícolas inspiradas em Lisenko, como o plantio superdenso, foram impostas contra a evidência, e cientistas que discordavam eram perseguidos. A campanha contra pardais, que comiam grãos, ajudou a provocar pragas de insetos. A fome resultante matou dezenas de milhões de pessoas; as estimativas variam muito, de cerca de 15 a mais de 40 milhões.</p>
<h2>Também nas democracias</h2>
<ul><li><strong>Tuskegee (EUA, 1932–1972)</strong> e os <strong>experimentos na Guatemala</strong> (1946–1948), em que o serviço de saúde americano infectou pessoas com sífilis e gonorreia de propósito.</li>
<li><strong>Esterilizações forçadas</strong> por leis eugênicas nos EUA, na Suécia e em outros países, algumas até os anos 1970.</li>
<li><strong>MKUltra:</strong> experimentos da CIA com drogas e técnicas de controle mental, em pessoas que não sabiam.</li></ul>
<h2>Armas e dilemas</h2>
<p>Fritz Haber ganhou o Nobel pela síntese da amônia, que permitiu fertilizantes para alimentar bilhões de pessoas, e também comandou o uso de gás cloro na Primeira Guerra. O Projeto Manhattan produziu as bombas de Hiroshima e Nagasaki. Muitos cientistas envolvidos passaram a defender o controle de armas, como no Manifesto Russell-Einstein (1955).</p>
<h2>O que esses casos ensinam</h2>
<ul class="lista-forte"><li><strong>O segredo é o ambiente do abuso:</strong> quase todos esses casos dependeram de sigilo; abertura e publicação são proteções.</li><li><strong>Ideologia acima da evidência</strong> produz tanto ciência falsa (Lisenko) quanto crueldade (ciência racial).</li><li><strong>Desumanizar vem antes de abusar:</strong> as vítimas eram tratadas como menos que pessoas.</li><li><strong>A ciência não traz sua própria ética:</strong> consentimento, comitês independentes, liberdade de crítica e controle democrático precisam vir de fora do laboratório.</li></ul>
<div class="nota"><strong>Comparação não é equivalência:</strong> os casos são muito diferentes em escala e intenção. Colocá-los lado a lado serve para mostrar padrões comuns, não para igualar regimes ou relativizar o Holocausto.</div>''',
fontes=[('Nazi human experimentation (Wikipédia)', WE + 'Nazi_human_experimentation'), ('Unidade 731 (Wikipédia)', WP + 'Unidade_731'), ('Political abuse of psychiatry in the Soviet Union (Wikipédia)', WE + 'Political_abuse_of_psychiatry_in_the_Soviet_Union'), ('Biopreparat (Wikipédia)', WE + 'Biopreparat'), ('Grande Fome Chinesa (Wikipédia)', WP + 'Grande_Fome_Chinesa'), ('Guatemala syphilis experiments (Wikipédia)', WE + 'Guatemala_syphilis_experiments')],
quiz=[('O que foi o programa T4 na Alemanha nazista?', ['Um programa de vacinação', 'O assassinato de pessoas com deficiência por médicos, em nome da “higiene racial”', 'Um laboratório de física', 'Um tratado internacional'], 1, 'As técnicas foram depois usadas no Holocausto.'),
 ('Qual elemento aparece em quase todos os casos de abuso da lição?', ['Financiamento privado', 'Sigilo', 'Revisão por pares', 'Publicação aberta'], 1, 'Abertura e publicação são proteções contra o abuso.'),
 ('Um governo quer pesquisar armas biológicas em segredo, sem supervisão independente, “pela segurança nacional”. O que a lição sugere?', ['Que é aceitável', 'Que sigilo sem controle independente é o ambiente típico dos abusos históricos', 'Que a ciência é sempre má', 'Nada'], 1, 'Biopreparat e Unidade 731 mostram o padrão.')],
analogia='A ciência é como uma faca muito afiada. Na mão de um cirurgião, salva vidas; na de um torturador, mata. A faca não escolhe: as regras, a vigilância e a ética de quem a usa é que decidem.',
crianca='A ciência pode ser usada para ajudar, como fazer vacinas, ou para machucar, como algumas pessoas malvadas fizeram no passado. Por isso existem regras para que ninguém seja machucado em nome da ciência.',
obj=['Descrever casos de ciência usada para o mal em regimes totalitários e em democracias.', 'Identificar padrões comuns: sigilo, ideologia, desumanização.', 'Explicar por que a ciência precisa de controles éticos externos.'],
caso=('Alguém diz que os dados dos experimentos nazistas deveriam ser usados, já que “o sofrimento já aconteceu”.', 'Que questões estão em jogo?', 'Se os dados são confiáveis (muitos não são, por falta de método), se usá-los legitima os crimes e se há alternativas. Muitos cientistas e eticistas rejeitam ou restringem esse uso; é um debate ético real.'),
erro=('“Esses horrores mostram que a ciência é má.”', 'Mostram que conhecimento e poder sem limites éticos podem servir à crueldade. Os mesmos casos levaram às regras de consentimento e aos comitês de ética.'),
ferr=None, pre=['etica-na-pesquisa'],
guardar=['Nazismo, Unidade 731, URSS e China maoísta usaram a ciência para matar, torturar e oprimir; democracias também cometeram abusos.', 'Sigilo, ideologia acima da evidência e desumanização são os padrões comuns.', 'A ética da ciência vem de fora: consentimento, crítica livre e controle independente.'],
pensar='Que pesquisa atual poderia ser usada para o mal, e que controle a impediria?'),

dict(slug='fraudes-cientificas', grupo='Ciência na prática', titulo='Fraudes científicas famosas', temas=['evidencias', 'sociedade'],
resumo='O Homem de Piltdown, a clonagem falsa de Hwang, os supercondutores inventados de Schön, Wakefield e Theranos: como fraudes acontecem e como a ciência as descobre.',
corpo='''
<p class="abre">Fraudes são raras em comparação com o volume de pesquisa, mas acontecem, e algumas enganaram o mundo por anos. Estudar como foram descobertas mostra tanto as falhas quanto a força do sistema científico.</p>
<h2>Os tipos de má conduta</h2>
<ul><li><strong>Fabricação:</strong> inventar dados.</li><li><strong>Falsificação:</strong> manipular dados, imagens ou métodos.</li><li><strong>Plágio:</strong> apresentar o trabalho de outros como próprio.</li></ul>
<p>Práticas questionáveis, como o p-hacking, são mais comuns e mais difíceis de detectar (veja a lição sobre a <a href="crise-de-replicacao.html">crise de replicação</a>).</p>
<h2>Casos famosos</h2>
<ul><li><strong>Homem de Piltdown (1912):</strong> fragmentos de crânio achados na Inglaterra foram apresentados como o “elo perdido” entre macacos e humanos. Em 1953, análises mostraram que era um crânio humano com a mandíbula de um orangotango, com dentes lixados. A fraude durou 40 anos, em parte porque confirmava o que alguns cientistas britânicos queriam acreditar.</li>
<li><strong>Jan Hendrik Schön (2002):</strong> físico dos Laboratórios Bell, publicou dezenas de artigos sobre supercondutividade e eletrônica molecular em revistas de elite. Colegas notaram gráficos idênticos em experimentos diferentes; uma investigação concluiu que ele havia fabricado dados.</li>
<li><strong>Hwang Woo-suk (2005):</strong> o cientista sul-coreano anunciou ter clonado embriões humanos e obtido células-tronco. Os dados eram falsos, e havia problemas éticos na obtenção de óvulos.</li>
<li><strong>Andrew Wakefield (1998):</strong> o artigo que ligava a vacina tríplice viral ao autismo foi retratado em 2010, depois que um jornalista revelou manipulação de dados e conflitos de interesse. O dano à vacinação dura até hoje.</li>
<li><strong>Diederik Stapel (2011):</strong> psicólogo social holandês que inventou dados em dezenas de estudos, descoberto por estudantes que desconfiaram de resultados bons demais.</li>
<li><strong>Theranos (2015–2022):</strong> a empresa prometia centenas de exames com uma gota de sangue. A tecnologia não funcionava; a fundadora, Elizabeth Holmes, foi condenada por fraude. O caso mostra o risco de anunciar resultados sem publicar dados para avaliação independente.</li></ul>
<h2>Como as fraudes são descobertas</h2>
<ul class="lista-forte"><li><strong>Replicação:</strong> outros tentam repetir e não conseguem.</li><li><strong>Olhos atentos:</strong> colegas, estudantes e revisores notam dados bons demais ou imagens duplicadas.</li><li><strong>Ferramentas estatísticas</strong> detectam padrões improváveis em dados inventados.</li><li><strong>Jornalismo investigativo</strong> e sites como o Retraction Watch acompanham retratações.</li><li><strong>Detetives de imagens</strong>, como a microbiologista Elisabeth Bik, encontram fotos manipuladas em milhares de artigos.</li></ul>
<h2>O que as fraudes ensinam</h2>
<p>A pressão por publicar, a busca por resultados espetaculares e a confiança cega em nomes famosos facilitam a fraude. Dados abertos, replicação e proteção a quem denuncia dificultam. Que tantas fraudes tenham sido descobertas por cientistas mostra a autocorreção funcionando, ainda que às vezes devagar demais.</p>
<div class="nota"><strong>Retratação não é vergonha da ciência:</strong> uma revista que retrata um artigo está corrigindo o registro. Desconfie mais de áreas que nunca retratam nada do que das que retratam.</div>''',
fontes=[('Scientific misconduct (Wikipédia)', WE + 'Scientific_misconduct'), ('Homem de Piltdown (Wikipédia)', WP + 'Homem_de_Piltdown'), ('Schön scandal (Wikipédia)', WE + 'Sch%C3%B6n_scandal'), ('Retraction Watch', 'https://retractionwatch.com/')],
quiz=[('Quais são as três formas principais de má conduta científica?', ['Erro, dúvida e revisão', 'Fabricação, falsificação e plágio', 'Indução, dedução e abdução', 'Publicação, citação e retratação'], 1, 'São as definições usadas por agências de pesquisa.'),
 ('Por que a fraude de Piltdown durou 40 anos?', ['Porque não havia cientistas', 'Em parte porque confirmava o que alguns cientistas queriam acreditar', 'Porque era verdadeira', 'Porque foi publicada em português'], 1, 'Viés de confirmação também protege fraudes.'),
 ('Uma empresa anuncia uma tecnologia revolucionária de diagnóstico, mas se recusa a publicar dados para avaliação independente. O que a lição sugere?', ['Confiar, pois é uma empresa grande', 'Desconfiar: o caso Theranos mostra o risco de resultados sem escrutínio independente', 'Que toda empresa frauda', 'Nada'], 1, 'Sem dados abertos à verificação, não há como saber.')],
analogia='O sistema científico contra fraudes é como o sistema imunológico. Algumas infecções passam despercebidas por um tempo, mas os anticorpos (replicação, revisão, colegas atentos) acabam encontrando a maioria. Um corpo sem imunidade é que estaria em perigo.',
crianca='Às vezes um cientista mente sobre o que descobriu. Mas outros cientistas tentam fazer igual, e quando não conseguem, desconfiam e descobrem a mentira.',
obj=['Distinguir fabricação, falsificação e plágio.', 'Conhecer fraudes famosas e como foram descobertas.', 'Explicar o que facilita e o que dificulta a fraude.'],
caso=('Um estudo apresenta resultados perfeitos, sem nenhuma variação entre participantes.', 'Por que isso é suspeito?', 'Dados reais têm ruído. Resultados bons demais foram o que levou estudantes a desconfiarem de Stapel e colegas a desconfiarem de Schön.'),
erro=('“Fraudes provam que a ciência não é confiável.”', 'Fraudes são raras e, em geral, descobertas por outros cientistas. Isso mostra a autocorreção funcionando, embora às vezes devagar.'),
ferr=None, pre=['consenso-cientifico', 'ciencia-a-servico-do-mal'],
guardar=['Fabricação, falsificação e plágio são as formas de má conduta.', 'Piltdown, Schön, Hwang, Wakefield, Stapel e Theranos.', 'Replicação, dados abertos e colegas atentos descobrem fraudes; retratar é corrigir.'],
pensar='Que resultado “bom demais para ser verdade” você já viu circular?'),
]

NOVAS3_AVANCADO = [
dict(slug='teorias-unificadas', grupo='Teorias e realidade', titulo='Teorias unificadas e a busca por elas', temas=['filosofia'],
resumo='De Newton a Maxwell, do Modelo Padrão à teoria de tudo: as grandes unificações da física, o que falta unir e se a ciência deve buscar uma teoria final.',
corpo='''
<p class="abre">Alguns dos maiores avanços da ciência foram <strong>unificações</strong>: mostrar que fenômenos que pareciam diferentes têm a mesma explicação. A busca por uma “teoria de tudo” é o ponto extremo dessa ambição, e levanta questões filosóficas sobre a unidade da natureza.</p>
<h2>As grandes unificações</h2>
<ul><li><strong>Newton (1687):</strong> a mesma gravitação explica a queda de uma maçã e a órbita da Lua; céu e Terra seguem as mesmas leis.</li>
<li><strong>Maxwell (1865):</strong> eletricidade, magnetismo e luz são manifestações de um único campo eletromagnético.</li>
<li><strong>Einstein (1905 e 1915):</strong> espaço e tempo formam o espaço-tempo; massa e energia são equivalentes; a gravidade é a curvatura do espaço-tempo.</li>
<li><strong>Força eletrofraca (anos 1960 e 1970):</strong> Glashow, Salam e Weinberg uniram o eletromagnetismo e a força nuclear fraca; as partículas previstas (W e Z) foram encontradas em 1983.</li>
<li><strong>Modelo Padrão:</strong> descreve as partículas e três das quatro forças fundamentais. Sua última peça prevista, o bóson de Higgs, foi detectada em 2012.</li></ul>
<h2>O que falta unir</h2>
<ul><li><strong>Grande unificação:</strong> teorias que uniriam a força forte à eletrofraca preveem que prótons decaem; experimentos como o Super-Kamiokande nunca observaram isso, o que descartou as versões mais simples.</li>
<li><strong>Gravidade quântica:</strong> a relatividade geral e a mecânica quântica são incompatíveis em condições extremas, como no Big Bang e no interior de buracos negros. Candidatas: teoria das cordas, gravidade quântica em laços e outras. Nenhuma tem confirmação experimental (veja o debate sobre a <a href="debates/teoria-das-cordas.html">teoria das cordas</a>).</li>
<li>Einstein passou as últimas três décadas da vida buscando uma teoria de campo unificado, sem sucesso.</li></ul>
<h2>A unidade da ciência</h2>
<p>A ideia de unificação vai além da física. O positivismo lógico tinha o projeto de uma <strong>ciência unificada</strong>, com uma linguagem comum e a redução de todas as ciências à física. Edward O. Wilson chamou de <em>consiliência</em> a convergência entre áreas.</p>
<h2>Argumentos contra a teoria final</h2>
<ul class="lista-contra"><li><strong>Desunidade da ciência</strong> (John Dupré, Nancy Cartwright): a natureza pode ser “manchada”, com regiões governadas por leis diferentes, sem uma teoria única por trás.</li><li><strong>Ciências especiais</strong> (Jerry Fodor): mesmo com uma teoria final da física, biologia e economia continuariam precisando de leis próprias (realizabilidade múltipla).</li><li><strong>Limites do conhecimento:</strong> Stephen Hawking sugeriu, numa palestra de 2002, que os teoremas de Gödel podem impedir uma teoria final completa.</li><li><strong>O que “tudo” quer dizer:</strong> uma teoria de todas as partículas não explicaria a consciência, a história ou o sentido da vida.</li></ul>
<h2>Por que buscar, então?</h2>
<p>Mesmo quem duvida de uma teoria final reconhece que a busca por unificação foi extremamente fecunda: cada unificação trouxe previsões novas e tecnologias, do rádio ao GPS. O físico Steven Weinberg chamou essa busca de “sonho de uma teoria final”.</p>
<div class="nota"><strong>Cuidado com a teoria de tudo de vídeo:</strong> “teorias de tudo” anunciadas fora da física profissional, sem matemática testável nem previsões, são um sinal clássico de pseudociência.</div>''',
fontes=[('Theory of everything (Wikipédia)', WE + 'Theory_of_everything'), ('The Unity of Science (Stanford Encyclopedia)', SEP + 'scientific-unity/'), ('Modelo Padrão (Wikipédia)', WP + 'Modelo_Padr%C3%A3o'), ('Grand Unified Theory (Wikipédia)', WE + 'Grand_Unified_Theory')],
quiz=[('O que Maxwell unificou?', ['Gravidade e tempo', 'Eletricidade, magnetismo e luz', 'Biologia e química', 'Força forte e fraca'], 1, 'Os três são manifestações do campo eletromagnético.'),
 ('O que ainda falta unir na física fundamental?', ['Eletricidade e magnetismo', 'A relatividade geral (gravidade) e a mecânica quântica', 'Química e física', 'Nada'], 1, 'É o problema da gravidade quântica.'),
 ('Um filósofo diz que, mesmo com uma teoria final da física, a economia continuaria precisando de leis próprias. Que argumento é esse?', ['O das ciências especiais e da realizabilidade múltipla', 'O argumento do milagre', 'A metaindução pessimista', 'O problema de Gettier'], 0, 'É o argumento de Fodor contra a redução total.')],
analogia='Unificar teorias é como descobrir que vários rios nascem da mesma fonte. Cada descoberta assim simplificou o mapa e revelou caminhos novos. A teoria de tudo seria encontrar a nascente de todos os rios, se ela existir.',
crianca='Os cientistas descobriram que coisas que pareciam diferentes, como a eletricidade e a luz, eram a mesma coisa por dentro. Alguns sonham em descobrir uma única explicação para tudo no universo.',
obj=['Descrever as grandes unificações da física.', 'Explicar o que falta unir e as candidatas a teoria de tudo.', 'Avaliar argumentos a favor e contra uma teoria final e a unidade da ciência.'],
caso=('Um livro anuncia que um autor sem formação em física descobriu “a teoria de tudo”, unindo física, consciência e espiritualidade.', 'Que sinais de alerta aparecem?', 'Ausência de matemática testável e de previsões, publicação fora da comunidade científica e a pretensão de explicar tudo de uma vez.'),
erro=('“Uma teoria de tudo explicaria literalmente tudo.”', 'Explicaria as leis fundamentais da física. Biologia, mente, sociedade e história continuariam exigindo conceitos e explicações próprias.'),
ferr=None, pre=['interpretacoes-da-mecanica-quantica', 'reducionismo-e-emergencia'],
guardar=['Newton, Maxwell, Einstein, a eletrofraca e o Modelo Padrão foram grandes unificações.', 'Falta unir a gravidade à física quântica; nenhuma candidata foi confirmada.', 'Desunidade, ciências especiais e limites lógicos põem em dúvida uma teoria final.'],
pensar='Você acha que a natureza é, no fundo, simples, ou que a complexidade vai até o fim?'),

dict(slug='o-incognoscivel', grupo='Teorias e realidade', titulo='O incognoscível: há coisas que nunca poderemos saber?', temas=['epistemologia', 'filosofia'],
resumo='Do “ignorabimus” ao “precisamos saber e saberemos”, de Gödel e Turing ao horizonte cósmico e ao mistério da consciência: os limites do conhecimento, os provados e os supostos.',
corpo='''
<p class="abre">Toda pergunta tem resposta que podemos encontrar? Ou há coisas que, por princípio, nunca poderemos saber? A pergunta pelo <strong>incognoscível</strong> atravessa a história da filosofia e ganhou, no século XX, respostas surpreendentemente precisas.</p>
<h2>A disputa histórica</h2>
<ul><li><strong>Kant:</strong> conhecemos as coisas como nos aparecem (fenômenos), não como são em si mesmas (o númeno).</li>
<li><strong>Comte</strong> afirmou que nunca saberíamos a composição química das estrelas. Pouco depois, a espectroscopia a revelou, analisando a luz delas.</li>
<li><strong>Emil du Bois-Reymond</strong>, fisiologista alemão, declarou em 1872 e 1880 que certas questões, como a natureza da matéria e a origem da consciência, eram para sempre inacessíveis: <em>ignoramus et ignorabimus</em> (“não sabemos e não saberemos”).</li>
<li><strong>David Hilbert</strong> respondeu em 1930, num discurso famoso: “precisamos saber, e saberemos”. No dia anterior, no mesmo congresso, o jovem Kurt Gödel havia anunciado o resultado que mostrava um limite ao programa de Hilbert.</li></ul>
<h2>Limites demonstrados</h2>
<ul><li><strong>Incompletude de Gödel (1931):</strong> qualquer sistema matemático consistente, capaz de expressar a aritmética, contém afirmações verdadeiras que não podem ser provadas dentro dele.</li>
<li><strong>Problema da parada de Turing (1936):</strong> não existe um programa que decida, para qualquer programa, se ele vai parar ou rodar para sempre.</li>
<li><strong>Princípio da incerteza de Heisenberg:</strong> não é possível conhecer com precisão arbitrária, ao mesmo tempo, a posição e o momento de uma partícula.</li>
<li><strong>Caos:</strong> em sistemas caóticos, como o tempo atmosférico, pequenas incertezas crescem tão rápido que a previsão de longo prazo é impossível na prática.</li>
<li><strong>Horizonte cósmico:</strong> a luz de regiões muito distantes do universo nunca chegará até nós; há partes do universo que não podemos observar.</li></ul>
<h2>Limites supostos</h2>
<ul><li><strong>Misterianismo</strong> (Colin McGinn): talvez a mente humana não tenha os conceitos necessários para entender a consciência, como um cão não pode entender cálculo.</li>
<li><strong>Ceticismo radical:</strong> nunca poderíamos excluir que estamos sonhando ou numa simulação.</li>
<li><strong>Paradoxo de Fitch:</strong> um argumento lógico mostra que, se toda verdade pudesse ser conhecida, toda verdade já seria conhecida. Como nem tudo é conhecido, haveria verdades incognoscíveis.</li></ul>
<h2>Lições</h2>
<ul class="lista-forte"><li><strong>Humildade dupla:</strong> a história está cheia de previsões erradas de que algo jamais seria conhecido (Comte, as estrelas). Mas também há limites rigorosamente demonstrados.</li><li><strong>Saber os limites é saber algo:</strong> os teoremas de Gödel e Turing são conhecimento sobre o conhecimento, e fundaram a ciência da computação.</li><li><strong>Limites não são licença:</strong> que algumas coisas sejam incognoscíveis não torna verdadeira nenhuma resposta específica a elas.</li></ul>
<div class="nota"><strong>Agnosticismo:</strong> o termo foi cunhado por Thomas Huxley em 1869 para quem considera certas questões, como a existência de Deus, fora do alcance do conhecimento. É uma posição sobre o que podemos saber, não sobre o que é verdade.</div>''',
fontes=[('Ignoramus et ignorabimus (Wikipédia)', WE + 'Ignoramus_et_ignorabimus'), ('Gödel\'s Incompleteness Theorems (Stanford Encyclopedia)', SEP + 'goedel-incompleteness/'), ('Halting problem (Wikipédia)', WE + 'Halting_problem'), ('Fitch\'s Paradox of Knowability (Stanford Encyclopedia)', SEP + 'fitch-paradox/'), ('Mysterianism (Wikipédia)', WE + 'New_mysterianism')],
quiz=[('O que Comte disse que nunca saberíamos, e o que aconteceu?', ['A idade da Terra; descobrimos pelos fósseis', 'A composição das estrelas; a espectroscopia a revelou', 'A origem da vida; foi descoberta', 'A natureza da luz; nunca soubemos'], 1, 'É o exemplo clássico de limite declarado cedo demais.'),
 ('O que o problema da parada de Turing mostra?', ['Que computadores param sempre', 'Que nenhum programa pode decidir, para todo programa, se ele vai parar', 'Que a matemática está errada', 'Que o caos é previsível'], 1, 'É um limite demonstrado da computação.'),
 ('Alguém diz: “a ciência nunca vai explicar a consciência, então minha explicação espiritual é a verdadeira”. Qual a lição?', ['Concordar', 'Mesmo que algo fosse incognoscível, isso não tornaria verdadeira nenhuma resposta específica', 'A consciência já foi explicada', 'A pergunta não faz sentido'], 1, 'Limites não são licença para afirmar.')],
analogia='O conhecimento humano é como a luz de uma lanterna numa caverna enorme. Durante séculos, alguns disseram “aquela parede nunca será iluminada”, e a lanterna melhorou e a iluminou. Mas também descobrimos que certas regiões, por causa da forma da própria caverna, nenhuma lanterna alcança.',
crianca='Será que existem coisas que ninguém nunca vai conseguir descobrir? Às vezes as pessoas disseram que sim e depois alguém descobriu. Mas os matemáticos provaram que algumas coisas nem os computadores mais poderosos conseguem resolver.',
obj=['Reconstruir a disputa entre o “ignorabimus” e o “saberemos”.', 'Distinguir limites demonstrados (Gödel, Turing, incerteza, caos, horizonte) de limites supostos.', 'Tirar lições sobre humildade e sobre o uso indevido da ideia de incognoscível.'],
caso=('Um palestrante diz que “a física quântica provou que nada pode ser conhecido com certeza, então qualquer crença é válida”.', 'O que está errado?', 'O princípio da incerteza limita a medida simultânea de certas grandezas; não diz nada sobre crenças em geral. E limites ao conhecimento não validam nenhuma crença específica.'),
erro=('“Se algo ainda não foi explicado, nunca será.”', 'A história mostra muitas previsões desse tipo erradas. Só alguns limites foram demonstrados rigorosamente.'),
ferr=None, pre=['cientificismo-e-limites-da-ciencia', 'ciencia-da-consciencia'],
guardar=['O ignorabimus de Du Bois-Reymond contra o “saberemos” de Hilbert.', 'Gödel, Turing, incerteza, caos e horizonte cósmico são limites demonstrados.', 'Previsões de incognoscibilidade já falharam; limites não validam respostas específicas.'],
pensar='Há alguma pergunta que você acha que a humanidade nunca vai responder? Por quê?'),
]
