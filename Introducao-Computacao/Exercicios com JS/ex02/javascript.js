/* Pratica 01 */
/* let num = 9

if (num >= 0){
    console.log("positivo");
}
else{
    console.log("negativo")
} */


/* Pratica 02 */

/* let mes_ano = prompt("Informe o mês para consulta: ")

switch (Number(mes_ano)) {
    case 1:
        console.log("voce escolheu janeiro")
        break
    case 2:
        console.log("voce escolheu fevereiro")
        break
    case 3:
        console.log("voce escolheu março")
        break
    case 4:
        console.log("você escolheu abril")
        break
    case 5:
        console.log("voce escolheu maio")
        break
    case 6:
        console.log("voce escolheu junho")
        break
    case 7:
        console.log("voce escolheu julho")
        break
    case 8:
        console.log("voce escolheu agosto")
        break
    case 9:
        console.log("voce escolheu setembro")
        break
    case 10:
        console.log("voce escolheu outubro")
        break
    case 11:
        console.log("voce escolheu novembro")
        break
    case 12:
        console.log("voce escolheu dezembro")
        break
    default:
        console.log("Inválido. Insira um número de 1 a 12.");
        break
} */


/* Pratica 03 */
/* 
for (let i = 1; i <= 10; i++) {
    if (i % 2 === 0) {
        console.log("O numero ", i," é PAR!");
    }
    else {
        console.log("O número ", i, " é ÍMPAR!");
    }
    
} */


/* Pratica 04 */

/* let i = 0
while (i <= 10) {
    let impar = (i % 2 === 1)
    console.log("O número ", i, " é impar?? ", impar);
    i++
} */


/* Pratica 05 */
/* i = 0
let soma = 0
do {
    soma = soma + i // Conceito de acumulador.
    i++
}while(i <= 5)

console.log("A soma dos numeros de 1 a 5 é: ", soma); */


/* Pratica 06 */

/* let alunos = ["João", "Maria", "Pedro", "Ana", "Luiza"];

let i = 0
for (i in alunos) {
    console.log(i);
} */

/* let alunos = ["João", "Maria", "Pedro", "Ana", "Luiza"];

let i = 0
for (i of alunos) {
    console.log(i);
} */

/* Pratica 07 */

let dataInicial = new Date("2022-04-26");
let dataFinal = new Date("2024-05-01");

diferencaEmMilissegundos = dataFinal.getTime() - dataInicial.getTime();

console.log(diferencaEmMilissegundos);

diferencaEmDias = diferencaEmMilissegundos / (1000 * 3600 * 24)

console.log(diferencaEmDias);