programa {
  funcao inicio() {
    real peso, altura, calculoIMC
    cadeia classificacaoImc

    escreva("*** Cálculo de IMC ***")
    escreva("\nInforme o seu peso em Kg: ")
    leia(peso)
    escreva("\nInforme sua altura em Metros: ")
    leia(altura)

    calculoIMC = peso/(altura*altura)

    se (calculoIMC < 18.5) {
      classificacaoImc = "Abaixo do peso"
    }

    senao se(calculoIMC >= 18.5 e calculoIMC <= 24.9) {
      classificacaoImc = "Peso ideal"
    }
    
    senao se(calculoIMC >= 25 e calculoIMC <= 29.9) {
      classificacaoImc = "Sobrepeso"
    }
    
    senao se (calculoIMC >= 30 e calculoIMC <= 39.9) {
      classificacaoImc = "Obesidade"
    }

    senao {
      classificacaoImc = "Obesidade Mórbida"
    }

    escreva("Sua classificação de IMC é ", classificacaoImc, ".")
  }
}
