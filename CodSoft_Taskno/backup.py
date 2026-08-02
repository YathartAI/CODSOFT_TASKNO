# CODSOFT TASK 2.
# Tic Tac Toe. 
import random


print("="*50)
print("🎮 Welcome to Tic Tac Toe Ai 🎮!")
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
    print("\n🤖 AI is making a move...")

    available_moves = []

    for i in range(9):
        if Board[i] not in ["X", "O"]:
            available_moves.append(i)

    if available_moves:
        move = random.choice(available_moves)
        Board[move] = "O"


        print_board()


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


if __name__ == "__main__":
    while True:
        print_board()

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

        