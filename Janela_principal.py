import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import Conexao_sql as con
import tela_alunos
import tela_curso
import tela_professores
from PIL import Image
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        self.title("Gerenciador de Alunos")

        self.frame_principal = ctk.CTkFrame(self, width=300, height=400, corner_radius=15, border_width=2)
        self.frame_principal.pack(pady=50, padx=50, expand=True)

        self.frame_principal.grid_rowconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(1, weight=1)
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_columnconfigure(1, weight=1)

        icone1 = "aluno.png"
        icone2 = "curso.png"
        icone3 = "professor.png"
        icone4 = "aviso.png"

        self.imagen1 = ctk.CTkImage(dark_image=Image.open(icone1), size=(100, 100))
        self.imagen2 = ctk.CTkImage(dark_image=Image.open(icone2), size=(100, 100))
        self.imagen3 = ctk.CTkImage(dark_image=Image.open(icone3), size=(100, 100))
        self.imagen4 = ctk.CTkImage(dark_image=Image.open(icone4), size=(100, 100))
         
        self.text_menu = ctk.CTkLabel(self.frame_principal, text="Opções", font=("Arial", 25))
        self.text_menu.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        
        self.btn_alunos = ctk.CTkButton(self.frame_principal, image=self.imagen1, text="Alunos", command=self.abrirJanelaAluno, compound="top", width=200, height=100)
        self.btn_alunos.grid(row=1, column=0, padx=40, pady=10, sticky="ew")

        self.btn_cursos = ctk.CTkButton(self.frame_principal,image=self.imagen2, text="Cursos", command=self.abrirJanelaCurso, compound="top", width=200, height=100)
        self.btn_cursos.grid(row=1, column=1, padx=40, pady=10, sticky="ew")

        self.btn_profs = ctk.CTkButton(self.frame_principal, image=self.imagen3, text="Professores", command=self.abrirJanelaProf, compound="top", width=200, height=100)
        self.btn_profs.grid(row=2, column=0, padx=40, pady=10, sticky="ew")

        self.btn_profs = ctk.CTkButton(self.frame_principal, image=self.imagen4, text="Avisos", compound="top", width=200, height=100)
        self.btn_profs.grid(row=2, column=1, padx=40, pady=10, sticky="ew")
    
    def abrirJanelaAluno(self):
        self.janelaAluno = tela_alunos.Aluno().iniciar()

    def abrirJanelaCurso(self):
        self.janelaCurso = tela_curso.Curso().iniciar()
    
    def abrirJanelaProf(self):
        self.janelaProf = tela_professores.Prof().iniciar()
    
if __name__ == "__main__":
    app = App()
    app.mainloop()