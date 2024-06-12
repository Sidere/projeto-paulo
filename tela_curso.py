import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import Conexao_sql as con

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class Curso(ctk.CTkToplevel):
    def __init__(self):
        ##tk.Tk.__init__()
        super().__init__()
        self.geometry("1100x500")
        self.title("Gerenciador de Cursos")

        self.focus_set()
        self.grab_set()
        self.attributes('-topmost', True)
        self.attributes('-topmost', False)

        ## Conexão ao banco de dados do Mysql
        self.bd = con.ConexaoMYSQL(host="localhost", user="root", password="WLY42315!", database="ete")
        self.bd.conectarBanco()

        ## Fechar o banco, função para fechar janela do banco de dados.
        self.protocol("WM_DELETE_WINDOW", self.fecharJanela)

        self.frame_principal = ctk.CTkFrame(self, width=500, height=200, corner_radius=15, border_width=2)
        self.frame_principal.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.telaCadastrarCurso()
        
        self.frame_menu = ctk.CTkFrame(self, width=300)
        self.frame_menu.grid_rowconfigure(4, weight=1)
        self.frame_menu.grid_columnconfigure(0, weight=1)
        self.frame_menu.grid(row=0, column=0, sticky="nswe")
        
        self.text_menu = ctk.CTkLabel(self.frame_menu, text="Menu Cursos", font=("Arial", 25))
        self.text_menu.grid(row=0, column=0, padx=20, pady=20)

        self.btn_cad_cursos = ctk.CTkButton(self.frame_menu, text="Cadastrar", command=self.telaCadastrarCurso)
        self.btn_cad_cursos.grid(row=1, column=0, padx=20, pady=10)

        self.btn_cadastros = ctk.CTkButton(self.frame_menu, text="Cadastros", command=self.telaCursoCadastrado)
        self.btn_cadastros.grid(row=2, column=0, padx=20, pady=10)
        
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_columnconfigure(1, weight=1)
        self.frame_principal.grid_columnconfigure(2, weight=1)
        self.frame_principal.grid_columnconfigure(3, weight=1)
        self.frame_principal.grid_columnconfigure(4, weight=1)
        self.frame_principal.grid_columnconfigure(5, weight=1)
    
    def telaCadastrarCurso(self):
        self.apagarFrame()
        self.titulo = ctk.CTkLabel(self.frame_principal, text="Cadastro de Curso", font=("Arial", 25))
        self.titulo.grid(row=0, column=0, columnspan=6, pady=20, padx=20)

        ## Campo do Nome
        self.Lnome = ctk.CTkLabel(master=self.frame_principal, text="NOME")
        self.Lnome.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.nome_entrada = ctk.CTkEntry(master=self.frame_principal, placeholder_text="Insira o nome do curso...", width=200, corner_radius=10)
        self.nome_entrada.grid(row=1, column=1, columnspan=3, pady=20, padx=20, sticky="ew")

        ## Campo da duração
        self.duracao = ctk.CTkLabel(master=self.frame_principal, text="DURAÇÃO")
        self.duracao.grid(row=1, column=4, pady=20, padx=20, sticky="ew")
        self.duracao_entrada = ctk.CTkEntry(master=self.frame_principal, width=200, corner_radius=10, placeholder_text="Em meses")
        self.duracao_entrada.grid(row=1, column=5, pady=20, padx=20, sticky="ew")

        ## CAMPO DA MODALIDADE
        self.valor_mod = tk.StringVar(value="None")
        self.Lmod = ctk.CTkLabel(master=self.frame_principal, text="MODALIDADE")
        self.Lmod.grid(row=3, column=0, pady=20, padx=20, sticky="ew")

        self.mod_P = ctk.CTkRadioButton(master=self.frame_principal, text="PRESENCIAL", width=5, height=5, value="PRESENCIAL", variable=self.valor_mod)
        self.mod_P.grid(row=3, column=1, pady=20, padx=20, sticky="ew")

        self.mod_EAD = ctk.CTkRadioButton(master=self.frame_principal, text="EAD", width=5, height=5, value="EAD", variable=self.valor_mod)
        self.mod_EAD.grid(row=3, column=2, pady=20, padx=20, sticky="ew")

        ## Campo do TURNO
        self.valor_turno = tk.StringVar(value="None")
        self.Lturno = ctk.CTkLabel(master=self.frame_principal, text="TURNO")
        self.Lturno.grid(row=4, column=0, pady=20, padx=20, sticky="ew")

        self.turno_M = ctk.CTkRadioButton(master=self.frame_principal, text="MATUTINO", width=5, height=5, value="MATUTINO", variable=self.valor_turno)
        self.turno_M.grid(row=4, column=1, pady=10, padx=10, sticky="ew")

        self.turno_V = ctk.CTkRadioButton(master=self.frame_principal, text="VESPERTINO", width=5, height=5, value="VESPERTINO", variable=self.valor_turno)
        self.turno_V.grid(row=4, column=2, pady=10, padx=10, sticky="ew")

        self.turno_N = ctk.CTkRadioButton(master=self.frame_principal, text="NOTURNO", width=5, height=5, value="NOTURNO", variable=self.valor_turno)
        self.turno_N.grid(row=4, column=3, pady=20, padx=20, sticky="ew")

        self.turno_i = ctk.CTkRadioButton(master=self.frame_principal, text="INTEGRAL", width=5, height=5, value="INTEGRAL", variable=self.valor_turno)
        self.turno_i.grid(row=4, column=4, pady=20, padx=20, sticky="ew")

        ##Campo Botão "Salvar"
        self.btn_salvar = ctk.CTkButton(master=self.frame_principal, text="Salvar", corner_radius=10, command=self.coletarDados_Cadastro)
        self.btn_salvar.grid(row=5, column=0, columnspan=5, pady=20, padx=20)

        ##Campo botão "Limpar"
        self.btn_limpar = ctk.CTkButton(master=self.frame_principal, text="Limpar", corner_radius=10, command=self.apagarDados_Cadastro)
        self.btn_limpar.grid(row=5, column=2, columnspan=5, pady=20, padx=20)

    def telaCursoCadastrado(self):
        self.apagarFrame()
        self.titulo = ctk.CTkLabel(self.frame_principal, text="Cursos Cadastrados")
        self.titulo.grid(row=0, column=0, columnspan=6, pady=20, padx=20)

        # Cria rótulos para os cabeçalhos da tabela
        self.colunas = ["ID", "Nome do Curso", "Duração", "Modalidade", "Turno"]
        for idx, self.colunas in enumerate(self.colunas):
            self.colunas = ctk.CTkLabel(self.frame_principal, text=self.colunas)
            self.colunas.grid(row=1, column=idx, padx=10, pady=10)

        # Carrega os dados dos alunos
        self.carregarDadosCursos()

    def carregarDadosCursos(self):
        # Obtém os dados dos alunos do banco de dados
        self.linhas = self.bd.DadosTabelaCursos()

        # Exibe os dados dos alunos na forma de uma tabela
        for linha_indice, linha_dado in enumerate(self.linhas, start=2):
            for coluna, cedula_dado in enumerate(linha_dado):
                cedula_label = ctk.CTkLabel(self.frame_principal, text=str(cedula_dado))
                cedula_label.grid(row=linha_indice, column=coluna, padx=10, pady=10)

    def apagarFrame(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    def coletarDados_Cadastro(self):
        try:
            self.nome_curso = self.nome_entrada.get()
            self.duracao = self.duracao_entrada.get()
            self.modalidade = self.valor_mod.get()
            self.turno = self.valor_turno.get()
        except:
            messagebox.showerror("ERRO", "Digite os dados corretamente")
        else:
            self.bd.tabelaCursos(self.nome_curso, self.duracao, self.modalidade, self.turno)
        finally:
            messagebox.showinfo("SUCESSO", "Curso cadastrado com sucesso!")
            self.apagarDados_Cadastro()
    
    def apagarDados_Cadastro(self):
        self.nome_entrada.delete(0, "end")
        self.duracao_entrada.delete(0, "end")
        self.valor_mod.set(None)
        self.valor_turno.set(None)

    def fecharJanela(self):
        self.bd.fecharBanco()
        self.destroy()

    def telaCadastroACursos(self):
        self.apagarFrame()
        self.titulo = ctk.CTkLabel(self.frame_principal, text="Cursos cadastrados", font=("Arial", 25))
        self.titulo.grid(row=0, column=0, columnspan=6, pady=20, padx=20)

    def iniciar(self):
            self.mainloop()

if __name__ == "__main__":
    app = Curso()
    app.iniciar()