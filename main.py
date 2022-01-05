num = 0

commands = ["i", "d", "s", "o", "h", "p"]

with open("code.df", "r") as file:
    f = file.read()

code = []

for char in f:
    if char not in commands:
        continue
    code.append(char)

def i():
    global num
    num += 1

def d():
    global num
    num -= 1

def s():
    global num
    num *= num

def h():
    global num
    num //= 2

def o():
    global num
    print(num)

def p():
    global num
    print(chr(num))

for char in code:
    if num == -1 or num == 256:
        num = 0

    match char:
        case "i":
            i()
        case "d":
            d()
        case "s":
            s()
        case "o":
            o()
        case "h":
            h()
        case "p":
            p()