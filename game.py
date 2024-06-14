def print_board(board):
    # Function to print the Tic Tac Toe board
    for row in board:
        print("|".join(row))  # Join the elements of the row with '|' and print the row
        print("-----")  # Print a separator line after each row

def check_win(board, player):
    # Function to check if the current player has won
    # Check rows
    for row in board:
        if row == [player, player, player]:
            return True
    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)] == [player, player, player]:
            return True
    # Check diagonals
    if [board[i][i] for i in range(3)] == [player, player, player]:
        return True
    if [board[i][2-i] for i in range(3)] == [player, player, player]:
        return True
    return False

def tic_tac_toe():
    # Initialize an empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']  # Define the two players
    current_player = 0  # Start with the first player ('X')

    while True:
        print_board(board)  # Print the current state of the board
        print(f"Player {players[current_player]}'s turn.")  # Announce which player's turn it is

        # Get player move
        row = int(input("Enter row (0, 1, or 2): "))  # Prompt the player to enter the row number
        col = int(input("Enter column (0, 1, or 2): "))  # Prompt the player to enter the column number

        # Check if move is valid
        if board[row][col] == " ":
            board[row][col] = players[current_player]  # Place the player's marker on the board

            # Check for a win
            if check_win(board, players[current_player]):
                print_board(board)  # Print the final state of the board
                print(f"Player {players[current_player]} wins!")  # Announce the winner
                break  # Exit the game loop

            # Check for a draw
            if all(cell != " " for row in board for cell in row):
                print_board(board)  # Print the final state of the board
                print("It's a draw!")  # Announce the draw
                break  # Exit the game loop

            # Switch players
            current_player = 1 - current_player  # Switch to the other player
        else:
            print("Invalid move. Try again.")  # Inform the player that the move is invalid and prompt again

# Run the game
tic_tac_toe()  # Start the Tic Tac Toe game by calling the tic_tac_toe function
