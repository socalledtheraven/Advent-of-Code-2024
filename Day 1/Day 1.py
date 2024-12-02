def get_lines(filename: str):
    with open(filename, "r") as f:
        contents = f.readlines()

    l1 = []
    l2 = []
    for line in contents:
        l1.append(int(line.split("   ")[0]))
        l2.append(int(line.split("   ")[1]))

    return l1, l2


def distance(filename: str):
    l1, l2 = get_lines(filename)
    l1.sort()
    l2.sort()

    total = 0
    for i in range(len(l1)):
        dis = abs(l1[i] - l2[i])
        total += dis

    return total


def similarity_score(filename: str):
    l1, l2 = get_lines(filename)

    total_score = 0
    for i in range(len(l1)):
        number_of_appearances = l2.count(l1[i])
        score = number_of_appearances * l1[i]
        total_score += score

    return total_score


print(similarity_score("Day 1 Input"))
