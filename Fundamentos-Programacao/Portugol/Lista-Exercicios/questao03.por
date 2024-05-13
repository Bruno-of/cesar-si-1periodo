programa {
  funcao inicio() {
    cadeia nomeAluno
    real nota01, nota02, nota03, mediaFinal

    escreva("*** Cálculo de média ponderada ***")
    escreva("\nOlá. Me diga o seu nome: ")
    leia(nomeAluno)

    escreva("\nAgora informe suas três notas para o cálculo.")
    escreva("\nNota 1: ")
    leia(nota01)
    escreva("\nNota 2: ")
    leia(nota02)
    escreva("\nNota 3: ")
    leia(nota03)

    mediaFinal = ( (nota01 * 2) + (nota02 * 3) +(nota03 * 5) )/10

    se (mediaFinal <= 4.9) {
      escreva("Você está reprovado.\n Sua nota atingiu ", mediaFinal, " pontos.")
    }

    senao se( mediaFinal >= 5.0 e mediaFinal <= 6.9) {
      escreva("Você está em recuperação.\n Sua nota atingiu ", mediaFinal," pontos.")
    }
    senao{
      escreva("Parabéns, ", nomeAluno,". Você está aprovado!\nSua nota foi de: ", mediaFinal, " pontos :D")
    }
  }
}
