programa {
  funcao inicio() {
    real horasDeAtividade, qtdPontos

    escreva("*** Pontuação por atividade Física ***")
    escreva("\nInforme quantas horas de atividade física você realizou no mês: ")
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
    
    escreva("\nA quantidade de pontos que você obteve nesse mês é de: ", qtdPontos, ".")
    escreva("\nAproveite para trocar seus pontos por dinheiro em nossas lojas parceiras!")
  }
}
