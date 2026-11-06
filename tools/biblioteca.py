"""Livros e sites. LIVROS: (título, autor, descrição, seção, url). SITES: (nome, url, descrição, grupo, âmbito).
As fichas mostram o autor do livro como referência bibliográfica (o rótulo das fontes nas páginas mostra só o título)."""
from urllib.parse import quote
def b(t, a, d, n, u=None): return (t, a, d, n, u or 'https://www.google.com/search?tbm=bks&q=' + quote(t + ' ' + a))
INI, INTM, AVA, PSE = 'Iniciante', 'Intermediário', 'Avançado', 'Pseudociência e desinformação'
SECOES_L = [
 (INI, 'Para começar: leitura acessível, sem pré-requisitos.'),
 (INTM, 'Epistemologia e filosofia da ciência, com alguma densidade.'),
 (AVA, 'Os clássicos e os debates atuais, para quem quer ir fundo.'),
 (PSE, 'Como reconhecer e responder a pseudociências, negacionismo e desinformação.'),
]
LIVROS = [
b('O Mundo Assombrado pelos Demônios', 'Carl Sagan', 'A ciência como uma vela no escuro e o kit de detecção de besteiras.', INI),
b('Ciência Picareta', 'Ben Goldacre', 'Como a má ciência, a mídia e a indústria enganam sobre saúde.', INI),
b('Pensar Rápido e Devagar', 'Daniel Kahneman', 'Os dois sistemas da mente e os vieses que afetam nosso julgamento.', INI),
b('A Mente Batedora (The Scout Mindset)', 'Julia Galef', 'Por que algumas pessoas veem as coisas com clareza e outras não.', INI),
b('Como Mentir com Estatística', 'Darrell Huff', 'O clássico curto sobre gráficos e números enganosos.', INI),
b('Factfulness', 'Hans Rosling', 'Dez instintos que distorcem nossa visão do mundo, e como corrigi-los.', INI),
b('Testing Treatments', 'Imogen Evans, Hazel Thornton, Iain Chalmers', 'Por que tratamentos precisam ser testados, com versão gratuita online.', INI, 'https://www.testingtreatments.org/'),
b('O Que É Ciência, Afinal?', 'Alan Chalmers', 'A introdução mais usada à filosofia da ciência, de Bacon a Feyerabend.', INTM),
b('Filosofia da Ciência: uma brevíssima introdução', 'Samir Okasha', 'Indução, explicação, realismo e revoluções em poucas páginas.', INTM),
b('Teoria do Conhecimento', 'Johannes Hessen', 'Introdução clássica às questões da epistemologia.', INTM),
b('Os Problemas da Filosofia', 'Bertrand Russell', 'Conhecimento, aparência e realidade, num livro curto e claro.', INTM),
b('Lógica da Pesquisa Científica', 'Karl Popper', 'A falseabilidade e o método das conjecturas e refutações.', INTM),
b('A Estrutura das Revoluções Científicas', 'Thomas Kuhn', 'Paradigmas, ciência normal e revoluções.', INTM),
b('Contra o Método', 'Paul Feyerabend', 'A crítica às metodologias rígidas e o pluralismo.', AVA),
b('A Metodologia dos Programas de Pesquisa Científica', 'Imre Lakatos', 'Programas progressivos e degenerativos.', AVA),
b('Defending Science, Within Reason', 'Susan Haack', 'A ciência defendida contra cientificistas e relativistas.', AVA),
b('The Scientific Image', 'Bas van Fraassen', 'O empirismo construtivo e o debate sobre realismo.', AVA),
b('Representing and Intervening', 'Ian Hacking', 'Experimentos, entidades e o realismo da prática.', AVA),
b('Science as Social Knowledge', 'Helen Longino', 'Valores, crítica e objetividade como conquista coletiva.', AVA),
b('Why Trust Science?', 'Naomi Oreskes', 'Por que confiar na ciência, mesmo sabendo que ela erra.', AVA),
b('Science, Policy, and the Value-Free Ideal', 'Heather Douglas', 'O argumento do risco indutivo e o papel dos valores.', AVA),
b('Que Bobagem! Pseudociências e outros absurdos que não merecem ser levados a sério', 'Natalia Pasternak e Carlos Orsi', 'Homeopatia, astrologia, terapias alternativas, antivacina e outras: por que não se sustentam, por dois divulgadores brasileiros.', PSE),
b('Nonsense on Stilts', 'Massimo Pigliucci', 'Como distinguir ciência de pseudociência na prática.', PSE),
b('Mercadores da Dúvida', 'Naomi Oreskes e Erik Conway', 'Como um pequeno grupo de cientistas obscureceu a verdade sobre o tabaco e o clima.', PSE),
b('A Falsa Medida do Homem', 'Stephen Jay Gould', 'A história do racismo científico e da medição enviesada da inteligência.', PSE),
b('Foolproof', 'Sander van der Linden', 'A ciência da desinformação e da inoculação psicológica.', PSE),
b('Pseudociência e Ideologia', 'Mario Bunge', 'Critérios para reconhecer pseudociências, de um físico e filósofo latino-americano.', PSE),
b('Bad Pharma', 'Ben Goldacre', 'Como a indústria farmacêutica distorce a evidência, e o que fazer.', PSE),
]
NAC, INT = 'Em português', 'Em inglês'
GRUPOS_S = ['Enciclopédias, referência e dados', 'Evidência em saúde', 'Checagem e desinformação', 'Divulgação científica']
SITES = [
('Stanford Encyclopedia of Philosophy', 'https://plato.stanford.edu/', 'A enciclopédia de filosofia mais respeitada, com verbetes de especialistas.', 'Enciclopédias, referência e dados', INT),
('Internet Encyclopedia of Philosophy', 'https://iep.utm.edu/', 'Verbetes revisados, em geral mais introdutórios.', 'Enciclopédias, referência e dados', INT),
('Crítica na Rede', 'https://criticanarede.com/', 'Textos de filosofia em português, com boa seção de epistemologia.', 'Enciclopédias, referência e dados', NAC),
('Biblioteca de Dados (BiblioVerse)', 'https://data.biblioverse.org/', 'Catálogo das melhores fontes de dados e estatísticas, organizadas por tema.', 'Enciclopédias, referência e dados', NAC),
('SciELO', 'https://scielo.org/', 'Biblioteca de revistas científicas latino-americanas de acesso aberto.', 'Enciclopédias, referência e dados', NAC),
('Cochrane Brasil', 'https://brazil.cochrane.org/', 'Revisões sistemáticas independentes sobre tratamentos.', 'Evidência em saúde', NAC),
('Testing Treatments interactive', 'https://www.testingtreatments.org/', 'Por que e como tratamentos devem ser testados.', 'Evidência em saúde', INT),
('Conitec', 'https://www.gov.br/conitec/pt-br', 'Avaliações de tecnologias em saúde que orientam o SUS.', 'Evidência em saúde', NAC),
('Science-Based Medicine', 'https://sciencebasedmedicine.org/', 'Análises críticas de tratamentos e práticas alternativas.', 'Evidência em saúde', INT),
('Biblioteca da Racionalidade (BiblioVerse)', 'https://thinking.biblioverse.org/', 'Catálogo pesquisável de pensamento crítico, racionalidade e evidências.', 'Checagem e desinformação', NAC),
('Biblioteca de Conspirações (BiblioVerse)', 'https://conspiracy.biblioverse.org/', 'Teorias da conspiração, pseudociências e crenças falsas, e como desmenti-las.', 'Checagem e desinformação', NAC),
('Agência Lupa', 'https://lupa.uol.com.br/', 'Checagem de fatos, incluindo saúde e ciência.', 'Checagem e desinformação', NAC),
('Aos Fatos', 'https://www.aosfatos.org/', 'Checagem de fatos e investigação sobre desinformação.', 'Checagem e desinformação', NAC),
('Skeptical Science', 'https://skepticalscience.com/', 'Respostas aos argumentos do negacionismo climático, com as técnicas FLICC.', 'Checagem e desinformação', INT),
('Instituto Questão de Ciência', 'https://www.revistaquestaodeciencia.com.br/', 'Revista brasileira de defesa da ciência e crítica às pseudociências.', 'Checagem e desinformação', NAC),
('Our World in Data', 'https://ourworldindata.org/', 'Dados e gráficos sobre os grandes problemas do mundo, com fontes.', 'Divulgação científica', INT),
('Pesquisa FAPESP', 'https://revistapesquisa.fapesp.br/', 'Jornalismo científico sobre a pesquisa feita no Brasil.', 'Divulgação científica', NAC),
('Ciência Hoje', 'https://cienciahoje.org.br/', 'Revista de divulgação científica da SBPC.', 'Divulgação científica', NAC),
('Universo Racionalista', 'https://universoracionalista.org/', 'Portal brasileiro de divulgação científica, ceticismo e pensamento racional.', 'Divulgação científica', NAC),
]
