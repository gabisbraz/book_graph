# BIBLIOTECA CONECTADA: Explorando Relações entre Livros

NXT Reads: Explorando Relações entre Livros

# 1. Definição do problema
## a. Introdução
O problema selecionado é a dificuldade de encontrar conexões entre tipos de livros, seja em uma biblioteca ou na internet. Com a grande quantidade de títulos disponíveis, os leitores muitas vezes não sabem quais livros estão relacionados por temas semelhantes. Isso pode levar a uma experiência de leitura insatisfatória. A aplicação proposta usa um grafo, onde os livros são representados como vértices e as arestas indicam a similaridade entre eles. Assim, a ferramenta ajuda os leitores a descobrir novas obras baseadas em interesses comuns, facilitando a navegação e a exploração de conteúdos relacionados.

## b. Tecnologias Utilizadas

### 2.1 Linguagem de Programação
Python: A escolha da linguagem Python foi motivada pela sua simplicidade e pela vasta gama de bibliotecas disponíveis para manipulação de dados e construção de grafos. A linguagem permite um desenvolvimento rápido e eficiente, ideal para protótipos e projetos experimentais.

### 2.2 Bibliotecas e Frameworks
Loguru: Esta biblioteca foi utilizada para facilitar o registro de logs no sistema, permitindo acompanhar o fluxo do programa e diagnosticar possíveis problemas durante a execução. Loguru fornece uma interface simples e rica para criar logs estruturados.
Pyvis: Utilizada para a visualização dos grafos, Pyvis oferece ferramentas que permitem criar representações gráficas interativas de redes. Através dela, os usuários podem visualizar as conexões entre os livros e explorar as relações de maneira intuitiva.
Openpyxl: Esta biblioteca foi utilizada para manipulação de arquivos Excel, permitindo a leitura e escrita de dados de forma simples. No projeto, foi fundamental para armazenar informações sobre os livros e suas relações em formato tabular.
Pandas: Pandas é uma biblioteca poderosa para análise de dados em Python. No nosso projeto, foi utilizada para organizar e manipular os dados coletados da API OpenLibrary, facilitando a manipulação e análise dos dados relacionados aos livros e gêneros.
Requests: Esta biblioteca foi utilizada para realizar chamadas HTTP à API OpenLibrary. Através do Requests, conseguimos capturar informações detalhadas sobre livros, incluindo títulos, autores, gêneros e outros metadados necessários para construir o grafo.

### 2.3 Estruturas de Dados
Grafo em Lista de Adjacência: A estrutura escolhida para representar os livros e suas conexões é um grafo não direcionado, onde cada livro é um vértice e as arestas indicam a similaridade entre eles. O peso das arestas representa o número de gêneros relacionados. Essa abordagem permite uma exploração eficiente das relações entre os livros.
## c. Captura de Dados
Para a captura dos dados, utilizamos a API OpenLibrary. A OpenLibrary é uma plataforma aberta que disponibiliza informações sobre milhões de livros, permitindo acesso a uma vasta base de dados. Os passos para a captura de dados foram:
Configuração da API: Utilizamos a biblioteca Requests para enviar requisições à API, especificando os parâmetros necessários, como gênero, autor e título do livro.
Coleta de Dados: A partir das respostas da API, extraímos informações relevantes como títulos, autores e gêneros dos livros. Utilizamos o Pandas para organizar esses dados em um DataFrame.
Armazenamento e Processamento: Os dados coletados foram processados e armazenados em um formato que permite a construção do grafo. Os gêneros e suas relações foram armazenados para facilitar a navegação e busca de livros relacionados.

