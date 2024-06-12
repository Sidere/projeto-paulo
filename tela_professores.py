import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import Conexao_sql as con

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
class Prof(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1100x500")
        self.title("Gerenciador de Professores")

        self.focus_set()
        self.grab_set()
        self.attributes('-topmost', True)
        self.attributes('-topmost', False)

        # Conexão ao banco de dados MySQL
        self.bd = con.ConexaoMYSQL(host="localhost", user="root", password="WLY42315!", database="ete")
        self.bd.conectarBanco()

        # Fechar o banco quando a janela for fechada
        self.protocol("WM_DELETE_WINDOW", self.fecharJanela)

        # Frame principal
        self.frame_principal = ctk.CTkFrame(self, width=500, height=200, corner_radius=15, border_width=2)
        self.frame_principal.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.telaCadastrarProfessor()

        # Menu lateral
        self.frame_menu = ctk.CTkFrame(self, width=300)
        self.frame_menu.grid(row=0, column=0, sticky="nswe")

        self.text_menu = ctk.CTkLabel(self.frame_menu, text="Menu Professores", font=("Arial", 25))
        self.text_menu.grid(row=0, column=0, padx=20, pady=20)

        self.btn_cad_professor = ctk.CTkButton(self.frame_menu, text="Cadastrar", command=self.telaCadastrarProfessor)
        self.btn_cad_professor.grid(row=1, column=0, padx=20, pady=10)

        self.btn_cadastros = ctk.CTkButton(self.frame_menu, text="Cadastros", command=self.telaCadastrosProfessor)
        self.btn_cadastros.grid(row=2, column=0, padx=20, pady=10)

        # Configurações do frame principal
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_columnconfigure(1, weight=1)
        self.frame_principal.grid_columnconfigure(2, weight=1)
        self.frame_principal.grid_columnconfigure(3, weight=1)
        self.frame_principal.grid_columnconfigure(4, weight=1)
        self.frame_principal.grid_columnconfigure(5, weight=1)

    def telaCadastrarProfessor(self):
        self.apagarFrame()
        self.titulo = ctk.CTkLabel(self.frame_principal, text="Cadastro de Professor", font=("Arial", 25))
        self.titulo.grid(row=0, column=0, columnspan=6, pady=20, padx=20)

        # Campo do Nome
        self.Lnome = ctk.CTkLabel(master=self.frame_principal, text="Nome")
        self.Lnome.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.nome_entrada = ctk.CTkEntry(master=self.frame_principal, width=200, corner_radius=10)
        self.nome_entrada.grid(row=1, column=1, columnspan=3, pady=20, padx=20, sticky="ew")

        # Campo do Curso que Leciona
        self.Lcurso = ctk.CTkLabel(master=self.frame_principal, text="Curso que Leciona")
        self.Lcurso.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.curso_entrada = ctk.CTkEntry(master=self.frame_principal, width=200, corner_radius=10)
        self.curso_entrada.grid(row=2, column=1, columnspan=3, pady=20, padx=20, sticky="ew")

        # Botão "Salvar"
        self.btn_salvar = ctk.CTkButton(master=self.frame_principal, text="Salvar", command=self.coletarDadosCadastro)
        self.btn_salvar.grid(row=3, column=0, columnspan=5, pady=20, padx=20)

        # Botão "Limpar"
        self.btn_limpar = ctk.CTkButton(master=self.frame_principal, text="Limpar", command=self.apagarDadosCadastro)
        self.btn_limpar.grid(row=3, column=2, columnspan=5, pady=20, padx=20)

    def telaCadastrosProfessor(self):
        self.apagarFrame()
        self.titulo = ctk.CTkLabel(self.frame_principal, text="Lista de Professores", font=("Arial", 25))
        self.titulo.grid(row=0, column=0, columnspan=6, pady=20, padx=20)

        self.colunas = ["ID", "Nome do Curso", "CursoID"]
        for idx, self.colunas in enumerate(self.colunas):
            self.colunas = ctk.CTkLabel(self.frame_principal, text=self.colunas)
            self.colunas.grid(row=1, column=idx, padx=10, pady=10)

        # Carrega os dados dos alunos
        self.carregarDadosProfs()

    def carregarDadosProfs(self):
        # Obtém os dados dos alunos do banco de dados
        self.linhas = self.bd.DadosTabelaProfs()

        # Exibe os dados dos alunos na forma de uma tabela
        for linha_indice, linha_dado in enumerate(self.linhas, start=2):
            for coluna, cedula_dado in enumerate(linha_dado):
                cedula_label = ctk.CTkLabel(self.frame_principal, text=str(cedula_dado))
                cedula_label.grid(row=linha_indice, column=coluna, padx=10, pady=10)

    def apagarFrame(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    def coletarDadosCadastro(self):
        try:
            nome = self.nome_entrada.get().lower()
            curso_leciona = self.curso_entrada.get()
        except:
            messagebox.showerror("ERRO", "Digite os dados corretamente")
        else:
            self.bd.tabelaProfessores(nome, curso_leciona)
            messagebox.showinfo("SUCESSO", "Professor cadastrado com sucesso!")
            self.apagarDadosCadastro()

    def apagarDadosCadastro(self):
        self.nome_entrada.delete(0, "end")
        self.curso_entrada.delete(0, "end")

    def fecharJanela(self):
        self.bd.fecharBanco()
        self.destroy()
        
    def iniciar(self):
            self.mainloop()

if __name__ == "__main__":
    app = Prof()
    app.iniciar()
