/* Entradas */
let nome_cliente = prompt("Insira o seu nome:")

/* Atribuindo letiaveis das compras */
let produto1 = "Shampoo"
let marca_produto1 = "Seda"
let preco_produto1 = 7.50

let produto2 = "Condicionador"
let marca_produto2 = "Pantene"
let preco_produto2 = 16.25

/* Cálculo do preço total das compras */
let total_compra = preco_produto1 + preco_produto2

/* Atribuição dos valores percentuais de taxas */
const TAXA_IMPOSTO = 0.1
const TAXA_FRETE = 0.15

/* Cálculo do valor das taxas */
let imposto = TAXA_IMPOSTO * total_compra
let frete = TAXA_FRETE * total_compra

/* Cálculo do preço final da compra */
let total_final = total_compra + frete + imposto

/* let mais_caro = Boolean(preco_produto2 > preco_produto1)
 */

// Saídas de dados

console.log("Compras de ", nome_cliente)
/* Produto 1 */
console.log("Produto 1: ", produto1)
console.log("Marca: ", marca_produto1)
console.log("Preço R$", preco_produto1)

/* Produto 2 */
console.log("Produto 1: ", produto2)
console.log("Marca: ", marca_produto2)
console.log("Preço R$", preco_produto2)
console.log("Total da compra: RS", total_compra)

console.log("Imposto: R$", imposto)
console.log("Frete: R$", frete)

console.log("Total da compra após imposto e frete: R$", parseFloat(total_final.toFixed(2)))

/* O "parseFloat(numero) diz a respeito de um método de conversão de String para Float" */
/* Já o numero.toFixed(valor) é um método usado para arrendondar um número para um valor de casas decimais.
É importante lembrar que esse método retorna o número no formato de uma String */


/* console.log(nome_cliente, ", você comprou um", produto1, " da marca ", marca_produto1, " com o valor de R$",  preco_produto1) */
/* console.log("\nO produto 2 é mais caro que o produto 1?\nResposta: ", mais_caro) */