## d. Gêneros Literários Utilizados
No desenvolvimento da aplicação, uma ampla variedade de gêneros literários foi considerada para garantir que os leitores pudessem encontrar livros relacionados de forma eficaz. A seguir, estão listados todos os 80 gêneros utilizados nos dados capturados: ['Amizade', 'Antologias', 'Antropologia', 'Arte', 'Aspectos Sociais', 'Autoajuda', 'Aventura', 'Biografia', 'Cinema', 'Comédia', 'Contos', 'Contos Infantis', 'Contos de Fadas', 'Crítica Literária', 'Drama', 'Drama Familiar', 'Drama Feminino', 'Drama Social', 'Educação', 'Erótica', 'Ficção', 'Ficção Adaptada', 'Ficção Americana', 'Ficção Animal', 'Ficção Britânica', 'Ficção Canadense', 'Ficção Chinesa', 'Ficção Científica', 'Ficção Científica e Fantástica', 'Ficção Clássica', 'Ficção Contemporânea', 'Ficção Dystópica', 'Ficção Europeia', 'Ficção Fantástica', 'Ficção Gótica', 'Ficção Histórica', 'Ficção Infantil', 'Ficção Juvenil', 'Ficção Literária', 'Ficção Médica', 'Ficção Policial', 'Ficção Política', 'Ficção Psicológica', 'Ficção Russa', 'Ficção de Crime', 'Ficção de Fantasia', 'Ficção de Formação', 'Ficção de Horror', 'Filosofia', 'Folclore', 'Gênero não definido', 'História', 'Histórico', 'Literatura', 'Literatura Alemã', 'Literatura Americana', 'Literatura Britânica', 'Literatura Chinesa', 'Literatura Diversa', 'Literatura Feminina', 'Literatura Hispânica', 'Literatura Infantil', 'Literatura Inglesa', 'Literatura Juvenil', 'Literatura LGBTQ+', 'Literatura Masculina', 'Literatura de Fantasia', 'Literatura para Adultos', 'Livros para Colorir', 'Mistério', 'Poesia', 'Política', 'Psicologia', 'Quadrinhos', 'Referência', 'Relações', 'Relações Familiares', 'Romance', 'Teatro Infantil', 'Viagem']

## e. Similaridades Consideradas e Exemplos
As similaridades entre os livros foram fundamentais para a construção do grafo, influenciando diretamente a conexão entre os vértices e os pesos das arestas. No nosso modelo, as seguintes similaridades foram consideradas:
Gêneros em Comum: A presença de gêneros compartilhados entre os livros foi um dos principais critérios para determinar a similaridade. Quanto mais gêneros em comum um par de livros tiver, maior será o peso da aresta entre eles.

### Exemplo de Similaridade

Para ilustrar como as similaridades são representadas no grafo, consideremos o seguinte exemplo:

**Grafo Simplificado:**

- Livro A: "Romeo and Juliet" (ID: 33, Gêneros: Drama, Romance, Ficção, História, Literatura)
- Livro B: "The Book Thief" (ID: 47, Gêneros: Ficção, História, Literatura)

**As conexões seriam:**

- Romeo and Juliet <--> The Book Thief

- **Peso da Aresta**: 3

- **Gêneros em Comum**: Ficção, História, Literatura

Neste exemplo, os livros "Romeo and Juliet" e "The Book Thief" têm uma conexão significativa, pois compartilham três gêneros em comum. O peso da aresta entre eles é 3, refletindo a quantidade de gêneros que se sobrepõem. Essa abordagem não só quantifica a similaridade, mas também fornece uma base para que os leitores possam descobrir novos livros que se alinhem com seus interesses.

## f. Estrutura do Grafo
### Modelagem dos Vértices e Arestas
Para modelar um grafo, utilizamos duas classes principais: Vertice e Aresta.

**Classe Vertice**
Cada vértice representa um ponto no grafo e pode conter informações relevantes. No nosso modelo, cada vértice possui os seguintes atributos:
id: Um identificador único para o vértice, permitindo que ele seja referenciado facilmente.
informacoes: Um dicionário que pode armazenar dados adicionais sobre o vértice, como informações de pesos, nomes ou qualquer outro atributo necessário.
aresta: Uma lista que contém todas as arestas que saem desse vértice, possibilitando acesso rápido às conexões do vértice.

**Classe Aresta**
Cada aresta representa uma conexão entre dois vértices. Os atributos da classe Aresta incluem:
origem: O vértice de origem da aresta.
destino: O vértice de destino da aresta.
peso: Um valor que pode representar o custo ou distância da aresta, permitindo modelar grafos ponderados.

