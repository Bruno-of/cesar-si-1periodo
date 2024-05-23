import os, json
from time import sleep
from utils import limpar_tela, carregar_pessoa_fisica, salvar_pessoa_fisica
from utils import carregar_ong, salvar_ong
from utils import carregar_pet, salvar_pet


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
      print(">>> Opção inválida!!! Digite um número inteiro <<<\n")
      sleep(2)
      menu_cadastro()


def cadastro_pessoa_fisica():
   from cruds import menu_crud
   limpar_tela()
   print("*** Cadastro de Pessoa ***\n")
   
   nome_pessoa = input("Nome completo: ").title()
   cpf_pessoa = input("CPF: ")
   idade_pessoa = int(input("Idade: "))
   endereco_pessoa = input("Endereço: ").title()
   cidade_pessoa = input("Cidade: ").title()
   estado_pessoa = input("Estado: ").title()

   # IMPLEMENTAR: comparação de CPFs para não permitir cpf's identicos.
   
   pessoas_fisicas = carregar_pessoa_fisica()

   usuario = {
        "Nome" : nome_pessoa,
        "CPF" : cpf_pessoa,
        "Idade" : idade_pessoa,
        "Endereço" : endereco_pessoa,
        "Cidade" : cidade_pessoa,
        "Estado" : estado_pessoa
   }

   pessoas_fisicas[cpf_pessoa] = usuario

   salvar_pessoa_fisica(pessoas_fisicas)

   print("\nCadastro realizado com sucesso!")
   print("Voltando ao menu de CRUD...\n")
   sleep(3)
   menu_crud()


def cadastro_ong():
   from cruds import menu_crud
   print("*** Cadastro de ONG ***\n")
   nome_ong = input("Nome da organização: ").title()
   cnpj_ong = input("CNPJ: ")
   endereco_ong = input("Endereço: ").title()
   cidade_ong = input("Cidade: ").title()
   estado_ong = input("Estado: ").title()

   ongs = carregar_ong()


   # IMPLEMENTAR: comparação de CNPJs para não permitir CNPJs identicos.

   
   usuario_ong = {
        "Nome" : nome_ong,
        "CNPJ" : cnpj_ong,
        "Endereço" : endereco_ong,
        "Cidade" : cidade_ong,
        "Estado" : estado_ong
   }
   

   ongs[cnpj_ong] = usuario_ong

   salvar_ong(ongs)

   print("\nCadastro da ONG realizado com sucesso!")
   print("Voltando ao menu de CRUD...\n")
   sleep(2)
   menu_crud()
   pass


def cadastro_pet():
   from cruds import menu_crud
   print("*** Cadastro de PET ***\n")
   nome_pet = input("Nome do pet: ").title()
   raca_pet = input("Raça: ").title()
   idade_pet = int(input("Idade: "))
   endereco_pet = input("Endereço: ").title()
   cidade_pet = input("Cidade: ").title()
   estado_pet = input("Estado: ").title()
   
   pets = carregar_pet()

   # IMPLEMENTAR: O pet precisa estar vinculado à uma PESSOA ou ONG. usar isso como identificador.

   pet = {
        "Nome" : nome_pet,
        "Raça" : raca_pet,
        "Idade" : idade_pet,
        "Endereço" : endereco_pet,
        "Cidade" : cidade_pet,
        "Estado" : estado_pet
   }

   pets[nome_pet] = pet

   salvar_pet(pets)

   print("\nCadastro do pet realizado com sucesso!")
   print("Voltando ao menu de CRUD...\n")
   sleep(3)
   menu_crud()
   pass