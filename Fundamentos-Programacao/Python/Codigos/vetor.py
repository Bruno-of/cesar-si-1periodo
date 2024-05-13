peso_produtos = []

qtd_produtos = int(input("Informe a quantidade de produtos vendidos: "))

i = 0
acumulador_peso = 0
for i in range (qtd_produtos):
    peso_produtos.append(float(input("Insira o peso dos produtos vendidos no dia: ")))

for peso in (peso_produtos):
    acumulador_peso = acumulador_peso + peso

peso_medio = acumulador_peso/qtd_produtos
menor_peso = min(peso_produtos)
maior_peso = max(peso_produtos)

print(f"O peso médio é: {peso_medio}")
print(f"O menor peso é: {menor_peso}")
print(f"O maior peso é: {maior_peso}")


preco_por_kg = 4.35

total_arrecadado = preco_por_kg * acumulador_peso
print(f"O total arrecadado no dia é: {total_arrecadado}")



