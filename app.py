import crud
import crudvec

def main():
    dados = []
    dadosvec = []
    case = str(input("Deseja visualizar pessoas(P) ou veiculos(V)? V/P"))
    if case == "P":
        while True:
            print("\nMenu Principal Pessoas:")
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
    else:
        while True:
            print("\nMenu Principal Veiculos:")
            print("1. Visualizar Dados")
            print("2. Inserir Dados")
            print("3. Atualizar Dados")
            print("4. Excluir Dados")
            print("5. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                crudvec.visualizar_dadosvec(dadosvec)
            elif escolha == "2":
                crudvec.inserir_dadosvec(dadosvec)
            elif escolha == "3":
                crudvec.atualizar_dadosvec(dadosvec)
            elif escolha == "4":
                crudvec.excluir_dadosvec(dadosvec)
            elif escolha == "5":
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")



main()
