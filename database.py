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
    except mysql.connector.Error as e:
        print(f"Erro de banco de dados: {e}")
        return None

def fechar_conexao(conexao):
    if conexao and conexao.is_connected():
        conexao.close()
        print("A conexão com o banco de dados foi encerrada com sucesso.")
    else:
        print("Não havia conexão ativa para fechar o banco de dados.")