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
from pathlib import Path

DIR_ROOT = str(Path(__file__).parents[3])
if DIR_ROOT not in sys.path:
    sys.path.append(DIR_ROOT)

try:
    from app.utils.classes.vertice import Vertice
except ModuleNotFoundError:
    from utils.classes.vertice import Vertice


class Aresta:
    def __init__(
        self, origem: Vertice, destino: Vertice, peso: int, generos_comuns: list
    ):
        """
        Inicializa uma aresta entre dois vértices.

        Args:
            origem (Vertice): O vértice de origem.
            destino (Vertice): O vértice de destino.
            peso (int): O peso da aresta.
            generos_comuns (list): Lista de gêneros em comum entre os dois livros.
        """
        self.origem = origem
        self.destino = destino
        self.peso = peso
        self.generos_comuns = generos_comuns

    def __repr__(self):
        return f"Aresta(de {self.origem.id} para {self.destino.id}, peso={self.peso}, gêneros={self.generos_comuns})"
