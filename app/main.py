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

import sys

from time import sleep
from pathlib import Path

from loguru import logger

DIR_ROOT = str(Path(__file__).parents[1])
if DIR_ROOT not in sys.path:
    sys.path.append(DIR_ROOT)

try:
    from app.utils.classes.grafo_nd import TGrafoND
except ModuleNotFoundError:
    from utils.classes.grafo_nd import TGrafoND


def main(graph_object: TGrafoND):
    """FUNÇÃO PRINCIPAL DA APLICAÇÃO.

    Args:
        graph_object (TGrafoND): OBJETO DA CLASSE TGrafoND.
    """

    while True:

        # EXIBE O MENU DE OPÇÕES PARA O USUÁRIO
        print(
            """\n
=======================================================
BIBLIOTECA CONECTADA: Explorando Relações entre Livros
=======================================================

Escolha uma das opções abaixo:
1) Ler dados do arquivo grafo_input.txt
2) Gravar dados no arquivo grafo_output.txt
3) Inserir vértice
4) Inserir aresta
5) Remover vértice
6) Remover aresta
7) Mostrar conteúdo do arquivo
8) Mostrar grafo
9) Apresentar a conexidade
10) Calcular grau dos vértices
11) Verificar se o grafo é Euleriano
12) Verificar se o grafo admite ciclo Hamiltoniano
13) Colorir grafo
14) Renderizar grafo visual
15) Sair\n"""
        )

        # RECEBE A OPÇÃO ESCOLHIDA PELO USUÁRIO
        opcao = input("Digite a opção desejada: ").lower()

        # LER DADOS DO ARQUIVO
        if opcao == "1":
            graph_object.leArquivo(
                nome_arquivo=str(Path(DIR_ROOT, "app/data/input/grafo_5.txt"))
            )
            print("Leitura do grafo realizada com sucesso!")

        # GRAVAR DADOS NO ARQUIVO
        elif opcao == "2":
            graph_object.gravarGrafo(
                nome_arquivo=str(Path(DIR_ROOT, "app/data/output/grafo_5.txt"))
            )
            print("Gravação do grafo realizada com sucesso!")

        # INSERIR UM VÉRTICE
        elif opcao == "3":
            livro = input("INSIRA O NOME DO LIVRO: ")
            graph_object.insereVertice(nome_livro=livro)

        # INSERIR UMA ARESTA
        elif opcao == "4":
            try:
                # SOLICITA AO USUÁRIO AS INFORMAÇÕES NECESSÁRIAS PARA A INSERÇÃO DA ARESTA
                v1 = int(input("INSIRA O VÉRTICE 1: "))
                v2 = int(input("INSIRA O VÉRTICE 2: "))
                peso = int(input("INSIRA O PESO DA ARESTA: "))
                generos = input(
                    "INSIRA OS GÊNEROS EM COMUM (separados por ';'): "
                ).split(";")

                # CHAMA A FUNÇÃO PARA INSERIR A ARESTA COM OS PARÂMETROS RECEBIDOS
                graph_object.insereAresta(
                    vertice_origem_id=v1,
                    vertice_destino_id=v2,
                    peso=peso,
                    generos_comuns=generos,
                )
                sleep(2)
                graph_object.imprimeGrafo()  # IMPRIME O GRAFO ATUALIZADO
            except Exception:
                logger.info(
                    "INPUT FORNECIDO INVÁLIDO, TENTE NOVAMENTE!"
                )  # MENSAGEM DE ERRO CASO OS DADOS ESTEJAM INCORRETOS
                continue  # VOLTA AO MENU PRINCIPAL

        # REMOVER UM VÉRTICE
        elif opcao == "5":
            try:
                graph_object.imprimeRelacaoVertices()  # EXIBE A RELAÇÃO DE VÉRTICES EXISTENTES
                v = int(input("INSIRA O NÚMERO DO VÉRTICE A SER REMOVIDO: "))

                # REMOVE O VÉRTICE SELECIONADO
                graph_object.removeVertice(vertice_id=v)
                sleep(2)
                graph_object.imprimeGrafo()  # IMPRIME O GRAFO ATUALIZADO
            except Exception:
                logger.info("INPUT FORNECIDO INVÁLIDO, TENTE NOVAMENTE!")
                continue  # VOLTA AO MENU PRINCIPAL

        # REMOVER UMA ARESTA
        elif opcao == "6":
            try:
                # SOLICITA AO USUÁRIO AS INFORMAÇÕES DOS VÉRTICES DA ARESTA A SER REMOVIDA
                v1 = int(input("INSIRA O VÉRTICE 1: "))
                v2 = int(input("INSIRA O VÉRTICE 2: "))
                # CHAMA A FUNÇÃO PARA REMOVER A ARESTA
                graph_object.removeAresta(vertice_origem_id=v1, vertice_destino_id=v2)
                sleep(2)
                graph_object.imprimeGrafo()  # IMPRIME O GRAFO ATUALIZADO
            except Exception:
                logger.info("INPUT FORNECIDO INVÁLIDO, TENTE NOVAMENTE!")
                continue  # VOLTA AO MENU PRINCIPAL

        # MOSTRAR CONTEÚDO DO ARQUIVO GRAFO.TXT
        elif opcao == "7":
            graph_object.exibirGrafoVisual()

        # MOSTRAR O GRAFO ATUAL
        elif opcao == "8":
            graph_object.imprimeGrafo()

        # APRESENTAR A CONEXIDADE DO GRAFO
        elif opcao == "9":
            graph_object.tipo_conexidade()

        # CALCULAR O GRAU DOS VÉRTICES
        elif opcao == "10":
            graph_object.grau_vertices()

        # VERIFICAR SE O GRAFO É EULERIANO
        elif opcao == "11":
            graph_object.eh_grafo_euleriano()

        # VERIFICAR SE O GRAFO ADMITE CICLO HAMILTONIANO
        elif opcao == "12":
            graph_object.eh_grafo_hamiltoniano()

        # COLORIR O GRAFO
        elif opcao == "13":
            graph_object.colorir_grafo()

        # RENDERIZAR O GRAFO VISUAL
        elif opcao == "14":
            graph_object.renderizar_grafo()

        # SAIR DO PROGRAMA
        elif opcao == "15":
            logger.info("Saindo...")
            break

        # CASO A OPÇÃO SEJA INVÁLIDA
        else:
            logger.error("Opção inválida. Tente novamente.")


if __name__ == "__main__":

    # CRIA UM OBJETO DA CLASSE TGrafoND
    book_graph = TGrafoND()

    # INICIA O MENU PRINCIPAL PASSANDO O OBJETO GRAFO COMO PARÂMETRO
    main(graph_object=book_graph)
