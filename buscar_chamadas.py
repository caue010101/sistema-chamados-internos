import json

def procurar_chamado():

    with open('data/chamados.json', 'r') as f:
        chamados = json.load(f)

    selecionar_opção = input(
        'Selecione a forma de busca\n'
        '1 para buscar via protocolo\n'
        '2 para buscar via nome\n'
        '3 para buscar via turma\n'
    )

    if selecionar_opção == '1':

        digitar_protocolo = input('Digite o protocolo do chamado\n')

        encontrado = False

        for chamado in chamados:

            if chamado['protocolo'] == digitar_protocolo:

                print(chamado)

                encontrado = True


        if encontrado == False:

            print('Protocolo digitado incorretamente')

    elif selecionar_opção == '2':
        digitar_nome = input('Digite o nome\n')

        encontrado = False

        for chamado in chamados:
            if chamado['nome'] == digitar_nome:
                print(chamado)
                encontrado = True

        if encontrado == False:
            print('Nome digitado incorretamente')

    elif selecionar_opção == '3':
        digitar_turma = input('Digite a turma\n')
        encontrado = False
        for chamado in chamados:
            if chamado['turma'] == digitar_turma:
                print(chamado)
                encontrado = True
        else:
            print('Turma digitado incorretamente')
