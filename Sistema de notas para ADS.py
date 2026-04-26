# Sistema de notas para o curso de Análise e Desenvolvimento de Sistemas (ADS)
curso = input("Qual é o seu curso? ").lower().strip()
if "ads" not in curso:
    resposta = input("Curso diferente de ADS, deseja prosseguir? (s/n) ").lower().strip()
    if resposta != 's':
        print("Encerrando o programa. Até mais!")
        exit()
else:
    print("Bem-vindo(a) ao curso de Análise e Desenvolvimento de Sistemas!")

np1 = float(input("Digite a nota da NP1: "))
np2 = float(input("Digite a nota da NP2: "))
pim = float(input("Digite a nota do PIM: "))
ms = (4*np1 + 4*np2 + 2*pim) / 10
print(f"Sua média do semestre é: {ms:.2f}")
if ms >= 7:
    print("Aprovado(a)")
else:
    print("Você vai precisar fazer exame")
# Cálculo da nota necessária no exame para atingir média 7
    exame_necessario = 14 - ms
    
    if exame_necessario > 10:
        print("Mesmo tirando 10 no exame, não será possível atingir média 7.")
    else:
        print(f"Você precisa tirar pelo menos {exame_necessario:.2f} no exame.")

        nota_exame = float(input("Digite a nota do exame: "))
        media_final = (ms + nota_exame) / 2

        print(f"Sua média final é: {media_final:.2f}")

        if media_final >= 7:
            print("Aprovado(a) após exame!")
        else:
            print("Reprovado(a).")