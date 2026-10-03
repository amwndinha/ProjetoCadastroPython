import json

# Persistência de dados com JSON
def carregar_usuarios(): # Cria uma função para carregar os usúarios.
    try: # python, tente executar esse código.
        with open("usuarios.json", "r") as arquivo: # Abra o arquivo usuarios.json para leitura "r" e chame o arquivo de arquivo.
            return json.load(arquivo) # json.load() pega o conteúdo do arquivo JSON e transforma novamente em um objeto Python.
    except FileNotFoundError: # Se o arquivo usuarios.json não existir, faça o que está aqui.
        return [] # Se o arquivo não existir, a função retorna uma lista vazia.

def salvar_usuarios(): # criar uma função para salvar os dados do usúario em json.
    with open("usuarios.json", "w") as arquivo: # Abra o arquivo usuarios.json para escrita "w" e chame esse arquivo de arquivo.
        json.dump(usuarios, arquivo, indent=4) # Pegue a lista usuarios e salve dentro desse arquivo em formato JSON, deixando tudo organizado com 4 espaços.

usuarios = carregar_usuarios()

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
        # Cadastro de Usuarios
        print("\n------ CADASTRAR USÚARIOS ------")
        while True:
            nome = input("Digite o nome: ").strip() #o .strip remove espaços desnecessários.
            if nome:
                break
            print("o nome não pode ficar vazio!")

        while True: 
            try:
                idade = int(input("Digite a idade: "))
                if idade < 0:
                    print("A idade precisa ser válida!")
                else: 
                    break
            except ValueError:
                print("Digite uma idade válida!")
        
        while True:
            email = input("Digite o email: ").strip()
            if "@" in email:
                break
            print("Digite um email válido.")
        
        while True:
            telefone = input("Digite o telefone: ").strip()
            if telefone:
                break
            print("O telefone não pode ficar vazio.")

        usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "telefone": telefone
        }

        usuarios.append(usuario)
        salvar_usuarios()
        print("Usuário cadastrado com sucesso!")
        print("--------------------------------")

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
        print("\n------ BUSCAR USÚARIO ------")
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

    # Atualização de usúarios
    elif opcao == "4":
        print("\n------ ATUALIZAR USÚARIO ------") 
        nome_usuario = input("Digite o nome do usúario que deseja atualizar: ")
        encontrado = False

        for usuario in usuarios:
            if usuario["nome"] == nome_usuario:
                  novo_nome = input("Digite o novo nome: ").strip()
                  
                  while True:
                        try:
                            nova_idade = int(input("Digite a nova idade: "))

                            if nova_idade < 0:
                                print("A idade não pode ser negativa.")
                            else:
                                break

                        except ValueError:
                            print("Digite uma idade válida.")
                  
                  novo_email = input("Digite o novo email: ").strip()
                  while "@" not in novo_email:
                        print("Digite um email válido.")
                        novo_email = input("Digite o novo email: ").strip()
                  
                  novo_telefone = input("Digite o novo telefone: ").strip() 

                  usuario["nome"] = novo_nome
                  usuario["idade"] = nova_idade
                  usuario["email"] = novo_email
                  usuario["telefone"] = novo_telefone

                  salvar_usuarios()      
                  encontrado = True

                  print("Usúario atualizado com sucesso!")
                  print("-------------------------------")

        if not encontrado:
            print("Usúario não encontrado!")
            print("-------------------------------")

    # Exclusão de usúario
    elif opcao == "5":
        print("\n------ EXCLUIR USÚARIO ------")
        nome_usuario = input("Digite o nome do usúario que deseja excluir: ")
        encontrado = False

        for usuario in usuarios:
            if usuario["nome"] == nome_usuario:
                usuarios.remove(usuario)
                salvar_usuarios()

                encontrado = True

                print("usúario excluído com sucesso!")
                print("-----------------------------")
                break

        if not encontrado:
            print("Usúario não encontrado.")
            print("-----------------------------")

    # Opção sair
    elif opcao == "6":
        print("\nPrograma Encerrado!")
        break
    else: 
        print("\nOpção Inválida")
