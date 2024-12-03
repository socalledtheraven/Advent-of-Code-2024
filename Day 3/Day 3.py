import re


def decorrupt(filename: str):
    with open(filename, "r") as f:
        content = f.read()

    multiplications = re.findall(r"mul\([0-9]*,[0-9]*\)", content)

    total = 0
    for multiplication in multiplications:
        multiplication = multiplication.replace("mul", "").replace("(", "").replace(")", "").split(",")
        total += int(multiplication[0]) * int(multiplication[1])

    return total


def decorrupt_enhanced(filename: str):
    with open(filename, "r") as f:
        content = f.readlines()

    content = "".join([s.strip() for s in content])  # the fucking newlines were the issue
    content = re.sub(r"(?<=don't\(\))(.*?)(?=do\(\))", "", content)
    content = content.replace("don't()do()", "")
    multiplications = re.findall(r"mul\([0-9]*,[0-9]*\)", content)

    total = 0
    for multiplication in multiplications:
        multiplication = multiplication.replace("mul", "").replace("(", "").replace(")", "").split(",")
        total += int(multiplication[0]) * int(multiplication[1])

    return total


print(decorrupt_enhanced("Day 3 Input"))
