programa {
  funcao inicio() {
    real valorBolo, precoUnitarioSalgado, totalGastoSalgados = 0
    real valorPorPessoa, valorTotal
    inteiro qtdSalgado, QTD_PARTICIPANTES = 11
    

    escreva("*** Festa de aniversário do escritório ***\n")
    escreva("Ana, informe o valor do bolo escolhido: ")
    leia(valorBolo)
    escreva("\nCerto, agora diga a quantidade dos salgados escolhidos e também o preço unitário de cada um")
    para (inteiro tipoSalgados = 1; tipoSalgados <=3; ++tipoSalgados) {
      escreva("\n\nQuantidade do salgado ", tipoSalgados, ": ")
      leia(qtdSalgado)
      escreva("\nPreço unitário do salgado ", tipoSalgados, ": ")
      leia(precoUnitarioSalgado)

      totalGastoSalgados = totalGastoSalgados + (qtdSalgado * precoUnitarioSalgado)
    }
     
    valorTotal = valorBolo + totalGastoSalgados
    valorPorPessoa = (valorBolo + totalGastoSalgados) / QTD_PARTICIPANTES

    escreva("\nO valor total gasto para a festa é de: R$", valorTotal, " reais.")
    escreva("\nE o valor que cada participante da festa deve pagar é: R$", valorPorPessoa, "reais.")
  }
}

