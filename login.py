def cadastrar_usuario(usuario, senha):
    with open("contas.txt", "a") as file:
        file.write(f"{usuario}:{senha}\n")

def confirmar_senha(senha, confirmacao_senha):
    while senha != confirmacao_senha:
        print('senhas não conferem')
        senha = input('Digite a senha novamente: ')
        confirmacao_senha = input('Confirme a senha: ')
    return senha

def confirmar_login(usuario, senha):
    with open("contas.txt", "r") as contas:
        for linha in contas:
            user, passwd = linha.strip().split(":")
            if user == usuario and passwd == senha:
                return True
    return False




while True:
    print('Escolha uma opção:')
    print('1) Login')
    print('2) Cadastro')
    print('3) Sair')
    opcao = int(input('> '))

    if(opcao == 1):
        print('opcao de login')
        usuario = input('Digite o nome de usuário: ')
        senha = input('Digite a senha: ')
        if confirmar_login(usuario, senha): print('login realizado com sucesso!')
        
    elif(opcao == 2):
        usuario = input('Digite o nome de usuário: ')
        senha = input('Digite a senha: ')
        confirmacao_senha = input('Confirme a senha: ')
        
        senha = confirmar_senha(senha, confirmacao_senha)
        cadastrar_usuario(usuario, senha)
        print("usuario cadastrado com sucesso")
        


        
    elif(opcao == 3):
        print('bye')
        break
    else: print('opção inválida, tente novamente')