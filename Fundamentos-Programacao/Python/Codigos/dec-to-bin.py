# Decimal to binary converter

decimal_number = int(input("Write the decimal number: "))
binary = ""

if decimal_number == 0:
    binary = '0'

else:
    while (decimal_number > 0):
        reminder = decimal_number % 2
        binary = str(reminder) + binary
        decimal_number = decimal_number // 2

print(f"The number is {binary} in binary.")
