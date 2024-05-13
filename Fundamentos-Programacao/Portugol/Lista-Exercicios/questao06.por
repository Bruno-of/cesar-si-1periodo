//Esse dava pra fazer com "faca" "enquanto" também
programa {
  funcao inicio() {
    real saldo = 3500, valorParaSacar, saqueEfetuado
    caracter resposta

    escreva("*** Bem vindo ao Caixa eletrônico ***")
    escreva("\nSeu saldo é de R$", saldo, " reais.")

    escreva("\nVocê deseja realizar um saque na sua conta? [S/N]: ")
    leia(resposta)

    enquanto (resposta != 'N' e resposta != 'n') {
      escreva("\nQual o valor do saque?\n-> ")
      leia(valorParaSacar)

      se (valorParaSacar > 0 e  valorParaSacar <= saldo) {
        escreva("\nSaque efetuado com sucesso!")
        escreva("\nVocê sacou um valor de R$", valorParaSacar, " de um total de R$", saldo," reais.")
        saldo = saldo - valorParaSacar
        escreva("\nSeu saldo atual é de R$", saldo, " reais.")
      }

      senao se(valorParaSacar <= 0 ou valorParaSacar > saldo) {
        escreva("\nFundos insuficientes.")
        escreva("\nO seu saldo atual é R$", saldo)
        escreva("\nInforme um novo valor de saque.")
      }

      escreva("\n\nVocê deseja realizar um novo saque? [S/N]: ")
      leia(resposta)
      limpa()
    }    
  }
}
