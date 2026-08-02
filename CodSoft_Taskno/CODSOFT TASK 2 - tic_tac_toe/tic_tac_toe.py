# CODSOFT TASK 2.
# Tic Tac Toe. 
import time


print("="*50)
print("🎮 Welcome to Tic Tac Toe Ai 🎮!")
print("🧑‍💻 Developed by yatharth Singhal")
print("="*50)



Board = ["1", "2", "3", 
         "4", "5", "6", 
         "7", "8", "9"]
  # Represents the 3x3 Tic Tac Toe board




def print_board():
    """Prints the current state of the Tic Tac Toe board."""
    print("\n")
    print(f" {Board[0]} | {Board[1]} | {Board[2]} ")
    print("---+---+---")
    print(f" {Board[3]} | {Board[4]} | {Board[5]} ")
    print("---+---+---")
    print(f" {Board[6]} | {Board[7]} | {Board[8]} ")
    print("\n")

    

def player_move():
    while True:
        try:
            choice = int(input("\n🎯 Enter your move (1-9): "))

            if 1 <= choice <= 9:

                if Board[choice - 1] not in ["X", "O"]:
                    Board[choice - 1] = "X"
                    break

                else:
                    print("❌ Position already occupied!")

            else:
                print("❌ Enter a number between 1 and 9.")

        except ValueError:
            print("❌ Please enter a valid number.")



def computer_move():

    print("\n🤖 AI is thinking...")
    time.sleep(1)

    move = best_move()

    if move is not None:
        Board[move] = "O"

        print_board()


def reset_board():
    global Board
    Board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]
    


def check_winner(player):

    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for combination in winning_combinations:
        if (Board[combination[0]] == player and
            Board[combination[1]] == player and
            Board[combination[2]] == player):
            return True

    return False

def check_draw():
    for cell in Board:
        if cell not in ["X", "O"]:
            return False
    return True

def available_moves():
    moves = []

    for i in range(9):
        if Board[i] not in ["X", "O"]:
            moves.append(i)

    return moves

def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if check_draw():
        return 0

    if is_maximizing:

        best_score = -1000

        for move in available_moves():

            temp = Board[move]
            Board[move] = "O"

            score = minimax(False)

            Board[move] = temp

            best_score = max(best_score, score)

        return best_score

    else:

        best_score = 1000

        for move in available_moves():

            temp = Board[move]
            Board[move] = "X"

            score = minimax(True)

            Board[move] = temp

            best_score = min(best_score, score)

        return best_score


def best_move():
    best_score = -1000
    move = None

    for i in available_moves():
        temp = Board[i]
        Board[i] = "O"

        score = minimax(False)

        Board[i] = temp

        if score > best_score:
            best_score = score
            move = i

    return move

    


if __name__ == "__main__":
    while True:
        reset_board()
        print_board()

        while True:
            player_move()

            if check_winner("X"):
                print_board()
                print("🎉 Congratulations! You Win!")
                break

            if check_draw():
                print_board()
                print("🤝 It's a Draw!")
                break

            computer_move()

            if check_winner("O"):
                print_board()
                print("🤖 AI Wins!")
                break

            if check_draw():
                print_board()
                print("🤝 It's a Draw!")
                break

            print_board()

        again = input("\n🔄 Play Again? (y/n): ").lower()

        if again != "y":
            print("\n==========================================")
            print("🎉 Thanks for playing Tic-Tac-Toe AI!")
            print("👨‍💻 Developed by Yatharth Singhal")
            print("==========================================")
            break