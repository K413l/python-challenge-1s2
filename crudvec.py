def visualizar_dadosvec(dadosvec):
    if not dadosvec:
        print("Nenhum dado disponível.")
    else:
        for i, registro in enumerate(dadosvec, 1):
            print(f"Registro {i}: {registro}")


def inserir_dadosvec(dadosvec):
    try:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        novo_registro = {"Nome": nome, "Idade": idade}
        dadosvec.append(novo_registro)
        print("dadosvec inseridos com sucesso.")
    except ValueError:
        print("Erro: Idade deve ser um número inteiro válido.")


def atualizar_dadosvec(dadosvec):
    visualizar_dadosvec(dadosvec)
    try:
        indice = int(input("Digite o número do registro que deseja atualizar: ")) - 1
        if 0 <= indice < len(dadosvec):
            nome = input("Digite o novo nome: ")
            idade = int(input("Digite a nova idade: "))

            dadosvec[indice]["Nome"] = nome
            dadosvec[indice]["Idade"] = idade
            print("dadosvec atualizados com sucesso.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Erro: Idade deve ser um número inteiro válido.")


def excluir_dadosvec(dadosvec):
    visualizar_dadosvec(dadosvec)
    try:
        indice = int(input("Digite o número do registro que deseja excluir: ")) - 1
        if 0 <= indice < len(dadosvec):
            del dadosvec[indice]
            print("Registro excluído com sucesso.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Erro: Índice deve ser um número inteiro válido.")
