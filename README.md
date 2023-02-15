# Projeto: Restaurant Orders
Este projeto foi desenvolvido enquanto estudante da Trybe no módulo de Ciências da Computação.

---
## Sobre o Projeto
### Situação Problema
Uma lanchonete possui um sistema de registro de pedidos em planilha, onde é anotado o nome do cliente, o pedido e o dia da semana. Visando automatizar o sistema e melhorar a gestão interna, a lanchonete encomendou o projeto *Restaurant Orders*.

O objetivo é utilizar o **`Python`** para implementar um sistema automatizado de faturamento de pedidos em uma lanchonete, capaz de salvar o nome da pessoa cliente, o que foi pedido e o dia da semana em que ocorreu o atendimento.

O projeto deve ter duas funcionalidades principais:
  - **Gerar relatórios dos pedidos**: esses relatórios podem conter informações sobre os pedidos ou sobre os clientes, como dias preferidos em que vem a loja e pratos que mais pede.
  
  - **Controle de estoque**: para controlar o que o cardápio digital oferece para os clientes, é realizado um controle de estoque, evitando que os pratos com ingredientes indisponíveis sejam pedidos.

---
## Habilidades Desenvolvidas
  - Manipulação de e estruturas *Hashmap*, *Dict* e *Set*.

---
## Código Desenvolvido
### 01. Campanha de Publicidade
Para promover ações de marketing, a agência de publicidade precisou de alguns dados. Para isso, foi desenvolvido o método `analyze_log` no módulo `src/analyze_log`.

Ele responde as seguintes perguntas:
  - Qual o prato mais pedido por 'Maria'?
  - Quantas vezes 'Arnaldo' pediu 'hambúrguer'?
  - Quais pratos 'João' nunca pediu?
  - Quais dias 'João' nunca foi à lanchonete?

As respostas são salvas em um arquivo *.txt*.

### 02. Análises Contínuas
Implementa a classe `TrackOrders`, capaz de gerar informações contínuas sobre os pedidos. Com ela, é possível:
  - Adicionar novos pedidos com o método `add_new_order`.

Além de buscar as seguintes informações: 
  - Prato favorito de um cliente (`get_most_ordered_dish_per_customer`).
  - Pratos nunca pedidos por um cliente (`get_never_ordered_per_customer`).
  - Dias que um cliente nunca veio (`get_days_never_visited_per_customer`).
  - Dia com mais movimento (`get_busiest_day`).
  - Dia com menos movimento (`get_least_busy_day`).

### 03. Controle de Estoque
O sistema de controle de estoque da lanchonete era feito manualmente. No final de cada semana, era feita a contagem dos ingredientes do estoque e de quanto seria necessário comprar para atingir o estoque mínimo.

O novo sistema automatizado realiza essas funções automaticamente, imprimindo uma lista das quantidades de cada ingrediente, com base nos pedidos entregues.

O sistema tem como base a classe `InventoryControl` que, através da composição de classe, tem como propriedade uma instância de **TrackOrders**. Seus métodos são capazes de:
  - Adicionar um novo pedido através de uma instância de **TrackOrders** (`add_new_order`).
  - Gerar uma estrutura **dict** listando os ingredientes e a quantidade que deve ser comprada para atingir o estoque mínimo (`get_quantities_to_buy`).

### 04. Estoque Pode Acabar
Com o sistema de controle de estoque funcionando. É necessário garantir que todos os pratos oferecidos possuem os ingredientes necessários.

Para isso, a classe **InventoryControl** ganhará um novo método, o `get_available_dishes`, que:
  - Retorna um conjunto (**set**) de pratos que possuem ingredientes disponíveis no estoque.

---
## O que foi Utilizado?
  - Python.
  - Pubsub.
  - Flake8, Black.
  - Pytest, Pytest-json, Pytest-cov.

---
## Rodando Localmente
1. Clone o repositório e abra a pasta raiz.
2. Ative o ambiente virtual do python pelo terminal:
  ```bash
    python3 -m venv .venv && source .venv/bin/activate
  ```
3. Instale as dependências pelo terminal:
  ```bash
    python3 -m pip install -r dev-requirements.txt
  ```
4. Rode o comando para ver exemplos de uso:
  ```bash
    python3 src/main.py
  ```
