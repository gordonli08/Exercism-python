def annotate(minefield):
    # Function body starts here
    if not minefield:
        return minefield
    if len(set(len(row) for row in minefield)) != 1:
        raise ValueError('Rows of different length')
    minefield = [list(row) for row in minefield]

    for y, row in enumerate(minefield):
        for x, space in enumerate(row):
            if space not in [" ", "*"]:
                raise ValueError("Invalid character in minefield")
            elif space == " ":
                count = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if ((i == 0 and j == 0) or 
                            y + j < 0 or
                            x + i < 0 or
                            y + j >= len(minefield) or
                            x + i >= len(minefield[0])):
                            continue
                        if minefield[y+j][x+i] == "*":
                            count += 1
                if count:
                    minefield[y][x] = str(count)
    return ["".join(row) for row in minefield]
