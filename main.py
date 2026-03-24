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
    if conn is None: return
    cursor = conn.cursor()
    cursor.execute("SELECT id_produto, nome, preco_venda, estoque FROM produtos")
    produtos = cursor.fetchall()

    print("\n" + "-" * 30)
    print("ESTOQUE ATUAL")
    print("-" * 30)
    for p in produtos:
        print(f"ID: {p[0]} | {p[1]} | R${p[2]} | Estoque: {p[3]}")

    cursor.close()
    conn.close()

def registrar_venda():
    conn = criar_conexao()
    if conn is None: return
    cursor = conn.cursor()

    try:
        entrada_id = input("Digite o ID do produto: ")
        if not entrada_id.isdigit():
            print("\nErro: O ID deve ser apenas números!")
            return

        entrada_qtd = input("Digite a quantidade: ")
        if not entrada_qtd.isdigit():
            print("\nErro: A quantidade deve ser apenas números!")
            return

        id_prod = int(entrada_id)
        qtd_venda = int(entrada_qtd)

        cursor.execute("SELECT nome, preco_venda, estoque FROM produtos WHERE id_produto = %s", (id_prod,))
        produto = cursor.fetchone()
        if produto and produto[2] >= qtd_venda:
            nome, preco, estoque_no_banco = produto
            valor_total = preco * qtd_venda

            cursor.execute(
                "INSERT INTO vendas (data_venda, valor_total, metodo_pagamento) VALUES (NOW(), %s, 'Dinheiro')",
                (valor_total,))
            id_venda = cursor.lastrowid

            cursor.execute(
                "INSERT INTO itens_venda (id_venda, id_produto, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)",
                (id_venda, id_prod, qtd_venda, preco))

            novo_estoque = estoque_no_banco - qtd_venda
            cursor.execute("UPDATE produtos SET estoque = %s WHERE id_produto = %s", (novo_estoque, id_prod))

            conn.commit()
            print("-" * 30)
            print(f"Venda realizada: {qtd_venda}x {nome}")
            print(f"Total: R${valor_total:.2f}")
            print("-" * 30)
        else:
            print("\nErro: Produto não encontrado ou estoque insuficiente!")

    except Exception as e:
        print(f"Erro na venda: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


while True:
    print("\n=== SISTEMA DE MERCADO ===")
    print("1 - Listar produtos")
    print("2 - Registrar venda")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_produtos()
    elif opcao == "2":
        registrar_venda()
    elif opcao == "0":
        print("Saindo do sistema... Até logo :)")
        break
    else:
        print("Opção inválida!")