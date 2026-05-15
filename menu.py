import chamados


def menu():

    while True:

        print("======== SISTEMA DE CHAMADOS =========")

        print("1 - Cadastrar chamado ")
        print("2 - Listar chamados ")
        print("3 - Buscar chamados ")
        print("4 - Atualizar status ")
        print("5 - Finalizar chamado ")
        print("6 - Status geral ")
        print("0 - Sair ")

        opcao = input("Escolha uma das opçoes ")

        if (opcao == "1"):
            chamados.cadastrar_chamado()

        elif (opcao == "2"):
            chamados.listar_chamado()

        elif (opcao == "3"):
            chamados.buscar_chamado()

        elif (opcao == "4"):
            chamados.atualizar_chamado()

        elif (opcao == "5"):
            chamados.finalizar_chamado()

        elif (opcao == "6"):
            chamados.relatorio_geral()

        elif (opcao == "0"):
            print("Encerrando... ")
            break
        else:
            print("Opçao invalida, tente novamente ")
