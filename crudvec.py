def visualizar_dadosvec(dadosvec):
    if not dadosvec:
        print("Nenhum dado disponível.")
    else:
        for i, registro in enumerate(dadosvec, 1):
            print(f"Registro {i}: {registro}")


def inserir_dadosvec(dadosvec):
    try:
        Modelo = input("Digite o modelo: ")
        Marca = input("Digite a marca: ")
        Ano = int(input("Digite o ano do veiculo: "))
        Altura = input("Digite a altura do veiculo: ")
        Largura = input("Digite a largura do veiculo: ")
        Comprimento = input("Digite o Comrimento do veiculo: ")
        Peso = input("Digite o peso do veiculo: ")


        novo_registro = {"Modelo": Modelo, "Marca": Marca, "Ano": Ano, "Altura": Altura, "Largura": Largura, "Comprimento": Comprimento, "Peso": Peso}
        dadosvec.append(novo_registro)
        print("dadosvec inseridos com sucesso.")
    except ValueError:
        print("Erro: Idade deve ser um número inteiro válido.")


def atualizar_dadosvec(dadosvec):
    visualizar_dadosvec(dadosvec)
    try:
        indice = int(input("Digite o número do registro que deseja atualizar: ")) - 1
        if 0 <= indice < len(dadosvec):
            Modelo = input("Digite o modelo: ")
            Marca = input("Digite a marca: ")
            Ano = int(input("Digite o ano do veiculo: "))
            Altura = input("Digite a altura do veiculo: ")
            Largura = input("Digite a largura do veiculo: ")
            Comprimento = input("Digite o Comrimento do veiculo: ")
            Peso = input("Digite o peso do veiculo: ")

            dadosvec[indice]["Modelo"] = Modelo
            dadosvec[indice]["Marca"] = Marca
            dadosvec[indice]["Ano"] = Ano
            dadosvec[indice]["Altura"] = Altura
            dadosvec[indice]["largura"] = Largura
            dadosvec[indice]["Comprimento"] = Comprimento
            dadosvec[indice]["Peso"] = Peso
       
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
