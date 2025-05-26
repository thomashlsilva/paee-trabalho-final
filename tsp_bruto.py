from sys import maxsize
from itertools import permutations
import numpy as np
from datetime import datetime


def travellingSalesmanProblem(graph, start_node):
    """
    Soluciona o problema do caixeiro viajante via força bruta.
    """
    V = len(graph)
    vertices = [i for i in range(V) if i != start_node]

    min_path = maxsize
    for perm in permutations(vertices):
        current_cost = 0
        k = start_node
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start_node]  # volta ao início
        min_path = min(min_path, current_cost)

    return min_path


def main():
    # Exemplo com pequena dimensão, pois força bruta explode com n > 10
    V = 5  # Modificar conforme o teste
    np.random.seed(42)  # Para reprodutibilidade
    graph = np.random.randint(1, 100, (V, V))
    graph = (graph + graph.T) // 2  # Torna a matriz simétrica
    np.fill_diagonal(graph, 0)      # Distância para si mesmo é zero

    print("Matriz de distâncias:")
    print(graph)

    start_time = datetime.now()
    best_cost = travellingSalesmanProblem(graph, start_node=0)
    end_time = datetime.now()

    print(f"\nMelhor custo encontrado: {best_cost}")
    print(f"Tempo de execução: {end_time - start_time}")


if __name__ == "__main__":
    main()
