# Importando a biblioteca time para usar a função sleep
import time
# Criando um loop infinito para exibir o menu até que o usuário escolha sair
while True:
    print("\n-- Calculadora --")
    print("\n1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("\nEscolha uma opção de 1 a 5: ")
    if opcao == "1":
        #função eval() para avaliar a expressão inserida pelo usuário e convertê-la em um número
        parcela1 = eval(input("\nInsira a 1° parcela: "))
        parcela2 = eval(input("Insira a 2° parcela: "))
        print(f"{parcela1} + {parcela2} = {parcela1+parcela2}")
        time.sleep(3) #Pausa por 3 segundos

    elif opcao == "2":
        minuendo = eval(input("\nInsira o minuendo: "))
        subtraendo = eval(input("Insira o subtraendo: "))
        print(f"{minuendo} - {subtraendo} = {minuendo-subtraendo}")
        time.sleep(3)

    elif opcao == "3":
        fator1 = eval(input("\nInsira o 1° fator: "))
        fator2 = eval(input("Insira o 2° fator: "))
        print(f"{fator1} x {fator2} = {fator1*fator2}")
        time.sleep(3)

    elif opcao == "4":
        dividendo = eval(input("\nInsira o dividendo: "))
        divisor = eval(input("Insira o divisor: "))
        print(f"{dividendo} / {divisor} = {dividendo/divisor}")
        time.sleep(3)

    elif opcao == "5":
        print("\nSaindo...")
        break # Quebra o loop infinito para sair do programa
    else:
        print("\nOpção inválida!")
        time.sleep(2)
print("Até logo!")