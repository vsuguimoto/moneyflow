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
                categorias_id INTEGER,
                pessoas_id INTEGER NOT NULL,
                FOREIGN KEY (pessoas_id) REFERENCES pessoas (id),
                FOREIGN KEY (categorias_id) REFERENCES categorias (id)
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


    def criar_lancamento(self, nome, tipo, valor, data_compra, categorias_id, pessoas_id):
        cursor = self.conexao.cursor()
        cursor.execute(f"INSERT INTO lancamentos (nome, tipo, valor, data_compra, categorias_id, pessoas_id) VALUES ('{nome}', '{tipo}', {valor}, '{data_compra}', {categorias_id}, {pessoas_id})")
        self.conexao.commit()

    def apagar_lancamento(self, lancamento_id):
        cursor = self.conexao.cursor()
        cursor.execute(f"DELETE FROM lancamentos WHERE id = {lancamento_id}")


    def criar_visao_mes(self):
        cursor = self.conexao.cursor()
        cursor.execute('DROP TABLE IF EXISTS lancamentos_visao_mes')
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lancamentos_visao_mes AS
            SELECT
                pessoas.nome nome_pessoa,
                strftime('%Y-%m', lancamentos.data_compra) AS ano_mes,
                categorias.nome categoria,
                lancamentos.tipo tipo_lancamento,
                ROUND(SUM(lancamentos.valor),2) AS valor_total
            FROM lancamentos
            LEFT JOIN pessoas ON lancamentos.pessoas_id = pessoas.id
            LEFT JOIN categorias ON lancamentos.categorias_id = categorias.id
            GROUP BY pessoas.nome, ano_mes, categorias.nome, lancamentos.tipo;
        """)
        self.conexao.commit()
    
    def obter_visao_mes(self):
        cursor = self.conexao.cursor()
        visao_mes = cursor.execute("SELECT * FROM lancamentos_visao_mes")
        return visao_mes.fetchall()

    def obter_visao_geral(self):
        cursor = self.conexao.cursor()
        dados = cursor.execute("""
        SELECT
            pessoas.nome nome_pessoa,
            lancamentos.data_compra,
            lancamentos.nome nome_lancamento,
            categorias.nome categoria,
            lancamentos.tipo tipo_lancamento,
            lancamentos.valor
        FROM lancamentos
        LEFT JOIN pessoas ON lancamentos.pessoas_id = pessoas.id
        LEFT JOIN categorias ON lancamentos.categorias_id = categorias.id
        """)
        
        return dados.fetchall()
    
    def fechar_conexao(self):
        self.conexao.close()