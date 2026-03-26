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

## Business Intelligence
* Para transformar os dados brutos em decisões estratégicas, integrei o banco de dados MySQL a um Dashboard interativo no Power BI:
* **Monitor de Reposição:** Foi criado um alerta visual que identifica automaticamente produtos com estoque baixo e os coloca no topo da lista para compra.
* **Análise de Rentabilidade:** Cálculo de Margem de Lucro Real por produto através de medidas DAX.
* **Visão de Faturamento:** Gráficos que mostram a preferência de pagamento dos clientes (Pix, Cartão, Dinheiro) e o lucro total do período.
<img width="1460" height="821" alt="image" src="https://github.com/user-attachments/assets/ba2aec11-1724-40d8-b472-85d132c99b8c" />

## Tecnologias usadas
* **Python 3.12**
* **MySQL** (Banco de dados)
* **PyCharm**
* **Power BI Desktop** (Visualização de dados)
* **DAX** (Linguagem para cálculos de BI)
* **MySQL Connector** (Integração Banco -> BI)

## Como Executar o Projeto
1. Banco de Dados (MySQL)          
Certifique-se de que o XAMPP (ou similar) esteja rodando o serviço do MySQL.     
Importe o arquivo `mercado.sql` (disponível neste repositório) para criar a estrutura das tabelas e os dados iniciais. 
Caso precise alterar as credenciais de acesso, verifique o arquivo database.py.

2. Ambiente Python   
Instale as bibliotecas necessárias usando o terminal:
`pip install mysql-connector-python pandas`                
Execute o arquivo principal para abrir o menu do sistema:
`python main.py`

3. Dashboard (Power BI)        
Abra o arquivo `Dashboard_Vendas.pbix` no Power BI Desktop.

Caso os dados não carreguem de primeira, vá em Página Inicial > Transformar Dados > Configurações da Fonte de Dados e atualize o caminho para o seu localhost do MySQL.

---
**Desenvolvido por Pedro Pizzetti**
