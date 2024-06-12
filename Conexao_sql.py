import mysql.connector
from mysql.connector import Error


class ConexaoMYSQL:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None
    
    def conectarBanco(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conexao.cursor()
        except:
            print("ERRO: conexão interrompida.")
        else:
            print("Conexão feita")

    def tabelaAlunos(self, nome, nasc, mae, pai, cpf, gen, curso):
        try:
            self.comando = '''INSERT INTO alunos (Nome, Nascimento, Mae, Pai, CPF, Genero, CursoID) values (%s, %s, %s, %s, %s, %s, %s)'''
            self.cursor.execute(self.comando,(nome, nasc, mae, pai, cpf, gen, curso))
            self.conexao.commit()
        except Error as e:
            print(f"ERRO: {e}")
    
    def DadosTabelaAluno(self):
        try:
            self.cursor.execute('''SELECT * FROM alunos''')
            self.linhas = self.cursor.fetchall()
            return self.linhas
        except Error as e:
            print(f"ERRO: {e}")
    
    def tabelaCursos(self, nomecurso, duracao, modalidade, turno):
        try:
            self.comando = '''INSERT INTO cursos (NomeCurso, Duracao, Modalidade, Turno) values (%s, %s, %s, %s)'''
            self.cursor.execute(self.comando, (nomecurso, duracao, modalidade, turno))
            self.conexao.commit()
        except Error as e:
            print(print(f"ERRO: {e}"))

    def DadosTabelaCursos(self):
        try:
            self.cursor.execute('''SELECT * FROM cursos''')
            self.linhas = self.cursor.fetchall()
            return self.linhas
        except Error as e:
            print(f"ERRO: {e}")
    
    def tabelaProfessores(self, nome, cursoid):
        try:
            self.comando = '''INSERT INTO professores (Nome, CursoID) values (%s, %s)'''
            self.cursor.execute(self.comando, (nome, cursoid))
            self.conexao.commit()
        except Error as e:
            print(print(f"ERRO: {e}"))

    def DadosTabelaProfs(self):
        try:
            self.cursor.execute('''SELECT * FROM professores''')
            self.linhas = self.cursor.fetchall()
            return self.linhas
        except Error as e:
            print(f"ERRO: {e}")
    
    def fecharBanco(self):
        self.cursor.close()
        self.conexao.close()
        print("Conexão fechada.")