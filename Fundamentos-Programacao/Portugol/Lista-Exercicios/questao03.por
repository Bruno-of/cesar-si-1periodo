programa {
  funcao inicio() {
    cadeia nomeAluno
    real nota01, nota02, nota03, mediaFinal

    escreva("*** C�lculo de m�dia ponderada ***")
    escreva("\nOl�. Me diga o seu nome: ")
    leia(nomeAluno)

    escreva("\nAgora informe suas tr�s notas para o c�lculo.")
    escreva("\nNota 1: ")
    leia(nota01)
    escreva("\nNota 2: ")
    leia(nota02)
    escreva("\nNota 3: ")
    leia(nota03)

    mediaFinal = ( (nota01 * 2) + (nota02 * 3) +(nota03 * 5) )/10

    se (mediaFinal <= 4.9) {
      escreva("Voc� est� reprovado.\n Sua nota atingiu ", mediaFinal, " pontos.")
    }

    senao se( mediaFinal >= 5.0 e mediaFinal <= 6.9) {
      escreva("Voc� est� em recupera��o.\n Sua nota atingiu ", mediaFinal," pontos.")
    }
    senao{
      escreva("Parab�ns, ", nomeAluno,". Voc� est� aprovado!\nSua nota foi de: ", mediaFinal, " pontos :D")
    }
  }
}
