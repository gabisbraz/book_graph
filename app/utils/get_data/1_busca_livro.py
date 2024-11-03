import requests
import pandas as pd
from loguru import logger


def get_livro(titulo):
    titulo_formatado = titulo.replace(" ", "+")

    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{titulo_formatado}"

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        if "items" in dados and len(dados["items"]) > 0:
            livro = dados["items"][0]["volumeInfo"]

            title = livro.get("title", "Não disponível")

            authors = ", ".join(livro.get("authors", ["Não disponível"]))
            logger.debug(f"AUTOR: {authors}")

            description = livro.get("description", "Não disponível")
            logger.debug(f"DESCRIÇÃO: {description}")

            pageCount = livro.get("pageCount", "Não disponível")
            logger.debug(f"PÁGINAS: {pageCount}")

            genero = ", ".join(livro.get("categories", ["Não disponível"]))
            logger.debug(f"GÊNERO: {genero}")

            return {
                "Título": title,
                "Autor": authors,
                "Descrição": description,
                "Páginas": pageCount,
                "Gêneros": genero,
            }
        else:
            return {
                "Título": titulo,
                "Autor": "Não encontrado",
                "Descrição": "Não disponível",
                "Páginas": "Não disponível",
                "Gêneros": "Não disponível",
            }
    else:
        logger.error(f"Erro na requisição: {response.status_code}")
        return None


def processar_livros(arquivo_txt, arquivo_excel):
    lista_livros = []

    with open(arquivo_txt, "r") as file:
        for linha in file:
            titulo = linha.strip()
            if titulo:
                logger.info(f"Buscando livro: {titulo}...")
                dados_livro = get_livro(titulo)
                if dados_livro:
                    lista_livros.append(dados_livro)
                    logger.success(f"Livro adicionado a lista: {titulo}")

    df = pd.DataFrame(lista_livros)

    df.to_excel(arquivo_excel, index=False)
    logger.success(f"Os dados foram salvos no arquivo {arquivo_excel}.")


arquivo_txt = "app/aux_data/livros.txt"
arquivo_excel = "app/aux_data/result_API2.xlsx"
processar_livros(arquivo_txt, arquivo_excel)
