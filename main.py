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

def listar_produtos():
    conn = criar_conexao()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT id_produto, nome, preco_venda, estoque FROM produtos")
    produtos = cursor.fetchall()

    print("-"*30)
    print(" ESTOQUE ATUAL")
    print("-"*30 + "\n")
    for p in produtos:
        print(f"ID do produto: {p[0]} | {p[1]} | PREÇO: R${p[2]} | ESTOQUE: {p[3]}")

    cursor.close()
    conn.close ()

while True:
    print("-"*30 + "\n")
    print("SISTEMA DE MERCADO")
    print("-"*30 + "\n")
    print("1 - Listar produtos")
    print("2 - Registrar vendas (Em breve hehe)")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_produtos()
    elif opcao == "0":
        print("Saindo do sistema... Até logo :)")
        break
    else:
        print("Opção Inválida. Tente novamente")
