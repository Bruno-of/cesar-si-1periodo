import os, json
from time import sleep
from utils import limpar_tela
from utils import carregar_pessoa_fisica, salvar_pessoa_fisica
from utils import carregar_ong, salvar_ong
from utils import carregar_pet, salvar_pet


def menu_delecao():
   from cruds import menu_crud

   print("*** Menu de Deleção ***\n")

   print("[1] - Delecao de Pessoa Física")
   print("[2] - Delecao de ONG")
   print("[3] - Delecao de Pets")
   print("\n[0] - Voltar ao Menu de CRUD")

   try:
      opcao = int(input("\n\n> Informe a opção desejada: "))
      limpar_tela()

      match opcao:
         case 1:
            delecao_pessoa_fisica()
         case 2:
            delecao_ong()
         case 3:
            delecao_pet()
         case 0:
            menu_crud()
         case _:
            limpar_tela()
            print(">>> Opção fora do range do menu!!! Tente novamente <<<\n")
            sleep(2)
            menu_delecao()

   except ValueError:
      limpar_tela()
      print(">>> Opção inválida!!! Valor inserido não compatível! <<<\n")
      sleep(2)
      menu_delecao()


def delecao_pessoa_fisica():
   limpar_tela()
   print("*** Deleção de Pessoas ***")

   try:
      with open('cadastro_pessoa_fisica.json', 'r',
                encoding='utf-8') as arquivo:
         pessoas_fisicas = json.load(arquivo)
   except FileNotFoundError:
      pessoas_fisicas = {}

   if pessoas_fisicas:
      print("\nClientes cadastrados:")
      for cpf in pessoas_fisicas:
         print(f"Identificação da pessoa (CPF)- '{cpf}' ")
   else:
      print("Nenhuma pessoa física cadastrada.")
      input("\nPressione [ENTER] para voltar ao menu de deleção.")
      menu_delecao()

   pessoa_para_deletar = input(
       "\n> Digite o CPF do cliente para excluir seus dados ou aperte [0] para voltar ao menu de deleção: "
   )
   limpar_tela()

   if pessoa_para_deletar == '0':
      menu_delecao()

   if pessoa_para_deletar in pessoas_fisicas:
      print(f"\nDeletando a pessoa {pessoa_para_deletar}...")
      del pessoas_fisicas[pessoa_para_deletar]

      salvar_pessoa_fisica(pessoas_fisicas)

      print(f"A pessoa {pessoa_para_deletar} foi excluída com sucesso!")
      print("Voltando ao menu de deleção...")
      sleep(2)
      menu_delecao()

   else:
      print(
          f"Pessoa de CPF '{pessoa_para_deletar}' não encontrada nos cadastros."
      )
      print("Tente novamente.")
      sleep(3)
      delecao_pessoa_fisica()


def delecao_ong():
   limpar_tela()
   print("*** Deleção de ONGs ***")

   try:
      with open('cadastro_ong.json', 'r', encoding='utf-8') as arquivo:
         ongs = json.load(arquivo)
   except FileNotFoundError:
      ongs = {}

   if ongs:
      print("\nONGs cadastradas:")
      for cnpj in ongs:
         print(f"Identificação da ONG - {cnpj}")
   else:
      print("Nenhuma ONG cadastrada.")
      input("Pressione [ENTER] para voltar ao menu de deleção.")
      menu_delecao()

   ong_para_deletar = input(
       "\n> Digite o CNPJ da ONG para excluir seus dados ou aperte [0] para voltar ao menu de deleção: "
   )
   limpar_tela()

   if ong_para_deletar == '0':
      menu_delecao()

   if ong_para_deletar in ongs:
      print(f"Deletando a ONG {ong_para_deletar}...")
      del ongs[ong_para_deletar]

      salvar_ong(ongs)

      print(f"A ONG {ong_para_deletar} foi excluída com sucesso!")
      print("Voltando ao menu de deleção...")
      sleep(2)
      menu_delecao()

   else:
      limpar_tela()
      print(f"ONG de CPNJ '{ong_para_deletar}' não encontrada nos cadastros.")
      print("Tente novamente.")
      sleep(3)
      delecao_ong()


def delecao_pet():
   limpar_tela()
   print("*** Deleção de Pets ***")

   try:
      with open('cadastro_pet.json', 'r', encoding='utf-8') as arquivo:
         pets = json.load(arquivo)
   except FileNotFoundError:
      pets = {}

   if pets:
      print("\nPETS cadastrados:")
      for nome in pets:
         print(f"Identificação do PET - {nome}")
   else:
      print("Nenhum PET cadastrado.")
      input("Pressione [ENTER] para voltar ao menu de deleção.")
      menu_delecao()

   pet_para_deletar = input(
       "\n> Digite o nome do PET para excluir seus dados ou aperte [0] para voltar ao menu de deleção: "
   ).title()
   limpar_tela()

   if pet_para_deletar == '0':
      menu_delecao()

   if pet_para_deletar in pets:
      print(f"Deletando o PET {pet_para_deletar}...")
      del pets[pet_para_deletar]

      salvar_pet(pets)

      print(f"O PET {pet_para_deletar} foi excluída com sucesso!")
      print("Voltando ao menu de deleção...\n")
      sleep(2)
      menu_delecao()

   else:
      print(f"PET de nome '{pet_para_deletar}' não encontrada nos cadastros.")
      print("Tente novamente.")
      sleep(3)
      delecao_pet()
