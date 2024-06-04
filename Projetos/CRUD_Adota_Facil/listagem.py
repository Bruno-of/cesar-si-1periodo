import os, json
from time import sleep
from utils import limpar_tela


def menu_listagem():

    from cruds import menu_crud
    limpar_tela()

    print("*** Menu de Listagem ***\n")
    print("[1] - Listagem de Pessoa Física")
    print("[2] - Listagem de ONG")
    print("[3] - Listagem de Pets")
    print("\n[0] - Voltar ao Menu de CRUD")

    try:
        opcao = int(input("\n\n> Informe a opção desejada: "))
        limpar_tela()

        match opcao:
            case 1:
                listar_pessoa_fisica()
            case 2:
                listar_ong()
            case 3:
                listar_pets()
            case 0:
                menu_crud()
            case _:
                limpar_tela()
                print(
                    ">>> Opção fora do range do menu!!! Tente novamente <<<\n")
                sleep(2)
                menu_listagem()

    except ValueError:
        print("Opção inválida. Digite um número inteiro.")
        menu_listagem()



def listar_pessoa_fisica():
    from cruds import menu_crud
    limpar_tela()
    print("*** Listar Pessoas ***")

    try:
        with open('cadastro_pessoa_fisica.json', 'r', encoding='utf-8') as arquivo:
            pessoas_fisicas = json.load(arquivo)
    except FileNotFoundError:
        pessoas_fisicas = {}

    if pessoas_fisicas:
        print("\nPessoas Cadastradas:")
        for cpf in pessoas_fisicas:
            print(f"Identificação da pessoa (CPF)- {cpf}")
    else:
        print("\nNenhuma pessoa cadastrada.")

    consulta_pessoa = input(
        "\n> Digite o CPF da pessoa que deseja consultar ou aperte [0] para voltar ao menu de listagem: "
    )

    if consulta_pessoa == '0':
        menu_listagem()

    if consulta_pessoa in pessoas_fisicas:
        pessoa = pessoas_fisicas[consulta_pessoa]

        print(f"\n# Dados da pessoa de CPF '{consulta_pessoa}' #")
        print(f"- Nome: {pessoa['Nome']}")
        print(f"- CPF: {pessoa['CPF']}")
        print(f"- E-mail: {pessoa['E-mail']}")
        print(f"- Senha: {pessoa['Senha']}")
        print(f"- Idade: {pessoa['Idade']}")
        print(f"- Endereço: {pessoa['Endereço']}")
        print(f"- Cidade: {pessoa['Cidade']}")
        print(f"- Estado: {pessoa['Estado']}")
        print(f"- Cadastrou um Pet?: {pessoa['Cadastrou_Pet']}")

        opcao = input("\n> Deseja consultar mais uma Pessoa? [S/N] ").lower()

        if opcao == 's':
            limpar_tela()
            print("Fazendo mais uma consulta...")
            sleep(3)
            listar_pessoa_fisica()
        elif opcao == 'n':
            limpar_tela()
            print("Ok. Voltando ao menu de CRUD...")
            sleep(3)
            limpar_tela()
            menu_crud()
        else:
            limpar_tela()
            print("Opção inválida. Digite apenas [S] ou [N].\n")
            print("Voltando à listagem de pessoas...\n")
            sleep(3)
            listar_pessoa_fisica()
    else:
        limpar_tela()
        print(f"Pessoa de CPF '{consulta_pessoa}' não encontrada.\n")
        print("Tente novamente.\n")
        sleep(3)
        listar_pessoa_fisica()



