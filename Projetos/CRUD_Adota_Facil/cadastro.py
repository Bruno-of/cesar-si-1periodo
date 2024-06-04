import os, json
from time import sleep
from types import ClassMethodDescriptorType
from typing import cast
from utils import limpar_tela, carregar_pessoa_fisica, salvar_pessoa_fisica
from utils import carregar_ong, salvar_ong
from utils import carregar_pet, salvar_pet
from utils import validar_email


def menu_cadastro():
   from cruds import menu_crud
   
   print("*** Menu de Cadastro ***\n")

   print("[1] - Cadastro de Pessoa Física")
   print("[2] - Cadastro de ONG")
   print("[3] - Cadastro de Pets")
   print("\n[0] - Voltar ao Menu de CRUD")

   try:
      opcao = int(input("\n\n> Informe a opção desejada: "))
      limpar_tela()

      match opcao:
         case 1:
            cadastro_pessoa_fisica()
         case 2:
            cadastro_ong()
         case 3:
            cadastro_pet()
         case 0:
            menu_crud()
         case _:
            limpar_tela()
            print(">>> Opção fora do range do menu!!! Tente novamente <<<\n")
            sleep(2)
            menu_cadastro()

   except ValueError:
      limpar_tela()
      print(">>> Opção inválida!!! Valor inserido não compatível! <<<\n")
      sleep(2)
      menu_cadastro()







def cadastro_pessoa_fisica():
   from cruds import menu_crud
   limpar_tela()
   print("*** Cadastro de Pessoa ***\n")

   nome_pessoa = input("Nome completo: ").title()
   
   
   cpf_pessoa = input("CPF: ")
   while len(cpf_pessoa) != 11:
      print("CPF inválido! Por favor insira novamente, com 11 dígitos.")
      cpf_pessoa = input("CPF: ")
      
   
   email_pessoa = input("E-mail: ")
   while validar_email(email_pessoa) == False:
      print("E-mail inválido. Tente novamente.")
      email_pessoa = input("E-mail: ")

   
   senha_pessoa = input("Senha: ")
   idade_pessoa = input("Idade: ")
   endereco_pessoa = input("Endereço: ").title()
   cidade_pessoa = input("Cidade: ").title()
   estado_pessoa = input("Estado: ").title()
   cadastrar_pet = input("\nVocê vai cadastrar um PET? [S/N]: ").lower()

   if cadastrar_pet == 's':
      cadastrar_pet = True
   elif cadastrar_pet == 'n':
      cadastrar_pet = False
   else:
      while cadastrar_pet != 'n':
         print("\n >>> ERRO!. Digite apenas [S/N] para a opção de cadastrar um pet. <<<\n")
         cadastrar_pet = input("Você vai cadastrar um PET? [S/N]: ").lower()
      
   pessoas_fisicas = carregar_pessoa_fisica()

   usuario = {
       "Nome": nome_pessoa,
       "CPF": cpf_pessoa,
       "E-mail": email_pessoa,
       "Senha": senha_pessoa,
       "Idade": idade_pessoa,
       "Endereço": endereco_pessoa,
       "Cidade": cidade_pessoa,
       "Estado": estado_pessoa,
       "Cadastrou_Pet": cadastrar_pet
   }

   pessoas_fisicas[cpf_pessoa] = usuario

   salvar_pessoa_fisica(pessoas_fisicas)
   
   limpar_tela()
   print(f"\nCadastro de '{nome_pessoa}' realizado com sucesso!")
   print("Voltando ao menu de CRUD...\n")
   sleep(3)
   menu_crud()



def cadastro_ong():
   from cruds import menu_crud
   
   print("*** Cadastro de ONG ***\n")
   
   nome_ong = input("Nome da organização: ").title()
   cnpj_ong = input("CNPJ: ")
   
   while len(cnpj_ong) != 14:
      print("CNPJ inválido! Por favor insira novamente, com 14 dígitos.")
      cnpj_ong = input("CNPJ: ")

   
   email_ong = input("E-mail: ")
   while validar_email(email_ong) == False:
      print("E-mail inválido. Tente novamente.")
      email_ong = input("E-mail: ")

   
   senha_ong = input("Senha: ")
   endereco_ong = input("Endereço: ").title()
   cidade_ong = input("Cidade: ").title()
   estado_ong = input("Estado: ").title()
   instagram_ong = input("Instagram: ").title()
   cadastrar_pet = input("Você vai cadastrar um PET? [S/N]: ")

   if cadastrar_pet == 's':
      cadastrar_pet = True
   elif cadastrar_pet == 'n':
      cadastrar_pet = False
   else:
      while cadastrar_pet != 'n':
         print("\n >>> ERRO!. Digite apenas [S/N] para a opção de cadastrar um pet. <<<\n")
         cadastrar_pet = input("Você vai cadastrar um PET? [S/N]: ")
   
   ongs = carregar_ong()

   usuario_ong = {
       "Nome": nome_ong,
       "CNPJ": cnpj_ong,
       "E-mail": email_ong,
       "Senha": senha_ong,
       "Endereço": endereco_ong,
       "Cidade": cidade_ong,
       "Estado": estado_ong,
       "Instagram": instagram_ong,
       "Cadastrou_Pet": cadastrar_pet
   }

   ongs[cnpj_ong] = usuario_ong

   salvar_ong(ongs)

   limpar_tela()
   print(f"\nCadastro da ONG '{nome_ong}' realizado com sucesso!")
   print("Voltando ao menu de CRUD...\n")
   sleep(3)
   menu_crud()

   

def cadastro_pet():
   from cruds import menu_crud
   
   print("*** Cadastro de PET ***\n")

   
   
   nome_pet = input("Nome do pet: ").title()
   cep_pet = input("Digite o CEP onde o pet reside: ")
   especie_pet = input("Espécie (Gato/Cachorro): ")
   raca_pet = input("Raça: ").title()
   sexo_pet = input("Sexo: ")
   idade_pet = int(input("Idade: "))
   porte_pet = input("Porte: ").title()
   cor_pet = input("Cor: ").title()
   peso_pet = float(input("Peso (apenas números): "))
   castrado = input("Castrado: ").upper()
   vacinado = input("Vacinado: ").upper()
   vermifugado = input("Vermifugado: ").upper()
   
   pets = carregar_pet()

   pet = {
      "Nome": nome_pet,
      "CEP_onde_reside": cep_pet,
      "Espécie": especie_pet,
      "Raça": raca_pet,
      "Sexo": sexo_pet,
      "Idade": idade_pet,
      "Porte": porte_pet,
      "Cor": cor_pet,
      "Peso": peso_pet,
      "Castrado": castrado,
      "Vacinado": vacinado,
      "Vermifugado": vermifugado
   }

   pets[nome_pet] = pet

   salvar_pet(pets)

   limpar_tela()
   print(f"\nCadastro do pet '{nome_pet}' realizado com sucesso!")
   print("Voltando ao menu de CRUD...\n")
   sleep(3)
   menu_crud()
