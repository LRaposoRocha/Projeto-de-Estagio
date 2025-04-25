# 🏫 Sistema de Gerenciamento de Empréstimos de Materiais

## 🧠 Descrição

Este projeto foi desenvolvido para **automatizar o controle de empréstimos de materiais** em ambientes acadêmicos, eliminando o uso de fichas físicas.  
A aplicação é dividida em três módulos principais:

- Cadastro de Alunos
- Cadastro de Materiais
- Controle de Empréstimos Ativos

Toda a interface é construída com **Tkinter** e os dados são armazenados em **JSON**.

---

## 📋 Funcionalidades

- ✔️ Cadastro de novos alunos com verificação de RA
- ✔️ Cadastro de novos materiais e categorias personalizadas
- ✔️ Registro de novos empréstimos com data e hora automáticos
- ✔️ Busca automática de aluno pelo RA durante o empréstimo
- ✔️ Finalização de empréstimos diretamente pela interface
- ✔️ Interface amigável e intuitiva

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **Tkinter** (para a interface gráfica)
- **JSON** (armazenamento de dados)
- **OS** (gerenciamento de arquivos)
- **Datetime** (registro de data e hora)

---

## 🛠️ Instalação e Execução

### 🔹 Pré-requisitos

- Python instalado (versão 3.11 ou superior)

### 🔹 Passo a passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. (Opcional) Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o módulo desejado:
   ```bash
   python cadastroAlunos/cadastroAlunos_Tela.py
   ```
   ou
   ```bash
   python cadastroMateriais/cadastroMateriais_Tela.py
   ```
   ou
   ```bash
   python emprestimosAtivos/emprestimosAtivos_Tela.py
   ```

---

## 📂 Estrutura do Projeto

```
Projeto/
│
├── cadastroAlunos/
│   ├── cadastroAlunos_Tela.py
│   ├── cadastroAlunos_Funcoes.py
│   └── cadastroAlunos_Dados.json
│
├── cadastroMateriais/
│   ├── cadastroMateriais_Tela.py
│   ├── cadastroMateriais_Funcoes.py
│   ├── categoriasDados.json
│   └── valorDados.json
│
├── emprestimosAtivos/
│   ├── emprestimosAtivos_Tela.py
│   ├── emprestimosAtivos_Funcoes.py
│   └── emprestimosAtivos_Dados.json
│
└── README.md
```

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.