### Implementação da Lista de Adjacência
A lista de adjacência é uma maneira eficiente de representar grafos, onde cada vértice tem uma lista que contém suas arestas conectadas. A implementação da lista de adjacência na classe Grafo é feita da seguinte maneira:
A classe Grafo possui um dicionário chamado vertices, onde a chave é o id do vértice e o valor é um objeto Vertice. Essa estrutura permite acesso rápido a qualquer vértice por seu identificador.
Ao adicionar uma aresta, a função adicionar_aresta realiza as seguintes operações:
Verifica se ambos os vértices de origem e destino existem no grafo.
Cria uma nova instância da classe Aresta, passando os vértices de origem e destino e um peso, se aplicável.
Adiciona essa aresta à lista de arestas do vértice de origem.
Para completar a estrutura de lista de adjacência, a aresta também é registrada na lista de arestas do vértice de destino, se o grafo for não direcionado.

## g. Estrutura das opções da aplicação

### Ler dados do arquivo grafo_input.txt
Esta opção permite ao usuário carregar informações de um arquivo pré-definido.

### Gravar dados no arquivo grafo_output.txt
Com esta funcionalidade, o usuário pode salvar o estado atual do grafo em um arquivo.

### Inserir vértice
Permite adicionar novos livros ao grafo. O usuário insere o nome do livro, e este é adicionado como um vértice no grafo. 

### Inserir aresta
Essa opção possibilita criar relações entre livros, representadas como arestas no grafo. O usuário deve informar os vértices de origem e destino, o peso da conexão (por exemplo, relevância da relação) e os gêneros literários comuns entre os livros. A funcionalidade permite estabelecer conexões baseadas em gêneros compartilhados.

### Remover vértice
O usuário pode excluir livros (vértices) do grafo utilizando esta opção. É exibida uma lista dos vértices existentes, permitindo ao usuário selecionar o livro que deseja remover. A remoção atualiza o grafo eliminando as conexões associadas ao vértice.

### Remover aresta
Com esta funcionalidade, é possível apagar relações entre livros no grafo. O usuário informa os vértices conectados pela aresta que deseja remover, e a operação atualiza o grafo refletindo a ausência da relação.

### Mostrar conteúdo do arquivo
Essa opção exibe o grafo.

### Mostrar grafo
Permite visualizar o grafo na sua forma textual. O sistema imprime uma representação da estrutura atual, incluindo vértices e arestas, para que o usuário possa entender as conexões existentes.

### Apresentar a conexidade
Verifica e informa o tipo de conexidade do grafo, ou seja, se é conexo, fortemente conexo, ou desconexo. Essa análise é fundamental para entender como os livros estão relacionados no grafo.

### Calcular grau dos vértices
Calcula e apresenta o grau de cada vértice no grafo. O grau de um vértice representa o número de conexões que ele possui, o que pode indicar a popularidade ou relevância de um livro em relação a outros.

### Verificar se o grafo é Euleriano
Esta funcionalidade analisa se o grafo é Euleriano, ou seja, se possui um circuito em que todas as arestas são percorridas uma única vez. 

### Verificar se o grafo admite ciclo Hamiltoniano
Verifica a existência de um ciclo Hamiltoniano, onde todos os vértices são visitados exatamente uma vez. 

### Colorir grafo
Realiza uma coloração dos vértices do grafo de forma que vértices adjacentes possuam cores diferentes. 

### Recomendação de livros por gênero
Baseada em gêneros literários fornecidos pelo usuário, essa funcionalidade recomenda livros que compartilhem esses gêneros. A recomendação é feita analisando as conexões e pesos do grafo, destacando livros potencialmente interessantes para o usuário.

### Renderizar grafo visual
Gera uma representação gráfica interativa do grafo utilizando a biblioteca PyVis. Essa visualização permite explorar as conexões de forma intuitiva, facilitando a compreensão das relações entre os livros.

### Sair
Finaliza a execução da aplicação.

## h. Executar o código
1. Instalar as dependências necessárias a partir do arquivo requirements.txt (pip install -r requirements.txt)
2. Executar o arquivo main.py localizado dentro da pasta app (python app/main.py)