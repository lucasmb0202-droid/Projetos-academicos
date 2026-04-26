usuario_correto = "admin"
senha_correta = "senha1234"
# lower() converte a string para minúscula
# strip() remove espaços em branco no início e no final da string
# while True continuará solicitando as credenciais até que o login seja bem-sucedido
while True:
    usuario_input = input("Digite o nome de usuário: ").lower().strip()
    senha_input = input("Digite a senha: ").lower().strip()

    if usuario_input == usuario_correto and senha_input == senha_correta:
        print("Login bem-sucedido!")
        break
    elif usuario_input != usuario_correto: #elif para verificar se o nome de usuário está incorreto
        print("Usuário inválido.")
    else:
        print("Senha incorreta.")