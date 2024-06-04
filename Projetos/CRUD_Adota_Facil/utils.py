import os, platform, json


def limpar_tela():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')



def carregar_pessoa_fisica():
    try:
        with open('cadastro_pessoa_fisica.json', 'r',encoding='utf-8') as arquivo:
            pessoas_fisicas = json.load(arquivo)
    except FileNotFoundError:
        pessoas_fisicas = {}

    return pessoas_fisicas



def carregar_ong():
    try:
        with open('cadastro_ong.json', 'r', encoding='utf-8') as arquivo:
            ongs = json.load(arquivo)
    except FileNotFoundError:
        ongs = {}

    return ongs



def carregar_pet():
    try:
        with open('cadastro_pet.json', 'r', encoding='utf-8') as arquivo:
            pets = json.load(arquivo)
    except FileNotFoundError:
        pets = {}

    return pets



def salvar_pessoa_fisica(pessoas_fisicas):
    with open('cadastro_pessoa_fisica.json', 'w', encoding='utf-8') as arquivo:
        json.dump(pessoas_fisicas, arquivo, indent=4, ensure_ascii=False)



def salvar_ong(ongs):
    with open('cadastro_ong.json', 'w', encoding='utf-8') as arquivo:
        json.dump(ongs, arquivo, indent=4, ensure_ascii=False)



def salvar_pet(pets):
    with open('cadastro_pet.json', 'w', encoding='utf-8') as arquivo:
        json.dump(pets, arquivo, indent=4, ensure_ascii=False)



def validar_email(email):
    for letra in email:
      if letra == '@':
          return True
    return False
