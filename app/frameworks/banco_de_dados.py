import sqlite3

# Classe responsável pela manipulação do banco de dados
class BancoDeDados:
    def __init__(self):
        self.conexao = sqlite3.connect('MoneyFlow.db')
        self.criar_tabelas()
    

    def criar_tabelas(self):
        cursor = self.conexao.cursor()

        # Tabela de categorias
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """)

        # Tabela de lançamentos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lancamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT CHECK(tipo IN ('C', 'D')) NOT NULL,
                valor REAL NOT NULL,
                data_compra TIMESTAMP,
                categoria_id INTEGER,
                pessoa_id INTEGER NOT NULL,
                FOREIGN KEY (pessoa_id) REFERENCES pessoas (id),
                FOREIGN KEY (categoria_id) REFERENCES categorias (id)
            )
        """)

        # Tabela de lançamentos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """)

        self.conexao.commit()


    def criar_categoria(self, nome):
        cursor = self.conexao.cursor()
        cursor.execute(f"INSERT INTO categorias (nome) VALUES ('{nome}')")
        self.conexao.commit()

    def apagar_categoria(self, categoria_id):
        cursor = self.conexao.cursor()
        cursor.execute(f"DELETE FROM categorias WHERE id = {categoria_id}")
        self.conexao.commit()

    def obter_categoria(self):
        cursor = self.conexao.cursor()
        categorias = cursor.execute("SELECT id, nome FROM categorias")
        
        return categorias.fetchall()


    def criar_pessoa(self, nome):
        cursor = self.conexao.cursor()
        cursor.execute(f"INSERT INTO pessoas (nome) VALUES ('{nome}')")
        self.conexao.commit()

    def obter_pessoa(self):
        cursor = self.conexao.cursor()
        valores = cursor.execute("SELECT id, nome FROM pessoas")
        
        return valores.fetchall()


    def criar_lancamento(self, nome, tipo, valor, data_compra, categoria_id, pessoa_id):
        cursor = self.conexao.cursor()
        cursor.execute(f"INSERT INTO lancamentos (nome, tipo, valor, data_compra, categoria_id, pessoa_id) VALUES ('{nome}', '{tipo}', {valor}, '{data_compra}', {categoria_id}, {pessoa_id})")
        self.conexao.commit()

    def apagar_lancamento(self, lancamento_id):
        cursor = self.conexao.cursor()
        cursor.execute(f"DELETE FROM lancamentos WHERE id = {lancamento_id}")

    def fechar_conexao(self):
        self.conexao.close()