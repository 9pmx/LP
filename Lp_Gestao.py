# Gestão de Stock e Vendas - Garrafas de Água

produtos = {
    1: {"nome": "Garrafa 0.5L", "preco": 0.50, "quantidade": 100},
    2: {"nome": "Garrafa 1.5L", "preco": 0.80, "quantidade": 80},
    3: {"nome": "Pack 6x1.5L", "preco": 4.20, "quantidade": 50}
}

vendas = []

def mostrar_stock():
    print("\n=== Stock Atual ===")
    for id, info in produtos.items():
        print(f"{id} - {info['nome']} | Preço: €{info['preco']} | Quantidade: {info['quantidade']}")

def registar_venda():
    mostrar_stock()
    escolha = int(input("Escolha o ID do produto: "))
    quantidade = int(input("Quantidade vendida: "))

    if escolha in produtos and produtos[escolha]["quantidade"] >= quantidade:
        produtos[escolha]["quantidade"] -= quantidade
        total = quantidade * produtos[escolha]["preco"]
        vendas.append({"produto": produtos[escolha]["nome"], "quantidade": quantidade, "total": total})
        print(f"Venda registada! Total: €{total:.2f}")
    else:
        print("Erro: Produto inexistente ou stock insuficiente.")

def mostrar_vendas():
    print("\n=== Histórico de Vendas ===")
    for venda in vendas:
        print(f"{venda['quantidade']}x {venda['produto']} - Total: €{venda['total']:.2f}")

def menu():
    while True:
        print("\n--- Gestão de Garrafas de Água ---")
        print("1. Ver Stock")
        print("2. Registar Venda")
        print("3. Histórico de Vendas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_stock()
        elif opcao == "2":
            registar_venda()
        elif opcao == "3":
            mostrar_vendas()
        elif opcao == "4":
            print("A sair...")
            break
        else:
            print("Opção inválida!")

menu()
