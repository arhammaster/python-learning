board = (0,1,2,3,4,5,6,7,8)

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

player1 = input("Enter name of player 1: ")
player2 = input("Enter name of player 2: ")

print_board()

def winning_combinations():
    global board

    wins_row    = [(0,1,2), (3,4,5), (6,7,8)]
    wins_column = [(0,3,6), (1,4,7), (2,5,8)]
    wins_diagonal = [(0,4,8), (2,4,6)]
    all_wins = wins_row + wins_column + wins_diagonal
    for combo in all_wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            if board[combo[0]] == 'X':
                print(f"{player1} wins!")
                return True
            elif board[combo[0]] == 'O':
                print(f"{player2} wins!")
                return True
            
    return False
        
def make_move(position, symbol):
    global board
    board = tuple(symbol if i == position else board[i] for i in range(9))
    print_board()
    return winning_combinations()


count = 0
isWin = False;
while count < 9:
    if count == 0 or count == 2 or count == 4 or count == 6 or count == 8:
        player1_move = int(input(f"{player1}, enter your move (0-8): "))
        if board[player1_move] != player1_move:
            print("Invalid move. Try again,")
            continue
        isWin = make_move(player1_move, 'X')
    else:
        player2_move = int(input(f"{player2}, enter your move (0-8): "))
        if board[player2_move] != player2_move:
            print("Invalid move. Try again.")
            continue
        isWin = make_move(player2_move, 'O')
    if isWin :
        break
    count += 1

if not isWin:    
    print("It's a draw!")



