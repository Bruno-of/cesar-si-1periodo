programa {
  funcao inicio() {
    real largura, altura, area, qtdTinta

    escreva("Informe a largura da parede: ")
    leia(largura)
    escreva("\nAgora informe a altura da mesma: ")
    leia(altura)

    area = largura * altura
    qtdTinta = area/2
    escreva("\n\nA �rea da parede a ser pintada � de: ", area)
    escreva("\nE a quantidade de tinta necess�ria para o servi�o �: ", qtdTinta," litros.")
  }
}
