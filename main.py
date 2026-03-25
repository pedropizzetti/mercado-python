from database import criar_conexao
import processamento

conexao=criar_conexao()

if conexao:
    while True:
        print("-" * 30)
        print("Sistema de Mercado")
        print("-" * 30)
        print("1 - Listar produtos")
        print("2 - Registrar venda")
        print("3 - Gerar relatório")
        print("4 - Exportar para Excel/CSV")
        print("0 - Sair")
        opcao=input("Escolha uma opção: ")

        if opcao == "1":
            processamento.listar_produtos(conexao)
        elif opcao == "2":
            processamento.registrar_venda(conexao)
        elif opcao == "3":
            processamento.gerar_relatorio(conexao)
        elif opcao == "4":
            processamento.exportar_csv(conexao)
        elif opcao == "0":
            print("Saindo do sistema...")
            conexao.close()
            break
        else:
            print("Opção inválida! Tente novamente.")
else:
    print("Não foi possível iniciar o sistema sem conexão com o banco.")