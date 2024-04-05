number = int(input("Enter a digit: "))

prime = True

for each_no in range(2, number):
    if number % each_no == 0:
        prime = False
        break
if prime == True:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number")