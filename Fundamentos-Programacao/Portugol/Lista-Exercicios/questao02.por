programa {
  funcao inicio() {
    real largura, altura, area, qtdTinta

    escreva("Informe a largura da parede: ")
    leia(largura)
    escreva("\nAgora informe a altura da mesma: ")
    leia(altura)

    area = largura * altura
    qtdTinta = area/2
    escreva("\n\nA área da parede a ser pintada é de: ", area)
    escreva("\nE a quantidade de tinta necessária para o serviço é: ", qtdTinta," litros.")
  }
}
