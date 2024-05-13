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
    escreva("Por fim, informe o n�mero de anos para o investimento: ")
    leia(anosDeInvestimento)

    para (inteiro i = 1; i <= anosDeInvestimento; ++i) {
      valorAnualInvestimento = valorInicialInvestimento * taxaJurosAnual
      
      escreva("\nAo final do ano ", i, " voc� vai receber R$", valorAnualInvestimento, " reais do investimento feito.")  
    }

    valorFinalInvestimento = valorAnualInvestimento * anosDeInvestimento

    escreva("\n\n-> Em ", anosDeInvestimento, " anos, voc� vai receber um total de R$", valorFinalInvestimento, " reais de investimento.")
    escreva("\nVoc� deseja simular um novo investimento? [S/N]: ")
    leia(resposta)
    limpa()

    }enquanto(resposta != 'N' e resposta != 'n')
  }
}
