from collections import defaultdict

class grafo(object):
    def __init__(self, aresta, direcionado=False):
        self.adj = defaultdict(set) # adj = adjacência
        # Define se o grafo é direcionado ou não
        self.direcionado = direcionado
        # Adiciona as arestas iniciais ao grafo
        self.adicionar_aresta(aresta)

    def get_vertice(self):
        # Retorna uma lista com todos os vértices do grafo
        return list(self.adj.keys())
    
    def get_aresta(self):
        # Retorna uma lista de tuplas representando todas as arestas do grafo
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]
    
    def adicionar_aresta(self, aresta):
        # Adiciona múltiplas arestas ao grafo
        for u, v in aresta:
            self.adiciona_ligacao(u, v)

    def adiciona_ligacao(self, u, v):
        # Adiciona uma ligação (aresta) entre os vértices u e v
        self.adj[u].add(v)
        # Se o grafo não for direcionado, adiciona a ligação inversa também
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v):
        # Verifica se existe uma aresta entre u e v
        return u in self.adj and v in self.adj[u]
    
    def __len__(self):
        # Retorna o número de vértices do grafo
        return len(self.adj)
    
    def __str__(self):
        # Retorna uma representação em string do grafo
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))
    
    def __getitem__(self, v):
        # Permite acessar os vizinhos de um vértice usando a sintaxe do dicionário
        return self.adj[v]