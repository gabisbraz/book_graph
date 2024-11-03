import numpy as np
import ast


def ler_arquivo_e_criar_matriz(arquivo, vertices_selecionados):
    with open(arquivo, "r", encoding="utf-8") as f:
        # Ignora as primeiras duas linhas: tipo do grafo e número de vértices
        f.readline()
        num_vertices = int(f.readline().strip())

        # Ignora a lista de vértices (títulos dos livros)
        for _ in range(num_vertices):
            f.readline()

        # Lê a quantidade de arestas
        num_arestas = int(f.readline().strip())

        # Cria uma matriz de adjacência menor para os vértices selecionados
        matriz_adj_selecionada = np.zeros(
            (len(vertices_selecionados), len(vertices_selecionados)), dtype=int
        )

        # Lê as arestas e preenche a matriz de adjacência reduzida com os pesos
        for _ in range(num_arestas):
            linha = f.readline().strip()
            if linha:
                linha_split = linha.split(" ", 3)

                vertice1 = int(linha_split[0])
                vertice2 = int(linha_split[1])
                peso = int(linha_split[2])

                # Verifica se os vértices da aresta estão nos vértices selecionados
                if (
                    vertice1 in vertices_selecionados
                    and vertice2 in vertices_selecionados
                ):
                    idx1 = vertices_selecionados.index(vertice1)
                    idx2 = vertices_selecionados.index(vertice2)

                    # Preenche a matriz simetricamente, pois o grafo é não direcionado
                    matriz_adj_selecionada[idx1][idx2] = peso
                    matriz_adj_selecionada[idx2][idx1] = peso

    # Exibindo a matriz reduzida no formato desejado
    for i in range(len(vertices_selecionados)):
        print(", ".join(map(str, matriz_adj_selecionada[i])))


# Vértices que queremos selecionar (exemplo: 0, 1 e 2)
vertices_selecionados = [1, 2, 3, 4, 5, 6]

# Chame a função com o nome do arquivo e os vértices selecionados
arquivo = "app/data/output/grafo.txt"
ler_arquivo_e_criar_matriz(arquivo, vertices_selecionados)
