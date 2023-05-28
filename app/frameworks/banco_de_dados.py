import sqlite3

# Classe responsável pela manipulação do banco de dados
class BancoDeDados:
    def __init__(self, nome_banco):
        self.conexao = sqlite3.connect(nome_banco)
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conexao.cursor()

        # Tabela de categorias
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT
            )
        """)

        # Tabela de lançamentos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lancamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT CHECK(tipo IN ('C', 'D')) NOT NULL,
                valor REAL NOT NULL,
                categoria_id INTEGER,
                FOREIGN KEY (categoria_id) REFERENCES categorias (id)
            )
        """)

        self.conexao.commit()

    def criar_categoria(self, nome, descricao=None):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO categorias (nome, descricao) VALUES (?, ?)", (nome, descricao))
        self.conexao.commit()

    def apagar_categoria(self, categoria_id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM categorias WHERE id = ?", (categoria_id,))
        self.conexao.commit()

    def inserir_lancamento(self, nome, tipo, valor, categoria_id):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO lancamentos (nome, tipo, valor, categoria_id) VALUES (?, ?, ?, ?)",
                       (nome, tipo, valor, categoria_id))
        self.conexao.commit()

    def carregar_lancamentos_lote(self, lancamentos):
        cursor = self.conexao.cursor()
        cursor.executemany("INSERT INTO lancamentos (nome, tipo, valor, categoria_id) VALUES (?, ?, ?, ?)",
                           lancamentos)
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()