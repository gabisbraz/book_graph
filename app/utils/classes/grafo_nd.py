"""
Biblioteca Conectada: Explorando Relações entre Livros

Membros do Grupo:
1. Gabriella Silveira Braz - 10402554
2. Giovana Liao - 10402264
3. Maria Julia de Pádua - 10400630

Síntese do Conteúdo:
O menu interativo da aplicação é projetado para facilitar a interação do usuário com as 
funcionalidades disponíveis para gerenciar o grafo. Ele apresenta uma lista de opções 
numeradas, permitindo que o usuário selecione a operação desejada de forma intuitiva. 
As opções incluem a adição e remoção de vértices, que possibilitam ao usuário incluir 
ou excluir livros do grafo. Também há a possibilidade de adicionar e remover arestas, 
permitindo a criação ou a eliminação de relações entre os livros.

Além disso, o menu oferece opções para visualizar a lista de adjacência do grafo, 
proporcionando uma representação clara das conexões entre os livros. O usuário pode 
também acessar funções para carregar dados a partir de um arquivo, facilitando a 
importação de informações, e salvar a estrutura do grafo em um arquivo para registro 
ou análise posterior. Outra funcionalidade disponível no menu é a geração de um gráfico 
visual do grafo, utilizando a biblioteca PyVis, o que permite uma visualização mais 
intuitiva das relações entre os livros.

O menu é projetado para ser interativo e responsivo, com a opção de sair da aplicação 
a qualquer momento. Essa abordagem interativa garante que o usuário possa navegar 
facilmente entre as opções e realizar as operações desejadas de maneira eficiente.

"""

import ast
import sys
from pathlib import Path
from pyvis.network import Network

DIR_ROOT = str(Path(__file__).parents[3])
if DIR_ROOT not in sys.path:
    sys.path.append(DIR_ROOT)

try:
    from app.utils.classes.vertice import Vertice
    from app.utils.classes.aresta import Aresta
except ModuleNotFoundError:
    from utils.classes.vertice import Vertice
    from utils.classes.aresta import Aresta


