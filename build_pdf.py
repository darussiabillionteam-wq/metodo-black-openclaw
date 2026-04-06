from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.units import cm
from pathlib import Path

out_dir = Path(__file__).resolve().parent / 'assets'
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / 'Metodo-Black-Automacao-com-OpenClaw.pdf'

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleCenter', parent=styles['Title'], alignment=TA_CENTER, textColor=colors.black, fontSize=24, leading=30, spaceAfter=18))
styles.add(ParagraphStyle(name='BodyLarge', parent=styles['BodyText'], fontSize=12, leading=18, alignment=TA_LEFT, spaceAfter=10))
styles.add(ParagraphStyle(name='SmallMuted', parent=styles['BodyText'], fontSize=10, leading=14, textColor=colors.grey, alignment=TA_CENTER))

pages = [
    ("Método Black", "Automação com OpenClaw", [
        "Um guia prático para transformar agentes, bots e rotinas em operação digital enxuta.",
        "Objetivo: sair da curiosidade e chegar em ativos que economizam tempo, geram entrega e podem virar receita.",
        "Preço de lançamento do MVP: US$ 29.",
    ]),
    ("Como usar este material", "Leitura orientada a execução", [
        "Este PDF não foi escrito para impressionar tecnicamente. Foi escrito para fazer você agir.",
        "Cada capítulo responde a uma pergunta operacional: o que construir, em que ordem, como validar e como transformar automação em oferta.",
        "Se você aplicar só metade, já sai com um sistema melhor do que a maioria dos projetos que ficam apenas no discurso.",
    ]),
    ("Página 3", "O que é OpenClaw na prática", [
        "OpenClaw é uma base operacional para agentes que executam tarefas de verdade: pesquisa, conteúdo, integrações, mensagens, rotinas e coordenação.",
        "A vantagem não está só no chat. Está na combinação de contexto, ferramentas, memória e ação orientada a objetivo.",
        "Quem entende isso para de pensar em 'assistente fofo' e começa a pensar em 'infra de trabalho'.",
    ]),
    ("Página 4", "O erro mais caro", [
        "Muita gente tenta vender IA antes de ter um problema específico, um público específico e uma promessa clara.",
        "O resultado é previsível: páginas vagas, produtos genéricos e quase nenhuma compra.",
        "Automação útil começa na dor real, não na ferramenta bonita.",
    ]),
    ("Página 5", "A lógica do Método Black", [
        "A sequência correta é simples: captar sinal, validar interesse, criar um ativo mínimo, integrar pagamento e só então ampliar distribuição.",
        "Pular a validação faz você trabalhar mais e aprender menos.",
        "O método busca reduzir desperdício e aumentar velocidade de feedback.",
    ]),
    ("Página 6", "Escolha uma dor pagável", [
        "Dores pagáveis têm três traços: são frequentes, custam tempo ou dinheiro e já fazem alguém buscar solução hoje.",
        "Exemplos: responder leads devagar, produzir conteúdo sem consistência, perder venda por falta de follow-up, operar Telegram manualmente.",
        "Se a dor não dói no bolso, dificilmente vira venda rápida.",
    ]),
    ("Página 7", "Promessa orientada a resultado", [
        "Evite vender 'curso de OpenClaw'. Venda resultado mensurável com OpenClaw.",
        "Promessas melhores: reduzir horas de operação, acelerar resposta, montar funil simples, publicar conteúdo recorrente, organizar atendimento.",
        "O comprador quer ganho concreto, não apenas conhecimento abstrato.",
    ]),
    ("Página 8", "Oferta mínima que vende", [
        "Uma oferta mínima não precisa ser enorme. Precisa ser específica, clara e fácil de consumir.",
        "Pode ser um PDF operacional, um playbook com checklists, templates, scripts e uma trilha curta de implementação.",
        "O segredo é entregar clareza aplicável já na primeira leitura.",
    ]),
    ("Página 9", "Stack enxuta", [
        "Para um MVP de produto digital, você não precisa de arquitetura complexa.",
        "Uma landing page clara, um checkout funcional, um ativo digital bem estruturado e um canal de distribuição já são suficientes para testar venda.",
        "Simplicidade operacional aumenta a chance de lançar hoje.",
    ]),
    ("Página 10", "Pesquisa rápida de demanda", [
        "Use busca, comunidades e redes para observar linguagem real das pessoas.",
        "Procure perguntas repetidas, reclamações, improvisos e prints de resultado. Isso revela o que já tem urgência.",
        "A melhor copy quase sempre já está sendo dita pelo mercado.",
    ]),
    ("Página 11", "Validação sem burocracia", [
        "Você não precisa de 500 respostas. Precisa de algumas respostas certas.",
        "Converse com pessoas que já convivem com o problema e teste uma pergunta simples: 'se eu montar isso do jeito X, te ajuda de verdade?'.",
        "Observe linguagem, objeções, contexto e disposição de pagar.",
    ]),
    ("Página 12", "Precificação inicial", [
        "No MVP, o preço existe para gerar aprendizado e compromisso.",
        "US$ 29 funciona como faixa de entrada para uma compra impulsiva com valor percebido razoável.",
        "Depois das primeiras vendas, preço e empacotamento podem mudar rapidamente.",
    ]),
    ("Página 13", "A estrutura da landing page", [
        "Uma landing page enxuta deve responder: para quem é, qual resultado promete, o que está incluído, quanto custa e por que agir agora.",
        "Remova distrações. Um objetivo por página vende melhor que um menu cheio de caminhos paralelos.",
        "Texto curto, benefício claro e CTA repetido vencem páginas prolixas.",
    ]),
    ("Página 14", "Headline forte", [
        "Headline boa combina público, dor e transformação.",
        "Exemplo: 'Monte uma operação enxuta com OpenClaw para automatizar conteúdo, atendimento e rotina sem depender de time técnico'.",
        "Se a headline não deixa o leitor se reconhecer, a página perde força logo no topo.",
    ]),
    ("Página 15", "Bullets que puxam ação", [
        "Bullets servem para tornar o valor visível em segundos.",
        "Mostre entregáveis concretos: mapa de automações, modelos de prompts, checklists, fluxo de publicação e roteiro de implementação.",
        "Quanto mais tangível for a entrega, menor a fricção na compra.",
    ]),
    ("Página 16", "Objeções mais comuns", [
        "As objeções típicas são: 'não sou técnico', 'não tenho tempo', 'já comprei curso e não apliquei' e 'não sei se isso funciona no meu caso'.",
        "Responda todas na própria página com linguagem simples e prova contextual.",
        "Quem remove objeção antes do checkout melhora conversão sem aumentar tráfego.",
    ]),
    ("Página 17", "Checkout com Stripe", [
        "Stripe resolve pagamento com confiança visual, cartões internacionais e fluxo rápido.",
        "Para MVP, o ideal é checkout simples com descrição objetiva e redirecionamento claro após a compra.",
        "O trabalho do checkout é reduzir atrito, não contar história.",
    ]),
    ("Página 18", "Entrega do digital", [
        "No começo, a entrega pode ser simples: página de obrigado com acesso ao arquivo ou instrução clara de recebimento.",
        "Perfeição técnica não é requisito para validar demanda. Clareza e consistência são.",
        "Se vender, você automatiza depois. Primeiro prove tração.",
    ]),
    ("Página 19", "Conteúdo para atrair atenção", [
        "Os melhores posts de aquisição mostram microtransformações: antes e depois, erros caros, bastidores e atalhos operacionais.",
        "Evite falar só da ferramenta. Fale do ganho operacional ou financeiro que ela permite.",
        "Autoridade cresce quando você demonstra processo, não quando promete magia.",
    ]),
    ("Página 20", "Canais de distribuição", [
        "Comece pelos canais onde já existe acesso: grupo, lista, perfil social, contatos quentes e comunidade própria.",
        "No MVP, alcance menor com contexto vale mais que grande volume frio.",
        "Distribuição inteligente é escolher o público certo antes de ampliar alcance.",
    ]),
    ("Página 21", "Prova e credibilidade", [
        "Quando ainda não existe prova social forte, use prova de processo: clareza do método, material organizado, demonstrações e consistência da oferta.",
        "Não invente depoimentos. Construa confiança com honestidade e execução visível.",
        "Credibilidade sem teatro dura mais.",
    ]),
    ("Página 22", "Métricas mínimas", [
        "Para decidir rápido, acompanhe poucas métricas: visitas, cliques no CTA, checkouts iniciados e compras concluídas.",
        "Se muita gente visita e poucas clicam, o problema está na copy. Se clicam e não compram, revise preço, oferta ou checkout.",
        "Métrica boa é a que leva a decisão, não a vaidade.",
    ]),
    ("Página 23", "Iteração em 24 horas", [
        "Produto digital rápido melhora por ciclos curtos.",
        "Depois das primeiras 24 horas, ajuste headline, preço, bônus, CTA e posicionamento conforme o comportamento real.",
        "Esperar semanas para mexer é perder aprendizado barato.",
    ]),
    ("Página 24", "Automação de conteúdo", [
        "Uma das aplicações mais rentáveis do OpenClaw é transformar ideias, provas e rotinas em conteúdo reaproveitável.",
        "Isso reduz custo de criação e aumenta consistência de presença digital.",
        "Conteúdo que nasce de processo real converte melhor do que opinião genérica.",
    ]),
    ("Página 25", "Automação de atendimento", [
        "Outra frente poderosa é atendimento guiado por contexto: responder dúvidas, encaminhar próximos passos e organizar follow-up.",
        "Mesmo uma automação parcial já economiza energia operacional importante.",
        "Atendimento mais rápido costuma elevar percepção de valor.",
    ]),
    ("Página 26", "Automação de pesquisa", [
        "Com a combinação certa de memória, busca e síntese, OpenClaw acelera diagnóstico de mercado e leitura de sinais.",
        "Isso ajuda a escolher melhores ofertas, ângulos e oportunidades antes de gastar energia criando coisas aleatórias.",
        "Pesquisa bem aplicada evita semanas de trabalho desperdiçado.",
    ]),
    ("Página 27", "Operação solo", [
        "Quem opera sozinho precisa de alavanca, não de complexidade.",
        "O foco deve estar em sistemas pequenos que eliminam repetição e liberam tempo para vendas, melhoria e distribuição.",
        "Automação boa é a que torna a rotina mais leve e mais lucrativa.",
    ]),
    ("Página 28", "Erros para evitar", [
        "Não esconda preço, não complique o checkout, não faça página confusa e não escreva como se estivesse dando palestra técnica.",
        "Evite também criar um material inchado só para parecer premium.",
        "Valor percebido nasce de clareza, aplicabilidade e resultado esperado.",
    ]),
    ("Página 29", "Plano de execução em 1 dia", [
        "Manhã: definir promessa, estrutura e página. Tarde: ajustar checkout, gerar ativo e revisar copy. Noite: publicar e divulgar.",
        "Lançamento simples é principalmente decisão. Ferramentas já existem.",
        "Quem encurta o caminho para o mercado aprende mais rápido que quem fica polindo bastidor.",
    ]),
    ("Página 30", "Fechamento", [
        "O Método Black não é sobre estudar IA infinitamente. É sobre colocar automação para trabalhar a favor da operação.",
        "Lance pequeno, observe a resposta, ajuste sem apego e mantenha a cadência.",
        "Receita nasce quando execução encontra distribuição.",
    ]),
]


def header_footer(canvas, doc):
    page_num = canvas.getPageNumber()
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.grey)
    canvas.drawRightString(19.2*cm, 1.2*cm, f'{page_num}')
    canvas.drawString(1.8*cm, 1.2*cm, 'Método Black: Automação com OpenClaw')

story = []
for i, (label, title, body) in enumerate(pages):
    story.append(Spacer(1, 2.4*cm))
    story.append(Paragraph(label, styles['SmallMuted']))
    story.append(Spacer(1, 0.6*cm))
    story.append(Paragraph(title, styles['TitleCenter']))
    story.append(Spacer(1, 0.3*cm))
    for paragraph in body:
        story.append(Paragraph(paragraph, styles['BodyLarge']))
    if i < len(pages) - 1:
        story.append(PageBreak())

doc = SimpleDocTemplate(str(out), pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(out)
