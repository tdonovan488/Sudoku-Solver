
print("Example: \n0  1  2  | 3  4  5  | 6  7  8\n" +
"9  10 11 | 12 13 14 | 15 16 17\n" +
"18 19 20 | 21 22 23 | 24 25 26\n" +
"---------+----------+----------\n" +
"27 28 29 | 30 31 32 | 33 34 35\n" +
"36 37 38 | 39 40 41 | 42 43 44\n" +
"45 46 47 | 48 49 50 | 51 52 53\n" +
"---------+----------+----------\n" +
"54 55 56 | 57 58 59 | 60 61 62\n" + 
"63 64 65 | 66 67 68 | 69 70 71\n"+ 
"72 73 74 | 75 76 77 | 78 79 80")
board = raw_input("Input Board (Left To Right Row By Row Use Spaces For Blank Spots): ")
board_data = [[1,2,3,4,5,6,7,8,9]] * 81

board_list = []
for i in range(81):
    board_list.append(board[i])
board = board_list

# 0  1  2  | 3  4  5  | 6  7  8
# 9  10 11 | 12 13 14 | 15 16 17
# 18 19 20 | 21 22 23 | 24 25 26
# -------------------------------
# 27 28 29 | 30 31 32 | 33 34 35
# 36 37 38 | 39 40 41 | 42 43 44
# 45 46 47 | 48 49 50 | 51 52 53
# -------------------------------
# 54 55 56 | 57 58 59 | 60 61 62
# 63 64 65 | 66 67 68 | 69 70 71
# 72 73 74 | 75 76 77 | 78 79 80

def check_possibilities():
    for index,value in enumerate(board_data):
        if len(value) == 1:
            board[index] = str(value[0])
            board_data[index] = [value]

def combine_possibilities(index,array):
    new_array = []
    for i in board_data[index]:
        if i in array:
            new_array.append(i)
    return new_array


def check_grid_possibilities():
    for i in range(9):
        number = i + 1
        for y in range(3):
            for x in range(3):
                top_left = x * 3 + y * 27
                counter = []
                for grid_y in range(3):
                    for grid_x in range(3):
                        current_index = top_left + grid_x + (9 * grid_y)
                        if number in board_data[current_index]:
                            counter.append(current_index)

                if len(counter) == 1:
                    board_data[counter[0]] = [number]



def check_grid():
    for y in range(3):
        for x in range(3):
            full_grid = [1,2,3,4,5,6,7,8,9]
            top_left = x * 3 + y * 27
            for grid_y in range(3):
                for grid_x in range(3):
                    current_index = top_left + grid_x + (9 * grid_y)
                    if board[current_index] != " " and int(board[current_index]) in full_grid:
                        full_grid.remove(int(board[current_index]))
            for grid_y in range(3):
                for grid_x in range(3):
                    current_index = top_left + grid_x + (9 * grid_y)
                    if board[current_index] != " ":
                        continue
                    board_data[current_index] = combine_possibilities(current_index, full_grid)

def check_columns():
    for i in range(9):
        full_column = [1,2,3,4,5,6,7,8,9]
        for y in range(9):
            if board[y * 9 + i] != " ":
                board_data[y * 9 + i] = [int(board[y*9 + i])]
                full_column.remove(int(board[y*9 + i]))

        for y in range(9):
            if board[y * 9 + i] != " ":
                continue

            possibilities = full_column[:]
            for x in range(9):
                if board[y * 9 + x] != " " and int(board[y * 9 + x]) in possibilities:
                    possibilities.remove(int(board[y * 9 + x]))

            board_data[y * 9 + i] = combine_possibilities(y * 9 + i, possibilities)

def check_rows():
    for i in range(9):
        full_row = [1,2,3,4,5,6,7,8,9]
        for x in range(9):
            if board[x + i * 9] != " ":
                board_data[x + i * 9] = [int(board[x + i * 9])]
                full_row.remove(int(board[x + i * 9]))

        for x in range(9):
            if board[x + i * 9] != " ":
                continue

            possibilities = full_row[:]
            for y in range(9):
                if board[x + 9 * y] != " " and int(board[x + 9 * y]) in possibilities:
                    possibilities.remove(int(board[x + 9 * y]))

            board_data[x + i * 9] = combine_possibilities(x + i * 9,possibilities)

def display():
    for y in range(9):
        row_string = " "
        for x in range(9):
            row_string += board[y * 9 + x] + " "
            if (x + 1) % 3 == 0 and x != 8:
                row_string += "| "
        print(row_string)
        if (y + 1) % 3 == 0 and y != 8:
            print("------------------------")

print("")
print("Input: ")
display()
for i in range(100):
    check_columns()
    check_rows()
    check_grid()
    check_grid_possibilities()
    check_possibilities()
    if not " " in board:
        break

print(" ")
print("Solved: ")
display()
print("")
print("Copy: ")
string = ""
for i in board:
    string += i
print(string)

