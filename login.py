
def confirmar_senha(senha, confirmacao_senha):
    if senha != confirmacao_senha:
        print('senhas não conferem')
        senha = input('Digite a senha novamente')
        confirmacao_senha = input('Confirme a senha')
        confirmar_senha(senha, confirmacao_senha)
    return

while True:
    print('Escolha uma opção:')
    print('1) Login')
    print('2) Cadastro ')
    print('3) Sair ')
    opcao = int(input('>'))

    if(opcao == 1):
        usuario = input('Digite o nome de usuário')
        senha = input('Digite a senha')
        confirmacao_senha = input('Confirme a senha')
        confirmar_senha(senha, confirmacao_senha)


    elif(opcao == 2):
        print('opcao de cadastro')
    elif(opcao == 3):
        print('bye')
        break
    else: print('opção inválida, tente novamente')