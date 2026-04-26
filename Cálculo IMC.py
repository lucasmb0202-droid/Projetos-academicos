peso = float(input("Digite seu peso, em kg: "))
altura = float(input("Digite sua altura, em m: "))

imc = peso / altura**2
print(f"\nSeu IMC é: {imc:.2f}")
# Classificação do IMC
if imc<18.5:
    print("Você está abaixo do peso.")
elif imc<25:
    print("Você está com o peso normal.")
elif imc<30:
    print("Você está com sobrepeso.")
elif imc<35:
    print("Você está com obesidade grau 1.")
elif imc<40:
    print("Você está com obesidade grau 2.")
else:
    print("Você está com obesidade grau 3.")