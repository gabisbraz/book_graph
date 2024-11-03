import pandas as pd

file_path = "app/aux_data/copy.xlsx"
xls = pd.ExcelFile(file_path)

df = pd.read_excel(file_path, sheet_name="Sheet1")

grafo_tipo = 2
vertices = list(set(df["Livro 1"].tolist() + df["Livro 2"].tolist()))
vertices_dict = {v: idx for idx, v in enumerate(vertices)}
n = len(vertices)
m = df.shape[0]

grafo_lines = [f"{grafo_tipo}\n", f"{n}\n"]
for vertex, idx in vertices_dict.items():
    grafo_lines.append(f'{idx} "{vertex}"\n')

grafo_lines.append(f"{m}\n")
for _, row in df.iterrows():
    v1_idx = vertices_dict[row["Livro 1"]]
    v2_idx = vertices_dict[row["Livro 2"]]
    peso = row["Peso"]
    genero = row["Gênero"].split(", ")
    grafo_lines.append(f"{v1_idx} {v2_idx} {peso} {genero}\n")

grafo_file_path = "app/data/input/grafo_5.txt"
with open(grafo_file_path, "w") as file:
    file.writelines(grafo_lines)
