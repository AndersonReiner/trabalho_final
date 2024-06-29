import networkx as nx
import matplotlib.pyplot as plt

# Mapeamento de cidades para índices
city_to_index = {
    "Cáceres": 0,
    "Curvelândia": 1,
    "Mirassol D' Oeste": 2,
    "São José Dos Quatro Marcos": 3
}

# Número de cidades
n = len(city_to_index)

# Inicializa a matriz de adjacência com zeros
graph = [[0] * n for _ in range(n)]

# Lista de arestas (cidades e distâncias)
edges = [
    ("Cáceres", "Curvelândia", 64),
    ("Curvelândia", "Mirassol D' Oeste", 24),
    ("Mirassol D' Oeste", "São José Dos Quatro Marcos", 14),
    ("São José Dos Quatro Marcos", "Cáceres", 80)
]

# Preenche a matriz de adjacência com as distâncias
for city1, city2, distance in edges:
    i = city_to_index[city1]
    j = city_to_index[city2]
    graph[i][j] = distance
    graph[j][i] = distance  # Grafo não-direcional

# Função que verifica se a cidade v pode ser adicionada ao caminho Hamiltoniano
def is_safe(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False  # Sem conexão
    if v in path:
        return False  # Cidade já incluída
    return True

# Função recursiva para encontrar o ciclo Hamiltoniano
def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] != 0:
            return True
        else:
            return False

    for v in range(1, len(graph)):
        if is_safe(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1  # Backtracking
    return False

# Função principal para encontrar o ciclo Hamiltoniano
def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0  # Começa pela primeira cidade
    if not hamiltonian_cycle_util(graph, path, 1):
        return "Não existe ciclo Hamiltoniano"
    return path

# Função para desenhar o grafo e o ciclo Hamiltoniano
def draw_graph_with_cycle(graph, cycle, city_to_index):
    G = nx.Graph()
    pos = {}
    
    # Adiciona os nós e as arestas ao grafo NetworkX
    for city1, city2, distance in edges:
        G.add_edge(city1, city2, weight=distance)
    
    # Define a posição dos nós para uma melhor visualização
    pos = nx.spring_layout(G)

    # Desenha o grafo com todas as arestas
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Destaca as arestas do ciclo Hamiltoniano
    cycle_edges = [(list(city_to_index.keys())[cycle[i]], list(city_to_index.keys())[cycle[i+1]]) for i in range(len(cycle) - 1)]
    cycle_edges.append((list(city_to_index.keys())[cycle[-1]], list(city_to_index.keys())[cycle[0]]))
    nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color='r', width=2)

    # Mostra o grafo
    plt.title("Grafo e Ciclo Hamiltoniano")
    plt.show()

# Encontrar o ciclo Hamiltoniano para o grafo construído
cycle = hamiltonian_cycle(graph)

# Converter índices de volta para nomes de cidades
if isinstance(cycle, list):
    cycle_cities = [list(city_to_index.keys())[index] for index in cycle]
    print("Ciclo Hamiltoniano:", cycle_cities)
    # Desenhar o grafo com o ciclo Hamiltoniano
    draw_graph_with_cycle(graph, cycle, city_to_index)
else:
    print(cycle)
