import tkinter as tk
from tkinter import ttk
from cadastroAlunos_Funcoes import verificacao_Numerica, cadastrar_Aluno_Interface

cursos = ["Administração", "Arquitetura e Urbanismo", "Biomedicina", "Ciências Biológicas", "Ciências Contábeis", "Direito", "Educação Física", "Enfermagem", "Engenharia Civil", "Engenharia de Computação", "Engenharia de Produção", "Engenharia Elétrica", "Engenharia Mecânica", "Engenharia Química", "Farmácia", "Fisioterapia", "Jornalismo", "Nutrição", "Odontologia", "Pedagogia", "Psicologia", "Publicidade e Propaganda", "Relações Internacionais", "Sistemas de Informação"]

root_CadastroAluno = tk.Tk()
root_CadastroAluno.title("CADASTRO DE ALUNOS")
root_CadastroAluno.geometry("400x250")
root_CadastroAluno.resizable(False, False)

frame_Cadastro = tk.Frame(root_CadastroAluno)
frame_Cadastro.pack()

label_Titulo = tk.Label(frame_Cadastro, text = "CADASTRO DE ALUNOS", font = ("Arial", 14, "bold"))
label_Titulo.grid(row = 0, column = 0, columnspan = 2, pady = 10)

label_Nome = tk.Label(frame_Cadastro, text = "NOME:")
label_Nome.grid(row = 1, column = 0, padx = 0, pady = 10)

input_Nome = tk.Entry(frame_Cadastro, width = 40)
input_Nome.grid(row = 1, column = 1)

label_RA = tk.Label(frame_Cadastro, text = "RA:")
label_RA.grid(row = 2, column = 0, padx = 0, pady = 10)

input_RA = tk.Entry(frame_Cadastro, width = 40)
input_RA.grid(row = 2, column = 1)

validacao = root_CadastroAluno.register(verificacao_Numerica)
input_RA.config(validate = "key", validatecommand = (validacao, "%P"))

label_Curso = tk.Label(frame_Cadastro, text = "CURSO:")
label_Curso.grid(row = 3, column = 0, padx = 0, pady = 10)

combo_Curso = ttk.Combobox(frame_Cadastro, values = cursos, width = 37, state = "readonly")
combo_Curso.grid(row = 3, column = 1)

frame_Botoes = tk.Frame(frame_Cadastro)
frame_Botoes.grid(row = 4, column = 0, columnspan = 2, pady = 20)

botao_Cadastrar = tk.Button(
    frame_Botoes,
    text = "CADASTRAR",
    command = lambda: cadastrar_Aluno_Interface(
        input_Nome.get(),
        input_RA.get(),
        combo_Curso.get()
    )
)
botao_Cadastrar.pack(side = "left", padx = 10)

botao_Voltar = tk.Button(frame_Botoes, text = "VOLTAR")
botao_Voltar.pack(side = "left", padx = 10)

root_CadastroAluno.mainloop()
