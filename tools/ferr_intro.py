"""Texto fixo das páginas de ferramentas (2026-11-20): o que a ferramenta treina, como usar e que lições revisar.
Dá às páginas conteúdo legível sem JavaScript, para leitores e buscadores. FERR_INTRO[slug] = (parágrafos, lições)."""
FERR_INTRO = {
 'ciencia-ou-pseudociencia': ([
   'Este jogo treina a pergunta central da demarcação: o que separa uma afirmação científica de uma que só parece científica? Cada item descreve uma prática ou afirmação real ou típica. Em vez de decorar listas de pseudociências, você aprende a olhar para os sinais: a afirmação pode ser testada e dar errado? Quem a defende aceita evidência contrária? Ela se apoia em revisões sistemáticas ou em depoimentos?',
   'Não há pegadinha de vocabulário: palavras como “quântico”, “natural” ou “energia” aparecem dos dois lados. O que decide é o método. Depois de cada resposta, a explicação diz o motivo, e as lições abaixo aprofundam os critérios.'],
   ['o-que-e-pseudociencia', 'criterio-da-demarcacao', 'popper-e-a-falseabilidade', 'e-ciencia-ou-nao', 'niveis-de-evidencia']),
 'opiniao-crenca-ou-conhecimento': ([
   'Nem toda frase dita com convicção é conhecimento. Este exercício separa três coisas que o dia a dia mistura: preferências (gosto, que não precisa de prova), crenças sem boas razões (que podem até ser verdadeiras, por sorte) e conhecimento justificado (crença verdadeira apoiada em evidência ou em raciocínio confiável).',
   'A distinção vem da epistemologia, a parte da filosofia que estuda o conhecimento, e tem uso prático: ela diz quando uma discordância se resolve com dados, quando se resolve com argumentos e quando não precisa ser resolvida.'],
   ['opiniao-crenca-e-conhecimento', 'crenca-verdadeira-justificada', 'como-justificar-uma-crenca', 'o-que-e-epistemologia', 'o-problema-de-gettier']),
 'nivel-de-evidencia': ([
   'Estudos diferentes dão graus diferentes de confiança. Um relato de caso mostra que algo pode acontecer; um estudo observacional mostra associação; um ensaio clínico randomizado testa causa; uma revisão sistemática reúne todos os estudos de qualidade sobre a pergunta. Aqui você classifica estudos descritos em uma frase.',
   'A pirâmide é um atalho, não uma lei: um ensaio mal feito vale menos que um bom estudo observacional, e algumas perguntas só podem ser respondidas por observação. As lições abaixo explicam a pirâmide, seus limites e como ler um artigo.'],
   ['niveis-de-evidencia', 'experimentos-e-grupo-controle', 'pratica-baseada-em-evidencias', 'como-achar-e-julgar-artigos', 'experimentos-naturais']),
 'correlacao-ou-causa': ([
   'Manchetes do tipo “quem faz X tem mais Y” são comuns e quase sempre descrevem uma associação, não uma causa. Para cada uma, o jogo pede a explicação mais provável: causa direta, causa ao contrário, um terceiro fator que explica os dois (confusão), seleção de quem entrou no estudo ou simples acaso.',
   'É a habilidade mais útil para ler notícias de saúde, educação e economia. As lições abaixo mostram como os cientistas separam correlação de causa: grupo controle, randomização, experimentos naturais e estatística.'],
   ['correlacao-e-causalidade', 'experimentos-e-grupo-controle', 'experimentos-naturais', 'como-ler-noticia-de-ciencia', 'estatistica-para-entender-ciencia']),
 'consenso-ou-em-aberto': ([
   'A ciência não está “em dúvida sobre tudo” nem “certa de tudo”. Algumas conclusões são consenso, sustentadas por várias linhas de evidência independentes e por academias de ciência; outras são perguntas em aberto, investigadas ativamente; e outras foram testadas e refutadas.',
   'Saber em que categoria uma afirmação está é o primeiro passo para não cair em falso equilíbrio, quando um debate resolvido é apresentado como se tivesse dois lados iguais, nem em falsa certeza, quando uma hipótese é vendida como fato.'],
   ['consenso-cientifico', 'grandes-consensos-cientificos', 'perguntas-em-aberto', 'negacionismo-e-desinformacao', 'confianca-e-especialistas']),
 'que-corrente-e-essa': ([
   'As correntes da filosofia da ciência discordam sobre o que faz a ciência funcionar: a observação, a lógica, a falseabilidade, os paradigmas, a comunidade, a utilidade. Cada frase do jogo destaca um desses pontos focais, e você reconhece a corrente que o põe no centro.',
   'O objetivo não é decorar nomes, e sim perceber que cada corrente ilumina uma parte real da ciência e deixa outra na sombra. As páginas das correntes mostram forças, objeções e o que cada uma não é.'],
   ['positivismo', 'popper-e-a-falseabilidade', 'kuhn-e-os-paradigmas', 'lakatos-e-feyerabend', 'realismo-e-antirrealismo', 'sociologia-do-conhecimento-cientifico']),
 'quem-disse': ([
   'Doze teses que marcaram a forma como entendemos a ciência, de Bacon e Hume a Popper, Kuhn e Haack. Você liga cada ideia a quem a defendeu e, a cada resposta, vê o contexto da tese.',
   'Os pensadores aparecem pelo que propuseram, não por citações soltas: cada perfil do site traz as ideias principais, as obras e o que dizem os críticos.'],
   ['uma-breve-historia-da-ciencia', 'empirismo-e-racionalismo', 'o-problema-da-inducao', 'popper-e-a-falseabilidade', 'kuhn-e-os-paradigmas']),
 'detector-de-pseudociencia': ([
   'O detector reúne sinais de alerta que filósofos da ciência e céticos apontam em práticas pseudocientíficas: afirmações que não podem dar errado, apelo a depoimentos em vez de estudos controlados, ataque a quem critica, promessas de cura para muitas doenças, linguagem científica sem conteúdo testável e recusa a mudar diante de evidência.',
   'Ele não dá veredito. Uma prática com muitos sinais merece desconfiança e uma busca por revisões sistemáticas; uma com poucos sinais ainda precisa mostrar evidência a favor. Use-o com produtos, terapias, cursos e afirmações que circulam nas redes.'],
   ['o-que-e-pseudociencia', 'ceticismo-responsavel', 'falacias-e-argumentos', 'vieses-e-metodo', 'como-funciona-a-checagem']),
}

# Nomes que não podem ser buscados só pelo sobrenome no texto do site (outro autor ou palavra comum).
SO_NOME_COMPLETO = {'william-james', 'david-chalmers', 'rosalind-franklin', 'marie-curie', 'michael-e-mann', 'brian-cox', 'simon-singh',
                    'oliver-sacks', 'ronald-fisher', 'bill-nye', 'oswaldo-cruz', 'carlos-chagas', 'merton'}
