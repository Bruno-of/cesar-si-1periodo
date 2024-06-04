import os
from utils import limpar_tela
from time import sleep
import home, quem_somos, blog, loja, cruds, adote_ja


def menu_inicial():

    print("*** Bem vindo ao sistema Adota Fácil ***")
    print("\nMenu de acesso\n")
    print("[1] - Acessar página Home")
    print("[2] - Acessar página Adote Já")
    print("[3] - Acessar página Quem Somos")
    print("[4] - Acessar página Blog")
    print("[5] - Acessar página Loja")
    print("[6] - Acessar página CRUD do sistema")
    print("\n[0] - Para encerrar o sistema")

    try:
        opcao = int(input("\n\n> Informe a página a ser acessada: "))
        limpar_tela()
        match opcao:
            case 1:
                home.home()
            case 2:
                adote_ja.menu_adocao()
            case 3:
                quem_somos.quem_somos()
            case 4:
                blog.blog()
            case 5:
                loja.loja()
            case 6:
                cruds.menu_crud()
            case 0:
                exit()
            case _:
                limpar_tela()
                print(
                    ">>> Opção fora do range do menu!!! Tente novamente <<<\n")
                sleep(2)
                menu_inicial()

    except ValueError:
        limpar_tela()
        print(">>> Opção inválida!!! Digite um número inteiro. <<<\n")
        sleep(2)
        menu_inicial()

    print("Encerrando o programa...")
    exit()



def main():
    limpar_tela()
    menu_inicial()



if __name__ == '__main__':
    main()
