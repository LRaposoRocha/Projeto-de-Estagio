# More Tests

import os
import json
import tkinter as tk

pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_categorias = os.path.join(pasta_atual, "categoriasDados.json")
caminho_valores = os.path.join(pasta_atual, "valorDados.json")

def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def atualizar_Label(variavel_ItemComboBox, json_LabelsComponentes, lista_Frames, frame_CadastroMaterial):
    for _, frame in lista_Frames:
        frame.destroy()
    lista_Frames.clear()

    categoria = variavel_ItemComboBox.get()

    dados_salvos = {}
    if os.path.exists(caminho_valores):
        with open(caminho_valores, "r", encoding = "utf-8") as f:
            try:
                dados_salvos = json.load(f)
            except json.JSONDecodeError:
                dados_salvos = {}

    preenchido = dados_salvos.get(categoria, {})

    if categoria in json_LabelsComponentes:
        for label_texto in json_LabelsComponentes[categoria]:
            frame_linha = tk.Frame(frame_CadastroMaterial)
            frame_linha.pack(fill = 'both', pady = 10)
            lista_Frames.append((label_texto, frame_linha))

            label = tk.Label(frame_linha, text = label_texto)
            label.pack(side = 'left', padx = 5)

            entry = tk.Entry(frame_linha)
            entry.pack(side = 'right', padx = 5)
            entry.insert(0, preenchido.get(label_texto, ""))

def abrir_janela_categoria(root, frame_CadastroMaterial, variavel_ItemComboBox, combobox_SelecionarCategoria, json_LabelsComponentes, lista_Frames):
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Nova Categoria")
    centralizar_janela(nova_janela, 300, 400)

    frame_nova_categoria = tk.Frame(nova_janela)
    frame_nova_categoria.pack(pady = 10)

    tk.Label(frame_nova_categoria, text = "Nome da Categoria").pack()
    entry_nome_categoria = tk.Entry(frame_nova_categoria)
    entry_nome_categoria.pack()

    botao_adicionar_sub = tk.Button(nova_janela, text = "Nova Sub-Categoria")
    botao_adicionar_sub.pack(pady = 5)

    frame_subcategorias = tk.Frame(nova_janela)
    frame_subcategorias.pack(pady = 5)

    lista_entries_subcategorias = []

    def adicionar_subcategoria():
        frame_linha = tk.Frame(frame_subcategorias)
        frame_linha.pack(pady = 5)
        tk.Label(frame_linha, text = "Adicione as sub-categorias:").pack(side = "left", padx = 5)
        entry = tk.Entry(frame_linha)
        entry.pack(side = "right", padx = 5)
        lista_entries_subcategorias.append(entry)

    botao_adicionar_sub.config(command = adicionar_subcategoria)

    def salvar_categoria():
        nome = entry_nome_categoria.get().strip()
        subcategorias = [entry.get().strip() for entry in lista_entries_subcategorias if entry.get().strip()]
        if nome and subcategorias:
            json_LabelsComponentes[nome] = subcategorias
            with open(caminho_categorias, "w", encoding = "utf-8") as file:
                json.dump(json_LabelsComponentes, file, indent = 4, ensure_ascii = False)

            combobox_SelecionarCategoria['values'] = list(json_LabelsComponentes.keys())
            variavel_ItemComboBox.set(nome)
            atualizar_Label(variavel_ItemComboBox, json_LabelsComponentes, lista_Frames, frame_CadastroMaterial)
            nova_janela.destroy()

    tk.Button(nova_janela, text = "Salvar", command = salvar_categoria).pack(pady = 10)

def salvar_preenchimento(variavel_ItemComboBox, lista_Frames):
    categoria = variavel_ItemComboBox.get()
    preenchido = {}
    for label_texto, frame in lista_Frames:
        entry = frame.winfo_children()[1]
        preenchido[label_texto] = entry.get().strip()

    if categoria and preenchido:
        dados = {}
        if os.path.exists(caminho_valores):
            with open(caminho_valores, "r", encoding = "utf-8") as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = {}

        dados[categoria] = preenchido

        with open(caminho_valores, "w", encoding = "utf-8") as f:
            json.dump(dados, f, indent = 4, ensure_ascii = False)
