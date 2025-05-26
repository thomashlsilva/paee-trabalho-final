def read_file(filename):
    """
    Lê um arquivo no formato TSPLIB e retorna a matriz triangular em forma de lista.
    """
    matrix = []
    with open(filename, 'r') as file:
        started = False
        for line in file:
            line = line.strip()
            if line == "EOF":
                break
            if started:
                ex = line.split()
                matrix += [int(e) for e in ex]
            if line == "EDGE_WEIGHT_SECTION":
                started = True
    return matrix


def get_dimension(filename):
    """
    Extrai o tamanho (DIMENSION) da matriz diretamente do arquivo.
    """
    with open(filename, 'r') as file:
        for line in file:
            if "DIMENSION" in line:
                return int(line.split()[-1])
    raise ValueError("DIMENSION não encontrada no arquivo")


def complete_matrix(array, size):
    """
    Converte a lista da matriz triangular superior em uma matriz completa simétrica.
    """
    c = 0
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(i, size):
            matrix[i][j] = array[c]
            matrix[j][i] = array[c]
            c += 1
    return matrix


def save_matrix(matrix, output="out.txt"):
    """
    Salva a matriz em um arquivo de texto.
    """
    with open(output, 'w') as f:
        for row in matrix:
            f.write(" ".join(str(e) for e in row) + "\n")


def main():
    filename = "scripts-externos/data/si1032.txt"
    dim = get_dimension(filename)
    matrix_raw = read_file(filename)
    matrix = complete_matrix(matrix_raw, dim)
    save_matrix(matrix, output="out_si1032.txt")
    print(f"Matriz {dim}x{dim} salva em 'out_si1032.txt'")


if __name__ == '__main__':
    main()
