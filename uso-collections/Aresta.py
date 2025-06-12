from Grafo import grafo

# Lista de arestas (origem, destino)
aresta = [('A', 'B'), ('B', 'C'), ('C', 'B'), ('D', 'A'), ('E', 'B')]

# O grafo é direcionado a partir da lista de arestas
criar_grafo = grafo(aresta, direcionado=True)
print(criar_grafo.adj) # representação do grafo

print(criar_grafo.get_vertice())  # lista de vértices
print(criar_grafo.get_aresta())   # lista de arestas
print(criar_grafo.existe_aresta('A', 'B'))  # Verifica se existe a aresta de A para B
print(criar_grafo.existe_aresta('E', 'C'))  # Verifica se existe a aresta de E para C