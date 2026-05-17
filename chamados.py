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
    pass


def finalizar_chamado():
    pass


def relatorio_geral():
    with open('data/chamados.json', 'r') as f:
        chamados = json.load(f)

        tipo_relatorio = input('Qual tipo de relatorio?\n1 por status\n2 por turma\n3 por urgência\n')


    quantidade_aberto = 0
    quantidade_fechado = 0
    quantidade_em_andamento = 0
    quantidade_turmas = 0

    if tipo_relatorio == '1':
        chamados_aef = input('Escolha o status\nAberto(1)\nEm andamento(2)\nFechado(3)\nGeral(4)\n')

        if chamados_aef == '1':
            for chamado in chamados:
                if chamado['status'] == 'Aberto':
                    quantidade_aberto += 1
            print('Chamados Abertos:', quantidade_aberto)

        elif chamados_aef == '2':
            for chamado in chamados:
                if chamado['status'] == 'Em andamento':
                    quantidade_em_andamento += 1
            print('Chamados Em andamento:', quantidade_em_andamento)

        elif chamados_aef == '3':
            for chamado in chamados:
                if chamado['status'] == 'Finalizado':
                    quantidade_fechado += 1
            print('Chamados Finalizados:', quantidade_fechado)

        elif chamados_aef == '4':
            for chamado in chamados:
                if chamado['status'] == 'Aberto':
                    quantidade_aberto += 1
                elif chamado['status'] == 'Em andamento':
                    quantidade_em_andamento += 1
                elif chamado['status'] == 'Finalizado':
                    quantidade_fechado += 1
            print('RELATORIO DE CHAMADOS')
            print('Quantidade abertos:', quantidade_aberto)
            print('Quantidade Em andamento:', quantidade_em_andamento)
            print('Quantidade fechados:', quantidade_fechado)
            print('Total:', quantidade_aberto + quantidade_em_andamento + quantidade_fechado)

        else:
            print('Relatório Inválido')

    elif tipo_relatorio == '2':
        turma = input('Digite a turma\n')
        for chamado in chamados:
            if chamado['turma'] == turma:
                quantidade_turmas += 1
        print('Total de Chamados na sala:', quantidade_turmas)

    elif tipo_relatorio == '3':
        prioridade = input('Digite a prioridade (Baixa/Media/Alta)\n')
        quantidade_prioridade = 0
        for chamado in chamados:
            if chamado.get('prioridade') == prioridade:
                quantidade_prioridade += 1
        print(f'Total de chamados com prioridade {prioridade}:', quantidade_prioridade)