def listar_ong():

    from cruds import menu_crud
    limpar_tela()

    print("*** Listar ONGs ***")

    try:
        with open('cadastro_ong.json', 'r', encoding='utf-8') as arquivo:
            ongs = json.load(arquivo)
    except FileNotFoundError:
        ongs = {}

    if ongs:
        print("\nONGs Cadastradas:")
        for cnpj in ongs:
            print(f"CNPJ da ONG - {cnpj}")
    else:
        print("\nNenhuma ONG cadastrada.")

    consulta_ong = input(
        "\n> Digite o CNPJ da ONG que deseja consultar ou aperte [0] para voltar ao menu de listagem: "
    )

    if consulta_ong == '0':
        menu_listagem()

    if consulta_ong in ongs:
        ong = ongs[consulta_ong]

        print(f"\n# Dados da ONG '{consulta_ong}' #")
        print(f"- Nome: {ong['Nome']}")
        print(f"- CNPJ: {ong['CNPJ']}")
        print(f"- E-mail: {ong['E-mail']}")
        print(f"- Senha: {ong['Senha']}")
        print(f"- Endereço: {ong['Endereço']}")
        print(f"- Cidade: {ong['Cidade']}")
        print(f"- Estado: {ong['Estado']}")
        print(f"- Instagram: https://www.instagram.com/{ong['Instagram']}")
        print(f"- Cadastrou um Pet?: {ong['Cadastrou_Pet']}")

        opcao = input("\n> Deseja consultar mais uma ONG? [S/N] ").lower()
        if opcao == 's':
            limpar_tela()
            print("Fazendo mais uma consulta...")
            sleep(3)
            listar_ong()
        elif opcao == 'n':
            limpar_tela()
            print("Ok. Voltando ao menu de CRUD...")
            sleep(3)
            limpar_tela()
            menu_crud()
        else:
            limpar_tela()
            print("Opção inválida. Digite apenas [S] ou [N].\n")
            print("Voltando à listagem de ong...\n")
            sleep(3)
            listar_ong()
    else:
        limpar_tela()
        print(f"\nONG de CNPJ '{consulta_ong}' não encontrada.")
        print("Tente novamente.\n")
        sleep(3)
        listar_ong()


def listar_pets():
    
    from cruds import menu_crud
    print("*** Listar PETS ***")

    try:
        with open('cadastro_pet.json', 'r', encoding='utf-8') as arquivo:
            pets = json.load(arquivo)
    except FileNotFoundError:
        pets = {}

    if pets:
        print("\nPETS Cadastrados:")
        for id in pets:
            print(f"ID do PET - {id}")
    else:
        print("\nNenhum PET cadastrado.")

    consulta_pet = input(
        "\nDigite o ID do PET que deseja consultar ou aperte [0] para voltar ao menu de listagem: "
    ).title()

    if consulta_pet == '0':
        menu_listagem()

    if consulta_pet in pets:
        pet = pets[consulta_pet]

        print(f"\n# Dados do PET {consulta_pet} #")
        print(f"- Nome: {pet['Nome']}")
        print(f"- Espécie: {pet['Espécie']}")
        print(f"- CEP onde reside: {pet['CEP_onde_reside']}")
        print(f"- Raça: {pet['Raça']}")
        print(f"- Sexo: {pet['Sexo']}")
        print(f"- Idade: {pet['Idade']}")
        print(f"- Porte: {pet['Porte']}")
        print(f"- Cor: {pet['Cor']}")
        print(f"- Peso: {pet['Peso']}")
        print(f"- Castrado: {pet['Castrado']}")
        print(f"- Vacinado: {pet['Vacinado']}")
        print(f"- Vermifugado: {pet['Vermifugado']}")

        opcao = input("\n> Deseja consultar mais um PET? [S/N] ").lower()
        if opcao == 's':
            limpar_tela()
            print("Fazendo mais uma consulta...\n")
            sleep(3)
            listar_pets()
        elif opcao == 'n':
            limpar_tela()
            print("Ok. Voltando ao menu de CRUD...\n")
            sleep(3)
            limpar_tela()
            menu_crud()
        else:
            limpar_tela()
            print("Opção inválida. Digite apenas [S] ou [N].\n")
            print("Voltando à listagem de pets...\n")
            sleep(3)
            listar_pets()
    else:
        limpar_tela()
        print(f"\nPET de ID '{consulta_pet}' não encontrado.")
        print("Tente novamente.")
        sleep(3)
        listar_pets()
