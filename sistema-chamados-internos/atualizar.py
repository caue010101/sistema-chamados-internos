import json
chamados = []

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