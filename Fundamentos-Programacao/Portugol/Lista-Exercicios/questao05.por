programa {
  funcao inicio() {
    real horasDeAtividade, qtdPontos

    escreva("*** Pontua��o por atividade F�sica ***")
    escreva("\nInforme quantas horas de atividade f�sica voc� realizou no m�s: ")
    leia(horasDeAtividade)

    se (horasDeAtividade <= 10) {
      qtdPontos = horasDeAtividade * 2
    }
    senao se (horasDeAtividade > 10 e horasDeAtividade <= 20) {
      qtdPontos = horasDeAtividade * 5
    }

    senao {
      qtdPontos = horasDeAtividade * 10
    }
    
    escreva("\nA quantidade de pontos que voc� obteve nesse m�s � de: ", qtdPontos, ".")
    escreva("\nAproveite para trocar seus pontos por dinheiro em nossas lojas parceiras!")
  }
}
