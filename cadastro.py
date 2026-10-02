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
    
    # Cadastro de Usuarios
    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o email: ")
        telefone = input("Digite o telefone: ")

        usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "telefone": telefone
        }

        usuarios.append(usuario)
        print("\nUsuário cadastrado com sucesso!")

    # Lista de Usuarios  
    elif opcao == "2": 
        if len(usuarios) == 0:
            print("Nenhum usúario cadastrado.")
        else: 
            print("\n------ USÚARIOS CADASTRADOS ------")
    
            for usuario in usuarios:
                print(f"Nome: {usuario["nome"]}")
                print(f"Idade: {usuario["idade"]}")
                print(f"Email: {usuario["email"]}")
                print(f"Telefone: {usuario["telefone"]}")
                print("---------------------------------")
               
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
