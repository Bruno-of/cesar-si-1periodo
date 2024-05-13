# Código de Bruno Oliveira [S.I]

import os

# Variáveis Globais:
valor_total = 0
cont_bateria = 0
cont_pneu = 0
cont_filtro_oleo = 0
cont_pastilha_freio = 0

# Funções:
def menu():
    print("\n*** Loja de Carros ***")
    
    print("\nEscolha a sua peça no catálogo\n")
    print("\n1. Bateria - R$200 reais")
    print("\n2. Pneu - R$350 reais")
    print("\n3. Filtro de óleo - R$50 reais")
    print("\n4. Pastilha de freio - R$100 reais")
    print("\nOu aperte [5] para sair do sistema.")

def escolha():

    # Chamando as variáveis globais pra dentro da função:
    global valor_total, cont_bateria, cont_pneu, cont_filtro_oleo, cont_pastilha_freio

    # Atribuindo os preços à variáveis
    preco_bateria = 200
    preco_pneu = 350
    preco_filtro_oleo = 50
    preco_pastilha_freio = 100

    # Escolher uma opção
    opcao = int(input("\n-->> Digite a sua opção de escolha: "))

    match opcao:
        case 1:
            print("\nVocê escolheu uma bateria.")
            valor_total = valor_total + preco_bateria
            cont_bateria += 1
            
        case 2:
            print("\nVocê escolheu um pneu.")
            valor_total = valor_total + preco_pneu    
            cont_pneu += 1
            
        case 3:
            print("Você escolheu um filtro de óleo.")
            valor_total = valor_total + preco_filtro_oleo
            cont_filtro_oleo += 1
            
        case 4:
            print("\nVocê escolheu uma pastilha de freio.")
            valor_total = valor_total + preco_pastilha_freio
            cont_pastilha_freio += 1

        case 5:
            print("\nVocê escolheu sair do sistema.")
            print(f"Você comprou {cont_bateria} baterias, {cont_pneu} pneus, {cont_filtro_oleo} filtros de óleo e {cont_pastilha_freio} pastilhas de freio.")
            print(f"O valor final da compra é de: R${valor_total} reais.")

            return 0

    # Mostrar o valor atual da compra:
    print(f"\n>>> O valor atual da compra é de: R${valor_total} reais. <<<")

    # Perguntar se quer continuar comprando:
    continuar_comprando = input("\nVocê deseja continuar comprando? [S/N]: ")
    os.system('clear')
    
    # Se quiser, chamar novamente a função "menu" e a função "escolha":
    if continuar_comprando == 's' or continuar_comprando == 'S':
        menu()
        escolha()

    # Se não quiser, limpar a tela e encerrar o programa mostrando o valor final da compra:
    elif continuar_comprando == 'n' or continuar_comprando == 'N':
        os.system('clear')
        print("\nVocê decidiu encerrar o programa.")
        print(f"Você comprou {cont_bateria} baterias, {cont_pneu} pneus, {cont_filtro_oleo} filtros de óleo e {cont_pastilha_freio} pastilhas de freio.")
        print(f"O valor final da compra é de: R${valor_total} reais")

    # Se não digitar [S/N], informar opção inválida e encerrar o programa.
    else:
        print("\nOpção inválida.")
        print("Programa finalizado.")
        print(f"Você comprou {cont_bateria} baterias, {cont_pneu} pneus, {cont_filtro_oleo} filtros de óleo e {cont_pastilha_freio} pastilhas de freio.")
        print(f"O valor final da compra é de: R${valor_total} reais")
        
        return 0


# Chamada das funções:
def main():
    os.system('clear')
    menu()
    escolha()

# Definindo a função main:
if __name__ == '__main__':
    main()