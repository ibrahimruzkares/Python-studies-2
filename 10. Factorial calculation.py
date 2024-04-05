digit = int(input("Enter a digit: "))

factorial = 1
initial = 1

while initial <= digit:
    factorial *= initial
    initial += 1
print(f"{digit}! = {factorial}")