import os, json
from time import sleep
from utils import limpar_tela
from utils import carregar_pessoa_fisica, salvar_pessoa_fisica
from utils import carregar_ong, salvar_ong
from utils import carregar_pet, salvar_pet
from utils import validar_email


def menu_atualizacao():
  from cruds import menu_crud
  limpar_tela()
  print("*** Menu de Atualização ***\n")

  print("[1] - Atualização de Pessoa Física")
  print("[2] - Atualização de ONG")
  print("[3] - Atualização de Pets")
  print("\n[0] - Voltar ao Menu de CRUD")

  try:
    opcao = int(input("\n\n> Informe a opção desejada: "))
    limpar_tela()

    match opcao:
      case 1:
        atualizacao_pessoa_fisica()
      case 2:
        atualizacao_ong()
      case 3:
        atualizacao_pet()
      case 0:
        menu_crud()
      case _:
        limpar_tela()
        print(">>> Opção fora do range do menu!!! Tente novamente <<<\n")
        sleep(2)
        menu_atualizacao()

  except ValueError:
    limpar_tela()
    print(">>> Opção inválida!!! Valor inserido não compatível! <<<\n")
    sleep(2)
    menu_atualizacao()


def atualizacao_pessoa_fisica():
  from cruds import menu_crud
  limpar_tela()
  print("*** Atualizar Pessoas ***")
  try:
    with open('cadastro_pessoa_fisica.json', 'r', encoding='utf-8') as arquivo:
      pessoas_fisicas = json.load(arquivo)
  except FileNotFoundError:
    pessoas_fisicas = {}

  if pessoas_fisicas:
    print("\nPessoas cadastradas:")
    for cpf in pessoas_fisicas:
      print(f"Identificação da pessoa (CPF)- {cpf}")

  else:
    print("Não há nenhuma pessoa física cadastrada.\n")
    print("Voltando ao menu de Cruds")
    sleep(3)
    limpar_tela()
    menu_crud()

  pessoa_atualizar = input(
      "\n> Digite o CPF da pessoa que deseja atualizar ou aperte [0] para voltar ao menu de atualização: "
  )

  if pessoa_atualizar == '0':
    menu_atualizacao()

  if pessoa_atualizar in pessoas_fisicas:
    usuario = pessoas_fisicas[pessoa_atualizar]
    print(f"\n# Dados da pessoa de CPF '{usuario['CPF']}' #")
    print(f"- Nome: {usuario['Nome']}")
    print(f"- CPF: {usuario['CPF']}")
    print(f"- E-mail: {usuario['E-mail']}")
    print(f"- Senha: {usuario['Senha']}")
    print(f"- Idade: {usuario['Idade']}")
    print(f"- Endereço: {usuario['Endereço']}")
    print(f"- Cidade: {usuario['Cidade']}")
    print(f"- Estado: {usuario['Estado']}")

    novo_nome = input("\n\n> Digite o novo nome: ").title()
    
    novo_cpf = input("> Digite o novo CPF (apenas números): ")
    while len(novo_cpf) != 11:
      print("CPF inválido! Por favor insira novamente, com 11 dígitos.")
      novo_cpf = input("CPF: ")
    
      
    novo_email = input("> Digite o novo e-mail: ")
    while validar_email(novo_email) == False:
      print("E-mail inválido. Tente novamente.")
      novo_email = input("E-mail: ")
       
    nova_senha = input("> Digite a nova senha: ")
    nova_idade = int(input("> Digite a nova idade: "))
    novo_endereco = input("> Digite o novo endereço: ").title()
    nova_cidade = input("> Digite a nova cidade: ").title()
    novo_estado = input("> Digite o novo estado: ").title()

    del pessoas_fisicas[pessoa_atualizar]

    usuario['Nome'] = novo_nome
    usuario['CPF'] = novo_cpf
    usuario['E-mail'] = novo_email
    usuario['Senha'] = nova_senha
    usuario['Idade'] = nova_idade
    usuario['Endereço'] = novo_endereco
    usuario['Cidade'] = nova_cidade
    usuario['Estado'] = novo_estado

    pessoas_fisicas[novo_cpf] = usuario

  else:
    limpar_tela()
    print(f"Pessoa de CPF '{pessoa_atualizar}' não encontrada.\n")
    print("Tente novamente.\n")
    sleep(3)
    atualizacao_pessoa_fisica()

  with open('cadastro_pessoa_fisica.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoas_fisicas, arquivo, indent=4, ensure_ascii=False)

  print("\nPessoa física atualizada com sucesso!")
  print("Voltando ao menu CRUD")
  sleep(3)
  limpar_tela()
  menu_crud()


def atualizacao_ong():
  from cruds import menu_crud
  limpar_tela()
  print("*** Atualizar ONGs ***")
  try:
    with open('cadastro_ong.json', 'r', encoding='utf-8') as arquivo:
      ongs = json.load(arquivo)
  except FileNotFoundError:
    ongs = {}

  if ongs:
    print("\nONGs cadastradas:")
    for cnpj in ongs:
      print(f"CNPJ da ONG - {cnpj}")

  else:
    print("Não há nenhuma ONG cadastrada.\n")
    print("Voltando ao menu de Cruds")
    sleep(3)
    limpar_tela()
    menu_crud()

  ong_atualizar = input(
      "\n> Digite o CNPJ da ONG que deseja atualizar ou aperte [0] para voltar ao menu de atualização: "
  )

  if ong_atualizar == '0':
    menu_atualizacao()

  if ong_atualizar in ongs:
    usuario_ong = ongs[ong_atualizar]
    print(f"\n# Dados da ONG de CNPJ '{usuario_ong['CNPJ']}' #")
    print(f"- Nome: {usuario_ong['Nome']}")
    print(f"- CNPJ: {usuario_ong['CNPJ']}")
    print(f"- E-mail: {usuario_ong['E-mail']}")
    print(f"- Senha: {usuario_ong['Senha']}")
    print(f"- Endereço: {usuario_ong['Endereço']}")
    print(f"- Cidade: {usuario_ong['Cidade']}")
    print(f"- Estado: {usuario_ong['Estado']}")
    print(f"- Instagram: https://www.instagram.com/{usuario_ong['Instagram']}")

    novo_nome = input("\n\n> Digite o novo nome: ").title()
    
    novo_cnpj = input("> Digite o novo CNPJ: ")
    while len(novo_cnpj) != 14:
      print("CNPJ inválido! Por favor insira novamente, com 14 dígitos.")
      novo_cnpj = input("CNPJ: ")

    novo_email = input("> Digite o novo e-mail da ONG: ")
    while validar_email(novo_email) == False:
      print("E-mail inválido. Tente novamente.")
      novo_email = input("E-mail: ")
    
    nova_senha = input("> Digite a nova senha da ONG: ")
    novo_endereco = input("> Digite o novo endereço: ").title()
    nova_cidade = input("> Digite a nova cidade: ").title()
    novo_estado = input("> Digite o novo estado: ").title()
    novo_instagram = input("> Digite o novo Instagram da ONG: ")

    del ongs[ong_atualizar]

    usuario_ong['Nome'] = novo_nome
    usuario_ong['CNPJ'] = novo_cnpj
    usuario_ong['E-mail'] = novo_email
    usuario_ong['Senha'] = nova_senha
    usuario_ong['Endereço'] = novo_endereco
    usuario_ong['Cidade'] = nova_cidade
    usuario_ong['Estado'] = novo_estado
    usuario_ong['Instagram'] = novo_instagram

    ongs[novo_cnpj] = usuario_ong

  else:
    limpar_tela()
    print(f"\nONG de CNPJ '{ong_atualizar}' não encontrada.")
    print("Tente novamente.\n")
    sleep(3)
    atualizacao_ong()

  with open('cadastro_ong.json', 'w', encoding='utf-8') as arquivo:
    json.dump(ongs, arquivo, indent=4, ensure_ascii=False)

  print("\nOng atualizada com sucesso!")
  print("Voltando ao menu CRUD")
  sleep(2)
  limpar_tela()
  menu_crud()




def atualizacao_pet():
  from cruds import menu_crud
  print("*** Atualizar Pets ***")
  try:
    with open('cadastro_pet.json', 'r', encoding='utf-8') as arquivo:
      pets = json.load(arquivo)
  except FileNotFoundError:
    pets = {}

  if pets:
    print("\nPets cadastrados:")
    for nome_pet in pets:
      print(f"Nome do pet - {nome_pet}")

  else:
    print("Não há pets cadastrados.\n")
    print("Voltando ao menu de Cruds")
    sleep(3)
    limpar_tela()
    menu_crud()

  pet_atualizar = input(
      "\n> Digite o nome do PET que deseja atualizar ou aperte [0] para voltar ao menu de atualização: ").title()

  if pet_atualizar == '0':
    menu_atualizacao()

  if pet_atualizar in pets:
  
    print(f"\n# Dados do PET {pet_atualizar} #")
    pet = pets[pet_atualizar]
    print(f"- Nome: {pet['Nome']}")
    print(f"- CEP onde o pet reside: {pet['CEP_onde_reside']}")
    print(f"- Espécie: {pet['Espécie']}")
    print(f"- Raça: {pet['Raça']}")
    print(f"- Sexo: {pet['Sexo']}")
    print(f"- Idade: {pet['Idade']}")
    print(f"- Porte: {pet['Porte']}")
    print(f"- Cor: {pet['Cor']}")
    print(f"- Peso: {pet['Peso']}")
    print(f"- Vermifugado: {pet['Vermifugado']}")
    print(f"- Castrado: {pet['Castrado']}")
    print(f"- Vacinado: {pet['Vacinado']}")
    
    
    
    
    

    novo_nome = input("\n\n> Digite o novo nome: ").title()
    novo_cep = input("> Digite o novo CEP onde o pet reside: ")
    novo_especie = input("> Digite a espécie do pet: ")
    nova_raca = input("> Digite a nova raça: ").title()
    novo_sexo = input("> Digite o sexo do pet: ")
    novo_idade = int(input("> Digite a nova idade: "))
    novo_porte = input("> Digite o novo porte: ")
    novo_cor = input("> Digite a cor do pet: ")
    novo_peso = input("> Digite o peso do pet: ")
    novo_vermifugado = input("> Digite se o pet está vermifugado: ")
    novo_castrado = input("> Digite se o pet está castrado: ")
    novo_vacinado = input("> Digite o pet está vacinado: ")
    
    
    
    del pets[pet_atualizar]

    pet['Nome'] = novo_nome
    pet['Raça'] = nova_raca
    pet['Idade'] = novo_idade
    pet['Porte'] = novo_porte
    pet['CEP_onde_reside'] = novo_cep
    pet['Vermifugado'] = novo_vermifugado
    pet['Castrado'] = novo_castrado
    pet['Vacinado'] = novo_vacinado
    pet['Sexo'] = novo_sexo
    pet['Espécie'] = novo_especie
    pet['Cor'] = novo_cor
    pet['Peso'] = novo_peso
  
    pets[novo_nome] = pet

  else:
    limpar_tela()
    print("Pet não encontrado, por favor tente novamente!")
    print("Voltando ao menu de atualização.")
    sleep(2)
    atualizacao_pet()

  with open('cadastro_pet.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pets, arquivo, indent=4, ensure_ascii=False)

  print("\nPet atualizado com sucesso!")
  print("Voltando ao menu CRUD")
  sleep(2)
  limpar_tela()
  menu_crud()
