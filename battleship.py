from random import randint

board = []

#Create a board
for x in range(5):
  board.append(["O"] * 5)

#Remove all the quotes
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

#Set where the battleship will go
def random_row(board):
  return randint(1, len(board))

def random_col(board):
  return randint(1, len(board[0]))

ship_row = random_row(board)
ship_col = random_col(board)

#Comment the following two lines when playing so no one knows
print ship_row
print ship_col



#Makes game 4 turns long unless you win
def run_game():
  for turn in range(4):
      print "Turn", turn
      guess_row = int(raw_input("Guess Row: "))-1
      guess_col = int(raw_input("Guess Col: "))-1

      if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    
      else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
          print "Oops, that's not even in the ocean."

        elif(board[guess_row][guess_col] == "X"):
          print "You guessed that one already."

        elif((guess_row - ship_row == 1 or guess_row - ship_row == -1) and (guess_col - ship_col == 1 or guess_col - ship_col == -1)):
      	  print "Close, but no cigar!"
      	  print "You missed my battleship!"
          board[guess_row][guess_col] = "X"

        else:
          print "You missed my battleship!"
          board[guess_row][guess_col] = "X"

        if turn == 3:
          print "Game Over"
          print "Ship was at", ship_row, ship_col

        print "Turn", turn + 1
        print_board(board)

run_game()