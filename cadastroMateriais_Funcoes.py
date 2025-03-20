import tkinter as tk

def atualizar_Label(variavel_ItemComboBox, json_LabelsComponentes, lista_Frames, frame_CadastroMaterial):
    for frame in lista_Frames:
        frame.destroy()
    lista_Frames.clear()

    categoriaSelecionada = variavel_ItemComboBox.get()

    if categoriaSelecionada in json_LabelsComponentes:
        labels_Nome = json_LabelsComponentes[categoriaSelecionada]

        for labels_Informacao in labels_Nome:
            frame_Linha = tk.Frame(frame_CadastroMaterial)
            frame_Linha.pack(fill = 'both', pady = 10)
            lista_Frames.append(frame_Linha)
            
            label_Dinamica = tk.Label(frame_Linha, text = labels_Informacao)
            label_Dinamica.pack(side = 'left', padx = 5)
            
            entry_Dinamica = tk.Entry(frame_Linha)
            entry_Dinamica.pack(side = 'right', padx = 5)