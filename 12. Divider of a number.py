number = int(input("Enter a digit: "))


list = []

for bolen in range(1,number + 1):
    if number % bolen == 0:
        list.append(bolen)
        bolen += 1


print(list)

