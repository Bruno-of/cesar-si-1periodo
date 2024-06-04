import os, json
from time import sleep
from utils import limpar_tela


def loja():
  from main import menu_inicial
  print("Bem-vindo à nossa loja!\n")
  print("Aqui você encontrará produtos de qualidade para seu pet!\n")

  try:
    print ("*** Menu da Loja ***\n")
    print ("[1] - Cadastrar produto")
    print ("[2] - Listar produtos")
    print ("[3] - Atualizar produtos")
    print ("[4] - Excluir produtos")
    print ("\n[0] - Voltar ao menu Inicial")
    opcao = int(input("\n\n> Informe a opção desejada: "))
    limpar_tela()

    match (opcao):
      case 1:
        cadastro_produto()
      case 2:
        listagem_produto()
      case 3:
        atualizar_produto()
        pass
      case 4:
        deletar_produto()
        pass
      case 0:
        print ("Voltando ao menu inicial...")
        sleep(2)
        menu_inicial()
      case _:
        print("Opção inválida. Tente novamente.")
        sleep(2)
        loja()
        
        
  except ValueError:
    print("Opção inválida. Digite um número inteiro.")
    sleep(2)
    loja()


def cadastro_produto():
  print ("*** Menu de Cadastro ***\n")
  nome_produto = input("Insira o nome do produto: ").capitalize().title()
  preco_produto = float(input("Insira o preço do produto: "))
  quantidade_produto = int(input("Insira a quantidade de unidades do produto disponíveis: "))

  produto = {
      "nome": nome_produto,
      "preço": preco_produto,
      "unidades": quantidade_produto
  }

  try:
    with open('produtos.json', 'r', encoding='utf-8') as arquivo:
      produtos_loja = json.load(arquivo)

  except FileNotFoundError:
    produtos_loja = {}

  produtos_loja[nome_produto] = produto

  with open('produtos.json', 'w', encoding='utf-8') as arquivo:
    json.dump(produtos_loja, arquivo, indent=4, ensure_ascii=False)

  print("Cadastro realizado com sucesso!")
  print("Voltando ao menu da loja...")
  sleep(2)
  limpar_tela()
  loja()


def listagem_produto():
  limpar_tela()
  print ("*** Listagem de Produto ***\n")
  
  with open('produtos.json', 'r', encoding= 'utf-8') as arquivo:
    produtos_loja = json.load(arquivo)

  if produtos_loja:
    print("Os produtos disponíveis são:\n")
    for nome_produto in produtos_loja:
      print (nome_produto)
  else:
    print("Nenhum produto cadastrado.")

  
  visu_prod = input("\nDigite o nome do produto que deseja visualizar ou digite [0] para voltar ao menu da loja: ").capitalize().title()

  if visu_prod == '0':
    limpar_tela()
    loja()
  
  if visu_prod in produtos_loja:
    prod = produtos_loja[visu_prod]
    
    print(f"\nNome do produto: {visu_prod}")
    print(f"Preço do produto: {prod['preço']}")
    print(f"Quantidade disponível: {prod['unidades']}")

  else:
    print("Produto não encontrado, por favor tente novamente.")
    
  print ("\nListagem Concluída com sucesso!")
  print ("Voltando ao menu da loja")
  sleep(2)
  loja()


def atualizar_produto():
  limpar_tela()
  print ("*** Atualização de Produto ***\n")
  
  try:
    with open('produtos.json', 'r', encoding='utf-8') as arquivo:
      produtos_loja = json.load(arquivo)
  except FileNotFoundError:
    produtos_loja = {}

    
  if produtos_loja:
    print ("Os produtos disponíveis são:\n")
    for nome_produto in produtos_loja:
      print (nome_produto)
    
  else:
    print ("Não há nenhum produto cadastrado.\n")
    print ("Voltando ao menu da loja")
    sleep(2)
    limpar_tela()
    loja()

  produto_atualizar = input("\nDigite o nome do produto que deseja atualizar ou digite [0] para voltar ao menu da loja. ").capitalize().title()

  if produto_atualizar == '0':
    limpar_tela()
    loja()

  if produto_atualizar in produtos_loja:
    produto = produtos_loja[produto_atualizar]
    print(f"\nNome do produto: {produto_atualizar}")
    print(f"Preço do produto: {produto['preço']}")
    print(f"Quantidade disponível: {produto['unidades']}")

    novo_nome = input("\nDigite o novo nome do produto: ").capitalize().title()
    novo_preco = float(input("\nDigite o novo preço do produto: "))
    nova_quantidade = int(input("Digite a nova quantidade disponível: "))
    
    del produtos_loja[produto_atualizar]

    produto['nome'] = novo_nome 
    produto['preço'] = novo_preco
    produto['unidades'] = nova_quantidade

    produtos_loja[novo_nome] = produto

  else:
    print ("Produto não encontrado, por favor tente novamente")
    print ("Voltando ao menu de atualização")
    sleep(2)
    atualizar_produto()

  with open('produtos.json', 'w', encoding='utf-8') as arquivo:
    json.dump(produtos_loja, arquivo, indent=4, ensure_ascii=False)

  print("Produto atualizado com sucesso!")
  print("Voltando ao menu da loja")
  sleep(2)
  limpar_tela()
  loja()
  
def deletar_produto():
  limpar_tela()
  print ("*** Deleção de Produto ***\n")
  
  try:
    with open('produtos.json', 'r', encoding='utf-8') as arquivo:
      produtos_loja = json.load(arquivo)
  except FileNotFoundError:
    produtos_loja = {}

  if produtos_loja:
    print ("\nProdutos cadastrados:")
    for nome_produto in produtos_loja:
      print (nome_produto)
  else:
    print ("Não há nenhum produto cadastrado.\n")
    print ("Voltando ao menu da loja")
    sleep(2)
    loja()
    
  
  produto_deletar = input("Digite o nome do produto que deseja deletar ou aperte [0] para voltar ao menu. ").capitalize().title()

  if produto_deletar == '0':
    limpar_tela()
    loja()

  if produto_deletar in produtos_loja:
    del produtos_loja[produto_deletar]
  else:
    print ("Esse produto não está cadastrado!\n Voltando ao menu de deleção")
    sleep(2)
    deletar_produto()

  with open('produtos.json', 'w', encoding='utf-8') as arquivo:
    json.dump(produtos_loja, arquivo, indent=4, ensure_ascii=False)

  limpar_tela()
  print ("Produto deletado com sucesso! ")
  
  pr = input("\nDeseja deletar mais algum produto?" "\n" "[S] - Sim" "\n" "[N] - Não" "\n")
         
  if pr == "S" or pr == "s":
    limpar_tela()
    print ("Voltando ao menu de deleção")
    sleep(2)
    deletar_produto()
    
  elif pr == "N" or pr == "n":
    limpar_tela()
    print ("Voltando ao menu Loja")
    sleep(2)
    loja()

  else:
    limpar_tela()
    print ("Opção inválida. Retornando ao menu Loja")
    sleep(2)
    loja()
    