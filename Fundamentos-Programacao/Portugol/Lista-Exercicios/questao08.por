programa {
  funcao inicio() {
    inteiro numero, fatorial
    caracter resposta

    escreva("*** Calculadora de Fatorial ***")

    faca{
      escreva("\nInforme um número inteiro positivo: ")
      leia(numero)

      fatorial = 1
      
      para (inteiro i = 1; i <= numero; ++i) {
        fatorial = fatorial * i
      }

      escreva("\nO fatorial de ", numero, " é ", fatorial)
      escreva("\nVocê deseja calcular o fatorial de outro número? [S/N]: ")
      leia(resposta)
      limpa()

    } enquanto(resposta != 'N' e resposta != 'n')
  }
}
