import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_pdf import PdfPages

# Função para desenhar o grafo com as cores e pesos das arestas atualizados
def desenharGrafo(colors, weights):
    global contadorFigura
    nx.draw(G, with_labels=True, 
            pos=posicionamento, 
            edge_color=colors, 
            width=list(weights), 
            node_color='red')
    pdf.savefig()
    nomeDaImagem = f"figura_{str(contadorFigura)}.jpg"
    contadorFigura += 1
    plt.savefig(nomeDaImagem)
    plt.show()

# Função para desenhar o grafo pela primeira vez
def desenhoInicialDoGrafo():
    global weights, posicionamento
    for n1, n2 in arestas:
        G.add_edge(n1, n2, label=f"{n1}->{n2}", color='black', weight=1)

    colors, weights = definirAtributosDasArestas()
    posicionamento = nx.planar_layout(G)
    desenharGrafo(colors, weights)

# Função para pegar as cores e pesos das arestas do grafo
def definirAtributosDasArestas():
    colors = list(nx.get_edge_attributes(G, 'color').values())
    weights = list(nx.get_edge_attributes(G, 'weight').values())
    return colors, weights

# Atualiza o desenho do grafo quando uma aresta é visitada
def atualizarDesenhoDoGrafo(v1, v2):
    global corAtualizada, contadorDeCor, controleDeCor
    controleDeCor = True
    G.edges[v1, v2]["color"] = corAtualizada[contadorDeCor]  # Muda a cor da aresta visitada
    G.edges[v1, v2]["weight"] = 4  # Destaca a aresta aumentando o peso
    colors, weights = definirAtributosDasArestas()
    desenharGrafo(colors, weights)

# Inicializa variáveis de controle usadas na busca em profundidade
def inicializarVariaveisDeControle():
    global valorDeProfundidadeEntrada, valorDeProfundidadeSaida, profundidadeDeEntradaESaida, verticesPai, niveis, \
    controleDeVertices, demarcadores, verticeComSaidasValidas, \
    corAtualizada, contadorDeCor, controleDeCor
    valorDeProfundidadeEntrada = 0
    valorDeProfundidadeSaida = 0
    profundidadeDeEntradaESaida = {}
    verticesPai = {}
    niveis = {}
    controleDeVertices = {}
    demarcadores = set()
    verticeComSaidasValidas = set()
    corAtualizada = ['red', 'blue', 'green', 'yellow', 'orange']
    contadorDeCor = 0
    controleDeCor = True

# Função principal da busca em profundidade
def buscaEmProfundidade(vertices, arestas, verticeGrafo):
    inicializarVariaveisDeControle()
    grafo = {}
    # Monta o grafo como dicionário de listas
    for v in vertices:
        grafo[v] = []
        for a in arestas:
            if v == a[0]:
                grafo[v].append(a[1])
    for vertice in grafo:
        controleDeVertices[vertice] = vertice

    verticesPai[verticeGrafo] = None  # Raiz não tem pai
    quantidadeDeFilhosRaiz = procuraProximoVertice(grafo, verticeGrafo, 1)
    if quantidadeDeFilhosRaiz <= 1:
        verticeComSaidasValidas.remove(verticeGrafo)

# Função recursiva que faz a busca em profundidade
def procuraProximoVertice(grafo, verticeGrafo, nivel):
    global valorDeProfundidadeEntrada, valorDeProfundidadeSaida, contadorDeCor, controleDeCor
    valorDeProfundidadeEntrada += 1
    profundidadeDeEntradaESaida[verticeGrafo] = [valorDeProfundidadeEntrada, None]
    niveis[verticeGrafo] = nivel

    contadorDeFilhos = 0

    for proximoVertice in grafo.get(verticeGrafo, []):
        if not profundidadeDeEntradaESaida.get(proximoVertice):
            verticesPai[proximoVertice] = verticeGrafo
            contadorDeFilhos += 1
            atualizarDesenhoDoGrafo(verticeGrafo, proximoVertice)  # Destaca a aresta visitada
            procuraProximoVertice(grafo, proximoVertice, nivel + 1)
            # Atualiza o controle de vértices conforme a profundidade
            if niveis[controleDeVertices[proximoVertice]] < niveis[controleDeVertices[verticeGrafo]]:
                controleDeVertices[verticeGrafo] = controleDeVertices[proximoVertice]

            # Marca vértices especiais
            if verticeGrafo in demarcadores:
                verticeComSaidasValidas.add(verticeGrafo)
            else:
                if not profundidadeDeEntradaESaida[proximoVertice][1]:
                    if verticesPai[verticeGrafo] != proximoVertice:
                        if niveis[proximoVertice] < niveis[controleDeVertices[verticeGrafo]]:
                            controleDeVertices[verticeGrafo] = proximoVertice

    valorDeProfundidadeSaida += 1
    profundidadeDeEntradaESaida[verticeGrafo][1] = valorDeProfundidadeSaida
    # Marca vértices que são "demarcadores" e muda a cor para o próximo passo
    if controleDeVertices[verticeGrafo] in (verticeGrafo, verticesPai[verticeGrafo]):
        demarcadores.add(verticeGrafo)
        if controleDeCor:
            contadorDeCor += 1
            controleDeCor = False
    return contadorDeFilhos

# Cria o grafo direcionado
G = nx.DiGraph()
contadorFigura = 1
pdf = PdfPages("GrafoPassoAPasso.pdf")
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
arestas = [('A', 'B'), ('A', 'E'), ('B', 'C'), ('E', 'D'), ('E', 'F'), ('C', 'E'), ('F', 'D'), ('A', 'G'), ('G', 'D')]

desenhoInicialDoGrafo()
buscaEmProfundidade(vertices, arestas, 'A')  # Executa a busca em profundidade

pdf.close()