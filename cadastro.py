usuarios = []

while(True): 
    print("\n------ Sistema de Cadastro ------")
    print("---------------------------------")
    print("1 - Cadastrar usúario")
    print("2 - Listar usúario")
    print("3 - Buscar usúario")
    print("4 - Atualizar usúario")
    print("5 - Excluir usúario")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o email: ")
        telefone = input("Digite o telefone: ")

        usuario = {
        "\nnome": nome,
        "\nidade": idade,
        "\nemail": email,
        "\ntelefone": telefone
        }

        usuarios.append(usuario)
        print("\nUsuário cadastrado com sucesso!")

    elif opcao == "2": 
        print("\nLista de usúarios")
    elif opcao == "3":
        print("\nBuscar usúario")
    elif opcao == "4":
        print("\nAtualizar usúario") 
    elif opcao == "5":
        print("\nExcluir usúario")
    elif opcao == "6":
        print("\nPrograma Encerrado!")
        break
    else: 
        print("\nOpção Inválida")

print(usuarios)
