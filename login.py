def confirmar_senha(senha, confirmacao_senha):
    while senha != confirmacao_senha:
        print('senhas não conferem')
        senha = input('Digite a senha novamente: ')
        confirmacao_senha = input('Confirme a senha: ')
    return senha

while True:
    print('Escolha uma opção:')
    print('1) Login')
    print('2) Cadastro')
    print('3) Sair')
    opcao = int(input('> '))

    if(opcao == 1):
        print('opcao de login')
    
    elif(opcao == 2):
        usuario = input('Digite o nome de usuário: ')
        senha = input('Digite a senha: ')
        confirmacao_senha = input('Confirme a senha: ')
        senha = confirmar_senha(senha, confirmacao_senha)
        
    elif(opcao == 3):
        print('bye')
        break
    else: print('opção inválida, tente novamente')