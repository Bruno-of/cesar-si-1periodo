programa {
  funcao inicio() {
    inteiro idade, contadorHomem = 0, maiorIdade = 0, idadeMaisVelha = 0,
    mulherMaiorDeVinte=0, idadeTotal = 0

    real mediaIdadeGrupo
    caracter sexo

    escreva("*** Cadastro de Homens e Mulheres ***")

    para (inteiro pessoa = 1; pessoa <= 5; ++pessoa) {
      escreva("\nInforme a idade da pessoa ", pessoa, ": ")
      leia(idade)
      escreva("\nInforme o sexo da pessoa ", pessoa, " [M/F]: ")
      leia(sexo)
      //limpa()

      se (sexo == 'M' ou sexo == 'm') {
        ++contadorHomem
      }

      senao se (sexo == 'F' ou sexo == 'f') {
        se (idade > maiorIdade) {
          maiorIdade = idade
          idadeMaisVelha = idade
        }
        se (idade > 20) {
            ++mulherMaiorDeVinte
          }
      }

      idadeTotal += idade
      mediaIdadeGrupo = idadeTotal/5
    }

    escreva("\nA quantidade de homens cadastrados é: ", contadorHomem)
    escreva("\nA idade da mulher mais velha é: ", idadeMaisVelha, " anos.")
    escreva("\nA média de idade do grupo (ambos os sexos) é de: ", mediaIdadeGrupo, " anos.")
    escreva("\nA quantidade de mulheres com idade superior a 20 anos é: ", mulherMaiorDeVinte)
  }
}
