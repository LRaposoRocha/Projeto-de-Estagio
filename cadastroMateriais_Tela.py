import tkinter as tk
from tkinter import ttk
import json
from cadastroMateriais_Funcoes import atualizar_Label

root_CadastroMatereial = tk.Tk()
root_CadastroMatereial.title("Tela Cadastro de Materiais")
root_CadastroMatereial.geometry('300x400')

frame_CadastroMaterial = tk.Frame(root_CadastroMatereial)
frame_CadastroMaterial.pack()

button_AdicionarCategoria = tk.Button(frame_CadastroMaterial, text = "Nova Categoria")
button_AdicionarCategoria.pack(pady = 5)

variavel_ItemComboBox = tk.StringVar()
comboBox_ValorAtual = variavel_ItemComboBox.get()

combobox_SelecionarCategoria = ttk.Combobox(frame_CadastroMaterial, values = ["Resistor", "Capacitor", "Indutor", "Diodo"], state = 'readonly', textvariable = variavel_ItemComboBox)
combobox_SelecionarCategoria.pack(pady = 5)

with open("componentes.json", "r") as file:
    json_LabelsComponentes = json.load(file)

lista_Frames = []

combobox_SelecionarCategoria.bind("<<ComboboxSelected>>", lambda event: atualizar_Label(variavel_ItemComboBox, json_LabelsComponentes, lista_Frames, frame_CadastroMaterial))
combobox_SelecionarCategoria.bind("<Return>", lambda event: atualizar_Label(variavel_ItemComboBox, json_LabelsComponentes, lista_Frames, frame_CadastroMaterial))

label_MostraSelecao = tk.Label(frame_CadastroMaterial, text = comboBox_ValorAtual)
label_MostraSelecao.pack(pady = 5)

root_CadastroMatereial.mainloop()
