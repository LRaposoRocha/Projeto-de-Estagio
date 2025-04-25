import tkinter as tk
from tkinter import ttk

root_EA = tk.Tk()
root_EA.title = "Empréstimo de Materiais NPE"
root_EA.geometry("1100x619")
root_EA.resizable(False,False)

frame_Tabela = tk.Frame(root_EA)
frame_Tabela.pack()

label_Titulo = tk.Label(frame_Tabela, text = "EMRPÉSTIMOS ATIVOS")
label_Titulo.pack(pady = (100, 30))

colunas_EA = ("Data", "Hora", "Nome", "RA", "Curso")
tabela_EA = ttk.Treeview(root_EA, columns = colunas_EA, show = "headings")

for colunas in colunas_EA:
    tabela_EA.heading(colunas, text=colunas)

tabela_EA.pack()

root_EA.mainloop()