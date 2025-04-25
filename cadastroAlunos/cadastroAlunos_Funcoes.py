import os
import json
from tkinter import messagebox

pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_atual, "cadastroAlunos_Dados.json")

def verificacao_Numerica(ra):
    return ra.isdigit() or ra == ""

def cadastrar_Aluno_Interface(nome, ra, curso):
    if not nome.strip() or not ra.strip() or not curso.strip():
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
        return

    lista = []
    if os.path.exists(caminho_json):
        with open(caminho_json, "r", encoding = "utf-8") as f:
            try:
                lista = json.load(f)
            except json.JSONDecodeError:
                lista = []

    for aluno in lista:
        if aluno["ra"] == ra:
            messagebox.showerror("RA duplicado", "Esse RA já está cadastrado.")
            return

    lista.append({"nome": nome, "ra": ra, "curso": curso})
    with open(caminho_json, "w", encoding = "utf-8") as f:
        json.dump(lista, f, indent = 4, ensure_ascii = False)

    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso.")
