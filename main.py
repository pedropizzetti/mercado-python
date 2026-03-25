import database
from database import criar_conexao
import processamento

conexao = criar_conexao()

if conexao:
    while True:
        processamento.exibir_menu()
        opcao = input("Escolha uma opção: ")

        opcoes = {
            "1": processamento.registrar_venda,
            "2": processamento.listar_produtos,
            "3": processamento.cadastrar_produto,
            "4": processamento.excluir_produto,
            "5": processamento.gerar_relatorio,
            "6": processamento.exportar_csv,
            "7": processamento.relatorio_lucro
        }

        if opcao == "0":
            print("Saindo do sistema...")
            database.fechar_conexao(conexao)
            break
        elif opcao in opcoes:
            opcoes[opcao](conexao)
        else:
            print("\nOpção inválida! Tente novamente.")
            print("-" * 30)