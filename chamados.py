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
    pass


def atualizar_chamado():
    pass


def finalizar_chamado():
    pass


def relatorio_geral():
    pass


def relatorio_geral():
    pass
