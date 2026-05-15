from dados import *

usuario = ''
email = ''
senha = ''
cidade = ''
estado = ''

def escolher_opção():

    global usuario
    global email
    global senha
    global cidade
    global estado

    print('=====| ESCOLHA UMA FUNÇÃO |=====')
    print('===== - 1 PARA CADASTRAR CHAMADO - =====')
    print('===== - 2 PARA LOGIN - =====')
    print('===== - 3 PARA BUSCAR CHMADO - =====')
    print('===== - 4 PARA LISTAR CHAMADO - =====')
    print('===== - 5 PARA ATULIZAR STATUS - =====')
    print('===== - 6 PARA FINALIZAR CHAMADO - =====')
    print('===== - 7 PARA STATUS GERAL - =====')
    print('===== - 0 PARA SAIR - =====')

    opção = input('| Digite sua opção |\n')

    if opção == '1':

        print('| ESCREVA SEUS DADOS ABAIXO! |\n')

        usuario = cadastrar_usuario()
        email = cadastrar_email()
        senha = cadastrar_senha()
        cidade = cadastrar_cidade()
        estado = cadastrar_estado()

        print('===== DADOS CADASTRADOS =====')

    elif opção == '2':

        print('DIGITE SEUS DADOS CADASTRADOS!')

        usuario_login = input('Digite seu usuario\n')
        email_login = input('Digite seu email\n')
        senha_login = input('Digite sua senha\n')

        if (
            usuario_login == usuario and
            email_login == email and
            senha_login == senha
        ):

            print('Login realizado com sucesso!')

        else:

            print('Dados inseridos incorretamente!')

    elif opção == '3':
        buscar_nome = input('Digite seu nome\n')
        buscar_email = input('Digite seu email\n')
        buscar_cidade = input('Digite seu cidade\n')
        buscar_estado = input('Digite seu estado\n')
        buscar_senha = input('Digite sua senha\n')

        if (
            buscar_nome == usuario and buscar_email == email and buscar_cidade == cidade and buscar_estado == estado and buscar_senha == senha
        ):
            print('Chamado realizado!')
        else:
            print('Chamado nao realizado!')

    else:

        print('SUA ESCOLHA FOI INVÁLIDA!')


escolher_opção()