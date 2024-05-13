// Funções
function soma(x, y) {
    return x + y
}

function contador(inicio, fim) {
    for (let i = inicio; i <= fim; i++) {
        console.log(i)
    }
}

// Declarando variáveis

let num1 = parseInt(prompt("Informe o primeiro número: "))
let num2 = parseInt(prompt("Informe o segundo número: "))
let inicio = 0
let fim = soma(num1,num2)

// Execução
contador(inicio, fim)