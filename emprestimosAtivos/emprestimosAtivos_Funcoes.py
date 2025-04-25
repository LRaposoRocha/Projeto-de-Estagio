import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

caminho_json_emprestimos = "emprestimosAtivos/emprestimosAtivos_Dados.json"
caminho_json_alunos = "cadastroAlunos/cadastroAlunos_Dados.json"

def salvar_emprestimos(lista):
    with open(caminho_json_emprestimos, "w", encoding = "utf-8") as f:
        json.dump(lista, f, indent = 4)

def carregar_emprestimos(tabela):
    if not os.path.exists(caminho_json_emprestimos):
        return

    with open(caminho_json_emprestimos, "r", encoding = "utf-8") as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError:
            dados = []

    for item in dados:
        tabela.insert("", "end", values = (
            item["Data"],
            item["Hora"],
            item["Nome"],
            item["RA"],
            item["Curso"]
        ))

def abrir_novo_emprestimo(tabela):
    nova_janela = tk.Toplevel()
    nova_janela.title("Novo Empréstimo")
    nova_janela.geometry("350x280")

    frame = tk.Frame(nova_janela)
    frame.pack(padx = 10, pady = 10)

    campos = ["Data", "Hora", "RA", "Nome", "Curso"]
    entradas = {}

    for i, campo in enumerate(campos):
        tk.Label(frame, text = campo).grid(row = i, column = 0, sticky = "w", pady = 4)
        entry = tk.Entry(frame)
        entry.grid(row = i, column = 1)
        entradas[campo] = entry

    # Preenche data e hora (readonly)
    data_atual = datetime.now().strftime("%d/%m/%Y")
    hora_atual = datetime.now().strftime("%H:%M:%S")
    entradas["Data"].insert(0, data_atual)
    entradas["Data"].config(state = "readonly")
    entradas["Hora"].insert(0, hora_atual)
    entradas["Hora"].config(state = "readonly")

    # Colocar foco no RA
    entradas["RA"].focus_set()

    def ao_digitar_ra(event):
        ra = entradas["RA"].get()
        if len(ra) == 6:
            try:
                if os.path.exists(caminho_json_alunos):
                    with open(caminho_json_alunos, "r", encoding = "utf-8") as f:
                        try:
                            alunos = json.load(f)
                        except json.JSONDecodeError:
                            alunos = []
                else:
                    alunos = []

                for aluno in alunos:
                    if aluno["ra"] == ra:
                        entradas["Nome"].delete(0, tk.END)
                        entradas["Nome"].insert(0, aluno["nome"])
                        entradas["Curso"].delete(0, tk.END)
                        entradas["Curso"].insert(0, aluno["curso"])
                        return
                messagebox.showerror("Erro", "RA não encontrado no cadastro de alunos.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar aluno: {str(e)}")

    entradas["RA"].bind("<KeyRelease>", ao_digitar_ra)

    def salvar():
        dados_novos = {
            "Data": entradas["Data"].get(),
            "Hora": entradas["Hora"].get(),
            "RA": entradas["RA"].get(),
            "Nome": entradas["Nome"].get(),
            "Curso": entradas["Curso"].get()
        }

        if any(v.strip() == "" for v in dados_novos.values()):
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        if os.path.exists(caminho_json_emprestimos):
            with open(caminho_json_emprestimos, "r", encoding = "utf-8") as f:
                try:
                    dados_atuais = json.load(f)
                except json.JSONDecodeError:
                    dados_atuais = []
        else:
            dados_atuais = []

        dados_atuais.append(dados_novos)
        salvar_emprestimos(dados_atuais)

        tabela.insert("", "end", values = (
            dados_novos["Data"],
            dados_novos["Hora"],
            dados_novos["Nome"],
            dados_novos["RA"],
            dados_novos["Curso"]
        ))

        nova_janela.destroy()

    tk.Button(nova_janela, text = "Salvar Empréstimo", command = salvar).pack(pady = 10)

def excluir_emprestimo(valores, tabela, item_id):
    if not os.path.exists(caminho_json_emprestimos):
        return

    try:
        with open(caminho_json_emprestimos, "r", encoding = "utf-8") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = []
    except FileNotFoundError:
        dados = []

    dados = [d for d in dados if not (
        d["Data"] == valores[0] and
        d["Hora"] == valores[1] and
        d["Nome"] == valores[2] and
        d["RA"] == valores[3] and
        d["Curso"] == valores[4]
    )]

    salvar_emprestimos(dados)
    tabela.delete(item_id)
