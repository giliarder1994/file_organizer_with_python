import os
from tkinter.filedialog import askdirectory

path = askdirectory(title="Select a folder")

file_list = os.listdir(path)

locations = {
    "images": ['.png', '.jpg'],
    "spreadsheets": ['.xlsx'],
    "internet": ['.html'],
    "csv": ['.csv'],
    "pdf": ['.pdf']
}

for file in file_list:
    # 01 - Arquivo.pdf
    nome, extensao = os.path.splitext(f"{path}/{file}")
    for folder in locations:
        if extensao in locations[folder]:
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")
            os.rename(f"{path}/{file}", f"{path}/{folder}/{file}")
