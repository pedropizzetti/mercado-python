import mysql.connector

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mercado"
        )
        return conexao
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None