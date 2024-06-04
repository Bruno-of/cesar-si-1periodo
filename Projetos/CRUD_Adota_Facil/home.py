from utils import limpar_tela


def home():
    from main import menu_inicial
    limpar_tela()
    print("*** Nosso propósito e missões ***")
    print(
        "\nSomos apaixonados por pets!\nNosso propósito é ajudar as pessoas a encontrarem pets que possam ser adotados, a partir de uma plataforma WEB."
    )
    print(
        "\nGarantimos qualidade em nosso serviço e também um eficiente pós-adoção, gerando conforto e confiança."
    )
    print(
        "Nossa missão é fazer com que você, cliente, possa encontrar um pet que possa ser adotado, sem precisar sair de casa."
    )

    input("\n\n> [Pressione Enter para voltar ao menu inicial...]\n")
    menu_inicial()
