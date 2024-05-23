import os, json
from time import sleep
from utils import limpar_tela


def loja():
    
    print("Bem-vindo à nossa loja!\n")
    print("Aqui você pode encontrar produtos de qualidade para seu pet.")
    
    try:
      opcao = int(input("Por favor selecione uma das opções abaixo: \n[1] - Cadastrar produtos: \n[2] Listar produtos"))
      limpar_tela()
                        
      match (opcao):   
        case 1:   
          cadastro_produto()
          pass
        case 2: 
        #Listar produtos
          pass
        case 3:
          #Atualizar produtos
          pass
        case 4:
          #Deletar produtos
          pass
    except ValueError:
      print("Opção inválida. Digite um número inteiro.")
      loja()


def cadastro_produto():
  nome_produto = input("Insira o nome do produto: ")
  preco_produto = float(input("Insira o preço do produto: "))
  quantidade_produto = int(input("Insira a quantidade de unidades do produto disponíveis: "))
  
  produto = {
    "Nome": nome_produto,
    "Preço": preco_produto,
    "Unidades": quantidade_produto
  }
  
  try:
    with open('produtos.json', 'r', encoding = 'utf-8') as arquivo: 
      produtos_loja = json.load(arquivo)  
      
  except FileNotFoundError:
    produtos_loja = {}

  produtos_loja[nome_produto] = produto

  with open('produtos.json', 'w', encoding = 'utf-8') as arquivo:
     json.dump(produtos_loja, arquivo, indent=4) 

  print("Cadastro realizado com sucesso!")
  print("Voltando ao menu de cadastro...")
  sleep(2)
  loja()


def listagem_produto():
  pass
  
