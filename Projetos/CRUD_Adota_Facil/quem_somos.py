from utils import limpar_tela


def quem_somos():

    from main import menu_inicial
    limpar_tela()
    
    print("Conheça um pouco da nossa história:")
    print(
        "\nNossa história começou em 2024, quando um pequeno grupo de faculdade."
    )
    print("decidiu criar um projeto chamado adotafácil.")
    print("O objetivo sempre foi ajudar as pessoas a encontrar pets.")
    print("Através de uma PLATAFORMA WEB.")

    print("\nPerguntas frequentes:")
    print("\nComo funciona o processo de adoção dos pets?")
    print("\nA adoção dos pets é feita por meio de um cadastro")
    print("onde o usuário seleciona suas informações e a partir delas")
    print(
        "será possivel conectar o usuário a pets disponíveis dentro da sua região."
    )
    print("\nComo garantimos o histórico do animal?")
    print(
        "\nPara o animal ser cadastrado no site e preciso que a ONG forneça ")
    print("um histórico médico e comportamental detalhado do animal ")
    print(
        "para que possamos garantir a auntenticidade das informações e evitar")
    print("possiveis devoluções por conta de maus intendidos.")
    print("\nComo é feita a entrega do animal?")
    print("\nA entrega do animal deve ser acordada entre a ONG e o usuário.")

    input("Pressione Enter para voltar ao menu inicial...\n")

    menu_inicial()
