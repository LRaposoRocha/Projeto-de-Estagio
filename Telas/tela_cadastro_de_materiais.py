import tkinter as tk
from tkinter import ttk
import json

# Criação de variávies (listas) Globais.
listaLabels = []
listaEntrys = []
nomeEntry = []

# Aqui eu to importando todas as categorias do meu json.
def carregar_Dados_Json():

    try:
        with open("lista_labels_categorias.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    
# Criando uma variável que armazena a função carregar_Dados_Json (que importando todas as categorias do meu json).
variavel_Categoria_Labels = carregar_Dados_Json()

# Criando uma função que muda o texto de uma label de acordo com o item correspondente dentro do Combo Box.
def atualizar_Label(*args):

    label_MostraSelecao.config(text = variavel_ItemComboBox.get())

# Função capaz de salvar os dados no arquivo json.
def salvar_dados_json(dados):

    with open("categorias.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


# Essa função é resonsável por ... apago a label e a entry (tiro o conteúdo das mesmas, limpo), pego o o item da combo box e salvo numa variavel, 
def atualizacaoLabel():

    for label in listaLabels:
        label.pack_forget()
    for entry in listaEntrys:
        entry.pack_forget()

    listaLabels.clear()
    listaEntrys.clear()

    variavel_Categoria_Selecionada = variavel_ItemComboBox.get()

    if variavel_Categoria_Selecionada in variavel_Categoria_Labels: nome_labels = variavel_Categoria_Labels[variavel_Categoria_Selecionada]

    for nome in variavel_Categoria_Labels:
        label = tk.Label(frame_CadastroMaterial, text=nome)
        label.pack(pady=5)
        listaLabels.append(label)

        entry = tk.Entry(frame_CadastroMaterial)
        entry.pack(pady=5)
        listaEntrys.append(entry)

categorias_nomes_labels = carregar_Dados_Json()

def adicionar_categoria():
    categoria_nova = variavel_ItemComboBox.get()
    nomes_labels_nova_categoria = [entry_nome.get() for entry_nome in nomeEntry]

    if categoria_nova and nomes_labels_nova_categoria:
        categorias_nomes_labels[categoria_nova] = nomes_labels_nova_categoria
        salvar_dados_json(categorias_nomes_labels)
        atualizar_Label()

root_CadastroMaterial = tk.Tk()
root_CadastroMaterial.title("Tela Cadastro de Materiais")
#root_CadastroMaterial.resizable(False,False)
root_CadastroMaterial.geometry('300x150')

frame_CadastroMaterial = tk.Frame(root_CadastroMaterial)
frame_CadastroMaterial.pack()

button_AdicionarCategoria = tk.Button(frame_CadastroMaterial, text = "Nova Categoria")
button_AdicionarCategoria.grid(row = 0, column = 0, columnspan = 2, pady = 5)

variavel_ItemComboBox = tk.StringVar()
comboBox_ValorAtual = variavel_ItemComboBox.get()

combobox_SelecionarCategoria = ttk.Combobox(frame_CadastroMaterial, values = ["Resistor", "Capacitor", "Indutor", "Diodo", "Transistor", "LED", "Fotodiodo", "SCR", "Triac", "Optoacoplador", "Relé", "Varistor", "Termistor", "Cristal Oscilador", "Microfone", "Alto-falante", "Transformador", "Bobina de choque", "CI", "Regulador de Tensão", "Amplificador Operacional", "Multiplexador", "Demultiplexador", "Conversor A/D", "Conversor D/A", "Sensor de temperatura", "Sensor de umidade", "Sensor de pressão", "Sensor de luz", "Sensor de movimento", "Encoder", "Decodificador", "Potenciômetro", "Trimpot", "Dip switch", "Interruptor", "Chave reed", "Buzzer", "Fotorresistor", "Magnetômetro", "Giroscópio", "Acelerômetro", "Placa de RF", "Microcontrolador", "EEPROM", "Memória Flash", "Ponte de Diodos", "Fusível", "Antena", "Display"], state = 'readonly', textvariable = variavel_ItemComboBox)
combobox_SelecionarCategoria.grid(row = 1, column = 0, pady = 5)
combobox_SelecionarCategoria.bind("<<ComboboxSelected>>", atualizar_Label)
combobox_SelecionarCategoria.bind("<Return>", atualizar_Label)

button_ConfirmaSelecao = tk.Button(frame_CadastroMaterial, text = "Confimar Seleção")
button_ConfirmaSelecao.config(command = lambda: label_MostraSelecao.config(text = variavel_ItemComboBox.get()))
button_ConfirmaSelecao.grid(row = 1, column = 1, padx = 10, pady = 5)

label_MostraSelecao = tk.Label(frame_CadastroMaterial, text = comboBox_ValorAtual)
label_MostraSelecao.grid(row = 2, column = 0, columnspan = 2, pady = 5)

root_CadastroMaterial.mainloop()
