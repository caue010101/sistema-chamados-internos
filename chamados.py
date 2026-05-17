import json
from datetime import date


def cadastrar_chamado():

    nome = input("Digite seu nome: ")
    turma = input("Digite seu setor/turma: ")
    problema = input("Digite o tipo do problema ")
    descricao_problema = input("Descreva seu problema ")
    prioridade = input(
        "Qual seria a prioridade do seu problema (baixa, media, alta) ")

    with open('data/chamados.json', 'r') as f:
        chamados = json.load(f)
    protocolo = f'CH-{str(len(chamados) + 1).zfill(3)}'

    novo_chamado = {
        "protocolo": protocolo,
        "nome": nome,
        "turma": turma,
        "problema": problema,
        "descricao": descricao_problema,
        "status": "aberto",
        "data_abertura": date.today().isoformat(),
        "solucao": ""
    }

    chamados.append(novo_chamado)

    with open('data/chamados.json', 'w') as f:
        json.dump(chamados, f, indent=2, ensure_ascii=False)
    print(f'Chamado protocolo {protocolo} cadastrado com sucesso ')


def listar_chamado():
    pass


def buscar_chamado():

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


def atualizar_chamado():
        with open("data/chamados.json", "r") as f:
            chamados = json.load(f)

        protocolo = input('Digite o protocolo\n')
        novo_status = input('Novo Status:\n')

        encontrado = False

        for chamado in chamados:
            if chamado['protocolo'] == protocolo:
                chamado['status'] = novo_status

                encontrado = True

                break
        if encontrado:
            with open('data/chamados.json', 'w') as f:
                json.dump(chamados, f, indent=2, ensure_ascii=False)

            print('Chamado realizado com sucesso')
        else:
            print('Chamdado não encontrado')


def finalizar_chamado():
    pass


def relatorio_geral():
    pass


def relatorio_geral():
    pass
