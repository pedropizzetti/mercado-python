import mysql.connector
import csv


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

    print("\n" + "-" * 30)
    print("ESTOQUE ATUAL")
    print("-" * 30)
    for p in produtos:
        print(f"ID: {p[0]} | {p[1]} | R${p[2]} | Estoque: {p[3]}")

    cursor.close()
    conn.close()

def gerar_relatorio():
    conn = criar_conexao()
    if conn is None:
        return
    cursor = conn.cursor()

    try:
        cursor.execute("select sum(valor_total) from vendas")
        total = cursor.fetchone()[0] or 0

        cursor.execute("select nome, estoque from produtos where estoque < 5")
        baixos = cursor.fetchall()

        print("\n" + "-" * 30)
        print("RELATÓRIO DE VENDAS")
        print("-" * 30 + "\n")
        print(f"Faturamento total: {total:.2f}")
        print(f"Produtos em alerta: {len(baixos)}")
        for b in baixos:
            print(f" -> {b[0]} (Apenas {b[1]} unidades no estoque)")
        print("-" * 30)

    except Exception as e:
        print(f"Erro ao gerar relatorio: {e}")
    finally:
        cursor.close()
        conn.close()

def registrar_venda():
    conn = criar_conexao()
    if conn is None:
        return
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

        if qtd_venda <= 0:
            print("Erro. A quantidade deve ser maior que zero!")
            return

        print("Formas de pagamento::")
        print("1 - Dinheiro")
        print("2 - Cartão de Débito")
        print("3 - Cartão de Crédito")
        print("4 - Pix")
        op_pagamento=input("Escolha a opção: ")

        metodos = {"1": "Dinheiro", "2": "Débito", "3": "Crédito", "4": "Pix"}

        if op_pagamento not in metodos:
            print("\nErro: A forma de pagamento é inválida.")
            return
        pagamento_escolhido = metodos[op_pagamento]

        cursor.execute("SELECT nome, preco_venda, estoque FROM produtos WHERE id_produto = %s", (id_prod,))
        produto = cursor.fetchone()
        if produto and produto[2] >= qtd_venda:
            nome, preco, estoque_no_banco = produto
            valor_total = preco * qtd_venda

            cursor.execute(
                "INSERT INTO vendas (data_venda, valor_total, metodo_pagamento) VALUES (NOW(), %s, %s)",
                (valor_total, pagamento_escolhido))
            id_venda = cursor.lastrowid

            cursor.execute(
                "INSERT INTO itens_venda (id_venda, id_produto, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)",
                (id_venda, id_prod, qtd_venda, preco))

            novo_estoque = estoque_no_banco - qtd_venda
            cursor.execute("UPDATE produtos SET estoque = %s WHERE id_produto = %s", (novo_estoque, id_prod))

            conn.commit()
            print("-" * 30)
            print(f"Venda realizada: {qtd_venda}x {nome}")
            print(f"Total: R$ {valor_total:.2f} | Pagamento: {pagamento_escolhido}")
            print("-" * 30)
        else:
            print("\nErro: Produto não encontrado ou estoque insuficiente!")

    except Exception as e:
        print(f"Erro na venda: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def exportar_csv():
    conn = criar_conexao()
    if conn is None:
        return
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id_venda, data_venda, valor_total, metodo_pagamento FROM vendas")
        vendas = cursor.fetchall()

        with open("relatorio_vendas.csv", mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Id Venda", "Data", "Valor Total", "Pagamento"])
            escritor.writerows(vendas)
        print("\nSucesso! O arquivo 'relatorio_vendas.csv' foi criado com sucesso!")

    except Exception as e:
        print(f"Erro ao exportar: {e}")
    finally:
        cursor.close()
        conn.close()

while True:
    print("\n=== SISTEMA DE MERCADO ===")
    print("1 - Listar produtos")
    print("2 - Registrar venda")
    print("3 - Gerar relatorio")
    print("4 - Exportar para Excel/CSV")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_produtos()
    elif opcao == "2":
        registrar_venda()
    elif opcao == "0":
        print("Saindo do sistema... Até logo :)")
        break
    elif opcao == "3":
        gerar_relatorio()
    elif opcao == "4":
        exportar_csv()
    else:
        print("Opção inválida!")