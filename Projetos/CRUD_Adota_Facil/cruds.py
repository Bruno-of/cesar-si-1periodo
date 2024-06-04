import os, json
from time import sleep
from main import menu_inicial
from cadastro import menu_cadastro
from listagem import menu_listagem
from delecao import menu_delecao
from utils import limpar_tela
from atualizacao import menu_atualizacao


def salvar_pessoa_fisica(pessoas_fisicas):
  with open('cadastro_pessoa_fisica.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoas_fisicas, arquivo, indent=4, ensure_ascii=False)


def menu_crud():
  print("*** Menu CRUD ***\n")
  print("[1] - Cadastro no Sistema")
  print("[2] - Listagem de Informações")
  print("[3] - Atualizar Informações")
  print("[4] - Deletar Informações")
  print("\n[0] - Voltar ao Menu Inicial")

  try:
    opcao = int(input("\n\n> Informe a opção desejada: "))
    limpar_tela()

    match opcao:
      case 1:
        menu_cadastro()
      case 2:
        menu_listagem()
      case 3:
        menu_atualizacao()
      case 4:
        menu_delecao()
      case 0:
        menu_inicial()
      case _:
        limpar_tela()
        print(">>> Opção fora do range do menu!!! Tente novamente <<<\n")
        sleep(2)
        menu_crud()

  except ValueError:
    limpar_tela()
    print(">>> Opção inválida!!! Digite um número inteiro. <<<\n")
    sleep(2)
    menu_crud()