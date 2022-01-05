num = 0

with open("code.df", "r") as file:
    f = file.read()

code = []

for char in f:
    if char not in ["i", "d", "s", "o", "h"]:
        continue
    code.append(char)

for char in code:
    if num == -1 or num == 256:
        num = 0

    match char:
        case "i":
            num += 1
        case "d":
            num -= 1
        case "s":
            num *= num
        case "o":
            print(num)
        case "h":
            num //= 2