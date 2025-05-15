from database import Database

db = Database()

def menu():
    while True:
        print("\n=== SISTEMA NEOPEOPLE ===")
        print("1 - Cadastrar pessoa")
        print("2 - Listar pessoas")
        print("3 - Atualizar nome")
        print("4 - Remover pessoa")
        print("0 - Sair")

        opcao = input("Digite a opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = input("Idade: ")
            db.create_person(nome, int(idade))
            print(f"{nome} foi cadastrado(a) com sucesso.")
        elif opcao == "2":
            pessoas = db.list_people()
            if pessoas:
                print("\n-- Lista de Pessoas --")
                for pessoa in pessoas:
                    print(f"{pessoa['name']} - {pessoa['age']} anos")
            else:
                print("Nenhuma pessoa cadastrada.")
        elif opcao == "3":
            atual = input("Nome atual: ")
            novo = input("Novo nome: ")
            db.update_person(atual, novo)
            print("Nome atualizado com sucesso.")
        elif opcao == "4":
            nome = input("Nome da pessoa para remover: ")
            db.delete_person(nome)
            print("Pessoa removida com sucesso.")
        elif opcao == "0":
            print("Encerrando sistema...")
            db.close()
            break
        else:
            print("Opção inválida!")

menu()
