import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Conexao_sql as con

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
class Aluno(ctk.CTkToplevel):
    def __init__(self):
        ##tk.Tk.__init__(self, *args, **kwargs)
        super().__init__()
        self.geometry("1100x500")
        self.title("Gerenciador de Alunos")

        ## Conexão ao banco de dados do Mysql
        self.bd = con.ConexaoMYSQL(host="localhost", user="root", password="WLY42315!", database="ete")
        self.bd.conectarBanco()

        ## Fechar o banco, função para fechar janela do banco de dados.
        self.protocol("WM_DELETE_WINDOW", self.fecharJanela)

        self.frame_principal = ctk.CTkFrame(self, width=500, height=200, corner_radius=15, border_width=2)
        self.frame_principal.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.telaCadastrarAluno()
        
        self.frame_menu = ctk.CTkFrame(self, width=300)
        self.frame_menu.grid_rowconfigure(4, weight=1)
        self.frame_menu.grid_columnconfigure(0, weight=1)
        self.frame_menu.grid(row=0, column=0, sticky="nswe")
        
        self.text_menu = ctk.CTkLabel(self.frame_menu, text="Menu Cursos", font=("Arial", 25))
        self.text_menu.grid(row=0, column=0, padx=20, pady=20)

        self.btn_cad_aluno = ctk.CTkButton(self.frame_menu, text="Cadastrar", command=self.telaCadastrarAluno)
        self.btn_cad_aluno.grid(row=1, column=0, padx=20, pady=10)

        self.btn_cadastros = ctk.CTkButton(self.frame_menu, text="Cadastros", command=self.telaCadastrosAluno)
        self.btn_cadastros.grid(row=2, column=0, padx=20, pady=10)

        self.btn_boletim = ctk.CTkButton(self.frame_menu, text="Boletim", command=self.telaBoletim)
        self.btn_boletim.grid(row=3, column=0, padx=20, pady=10)
        
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_columnconfigure(1, weight=1)
        self.frame_principal.grid_columnconfigure(2, weight=1)
        self.frame_principal.grid_columnconfigure(3, weight=1)
        self.frame_principal.grid_columnconfigure(4, weight=1)
        self.frame_principal.grid_columnconfigure(5, weight=1)

    def telaCadastrarAluno(self):
        self.apagarFrame()
        self.titulo = ctk.CTkLabel(self.frame_principal, text="Cadastro de Aluno", font=("Arial", 25))
        self.titulo.grid(row=0, column=0, columnspan=6, pady=20, padx=20)

        ## Campo do Nome
        self.Lnome = ctk.CTkLabel(master=self.frame_principal, text="Name")
        self.Lnome.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.nome_entrada = ctk.CTkEntry(master=self.frame_principal, placeholder_text="Insira o nome do aluno...", width=200, corner_radius=10)
        self.nome_entrada.grid(row=1, column=1, columnspan=3, pady=20, padx=20, sticky="ew")

        ## NOME DA MÃE
        self.Lnome_Mae = ctk.CTkLabel(master=self.frame_principal, text="Nome da mãe")
        self.Lnome_Mae.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.nome_Mae_entrada = ctk.CTkEntry(master=self.frame_principal, placeholder_text="Insira o nome da mãe...", width=200, corner_radius=10)
        self.nome_Mae_entrada.grid(row=2, column=1, columnspan=3, pady=20, padx=20, sticky="ew")

        ## NOME DO PAI
        self.Lnome_Pai = ctk.CTkLabel(master=self.frame_principal, text="Nome do Pai")
        self.Lnome_Pai.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        self.nome_Pai_entrada = ctk.CTkEntry(master=self.frame_principal, placeholder_text="Insira o nome do pai...", width=200, corner_radius=10)
        self.nome_Pai_entrada.grid(row=3, column=1, columnspan=3, pady=20, padx=20, sticky="ew")

        ## Campo do Nascimento
        self.Lnasc = ctk.CTkLabel(master=self.frame_principal, text="Data de Nascimento")
        self.Lnasc.grid(row=3, column=4, pady=20, padx=20, sticky="ew")
        self.nasc_entrada = ctk.CTkEntry(master=self.frame_principal, width=200, corner_radius=10, placeholder_text="Ano-Mês-Dia")
        self.nasc_entrada.grid(row=3, column=5, pady=20, padx=20, sticky="ew")
        
        ## Campo do CPF
        self.Lcpf = ctk.CTkLabel(master=self.frame_principal, text="CPF")
        self.Lcpf.grid(row=1, column=4, pady=20, padx=20, sticky="ew")
        self.cpf_entrada = ctk.CTkEntry(master=self.frame_principal, placeholder_text="Insira o CPF...", width=200, corner_radius=10)
        self.cpf_entrada.grid(row=1, column=5, columnspan=3, pady=20, padx=20, sticky="ew")

        ## Campo do gênero
        self.valor_gen = tk.StringVar(value="None")
        self.Lgen = ctk.CTkLabel(master=self.frame_principal, text="Gênero")
        self.Lgen.grid(row=6, column=0, pady=20, padx=20, sticky="ew")

        self.gen_M = ctk.CTkRadioButton(master=self.frame_principal, text="Masculino", width=5, height=5, value="Masculino", variable=self.valor_gen)
        self.gen_M.grid(row=6, column=1, pady=10, padx=10, sticky="ew")

        self.gen_F = ctk.CTkRadioButton(master=self.frame_principal, text="Feminino", width=5, height=5, value="Feminino", variable=self.valor_gen)
        self.gen_F.grid(row=6, column=2, pady=10, padx=10, sticky="ew")

        self.gen_nulo = ctk.CTkRadioButton(master=self.frame_principal, text="Outro", width=5, height=5, value="Outro", variable=self.valor_gen)
        self.gen_nulo.grid(row=6, column=3, pady=20, padx=20, sticky="ew")
        
        ##Campo de Cursos
        self.Lcursos = ctk.CTkLabel(master=self.frame_principal, text="Curso")
        self.Lcursos.grid(row=2 ,column=4, pady=20, padx=20, sticky="ew")
        self.cursos = {
            "TDS": 1,
            "MKT": 2,
            "ADM": 3
        }
        self.curso_var = tk.StringVar(value="Selecione")
        self.cursos_entrada = ctk.CTkOptionMenu(master=self.frame_principal, values=list(self.cursos.keys()), width=200, corner_radius=10, variable=self.curso_var)
        self.cursos_entrada.grid(row=2, column=5, columnspan=3, pady=20, padx=20, sticky="ew")

        ##Campo Botão "Salvar"
        self.btn_salvar = ctk.CTkButton(master=self.frame_principal, text="Salvar", corner_radius=10, command=self.coletarDados_Cadastro)
        self.btn_salvar.grid(row=7, column=0, columnspan=5, pady=20, padx=20)

        ##Campo botão "Limpar"
        self.btn_limpar = ctk.CTkButton(master=self.frame_principal, text="Limpar", corner_radius=10, command=self.apagarDados_Cadastro)
        self.btn_limpar.grid(row=7, column=2, columnspan=5, pady=20, padx=20)

    def telaCadastrosAluno(self):
        self.apagarFrame()
        self.titulo = ctk.CTkLabel(self.frame_principal, text="Dados dos Alunos", font=("Arial", 25))
        self.titulo.grid(row=0, column=0, columnspan=8, pady=20, padx=20)

        # Cria rótulos para os cabeçalhos da tabela
        self.colunas = ["ID", "Nome", "Nascimento", "Nome da Mãe", "Nome do Pai", "CPF", "Gênero", "CursoID"]
        for idx, self.colunas in enumerate(self.colunas):
            self.colunas = ctk.CTkLabel(self.frame_principal, text=self.colunas)
            self.colunas.grid(row=1, column=idx, padx=10, pady=10)

        # Carrega os dados dos alunos
        self.carregarDadosAlunos()

    def carregarDadosAlunos(self):
        # Obtém os dados dos alunos do banco de dados
        self.linhas = self.bd.DadosTabelaAluno()

        # Exibe os dados dos alunos na forma de uma tabela
        for linha_indice, linha_dado in enumerate(self.linhas, start=2):
            for coluna, cedula_dado in enumerate(linha_dado):
                cedula_label = ctk.CTkLabel(self.frame_principal, text=str(cedula_dado))
                cedula_label.grid(row=linha_indice, column=coluna, padx=10, pady=10)

    def telaBoletim(self):
        self.janela_boletim = tk.Toplevel(self)
        self.janela_boletim.geometry("800x400")
        self.janela_boletim.title("Boletim")

        lbl_selecione_aluno = ctk.CTkLabel(self.janela_boletim, text="Selecione o Aluno:")
        lbl_selecione_aluno.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.combo_alunos = ctk.CTkComboBox(self.janela_boletim, values=self.obterListaAlunos())
        self.combo_alunos.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.btn_carregar_boletim = ctk.CTkButton(self.janela_boletim, text="Carregar Boletim", command=self.carregarBoletim)
        self.btn_carregar_boletim.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        self.treeview_boletim = ttk.Treeview(self.janela_boletim, columns=("Disciplina", "Nota", "Frequência"), show="headings")
        self.treeview_boletim.heading("Disciplina", text="Disciplina")
        self.treeview_boletim.heading("Nota", text="Nota")
        self.treeview_boletim.heading("Frequência", text="Frequência")
        self.treeview_boletim.column("Disciplina", width=200)
        self.treeview_boletim.column("Nota", width=100)
        self.treeview_boletim.column("Frequência", width=100)
        self.treeview_boletim.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.janela_boletim.grid_columnconfigure(0, weight=1)
        self.janela_boletim.grid_columnconfigure(1, weight=1)
        self.janela_boletim.grid_columnconfigure(2, weight=1)
        self.janela_boletim.grid_rowconfigure(1, weight=1)
    
    def obterListaAlunos(self):
        # Este método deve retornar uma lista com o nome dos alunos
        # Exemplo: ["Aluno 1", "Aluno 2", "Aluno 3"]
        return ["Aluno 1", "Aluno 2", "Aluno 3"]

    def carregarBoletim(self):
        aluno_selecionado = self.combo_alunos.get()
        if aluno_selecionado:
            boletim = [
                {"Disciplina": "Matemática", "Nota": "8.5", "Frequência": "95%"},
                {"Disciplina": "Português", "Nota": "7.0", "Frequência": "90%"},
                # Adicione mais disciplinas conforme necessário
            ]
            for item in self.treeview_boletim.get_children():
                self.treeview_boletim.delete(item)
            for item in boletim:
                self.treeview_boletim.insert("", "end", values=(item["Disciplina"], item["Nota"], item["Frequência"]))
        else:
            messagebox.showwarning("Aviso", "Selecione um aluno para carregar o boletim.")

    def apagarFrame(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    def coletarDados_Cadastro(self):
        try:
            self.nome = self.nome_entrada.get().upper()
            self.nasc = self.nasc_entrada.get()
            self.nome_mae = self.nome_Mae_entrada.get().upper()
            self.nome_pai = self.nome_Pai_entrada.get().upper()
            self.cpf = self.cpf_entrada.get()
            self.gen = self.valor_gen.get()
            self.curso_texto = self.cursos_entrada.get()
            self.curso = self.cursos[self.curso_texto]
        except:
            messagebox.showerror("ERRO", "Digite os dados corretamente")
        else:
            self.bd.tabelaAlunos(self.nome, self.nasc, self.nome_mae, self.nome_pai, self.cpf, self.gen, self.curso)
        finally:
            messagebox.showinfo("SUCESSO", "Aluno cadastrado com sucesso!")
            self.apagarDados_Cadastro()
    
    def apagarDados_Cadastro(self):
        self.nome_entrada.delete(0, "end")
        self.nasc_entrada.delete(0, "end")
        self.valor_gen.set(None)
        self.cpf_entrada.delete(0, "end")
        self.nome_entrada.delete(0, "end")

    def fecharJanela(self):
        self.bd.fecharBanco()
        self.destroy()
    
    def iniciar(self):
            self.mainloop()

if __name__ == "__main__":
    app = Aluno()
    app.iniciar()