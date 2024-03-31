
while True:
    print('Escolha uma opção:')
    print('1) Login')
    print('2) Cadastro ')
    print('3) Sair ')
    opcao = int(input())

    if(opcao == 1):
        print('opcao de login')
    elif(opcao == 2):
        print('opcao de cadastro')
    elif(opcao == 3):
        print('bye')
        break
    else: print('opção inválida, tente novamente')