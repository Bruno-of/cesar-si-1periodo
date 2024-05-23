from utils import limpar_tela

def blog():
    # Importamos a função main aqui porque estava dando conflitos ao colocar no início desta página, assim como nas outras também.
    from main import menu_inicial
    
    limpar_tela()
    print("*** Blog ***\n")
    print("Aqui você encontra algumas matérias sobre PETS\n")
    
    # Materia 1:
    print("1- **Como ensinar truques ao seu cão?**\n")
    print("  Qualquer adestramento de cachorro começa com os ensinamentos básicos. Um cão que não obedece a um mínimo de comandos não conseguirá aprender truques mais sofisticados, como saltar e pegar objetos específicos. Nesta matéria, ensinaremos como ensinar seu cachorrinho a sentar e deitar!!\n")
    
    # Materia 2:
    print("2- **Porque gatos não pegam carrapato normalmente?**\n")
    print("  Uma coisa deve ficar clara: os gatos podem, sim, pegar carrapato! Não é que exista uma preferência do parasita pelo cachorro, mas sim pelo fato de os felinos serem, em geral, mais higiênicos. Então, o carrapato em gato é raro, mas não impossível!\n")

    # Materia 3:
    print("3- **Linguagem corporal do cachorro: uma excelente forma de comunicação!**\n")
    print("  A linguagem corporal do cachorro é uma forma muito eficiente de comunicação. Por causa do extenso tempo de convívio com o ser humano, o cão consegue se fazer entender muito bem. Os cães têm uma forma única de comunicação. Eles expressam sentimentos e necessidades por meio de posturas, gestos, movimentos corporais e sons.\n")
    
    # Input para ver alguma matéria completa ou voltar ao menu inicial
    materia = int(input("\n> Você deseja ver alguma matéria completa? [1/2/3] ou [0] para voltar ao menu inicial: "))

    # IFs para mostrar as matérias completas ou voltar ao menu inicial
    if materia == 1:
        limpar_tela()
        print("**Como ensinar truques ao seu cão?**\n")
        print("Qualquer adestramento de cachorro começa com os ensinamentos básicos. Um cão que não obedece a um mínimo de comandos não conseguirá aprender truques mais sofisticados, como saltar e pegar objetos específicos. Nesta matéria, ensinaremos como ensinar seu cachorrinho a sentar e deitar!!\n")
        print("  Chame a atenção do peludo para o petisco. Deixe que ele veja que o receberá caso faça o que lhe foi mandado. Mova o petisco do focinho para a cabeça, pois esse movimento o fará sentar. Quando ele fizer isso, dê o petisco. Se ele ainda não entendeu o que fazer, faça o mesmo movimento até que ele sente sem você forçar, e dê o petisco. Logo ele compreenderá o que deve fazer. Aos poucos ele vai aprendendo com seu gesto e tudo fica mais fácil. O comando “deita” é ensinado da mesma forma que o “senta”. Para que ele entenda o que precisa fazer, pegue o petisco, o coloque no SENTA, abaixe o petisco até o chão mirando entre as patas da frente até deitar.\n")
        input("Pressione ENTER para voltar ao blog...")
        blog()

    elif materia == 2:
        limpar_tela()
        print("**Porque gatos não pegam carrapato normalmente?**\n")
        print("  Uma coisa deve ficar clara: os gatos podem, sim, pegar carrapato! Não é que exista uma preferência do parasita pelo cachorro, mas sim pelo fato de os felinos serem, em geral, mais higiênicos. Então, o carrapato em gato é raro, mas não impossível!")
        print("  Então, vamos às razões por que gato não pega carrapato normalmente. Todo mundo sabe que os felinos são famosos pela extrema limpeza e dedicação à higiene pessoal. Os bichanos passam em torno de 30 a 50% do dia tomando banhos de língua. Tanta meticulosidade serve para manter o pelo sedoso, macio e brilhante. Além disso, esse hábito de se lamber é uma forma de defesa natural contra diversos parasitas, incluindo o carrapato. A lambida dos gatos é tão forte que é capaz de retirar o carrapato da pelagem. Dessa forma, o parasita dificilmente consegue chegar até a pele para picá-lo e sugar o sangue. Esse é um dos motivos por que gato não pega carrapato normalmente.\n")
        input("Pressione ENTER para voltar ao blog...")
        blog()

    elif materia == 3:
        limpar_tela()
        print("**Linguagem corporal do cachorro: uma excelente forma de comunicação!**\n")
        print("  A linguagem corporal do cachorro é uma forma muito eficiente de comunicação. Por causa do extenso tempo de convívio com o ser humano, o cão consegue se fazer entender muito bem. Os cães têm uma forma única de comunicação. Eles expressam sentimentos e necessidades por meio de posturas, gestos, movimentos corporais e sons.\n")
        print("  Saber interpretar a linguagem corporal canina é muito importante para que o tutor e o pet tenham uma boa convivência. Isso também contribui para o vínculo entre os familiares e outros animais da casa. A linguagem corporal do cachorro é uma forma de comunicação que vem evoluindo ao longo do tempo. Com ela, ele se comunica com os humanos e com outros animais. Ao observar atentamente um cachorro, é possível dizer como está o humor dele. A postura corporal e outros sinais revelam o estado emocional do pet .\n")
        input("Pressione ENTER para voltar ao blog...")
        blog()

    elif materia == 0:
        menu_inicial()

    else:
        blog()

