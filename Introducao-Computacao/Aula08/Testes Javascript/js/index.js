/* geralmente a declaração de variáveis com "var" é usada
   para se referir a uma variável global.
   Já o "let", seria para variáveis de escopo de bloco ou internas.
   O "const" é usado para declarar variáveis constantes, que não podem ser reatribuidas.
*/


// printar diretamente no console
/* var nome = "Johann";
console.log(nome);

var nome2 = prompt("Informe o seu nome: ")
console.log(nome2)

const pi = 3.14159
var x = 13

{
    let x = 15
    console.log("Escopo de bloco: ", x)
}

console.log("Escopo global: ", x)
console.log("Constante: ", pi) */


{
    const frutas = ["maçã", "laranja", "melão", "banana", "pêra"]
    let ultima_fruta = frutas.pop()
    console.log(frutas)
    console.log(frutas.length)
    console.log(ultima_fruta)
}


/* {
    const cachorro = {
        nome: "Scooby",
        idade: 5,
        raca: "vira-lata",
        cor: "marrom",
        saudavel: true,
        
        latir: ()=>{
            console.log("woof woof")
        },
        comer: ()=>{
            console.log("schomp schomp")
        },
        dormir: ()=>{
            console.log("ZzzZZzZzzZZZzzzzZZZ")
        }
    }

    console.log(cachorro)
    cachorro.comer()
    cachorro.latir()
    cachorro.dormir()
} */
