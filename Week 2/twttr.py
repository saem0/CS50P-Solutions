input = input("Input: ")

print("Output: ", end="")


for letter in input:
    updated = ""
    if letter.lower() in "aeiou":
        print(updated, end="")
    else:
        print(letter, end="")
print()
