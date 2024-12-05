def transpose(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append([])
        for j in range(len(arr[0])):
            new_arr[i].append(arr[j][i])
        new_arr[i] = "".join(new_arr[i])

    return new_arr


def rotate_matrix(arr):
    # starts in the middle, goes [i][j]
    # then increment i and j separately and send them off to do [i][j]
    full_arr = []

    for i in range(len(arr)):
        bottom_diagonal = []
        top_diagonal = []

        for j in range(0, len(arr[0])-i):
            bottom_diagonal.append(arr[j+i][j])
            top_diagonal.append(arr[j][j+i])

        full_arr.append("".join(bottom_diagonal))
        if i != 0:  # to avoid a duplicate
            full_arr.append("".join(top_diagonal))

    return full_arr


def find_wordsearch_string_count(filename, word):
    with open(filename, "r") as f:
        wordsearch = f.readlines()
    wordsearch = [s.strip() for s in wordsearch]

    total_xmases = 0
    for line in wordsearch:
        total_xmases += line.count(word)
        reversed_line = line[::-1]
        total_xmases += reversed_line.count(word)  # reverses the string

    transposed_wordsearch = transpose(wordsearch)
    for line in transposed_wordsearch:
        total_xmases += line.count(word)
        reversed_line = line[::-1]
        total_xmases += reversed_line.count(word)  # reverses the string

    diagonal_wordsearch = rotate_matrix(wordsearch)
    for line in diagonal_wordsearch:
        total_xmases += line.count(word)
        reversed_line = line[::-1]
        total_xmases += reversed_line.count(word)  # reverses the string

    diagonal_transposed_wordsearch = rotate_matrix(transpose(wordsearch))
    for line in diagonal_transposed_wordsearch:
        total_xmases += line.count(word)
        reversed_line = line[::-1]
        total_xmases += reversed_line.count(word)  # reverses the string

    return total_xmases


def search_directions(wordsearch, word, x, y):
    line = wordsearch[y]
    words_present = 0

    if x+1 >= len(word):
        # search left
        left_findings = True
        for i in range(len(word)):
            letter = word[i]
            if letter != wordsearch[y][x-i]:
                left_findings = False
                break

        if left_findings:
            words_present += 1

    if x <= len(line) - len(word):
        # search right
        right_findings = True
        for i in range(len(word)):
            letter = word[i]
            if letter != wordsearch[y][x+i]:
                right_findings = False
                break

        if right_findings:
            words_present += 1

    if y+1 >= len(word):
        # search up
        up_findings = True
        for i in range(len(word)):
            letter = word[i]
            if letter != wordsearch[y-i][x]:
                up_findings = False
                break

        if up_findings:
            words_present += 1

    if y <= len(line) - len(word):
        # search down
        down_findings = True
        for i in range(len(word)):
            letter = word[i]
            if letter != wordsearch[y+i][x]:
                down_findings = False
                break

        if down_findings:
            words_present += 1

    # diagonals use prerequisites of their two directions combined
    if y <= len(line) - len(word) and x+1 >= len(word):
        # search diagonal down left
        down_left_findings = True
        for i in range(len(word)):
            letter = word[i]
            if letter != wordsearch[y+i][x-i]:
                down_left_findings = False
                break

        if down_left_findings:
            words_present += 1

    if y <= len(line) - len(word) and x <= len(line) - len(word):
        # search diagonal down right
        down_right_findings = True
        for i in range(len(word)):
            letter = word[i]
            if letter != wordsearch[y+i][x+i]:
                down_right_findings = False
                break

        if down_right_findings:
            words_present += 1

    if y+1 >= len(word) and x+1 >= len(word):
        # search diagonal up left
        up_left_findings = True
        for i in range(len(word)):
            letter = word[i]
            if letter != wordsearch[y-i][x-i]:
                up_left_findings = False
                break

        if up_left_findings:
            words_present += 1

    if y+1 >= len(word) and x <= len(line) - len(word):
        # search diagonal up right
        up_right_findings = True
        for i in range(len(word)):
            letter = word[i]
            if letter != wordsearch[y-i][x+i]:
                up_right_findings = False
                break

        if up_right_findings:
            words_present += 1

    return words_present


def depth_first_search(filename, word):
    with open(filename, "r") as f:
        wordsearch = f.readlines()
    wordsearch = [s.strip() for s in wordsearch]

    total_words = 0
    for i in range(len(wordsearch)):
        line = wordsearch[i]
        for j in range(len(line)):
            char = line[j]
            if char == word[0]:
                total_words += search_directions(wordsearch, word, j, i)

    return total_words


print(depth_first_search("Day 4 Input", "XMAS"))