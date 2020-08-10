digits_dict = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9"
}

def convert(input_grid):
    if len(input_grid) % 4 != 0 or any(len(line) % 3 != 0 for line in input_grid):
        print('hi')
        raise ValueError('Improper format')

    height = len(input_grid) // 4
    length = len(input_grid[0]) // 3
    ret = []
    for hh in range(height):
        digit_line = ''
        for ll in range(length):
            #print(f"${''.join([line[ll*3:ll*3+3] for line in input_grid[hh*4:hh*4+4]])}$")
            digit_line += digits_dict.get(
                ''.join([line[ll*3:ll*3+3] for line in input_grid[hh*4:hh*4+4]]),
                '?'
            )
        ret.append(digit_line)
    
    return ",".join(ret)

