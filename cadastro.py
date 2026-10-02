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

    # Listagem de Usuarios  
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

    # Busca de usúarios         
    elif opcao == "3":
        print("------ BUSCAR USÚARIO ------")
        nome_busca = input("Digite o nome do usuário: ")
        encontrado = False

        for usuario in usuarios:
            if usuario["nome"] == nome_busca:
                print("\nUsuário encontrado!")
                print(f"Nome: {usuario['nome']}")
                print(f"Idade: {usuario['idade']}")
                print(f"Email: {usuario['email']}")
                print(f"Telefone: {usuario['telefone']}")
                print("----------------------------")

                encontrado = True

        if not encontrado:
            print("Usuário não encontrado.")
            print("----------------------------")

    elif opcao == "4":
        print("------ ATUALIZAR USÚARIO ------") 
        nome_usuario = input("Digite o nome do usúario que deseja atualizar: ")
        encontrado = False

        for usuario in usuarios:
            if usuario["nome"] == nome_usuario:
                  novo_nome = input("Digite o novo nome: ")
                  nova_idade = int(input("Digite a nova idade: "))
                  novo_email = input("Digite o novo email: ")
                  novo_telefone = input("Digite o novo telefone: ")  

                  usuario["nome"] = novo_nome
                  usuario["idade"] = nova_idade
                  usuario["email"] = novo_email
                  usuario["telefone"] = novo_telefone

        print("Usúario atualizado com sucesso!")
        print("-------------------------------")

        if not encontrado:
            print("Usúario não encontrado!")
            print("-------------------------------")

    elif opcao == "5":
        print("\nExcluir usúario")
    elif opcao == "6":
        print("\nPrograma Encerrado!")
        break
    else: 
        print("\nOpção Inválida")
