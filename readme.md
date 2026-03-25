# Mercado-Python: Gestão & Inteligência de Dados
> Sistema back-end para controle de estoque e fluxo de caixa, integrado com MySQL.

---

## Sobre o Projeto
Olá! Este projeto nasceu da necessidade de unir a lógica de programação em **Python** com a persistência de dados em **SQL**. Mais do que um simples CRUD, o foco aqui foi garantir a **integridade dos dados** (estoque nunca fica negativo) e a **segurança** das transações.



## Tech Stack & Ferramentas
* **Linguagem:** Python 3.12 
* **Banco de Dados:** MySQL (via XAMPP) 
* **Ambiente:** PyCharm Professional 
* **Versionamento:** Git & GitHub

## Funcionalidades Principais
*  **Conexão Robusta:** Tratamento de erros para falhas de servidor.
*  **Validação de Entrada:** Proteção contra entradas de texto em campos numéricos (`isdigit`).
*  **Segurança SQL:** Prevenção total contra SQL Injection usando Placeholders.
*  **Lógica de Vendas:** 
    1. Verifica disponibilidade de estoque.
    2. Registra a venda principal.
    3. Vincula itens à venda (Relacionamento 1:N).
    4. Atualiza o saldo de produtos automaticamente.

## Tratamento de Erros (Resiliência)
O sistema utiliza o conceito de **Transações Automáticas**:
- **Commit:** A venda só é gravada se TODOS os passos funcionarem.
- **Rollback:** Se o banco falhar no meio, a operação é desfeita para não gerar dados "sujos".

## Próximos Passos (Roadmap)
- [ ] Criar dashboard no Power BI integrado ao banco.
- [ ] Gerar cupom fiscal em formato `.txt` ou `.pdf`.

---
🤓️ **Desenvolvido por Pedro Pizzetti** - *Estudante de Ciência de Dados focado em transformar linhas de código em insights reais.*
