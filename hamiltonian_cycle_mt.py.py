# Mapeamento de cidades para índices
city_to_index = {
    "Cáceres": 0,
    "Porto Esperidião": 1,
    "Glória D' Oeste": 2,
    "Curvelândia": 3,
    "Mirassol D' Oeste": 4,
    "São José Dos Quatro Marcos": 5,
    "Indiavai": 6,
    "Araputanga": 7,
    "Figueirópolis D' Oeste": 8,
    "Lambari D' Oeste": 9,
    "Rio Branco": 10,
    "Salto Do Céu": 11,
    "Reserva Do Cabaçal": 12,
    "Pontes Lacerda": 13,
    "Jauru": 14,
    "Vale são Domingos": 15
}

# Número de cidades
n = len(city_to_index)

# Inicializa a matriz de adjacência com zeros
graph = [[0] * n for _ in range(n)]

# Lista de arestas (cidades e distâncias)
edges = [
    ("Cáceres", "Curvelândia", 64),
    ("Cáceres", "Mirassol D' Oeste", 80),
    ("Cáceres", "Glória D' Oeste", 93),
    ("Cáceres", "Porto Esperidião", 107),
    ("Curvelândia", "Lambari D' Oeste", 39),
    ("Curvelândia", "Mirassol D' Oeste", 24),
    ("Mirassol D' Oeste", "São José Dos Quatro Marcos", 14),
    ("São José Dos Quatro Marcos", "Glória D' Oeste", 25),
    ("São José Dos Quatro Marcos", "Araputanga", 28),
    ("Araputanga", "Indiavai", 31),
    ("Araputanga", "Reserva Do Cabaçal", 55),
    ("Lambari D' Oeste", "Rio Branco", 17),
    ("Rio Branco", "Salto Do Céu", 15),
    ("Indiavai", "Figueirópolis D' Oeste", 20),
    ("Figueirópolis D' Oeste", "Jauru", 22),
    ("Jauru", "Vale são Domingos", 24),
    ("Vale são Domingos", "Pontes Lacerda", 35),
    ("Porto Esperidião", "Vale são Domingos", 112),
    ("Porto Esperidião", "Pontes Lacerda", 122)
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

# Encontrar o ciclo Hamiltoniano para o grafo construído
cycle = hamiltonian_cycle(graph)

# Converter índices de volta para nomes de cidades
if isinstance(cycle, list):
    cycle_cities = [list(city_to_index.keys())[index] for index in cycle]
    print("Ciclo Hamiltoniano:", cycle_cities)
else:
    print(cycle)
