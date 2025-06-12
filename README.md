# Teoria dos Grafos Aplicada a Python

Este projeto demonstra uma implementação simples de grafos em Python, permitindo a criação, manipulação e consulta de grafos direcionados ou não direcionados.

## Estrutura do Projeto

- [`Grafo.py`](Grafo.py): Contém a classe [`grafo`](Grafo.py), responsável pela estrutura e operações do grafo.
- [`aresta.py`](aresta.py): Exemplo de uso da classe [`grafo`](Grafo.py), criando um grafo direcionado a partir de uma lista de arestas e realizando operações básicas.
- `__pycache__/`: Diretório gerado automaticamente pelo Python para armazenar arquivos compilados.

## Funcionalidades

- Criação de grafos direcionados ou não direcionados.
- Adição de arestas.
- Consulta de vértices e arestas.
- Verificação da existência de uma aresta entre dois vértices.
- Representação do grafo por meio de dicionário de adjacências.

## Exemplo de Uso

Veja o arquivo [`aresta.py`](aresta.py) para um exemplo prático:

```python
from Grafo import grafo

# Lista de arestas (origem, destino)
aresta = [('A', 'B'), ('B', 'C'), ('C', 'B'), ('D', 'A'), ('E', 'B')]

# Criação de um grafo direcionado
criar_grafo = grafo(aresta, direcionado=True)
print(criar_grafo.adj) # representação do grafo

print(criar_grafo.get_vertice())  # lista de vértices
print(criar_grafo.get_aresta())   # lista de arestas
print(criar_grafo.existe_aresta('A', 'B'))  # Verifica se existe a aresta de A para B
print(criar_grafo.existe_aresta('E', 'C'))  # Verifica se existe a aresta de E para C
```