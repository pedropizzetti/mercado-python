import csv

def listar_produtos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id_produto, nome, categoria, preco_venda, estoque FROM produtos")
    produtos = cursor.fetchall()

    print("\n" + "-" * 70)
    print("LISTA DE PRODUTOS")
    print("-" * 70)
    print(f"{'ID':<4} | {'NOME':<30} | {'CATEGORIA':<15} | {'PREÇO':<10} | {'ESTOQUE'}")

    for p in produtos:
        print(f"{p[0]:<4} | {p[1]:<30} | {p[2]:<15} | R${p[3]:<8.2f} | {p[4]}")

    print("-" * 70)
    cursor.close()

def gerar_relatorio(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT SUM(valor_total) FROM vendas")
        total = cursor.fetchone()[0] or 0

        cursor.execute("SELECT nome, estoque FROM produtos WHERE estoque < 5")
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
        print(f"Erro ao gerar relatório: {e}")
    finally:
        cursor.close()

def registrar_venda(conn):
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

        print("Formas de pagamento:")
        print("1 - Dinheiro")
        print("2 - Cartão de Débito")
        print("3 - Cartão de Crédito")
        print("4 - Pix")
        op_pagamento = input("Escolha a opção: ")

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
            nome_arquivo = f"cupom_venda_{id_venda}.txt"
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write(f"--- MERCADO ---\n")
                f.write(f"Venda ID: {id_venda}\n")
                f.write(f"Produto: {nome}\n")
                f.write(f"Quantidade: {qtd_venda} x R$ {preco:.2f}\n")
                f.write(f"Total: R$ {valor_total:.2f}\n")
                f.write(f"Pagamento: {pagamento_escolhido}\n")
                f.write("-------------------------\n")
                f.write("Obrigado pela preferência! :)")
            print(f"Cupom fiscal gerado: {nome_arquivo}")

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

def cadastrar_produto(conn):
    cursor = conn.cursor()
    try:
        print("-" * 30)
        print("CADASTRO DE NOVO PRODUTO")
        print("-" * 30)
        nome=input("Digite o nome do produto: ")
        categoria=input("Digite o categoria do produto: ")
        custo=float(input("Digite o preço de custo: "))
        preco=float(input("Digite o preço de venda: "))
        estoque=int(input("Digite a quantidade inicial de estoque: "))

        sql = "INSERT INTO produtos (nome, categoria, preco_custo, preco_venda, estoque) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nome, categoria, custo, preco, estoque))

        conn.commit()
        print(f"\n{nome} foi cadastrado com sucesso!")
    except ValueError:
        print("\nErro. Preço de Custo, Preço de Venda e Estoque devem ser números.")
    except Exception as e:
        print(f"\nErro ao cadastrar: {e}")
        conn.rollback()
    finally:
        cursor.close()

def excluir_produto(conn):
    cursor = conn.cursor()
    try:
        print("-" * 30)
        print("EXCLUIR PRODUTO")
        print("-" * 30)
        id_prod=input("Digite o ID do produto que deseja remover: ")
        if not id_prod.isdigit():
            print("Erro: O ID deve conter apenas números!")
            return
        cursor.execute("select nome from produtos where id_produto = %s", (id_prod,))
        produto = cursor.fetchone()

        if produto:
            confirmar=input(f"Tem certeza que deseja excluir '{produto[0]}'? (S/N): ").upper()
            if confirmar == "S":
                cursor.execute("delete from produtos where id_produto = %s", (id_prod,))
                conn.commit()
                print(f"\nProduto '{produto[0]}' excluido com sucesso!")
            else:
                print("\nOperação cancelada!")
        else:
            print("\nErro: Produto não encontrado!")

    except Exception as e:
        print(f"Erro ao excluir: {e}")
        conn.rollback()
    finally:
        cursor.close()


def relatorio_lucro(conn):
    cursor = conn.cursor()
    try:
        sql = """
              SELECT p.nome, \
                     SUM(iv.quantidade)                                       as total_vendido, \
                     SUM(iv.quantidade * (iv.preco_unitario - p.preco_custo)) as lucro_total
              FROM itens_venda iv
                       JOIN produtos p ON iv.id_produto = p.id_produto
              GROUP BY p.id_produto \
              """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print("\n" + "=" * 50)
        print(f"{'PRODUTO':<30} | {'QTD':<5} | {'LUCRO (R$)'}")
        print("-" * 50)

        lucro_geral = 0
        for r in resultados:
            print(f"{r[0]:<30} | {r[1]:<5} | R$ {r[2]:>8.2f}")
            lucro_geral += r[2]

        print("-" * 50)
        print(f"LUCRO LÍQUIDO TOTAL: R$ {lucro_geral:.2f}")
        print("=" * 50)
    except Exception as e:
        print(f"Erro no relatório de lucro: {e}")
    finally:
        cursor.close()

def exportar_csv(conn):
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