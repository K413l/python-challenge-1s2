import crud
import crudvec

def main():
    # Inicialize a lista de dicionários vazia para armazenar os dados
    dados = []
    dadosvec = []

    while True:
        print("\nMenu Principal:")
        print("1. Visualizar Dados")
        print("2. Inserir Dados")
        print("3. Atualizar Dados")
        print("4. Excluir Dados")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            crud.visualizar_dados(dados)
        elif escolha == "2":
            crud.inserir_dados(dados)
        elif escolha == "3":
            crud.atualizar_dados(dados)
        elif escolha == "4":
            crud.excluir_dados(dados)
        elif escolha == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")





main()
