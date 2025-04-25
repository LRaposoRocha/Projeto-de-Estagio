import tkinter as tk
from tkinter import ttk
import json
from cadastroMateriais_Funcoes import atualizar_Label, abrir_janela_categoria, centralizar_janela, salvar_preenchimento

root = tk.Tk()
root.title("Tela Cadastro de Materiais")
centralizar_janela(root, 500, 500)

frame_CadastroMaterial = tk.Frame(root)
frame_CadastroMaterial.pack(pady = 10)

variavel_ItemComboBox = tk.StringVar()

try:
    with open("componentes.json", "r", encoding = "utf-8") as file:
        json_LabelsComponentes = json.load(file)
except FileNotFoundError:
    json_LabelsComponentes = {}

combobox_SelecionarCategoria = ttk.Combobox(
    frame_CadastroMaterial,
    values = list(json_LabelsComponentes.keys()),
    state = 'readonly',
    textvariable = variavel_ItemComboBox,
    width = 45
)
combobox_SelecionarCategoria.pack(pady = 5)

lista_Frames = []

frame_Botoes = tk.Frame(frame_CadastroMaterial)
frame_Botoes.pack(pady = 10)

tk.Button(
    frame_Botoes,
    text = "Nova Categoria",
    command = lambda: abrir_janela_categoria(
        root,
        frame_CadastroMaterial,
        variavel_ItemComboBox,
        combobox_SelecionarCategoria,
        json_LabelsComponentes,
        lista_Frames
    )
).pack(side = "left", padx = 5)

tk.Button(frame_Botoes, text = "Editar Categoria").pack(side = "left", padx = 5)

# 🔻 Botão SALVAR agora no final da janela e centralizado
frame_botao_salvar = tk.Frame(root)
frame_botao_salvar.pack(side = "bottom", pady = 20)

tk.Button(
    frame_botao_salvar,
    text = "Salvar",
    command = lambda: salvar_preenchimento(variavel_ItemComboBox, lista_Frames)
).pack()

combobox_SelecionarCategoria.bind(
    "<<ComboboxSelected>>",
    lambda event: atualizar_Label(
        variavel_ItemComboBox,
        json_LabelsComponentes,
        lista_Frames,
        frame_CadastroMaterial
    )
)

combobox_SelecionarCategoria.bind(
    "<Return>",
    lambda event: atualizar_Label(
        variavel_ItemComboBox,
        json_LabelsComponentes,
        lista_Frames,
        frame_CadastroMaterial
    )
)

if json_LabelsComponentes:
    primeira_categoria = list(json_LabelsComponentes.keys())[0]
    variavel_ItemComboBox.set(primeira_categoria)
    atualizar_Label(
        variavel_ItemComboBox,
        json_LabelsComponentes,
        lista_Frames,
        frame_CadastroMaterial
    )

root.mainloop()
