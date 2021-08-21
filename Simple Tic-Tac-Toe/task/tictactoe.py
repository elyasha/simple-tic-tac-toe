def print_board(cells):
    print("---------")
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")


def process_coordinates(x, y, cells, x_turn=True):
    move = "X" if x_turn else "O"
    try:
        x = int(x)
        y = int(y)
        if x not in {1, 2, 3} or y not in {1, 2, 3}:
            print('Coordinates should be from 1 to 3!')
            return cells
        if x == 1:
            if cells[y - 1] != "_":
                print("This cell is occupied! Choose another one!")
                return cells
            cells = cells[:y - 1] + move + cells[y:]
        elif x == 2:
            if cells[y + 2] != "_":
                print("This cell is occupied! Choose another one!")
                return cells
            cells = cells[:y + 2] + move + cells[y + 3:]
        elif x == 3:
            if cells[y + 5] != "_":
                print("This cell is occupied! Choose another one!")
                return cells
            cells = cells[:y + 5] + move + cells[y + 6:]
    except ValueError:
        print("You should enter numbers!")
        x, y = input("Enter the coordinates: ").split(" ")
        process_coordinates(x, y, cells)
    print_board(cells)
    return cells


def analyze_winner(cells):
    number_of_xs = cells.count("X")
    number_of_os = cells.count("O")
    x_is_winner = "XXX" == cells[0:3] or "XXX" == cells[3:6] or "XXX" == cells[6:9] or \
                  ("XXX" == f"{cells[0]}{cells[3]}{cells[6]}") \
                  or ("XXX" == f"{cells[1]}{cells[4]}{cells[7]}") or \
                  ("XXX" == f"{cells[2]}{cells[5]}{cells[8]}")
    o_is_winner = "OOO" == cells[0:3] or "OOO" == cells[3:6] or "OOO" == cells[6:9] or \
                  ("OOO" == f"{cells[0]}{cells[3]}{cells[6]}") \
                  or ("OOO" == f"{cells[1]}{cells[4]}{cells[7]}") or \
                  ("OOO" == f"{cells[2]}{cells[5]}{cells[8]}")
    if abs(number_of_os - number_of_xs) > 1:
        return "Impossible"
    if x_is_winner:
        if o_is_winner:
            return "Impossible"
        return "X wins"
    elif o_is_winner:
        if x_is_winner:
            return "Impossible"
        return "O wins"
    elif cells[0] == "X" and cells[4] == "X" and cells[8] == "X":
        return "X wins"
    elif cells[2] == "X" and cells[4] == "X" and cells[6] == "X":
        return "X wins"
    elif cells[0] == "O" and cells[4] == "O" and cells[8] == "O":
        return "O wins"
    elif cells[2] == "O" and cells[4] == "O" and cells[6] == "O":
        return "O wins"
    elif "_" not in cells:
        return "Draw"
    elif "_" in cells:
        return "Game not finished"
    return "Impossible"


def main():
    cells = input("Enter cells: ")
    print_board(cells)
    # result = analyze_winner(cells)
    # print(result)
    try:
        x, y = input("Enter the coordinates: ").split(" ")
        while process_coordinates(x, y, cells) != "ok":
            x, y = input("Enter the coordinates: ").split(" ")
    except ValueError:
        print("You must enter two coordinates")
        x, y = input("Enter the coordinates: ").split(" ")
        process_coordinates(x, y, cells)


def run_game():
    x_turn = True
    cells = "_________"
    print_board(cells)

    while analyze_winner(cells) == "Game not finished":
        x, y = input("Enter the coordinates: ").split(" ")
        new_cells = process_coordinates(x, y, cells, x_turn)
        if new_cells == cells:
            pass
        else:
            cells = new_cells
            x_turn = not x_turn
    print(analyze_winner(cells))


run_game()
