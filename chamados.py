import json
from datetime import date
chamados = []

def cadastrar_chamado():
    nome = input("Digite seu nome: ")
    turma = input("Digite seu setor/turma: ")
    problema = input("Digite o tipo do problema ")
    descricao_problema = input("Descreva seu problema ")
    prioridade = input("Qual seria a prioridade do seu problema (baixa, media, alta) ")

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
        "prioridade": prioridade,
        "solucao": ""
    }

    chamados.append(novo_chamado)

    with open('data/chamados.json', 'w') as f:
        json.dump(chamados, f, indent=2, ensure_ascii=False)
    print(f'Chamado protocolo {protocolo} cadastrado com sucesso')


def listar_chamado():
    pass


def buscar_chamado():
    with open('data/chamados.json', 'r') as f:
        chamados = json.load(f)

    selecionar_opcao = input(
        'Selecione a forma de busca\n'
        '1 para buscar via protocolo\n'
        '2 para buscar via nome\n'
        '3 para buscar via turma\n'
    )

    if selecionar_opcao == '1':
        digitar_protocolo = input('Digite o protocolo do chamado\n')
        encontrado = False
        for chamado in chamados:
            if chamado['protocolo'] == digitar_protocolo:
                print(chamado)
                encontrado = True
        if not encontrado:
            print('Protocolo não encontrado')

    elif selecionar_opcao == '2':
        digitar_nome = input('Digite o nome\n')
        encontrado = False
        for chamado in chamados:
            if chamado['nome'] == digitar_nome:
                print(chamado)
                encontrado = True
        if not encontrado:
            print('Nome não encontrado')

    elif selecionar_opcao == '3':
        digitar_turma = input('Digite a turma\n')
        encontrado = False
        for chamado in chamados:
            if chamado['turma'] == digitar_turma:
                print(chamado)
                encontrado = True
        if not encontrado:  # ✅ corrigido: era else do for
            print('Turma não encontrada')


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
            json.dump(chamados, f, indent=2, ensure_ascii=False)  # ✅ corrigido: era chamado
        print('Chamado atualizado com sucesso')
    else:
        print('Chamado não encontrado')


def finalizar_chamado():
    with open("data/chamados.json", "r") as f:
        chamados = json.load(f)

    protocolo = input("Digite seu protocolo: ")
    solucao = input("Digite a solucao do problema: ")
    encontrado = False

    for chamado in chamados:
        if chamado['protocolo'] == protocolo:
            chamado['status'] = 'resolvido'
            chamado['solucao'] = solucao
            encontrado = True
            break

    if encontrado:
        with open('data/chamados.json', 'w') as f:
            json.dump(chamados, f, indent=2, ensure_ascii=False)
        print(f"Solucao registrada: {solucao}")
    else:
        print("Protocolo não encontrado")


            encontrado = True

            break
    if encontrado:
        with open('data/chamados.json', 'w') as f:
            json.dump(chamado, f, indent=2, ensure_ascii=False)

        print('Chamado realizado com sucesso')
    else:
        print('Chamdado não encontrado')


def finalizar_chamado():

    with open("data/chamados.json", "r") as f:
        chamados = json.load(f)

    protocolo = input("Digite seu protocolo: ")
    solucao = input("Digite a solucao do problema: ")
    encontrado = False

    for chamado in chamados:
        if (chamado['protocolo'] == protocolo):
            chamado['status'] = 'resolvido'
            chamado['solucao'] = solucao

            encontrado = True
            break
    if encontrado:
        with open('data/chamados.json', 'w') as f:
            json.dump(chamados, f, indent=2, ensure_ascii=False)
        print(f"Solucao registrada: {solucao} ")
    else:
        print("protocolo nao encontrado")



def relatorio_geral():
    with open('data/chamados.json', 'r') as f:
        chamados = json.load(f)

    tipo_relatorio = input('Qual tipo de relatorio?\n1 por status\n2 por urgencia\n')
    quantidade_aberto = 0
    quantidade_fechado = 0
    quantidade_em_andamento = 0

    if tipo_relatorio == '1':
        chamados_aef = input('Escolha o status\nAberto(1)\nEm andamento(2)\nFechado(3)\nGeral(4)\n')

        if chamados_aef == '1':
            for chamado in chamados:
                if chamado['status'] == 'aberto':  # ✅ minúsculo
                    quantidade_aberto += 1
            print('Chamados Abertos:', quantidade_aberto)

        elif chamados_aef == '2':
            for chamado in chamados:
                if chamado['status'] == 'em andamento':  # ✅ minúsculo
                    quantidade_em_andamento += 1
            print('Chamados Em andamento:', quantidade_em_andamento)

        elif chamados_aef == '3':
            for chamado in chamados:
                if chamado['status'] == 'resolvido':  # ✅ minúsculo
                    quantidade_fechado += 1
            print('Chamados Fechados:', quantidade_fechado)

        elif chamados_aef == '4':
            for chamado in chamados:
                if chamado['status'] == 'aberto':
                    quantidade_aberto += 1
                elif chamado['status'] == 'em andamento':
                    quantidade_em_andamento += 1
                elif chamado['status'] == 'resolvido':
                    quantidade_fechado += 1
            print('Chamados total:', quantidade_aberto + quantidade_fechado + quantidade_em_andamento)

        else:
            print('Opção inválida')

    elif tipo_relatorio == '2':
        prioridade_alta = 0
        for chamado in chamados:
            if chamado.get('prioridade') == 'alta':
                prioridade_alta += 1
        print('Chamados com prioridade alta:', prioridade_alta)

    else:
        print('Relatório inválido')