class TGrafoND:
    def __init__(self):
        """
        Inicializa o grafo não direcionado com lista de adjacência.
        """
        self.vertices = []  # Lista de vértices
        self.lista_adjacencia = (
            {}
        )  # Lista de adjacência (dicionário onde cada vértice aponta para uma lista de arestas)

    def insereVertice(self, nome_livro: str):
        """
        Insere um vértice no grafo.

        Args:
            nome_livro (str): Nome do livro que o vértice irá representar.
        """
        novo_vertice = Vertice(len(self.vertices), nome_livro)
        self.vertices.append(novo_vertice)
        self.lista_adjacencia[novo_vertice.id] = (
            []
        )  # Inicializa a lista de adjacência para o novo vértice

    def removeVertice(self, vertice_id: int):
        """
        Remove um vértice do grafo, bem como todas as arestas associadas a ele.

        Args:
            vertice_id (int): O índice do vértice a ser removido.
        """
        # Remove as arestas que conectam outros vértices a este vértice
        for vertice, arestas in self.lista_adjacencia.items():
            self.lista_adjacencia[vertice] = [
                aresta for aresta in arestas if aresta.destino.id != vertice_id
            ]

        # Remove o próprio vértice e sua lista de adjacências
        del self.lista_adjacencia[vertice_id]

        # Remove o vértice da lista de vértices
        self.vertices = [
            vertice for vertice in self.vertices if vertice.id != vertice_id
        ]

        # Atualiza o ID dos vértices e lista de adjacência
        for i, vertice in enumerate(self.vertices):
            vertice.id = i  # Reatribui IDs
        self.lista_adjacencia = {
            i: self.lista_adjacencia.get(i, []) for i in range(len(self.vertices))
        }

    def insereAresta(
        self,
        vertice_origem_id: int,
        vertice_destino_id: int,
        peso: int = 1,
        generos_comuns=None,
    ):
        """
        Insere uma aresta entre dois vértices no grafo.

        Args:
            vertice_origem_id (int): Índice do vértice de origem.
            vertice_destino_id (int): Índice do vértice de destino.
            peso (int): Peso da aresta.
            generos_comuns (list): Gêneros em comum entre os livros.
        """
        if generos_comuns is None:
            generos_comuns = []

        vertice_origem = self.vertices[vertice_origem_id]
        vertice_destino = self.vertices[vertice_destino_id]

        # Cria uma nova aresta
        nova_aresta = Aresta(vertice_origem, vertice_destino, peso, generos_comuns)

        # Adiciona a aresta na lista de adjacência (grafo não-direcionado)
        self.lista_adjacencia[vertice_origem.id].append(nova_aresta)
        self.lista_adjacencia[vertice_destino.id].append(
            Aresta(vertice_destino, vertice_origem, peso, generos_comuns)
        )

    def removeAresta(self, vertice_origem_id: int, vertice_destino_id: int):
        """
        Remove uma aresta entre dois vértices.

        Args:
            vertice_origem_id (int): Índice do vértice de origem.
            vertice_destino_id (int): Índice do vértice de destino.
        """
        # Remove a aresta da lista de adjacência do vértice de origem
        self.lista_adjacencia[vertice_origem_id] = [
            aresta
            for aresta in self.lista_adjacencia[vertice_origem_id]
            if aresta.destino.id != vertice_destino_id
        ]
        # Remove a aresta da lista de adjacência do vértice de destino
        self.lista_adjacencia[vertice_destino_id] = [
            aresta
            for aresta in self.lista_adjacencia[vertice_destino_id]
            if aresta.destino.id != vertice_origem_id
        ]

    def tipo_conexidade(self):
        """
        Verifica se o grafo é conexo ou desconexo.
        Um grafo é conexo se todos os vértices estão conectados direta ou indiretamente.

        Returns:
            str: "Conexo" se o grafo for conexo, "Desconexo" caso contrário.
        """
        if not self.vertices:
            return "O grafo está vazio."

        visitados = set()

        # Função auxiliar para realizar a busca em profundidade (DFS)
        def dfs(vertice_id):
            visitados.add(vertice_id)  # Marca o vértice como visitado
            for aresta in self.lista_adjacencia[vertice_id]:
                if aresta.destino.id not in visitados:
                    dfs(aresta.destino.id)

        # Inicia a DFS a partir do primeiro vértice (ID 0)
        dfs(0)

        # Verifica se todos os vértices foram visitados
        if len(visitados) == len(self.vertices):
            print("Conexo")
        else:
            print("Desconexo")

    def imprimeGrafo(self):
        """
        Imprime a lista de adjacência do grafo, incluindo os nomes dos livros associados a cada vértice.
        """
        if not self.lista_adjacencia:
            print("A lista de adjacência está vazia.")
        else:
            print("Lista de Adjacência:")
            for vertice_id, arestas in self.lista_adjacencia.items():
                # Obtém o nome do livro associado ao vértice
                nome_livro = self.vertices[vertice_id].nome_livro
                arestas_str = ", ".join(
                    [
                        f"({aresta.destino.id}, '{self.vertices[aresta.destino.id].nome_livro}', peso={aresta.peso}, gêneros={aresta.generos_comuns})"
                        for aresta in arestas
                    ]
                )
                print(f"{vertice_id} ('{nome_livro}') -> {arestas_str}")

    def imprimeRelacaoVertices(self):
        """
        Exibe a relação dos vértices e os livros que eles representam.
        """
        print("Relação de Vértices e Livros:")
        for vertice in self.vertices:
            print(f"Vértice {vertice.id}: {vertice.nome_livro}")

    def leArquivo(self, nome_arquivo: str):
        """
        Lê o arquivo de entrada e popula o grafo com vértices e arestas.

        Args:
            nome_arquivo (str): O caminho do arquivo de entrada.
        """
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        num_livros = int(
            linhas[1].strip()
        )  # A segunda linha contém o número de livros (vértices)

        # Lendo os vértices
        for i in range(2, 2 + num_livros):
            partes = linhas[i].split(" ", 1)  # Divide na primeira ocorrência de espaço
            id_vertice = int(partes[0])  # Número do vértice
            nome_livro = (
                partes[1].strip().strip('"')
            )  # Nome do livro, removendo possíveis aspas
            self.insereVertice(nome_livro)  # Insere o vértice no grafo

        # Lendo o número de arestas
        num_arestas = int(linhas[2 + num_livros].strip())

        # Lendo as arestas
        for i in range(3 + num_livros, 3 + num_livros + num_arestas):
            partes = linhas[i].split(" ", 3)
            vertice_origem_id = int(partes[0])  # Primeiro vértice
            vertice_destino_id = int(partes[1])  # Segundo vértice
            peso = int(partes[2])  # Peso da aresta
            generos_comuns = ast.literal_eval(
                partes[3].strip()
            )  # Interpreta a lista de gêneros

            # Insere a aresta no grafo
            self.insereAresta(
                vertice_origem_id, vertice_destino_id, peso, generos_comuns
            )

    def gravarGrafo(self, nome_arquivo: str):
        """
        Grava o conteúdo do grafo em um arquivo no formato:
        - Tipo do grafo
        - Número de vértices (livros)
        - Listagem de vértices (ID e nome do livro)
        - Número de arestas
        - Arestas no formato: vertice_origem vertice_destino peso [gêneros]

        Args:
            nome_arquivo (str): O caminho do arquivo de saída.
        """
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            # Escreve o tipo do grafo (por exemplo, 2 para grafo não-direcionado)
            arquivo.write("2\n")

            # Escreve o número de vértices
            arquivo.write(f"{len(self.vertices)}\n")

            # Escreve os vértices com o formato: ID "nome do livro"
            for vertice in self.vertices:
                arquivo.write(f'{vertice.id} "{vertice.nome_livro}"\n')

            # Escreve o número de arestas
            total_arestas = (
                sum(len(arestas) for arestas in self.lista_adjacencia.values()) // 2
            )  # Como é grafo não-direcionado, cada aresta é contada duas vezes
            arquivo.write(f"{total_arestas}\n")

            # Escreve as arestas no formato: vertice_origem vertice_destino peso [gêneros]
            arestas_gravadas = (
                set()
            )  # Conjunto para evitar duplicidade (grafo não-direcionado)
            for vertice_origem_id, arestas in self.lista_adjacencia.items():
                for aresta in arestas:
                    # Para evitar duplicidade, gravamos a aresta apenas uma vez
                    if (
                        aresta.origem.id,
                        aresta.destino.id,
                    ) not in arestas_gravadas and (
                        aresta.destino.id,
                        aresta.origem.id,
                    ) not in arestas_gravadas:
                        # Adiciona a aresta ao conjunto para garantir que não seja repetida
                        arestas_gravadas.add((aresta.origem.id, aresta.destino.id))
                        # Escreve no arquivo
                        arquivo.write(
                            f"{aresta.origem.id} {aresta.destino.id} {aresta.peso} {aresta.generos_comuns}\n"
                        )

    def exibirGrafoVisual(self):
        """
        Exibe o conteúdo atual do grafo de forma visualmente compreensível e atraente.
        """
        print("===============================================================")
        print(f"Tipo do Grafo: Não Orientado com peso nas arestas")
        print(f"Número de Vértices: {len(self.vertices)}")
        print("---------------------------------------------------------------")

        print("Vértices e seus respectivos nomes:")
        for vertice in self.vertices:
            print(f"- Vértice {vertice.id}: {vertice.nome_livro}")

        print("---------------------------------------------------------------")
        print(
            "\nArestas (conexões entre os vértices) e seus respectivos pesos e gêneros comuns:"
        )

        arestas_exibidas = set()  # Conjunto para evitar duplicidade de arestas

        for vertice_origem_id, arestas in self.lista_adjacencia.items():
            for aresta in arestas:
                # Para evitar duplicação de arestas em grafos não-direcionados
                if (aresta.origem.id, aresta.destino.id) not in arestas_exibidas and (
                    aresta.destino.id,
                    aresta.origem.id,
                ) not in arestas_exibidas:
                    arestas_exibidas.add((aresta.origem.id, aresta.destino.id))
                    generos = (
                        ", ".join(aresta.generos_comuns)
                        if aresta.generos_comuns
                        else "Nenhum"
                    )
                    print(
                        f"- {aresta.origem.nome_livro} ({aresta.origem.id}) <--> {aresta.destino.nome_livro} ({aresta.destino.id}) | Peso: {aresta.peso} | Gêneros em comum: {generos}"
                    )

        if not arestas_exibidas:
            print("Não há arestas neste grafo.")

        print("===============================================================")

    def grau_vertices(self):
        """
        Calcula e imprime o grau de cada vértice do grafo.
        """
        for vertice in self.vertices:
            grau = len(self.lista_adjacencia[vertice.id])
            print(f"Vértice {vertice.id} ('{vertice.nome_livro}'): grau = {grau}")

    def eh_grafo_euleriano(self):
        """
        Verifica se o grafo é Euleriano ou se admite um percurso Euleriano.
        """
        graus_impares = sum(
            1
            for vertice in self.vertices
            if len(self.lista_adjacencia[vertice.id]) % 2 != 0
        )

        if graus_impares == 0:
            print("O grafo é Euleriano.")
        elif graus_impares == 2:
            print("O grafo admite um percurso Euleriano.")
        else:
            print("O grafo não é Euleriano e não admite percurso Euleriano.")

    def pode_adicionar(self, caminho, vertice_id):
        """
        Verifica se o vértice pode ser adicionado ao caminho.

        Args:
            caminho (list): O caminho atual.
            vertice_id (int): O ID do vértice a ser adicionado.

        Returns:
            bool: True se o vértice pode ser adicionado, False caso contrário.
        """
        # Se o vértice já está no caminho, não pode ser adicionado
        if vertice_id in caminho:
            return False

        # Se não é o primeiro vértice, deve haver uma aresta entre o último vértice no caminho e o novo vértice
        if caminho[-1] != -1:  # Verifica se já temos algum vértice no caminho
            ultimo_vertice_id = caminho[-1]
            arestas = self.lista_adjacencia[ultimo_vertice_id]
            for aresta in arestas:
                if aresta.destino.id == vertice_id:
                    return True
            return False  # Se não há aresta, não pode adicionar

        return True  # Se for o primeiro vértice, sempre pode adicionar

    def hamiltoniano_util(self, caminho, pos):
        # Se todos os vértices estão no caminho e há uma aresta de volta ao início
        if pos == len(self.vertices):
            # Verifica se existe uma aresta do último vértice no caminho de volta ao primeiro
            ultimo_vertice_id = caminho[pos - 1]
            return any(
                aresta.destino.id == caminho[0]
                for aresta in self.lista_adjacencia[ultimo_vertice_id]
            )

        for vertice_id in range(len(self.vertices)):
            # Adicione lógica para verificar se o vértice pode ser adicionado ao caminho
            if self.pode_adicionar(caminho, vertice_id):
                caminho[pos] = vertice_id

                if self.hamiltoniano_util(caminho, pos + 1):
                    return True

                # Backtrack
                caminho[pos] = -1

        return False

    def eh_grafo_hamiltoniano(self):
        """
        Verifica se o grafo admite um ciclo Hamiltoniano.
        """
        caminho = [-1] * len(self.vertices)
        caminho[0] = 0  # Começa do primeiro vértice

        if not self.hamiltoniano_util(caminho, 1):
            print("O grafo não admite um ciclo Hamiltoniano.")
        else:
            print("O grafo admite um ciclo Hamiltoniano.")

    def colorir_grafo(self):
        """
        Realiza a coloração do grafo.
        """
        cor = [-1] * len(self.vertices)
        cor[0] = 0  # A primeira cor é a 0

        for vertice_id in range(1, len(self.vertices)):
            # Obtenha as cores usadas pelos vizinhos
            vizinhos = [
                self.lista_adjacencia[vertice_id][i].destino.id
                for i in range(len(self.lista_adjacencia[vertice_id]))
            ]
            cores_usadas = set(
                cor[vizinho] for vizinho in vizinhos if cor[vizinho] != -1
            )

            # Atribua a menor cor disponível ao vértice
            for c in range(len(self.vertices)):
                if c not in cores_usadas:
                    cor[vertice_id] = c
                    break

        # Imprime as cores atribuídas
        for vertice_id, c in enumerate(cor):
            print(
                f"Vértice {vertice_id} ('{self.vertices[vertice_id].nome_livro}') tem cor {c}."
            )

    def renderizar_grafo(self, filename="grafo.html"):
        """
        Renderiza o grafo utilizando PyVis e salva em um arquivo HTML.

        Args:
            filename (str): O nome do arquivo onde o grafo será salvo.
        """
        # Cria um objeto Network do PyVis
        net = Network(notebook=True, height="750px", width="100%", directed=False)

        # Adiciona os vértices
        for vertice in self.vertices:
            net.add_node(vertice.id, label=vertice.nome_livro)

        # Adiciona as arestas
        for _, arestas in self.lista_adjacencia.items():
            for aresta in arestas:
                net.add_edge(
                    aresta.origem.id,
                    aresta.destino.id,
                    title=f"{aresta.peso} - {', '.join(aresta.generos_comuns)}",
                )

        # Renderiza o grafo e salva como um arquivo HTML
        net.show(filename)


# Exemplo de uso
if __name__ == "__main__":
    grafo = TGrafoND()

    grafo.leArquivo("app/data/grafo_raw_1.txt")
