# Mercado-Python
> Sistema para controlar estoque e vendas usando Python e MySQL.

## O que o projeto faz
Esse sistema ajuda a gerenciar um pequeno mercado. Ele permite cadastrar produtos, controlar a quantidade no estoque e registrar vendas. O diferencial é que ele não só guarda os dados, mas também gera documentos e relatórios úteis para o dia a dia.

## Como o código está organizado
Para o código não virar uma bagunça, dividi ele em três partes:
* **main.py:** É onde o programa começa. Ele exibe o menu e direciona para a função certa.
* **processamento.py:** Aqui fica toda a "mágica". É onde o cálculo de venda, o estoque e os relatórios são feitos.
* **database.py:** Cuida apenas da conexão com o banco de dados MySQL.

## O que eu adicionei de novo
* **Dicionário de Opções:** Em vez de usar um monte de `if/else`, usei um dicionário para chamar as funções. Isso deixa o código mais limpo e rápido.
* **Cupom Fiscal:** Toda vez que você faz uma venda, o sistema cria um arquivo `.txt` com o resumo da compra (ID, produto, total e forma de pagamento).
* **Relatório de Lucro:** O sistema faz uma conta automática (Preço de Venda - Preço de Custo) e mostra quanto você ganhou de verdade em cada produto.
* **Exportação para Excel (CSV):** Dá para exportar a lista de vendas para um arquivo que abre no Excel.

## 🛠Tecnologias usadas
* **Python 3.12**
* **MySQL** (Banco de dados)
* **PyCharm** (Onde escrevi o código)

## O que já está funcionando
- [x] Cadastro e exclusão de produtos.
- [x] Venda com baixa automática no estoque.
- [x] Verificação para não deixar o estoque ficar negativo.
- [x] Geração de cupom em texto.
- [x] Relatório de lucro por item.

---
**Desenvolvido por Pedro Pizzetti**