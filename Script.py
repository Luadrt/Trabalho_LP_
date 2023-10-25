import sqlite3
conn = sqlite3.connect("estoqueProdutos.db")
cursor = conn.cursor()


table_para_usuario = """
    CREATE TABLE usuario (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    )
"""

table_para_produtos = """
    CREATE TABLE produtos (
        id INTEGER PRIMARY KEY,
        usuario_id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        descricao TEXT NOT NULL,
        FOREING KEY (usuario_id) REFERENCES usuario (id)
    )
"""

cursor.execute(table_para_usuario)
cursor.execute(table_para_usuario)

conn.commit()
conn.close()






    
