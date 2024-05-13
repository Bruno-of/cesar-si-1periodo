# Binary to decimal converter

binary_number = input("Write the binary number: ")
list_binary_number = list(binary_number)
list_binary_number.reverse()

sum = 0

for i in range(len(list_binary_number)):
    sum = sum + int(list_binary_number[i]) * 2 ** i

print("The number in decimal is: ", sum)
