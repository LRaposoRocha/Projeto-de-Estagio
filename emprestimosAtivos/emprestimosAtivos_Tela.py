import tkinter as tk
from tkinter import ttk
from emprestimosAtivos_Funcoes import abrir_novo_emprestimo, carregar_emprestimos, excluir_emprestimo

root_EA = tk.Tk()
root_EA.title("Empréstimo de Materiais NPE")
root_EA.geometry("1100x619")
root_EA.resizable(False, False)

frame_Tabela = tk.Frame(root_EA)
frame_Tabela.pack()

label_Titulo = tk.Label(frame_Tabela, text = "EMPRÉSTIMOS ATIVOS")
label_Titulo.pack(pady = (100, 30))

colunas_EA = ("Data", "Hora", "Nome", "RA", "Curso")
tabela_EA = ttk.Treeview(root_EA, columns = colunas_EA, show = "headings")

for col in colunas_EA:
    tabela_EA.heading(col, text = col)

tabela_EA.pack()

botao_NovoEmprestimo = tk.Button(root_EA, text = "Novo Empréstimo", command = lambda: abrir_novo_emprestimo(tabela_EA))
botao_NovoEmprestimo.pack(pady = 20)

carregar_emprestimos(tabela_EA)

def abrir_opcoes_emprestimo(event):
    item_id = tabela_EA.focus()
    if not item_id:
        return
    valores = tabela_EA.item(item_id, "values")

    janela_opcoes = tk.Toplevel()
    janela_opcoes.title("Opções do Empréstimo")
    janela_opcoes.geometry("300x150")

    tk.Label(janela_opcoes, text = f"RA: {valores[3]}\nNome: {valores[2]}", pady = 10).pack()

    def finalizar():
        excluir_emprestimo(valores, tabela_EA, item_id)
        janela_opcoes.destroy()

    tk.Button(janela_opcoes, text = "Editar Empréstimo", width = 25).pack(pady = (5, 5))
    tk.Button(janela_opcoes, text = "Finalizar Empréstimo", width = 25, command = finalizar).pack(pady = (0, 10))

tabela_EA.bind("<ButtonRelease-1>", abrir_opcoes_emprestimo)

root_EA.mainloop()
