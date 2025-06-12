import matplotlib.pylab as grafico
import networkx as bibliotecaNetworkx

# Cria um novo grafo não direcionado
grafo = bibliotecaNetworkx.Graph()

# Adiciona os vértices ao grafo
grafo.add_node("A")
grafo.add_node("B")
grafo.add_node("C")
grafo.add_node("D")
grafo.add_node("E")
grafo.add_node("F")

# Adiciona as arestas (ligações) entre os vértices
grafo.add_edge("A", "B")
grafo.add_edge("B", "C")
grafo.add_edge("C", "D")
grafo.add_edge("D", "E")
grafo.add_edge("E", "F")
grafo.add_edge("F", "A")

# Define o posicionamento dos vértices em formato circular
posicionamento = bibliotecaNetworkx.circular_layout(grafo)

# Adiciona rótulos às arestas do grafo
bibliotecaNetworkx.draw_networkx_edge_labels(
    grafo,
    posicionamento,
    edge_labels={
        ("A", "B"): "Aresta A-B",
        ("B", "C"): "Aresta B-C",
        ("C", "D"): "Aresta C-D",
        ("D", "E"): "Aresta D-E",
        ("E", "F"): "Aresta E-F",
        ("F", "A"): "Aresta F-A"
    },
    font_color="red"
)

# Desenha o grafo com os vértices e arestas coloridos
bibliotecaNetworkx.draw(
    grafo,
    with_labels=True,
    pos=posicionamento,
    node_color="pink",
    edge_color="pink"
)

# Exibe o grafo na tela
grafico.savefig("meu_grafo.png", format="png", dpi=300)  # Salva o grafo como uma imagem
grafico.close()  # Fecha o gráfico