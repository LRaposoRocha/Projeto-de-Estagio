import tkinter as tk
from tkinter import ttk
import lista_labels_categorias

def carregar_Dados_Json():
    try:
        with open("lista_labels_categorias.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}


def atualizar_Label(*args):
    label_MostraSelecao.config(text = variavel_ItemComboBox.get())

listaLabels = []
listaEntrys = []

def atualizacaoLabel():

    for label in listaLabels:
        label.pack_forget()
    for entry in listaEntrys:
        entry.pack_forget()

    listaLabels.clear()
    listaEntrys.clear()

    variavel_Categoria_Selecionada = variavel_ItemComboBox.get()

    if variavel_Categoria_Selecionada in 

root_CadastroMatereial = tk.Tk()
root_CadastroMatereial.title("Tela Cadastro de Materiais")
#root_CadastroMatereial.resizable(False,False)
root_CadastroMatereial.geometry('300x150')

frame_CadastroMaterial = tk.Frame(root_CadastroMatereial)
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

root_CadastroMatereial.mainloop()
