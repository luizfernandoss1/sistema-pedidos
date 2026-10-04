#Meu projeto de lançamento de pedidos
comanda = []
total_conta = 0.0
while True:
    print("=====SISTEMA DE COMANDA=====")
    print()
    print("1- Adicionar item ao pedido")
    print("2- Mostrar comanda atual")
    print("3- Fechar conta e sair")
    opcao = int(input("Escolha uma opção: "))    
    if opcao == 3:
        print(f"\nConta finalizada! Total a pagar: R$ {total_conta:.2f}")
        print("Fechando o sistema, até logo!")
        break
    elif opcao == 1:
        item = input("Faça o seu pedido: ")
        preco = float(input(f"Digite o preço de {item}: R$ "))

        comanda.append(item)
        total_conta += preco 
        print(f"{item} adicionado com sucesso!\n")
    elif opcao == 2:
        for item in comanda:
            print(item)    
    else:
        print("Opção invalida! Por favor escolha 1, 2 ou 3\n!")  
              