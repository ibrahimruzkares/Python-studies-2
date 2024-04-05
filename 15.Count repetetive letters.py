text = input("Enter a text: ")

dict = {}

for letter in text:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1

for letter, count in dict.items():
    print(letter, count)