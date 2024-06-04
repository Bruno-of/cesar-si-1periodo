import os, json
from time import sleep
from utils import limpar_tela

def menu_adocao():
    from main import menu_inicial
    print("*** Menu Adote Já ***\n")
    print("[1] - Adotar um pet")
    print("[0] - Voltar ao menu inicial")

    try:
        opcao = int(input("\n\n> Informe a opção desejada: "))
        limpar_tela()
        match opcao:
            case 1:
                adotar_pets()
                pass
            case 0:
                menu_inicial()
            case _:
                limpar_tela()
                print(">>> Opção fora do range do menu!!! Tente novamente <<<\n")
                sleep(2)
                menu_adocao()
                   

    except ValueError:
        limpar_tela()
        print(">>> Opção inválida!!! Digite um número inteiro. <<<\n")
        sleep(2)
        menu_adocao()



def adotar_pets():
    print("*** Adotar PETS ***")

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

    opcao_adocao = input(
        "\nDigite o ID do PET que deseja adotar ou aperte [0] para voltar ao menu de adoção: ").title()

    if opcao_adocao == '0':
        menu_adocao()

    if opcao_adocao in pets:
        pet = pets[opcao_adocao]

        print(f"\n# Dados do PET {opcao_adocao} #")
        print(f"- Nome: {pet['Nome']}")
        print(f"- Espécie: {pet['Espécie']}")
        print(f"- CEP onde o pet reside: {pet['CEP_onde_reside']}")
        print(f"- Raça: {pet['Raça']}")
        print(f"- Sexo: {pet['Sexo']}")
        print(f"- Idade: {pet['Idade']}")
        print(f"- Porte: {pet['Porte']}")
        print(f"- Cor: {pet['Cor']}")
        print(f"- Peso: {pet['Peso']}")
        print(f"- Castrado: {pet['Castrado']}")
        print(f"- Vacinado: {pet['Vacinado']}")
        print(f"- Vermifugado: {pet['Vermifugado']}")

        opcao = input("\n> Deseja adotar este pet? [S/N] ").lower()

        if opcao == 's':
            limpar_tela()
            print(f"\nPet '{opcao_adocao}' adotado com sucesso!")
            print("Voltando ao menu de adoção...\n")
            sleep(3)
            menu_adocao()
        elif opcao == 'n':
            limpar_tela()
            print("Pet não adotado. Voltando ao menu de adoção...")
            sleep(3)
            menu_adocao()
        else:
            limpar_tela()
            print("\nOpção inválida. Tente novamente.")
            sleep(3)
            adotar_pets()

    else:
        limpar_tela()
        print(f"\nPET de ID '{opcao_adocao}' não encontrado.")
        print("Tente novamente.\n")
        sleep(3)
        menu_adocao()
