from database import criar_conexao
import processamento

conexao=criar_conexao()

if conexao:
    while True:
        print("\n" + "-" * 30)
        print("    SISTEMA DE MERCADO")
        print("-" * 30)
        print("1 - Registrar venda")
        print("2 - Listar produtos")
        print("3 - Cadastrar novo produto")
        print("4 - Excluir produto")
        print("5 - Gerar relatorio em tela")
        print("6 - Exportar relatório para Excel/CSV")
        print("7 - Relatório de lucratividade")
        print("0 - Sair")
        opcao=input("Escolha uma opção: ")

        if opcao == "1":
            processamento.registrar_venda(conexao)
        elif opcao == "2":
            processamento.listar_produtos(conexao)
        elif opcao == "3":
            processamento.cadastrar_produto(conexao)
        elif opcao == "4":
            processamento.excluir_produto(conexao)
        elif opcao == "5":
            processamento.gerar_relatorio(conexao)
        elif opcao == "6":
            processamento.exportar_csv(conexao)
        elif opcao == "7":
            processamento.relatorio_lucro(conexao)
        elif opcao == "0":
            print("Saindo do sistema...")
            conexao.close()
            break
        else:
            print("Opção inválida! Tente novamente.")
else:
    print("Não foi possível iniciar o sistema sem conexão com o banco.")