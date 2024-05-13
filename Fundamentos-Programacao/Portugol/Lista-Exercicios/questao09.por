programa {
  funcao inicio() {
   real valorInicialInvestimento, taxaJurosAnual, valorAnualInvestimento = 0, valorFinalInvestimento
   inteiro anosDeInvestimento
   caracter resposta

  faca {
    escreva("*** Simulador de Investimento Financeiro ***")
    escreva("\n\nInforme o valor inicial do seu investimento: ")
    leia(valorInicialInvestimento)
    escreva("Informe a taxa de juros anual (em porcentagem, ex: 0.25): ")
    leia(taxaJurosAnual)
    escreva("Por fim, informe o número de anos para o investimento: ")
    leia(anosDeInvestimento)

    para (inteiro i = 1; i <= anosDeInvestimento; ++i) {
      valorAnualInvestimento = valorInicialInvestimento * taxaJurosAnual
      
      escreva("\nAo final do ano ", i, " você vai receber R$", valorAnualInvestimento, " reais do investimento feito.")  
    }

    valorFinalInvestimento = valorAnualInvestimento * anosDeInvestimento

    escreva("\n\n-> Em ", anosDeInvestimento, " anos, você vai receber um total de R$", valorFinalInvestimento, " reais de investimento.")
    escreva("\nVocê deseja simular um novo investimento? [S/N]: ")
    leia(resposta)
    limpa()

    }enquanto(resposta != 'N' e resposta != 'n')
  }
}
