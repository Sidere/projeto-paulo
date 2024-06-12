import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import Conexao_sql as con
import tela_alunos
import tela_curso
import tela_professores
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Gerenciador de Alunos")

        self.frame_principal = ctk.CTkFrame(self, width=500, height=200, corner_radius=15, border_width=2)
        self.frame_principal.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.text_menu = ctk.CTkLabel(self.frame_principal, text="Testes", font=("Arial", 25))
        self.text_menu.grid(row=0, column=0, padx=20, pady=20)

        self.btn_cursos = ctk.CTkButton(self.frame_principal, text="Cursos", command=self.abrirJanelaCurso)
        self.btn_cursos.grid(row=1, column=0, padx=20, pady=10)

        self.btn_alunos = ctk.CTkButton(self.frame_principal, text="Alunos", command=self.abrirJanelaAluno)
        self.btn_alunos.grid(row=2, column=0, padx=20, pady=10)

        self.btn_profs = ctk.CTkButton(self.frame_principal, text="Professores", command=self.abrirJanelaProf)
        self.btn_profs.grid(row=3, column=0, padx=20, pady=10)
    
    def abrirJanelaAluno(self):
        self.janelaAluno = tela_alunos.Aluno().iniciar()

    def abrirJanelaCurso(self):
        self.janelaCurso = tela_curso.Curso().iniciar()
    
    def abrirJanelaProf(self):
        self.janelaProf = tela_professores.Prof().iniciar()
    
if __name__ == "__main__":
    app = App()
    app.mainloop()