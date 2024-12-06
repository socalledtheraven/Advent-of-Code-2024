def update_search_grid(search_grid, x, y, direction):
    new_row = list(search_grid[y])
    new_row[x] = "X"
    if direction == "^":
        new_other_row = list(search_grid[y-1])
        new_other_row[x] = direction
        search_grid[y-1] = "".join(new_other_row)
    elif direction == "v":
        new_other_row = list(search_grid[y+1])
        new_other_row[x] = direction
        search_grid[y+1] = "".join(new_other_row)
    elif direction == ">":
        new_row[x+1] = direction
    elif direction == "<":
        new_row[x-1] = direction

    search_grid[y] = "".join(new_row)
    return search_grid


def find_starting_position(search_grid):
    y, x = 0, 0
    for i in range(len(search_grid)):
        y = i
        row = search_grid[y]
        x = row.find("^")
        if x != -1:
            break

    return y, x


def get_next_tile_location(search_grid, x, y, direction):
    if direction == "^":
        if y - 1 >= 0:
            return y-1, x
        else:
            return -1
    elif direction == "v":
        if y + 1 < len(search_grid):
            return y+1, x
        else:
            return -1
    elif direction == ">":
        if x + 1 < len(search_grid[y]):
            return y, x+1
        else:
            return -1
    else:
        if x - 1 >= 0:
            return y, x-1
        else:
            return -1


def get_next_tile(search_grid, x, y, direction):
    loc = get_next_tile_location(search_grid, x, y, direction)
    if loc == -1:
        return loc
    else:
        return search_grid[loc[0]][loc[1]]


def get_grid(filename):
    with open(filename, "r") as f:
        search_grid = f.readlines()

    return [s.strip() for s in search_grid]


def count_positions(filename):
    search_grid = get_grid(filename)

    y, x = find_starting_position(search_grid)

    # go through with while until hitting hash or end of line
    # alternatively, measure position of things and do it precisely
    next_to_hash = False
    direction = "^"
    positions = 0
    all_position_details = []
    next_tile = get_next_tile(search_grid, x, y, direction)
    while next_tile != -1:
        if next_tile == "#":
            next_to_hash = True
        else:
            if next_tile == ".":
                positions += 1
                all_position_details.append((y, x, direction))

            if direction == "^":
                search_grid = update_search_grid(search_grid, x, y, direction)
                y -= 1  # y is indexed the other way round, remember
            elif direction == "v":
                search_grid = update_search_grid(search_grid, x, y, direction)
                y += 1
            elif direction == ">":
                search_grid = update_search_grid(search_grid, x, y, direction)
                x += 1
            elif direction == "<":
                search_grid = update_search_grid(search_grid, x, y, direction)
                x -= 1

        if next_to_hash:
            current_direction_index = "^>v<".find(direction)
            direction = "^>v<"[(current_direction_index + 1) % 4]  # should update it and wrap round once it finishes

        ""
        for row in search_grid:
            print(row)
        print()
        print("------------")
        print()
        ""

        next_tile = get_next_tile(search_grid, x, y, direction)

    return positions + 1, all_position_details


def print_obstacles(search_grid, obstacles):
    for i in range(len(search_grid)):
        for j in range(len(search_grid[i])):
            if (i, j) in obstacles:
                print("O", end="")
            else:
                print(search_grid[i][j], end="")
        print()
    print()
    print("------------")
    print()


def add_obstacles(filename):
    search_grid = get_grid(filename)

    y, x = find_starting_position(search_grid)

    # go through with while until hitting hash or end of line
    # alternatively, measure position of things and do it precisely
    direction = "^"
    previous_path_locations = []
    obstacles = []
    next_tile = get_next_tile(search_grid, x, y, direction)
    while next_tile != -1:
        current_direction_index = "^>v<".find(direction)
        theoretical_direction = "^>v<"[(current_direction_index + 1) % 4]  # should update it and wrap round once it finishes

        # for each tile, check if the theoretical direction change would put us back on a previous path
        # so find where the next tile would be
        # TODO: the general approach's solid, but needs to take into account the guard going off-script and pinball bouncing for a bit before landing in a previous position with previous direction. maybe some kind of recursive thing?
        theoretical_location = (*get_next_tile_location(search_grid, x, y, theoretical_direction), theoretical_direction)

        for i in range(len(search_grid)):
            for j in range(len(search_grid[i])):
                if (i, j) == theoretical_location[0:2]:
                    print("O", end="")
                else:
                    print(search_grid[i][j], end="")
            print()
        print()
        print("------------")
        print()

        if theoretical_location in previous_path_locations:
            obstacle_location = get_next_tile_location(search_grid, x, y, direction)
            obstacles.append(obstacle_location)


        if next_tile == "#":
            direction = theoretical_direction

        if direction == "^":
            search_grid = update_search_grid(search_grid, x, y, direction)
            y -= 1  # y is indexed the other way round, remember
        elif direction == "v":
            search_grid = update_search_grid(search_grid, x, y, direction)
            y += 1
        elif direction == ">":
            search_grid = update_search_grid(search_grid, x, y, direction)
            x += 1
        elif direction == "<":
            search_grid = update_search_grid(search_grid, x, y, direction)
            x -= 1

        previous_path_locations.append((y, x, direction))
        next_tile = get_next_tile(search_grid, x, y, direction)

    print_obstacles(search_grid, obstacles)

    return obstacles


# d = count_positions("test")
print(add_obstacles("test"))
