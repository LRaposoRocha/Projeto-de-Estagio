import tkinter as tk
from tkinter import ttk

def verificacao_Numerica(registro_Academico):
    return registro_Academico.isdigit() or registro_Academico == ""

root_CadAlu = tk.Tk()
root_CadAlu.title = "CADASTRO DE ALUNOS"
root_CadAlu.geometry("400x319")
root_CadAlu.resizable(False,False)

frame_Cadastro = tk.Frame(root_CadAlu)
frame_Cadastro.pack()

label_Titulo_CadAlu = tk.Label(frame_Cadastro, text = "CADASTRO DE ALUNOS", font = ("Arial", 14, "bold"))
label_Titulo_CadAlu.grid(row = 0, column = 0, columnspan = 2, pady = 10)

label_Nome_Aluno = tk.Label(frame_Cadastro, text = "NOME:")
label_Nome_Aluno.grid(row = 1, column = 0, padx = 0, pady = 10)

input_Nome_Aluno = tk.Entry(frame_Cadastro, width = 40)
input_Nome_Aluno.grid(row = 1, column = 1, padx = 0, pady = 0)

label_RA_Aluno = tk.Label(frame_Cadastro, text = "RA:")
label_RA_Aluno.grid(row = 2, column = 0, padx = 0, pady = 10)

input_RA_Aluno = tk.Entry(frame_Cadastro, width = 40)
input_RA_Aluno.grid(row = 2, column = 1, padx = 0, pady = 0)

validacao = root_CadAlu.register(verificacao_Numerica)
input_RA_Aluno.config(validate = "key", validatecommand = (validacao, "%P"))

label_Curso = tk.Label(frame_Cadastro, text = "CURSO:")
label_Curso.grid(row = 3, column = 0, padx = 0, pady = 10)

escolha_Curso = ttk.Combobox(frame_Cadastro, values = ["Administração", "Arquitetura e Urbanismo", "Biomedicina", "Ciências Biológicas", "Ciências Contábeis", "Direito", "Educação Física", "Enfermagem", "Engenharia Civil", "Engenharia de Computação", "Engenharia de Produção", "Engenharia Elétrica", "Engenharia Mecânica", "Engenharia Química", "Farmácia", "Fisioterapia", "Jornalismo", "Nutrição", "Odontologia", "Pedagogia", "Psicologia", "Publicidade e Propaganda", "Relações Internacionais", "Sistemas de Informação"], width = 37, state = "readonly")
escolha_Curso.grid(row = 3, column = 1, padx = 10, pady = 0)

frame_Botoes = tk.Frame(frame_Cadastro)
frame_Botoes.grid(row = 4, column = 0, columnspan = 2, pady = 20)

botao_Cadastrar_Aluno = tk.Button(frame_Botoes, text = "CADASTRAR")
botao_Cadastrar_Aluno.pack(side = "left", padx = 10)

botao_Voltar_Menu = tk.Button(frame_Botoes, text = "VOLTAR")
botao_Voltar_Menu.pack(side = "left", padx = 10)

root_CadAlu.mainloop()
