import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mercado"
    )

    if conexao.is_connected():
        print("Conectado com sucesso ao MySQL!")

        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")

        produtos = cursor.fetchall()
        for p in produtos:
            print(f"Produto encontrado: {p[1]} - Estoque: {p[5]}")

except Exception as e:
    print(f"Erro ao conectar: {e}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()