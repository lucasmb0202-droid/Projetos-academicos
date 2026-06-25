# Sistema de notas para o curso de Análise e Desenvolvimento de Sistemas (ADS)
curso = input("Qual é o seu curso? ").lower().strip()
if "ads" not in curso:
    resposta = input("Curso diferente de ADS, deseja prosseguir? (s/n) ").lower().strip()
    if resposta != 's':
        print("Encerrando o programa. Até mais!")
        exit()
else:
    print("Bem-vindo(a) ao curso de Análise e Desenvolvimento de Sistemas!")

# Entrada das notas
np1 = float(input("Digite a nota da NP1: "))
np2 = float(input("Digite a nota da NP2: "))
pim = float(input("Digite a nota do PIM: "))

# Média semestral
ms = (4 * np1 + 4 * np2 + 2 * pim) / 10
print(f"\nSua média semestral é: {ms:.2f}")

# Verificação da situação
if ms >= 7:
    print("Aprovado(a) sem exame!")
elif ms < 6.5:
    print("Exame necessário.")
    nota_exame = float(input("Digite a nota do exame: "))
    media_final = (ms + nota_exame) / 2

    print(f"Sua média final é: {media_final:.2f}")
    if media_final >= 5:
        print("Aprovado(a) após exame!")
    else:
        print("Reprovado(a).")
else:
    print("Situação intermediária (média entre 6,5 e 6,9).")
    print("Verifique o regulamento da instituição para este caso.")