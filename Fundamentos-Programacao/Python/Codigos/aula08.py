

while ph != -1:
    ph = int(input("Digite o PH da substancia: "))

    if ph == 7:
        print("neutro")
    elif ph > 7:
        print("basico")
    else:
        print("acido")
