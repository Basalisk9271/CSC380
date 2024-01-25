#include <iostream>
#include <string>
using namespace std;

enum Player
{
	Human = -1,
	Blank = 0,
	Computer = 1
};

// Function to print the board with colorful 
void printBoard(Player board[])
{

	// The "\e[34m" just colors the text
	// 34 colors the X's blue
	// 31 colors the O's red
	// 0 resets the colors back to normal
	for (int i = 0; i < 9; i++)
	{
		if ((i == 2) || (i == 5) || (i == 8))
		{
			if (board[i] == -1)
				cout << "\e[34m X\e[0m";
			else if (board[i] == 1)
				cout << "\e[31m O\e[0m";
			else
				cout << "  ";
		}
		else
		{
			if (board[i] == -1)
				cout << "\e[34m  X \e[0m|";
			else if (board[i] == 1)
				cout << "\e[31m  O \e[0m|";
			else
				cout << "    |";
		}
		if (((i + 1) % 3 == 0) && (i != 8))
		{
			cout << endl
				 << "----|----|----" << endl;
		}
		if (i == 8)
			cout << endl;
	}
}

// Checks the board to see if there is a winner. Used to determine who won the game overall
bool checkWinner(Player board[])
{
	// Check rows and columns
	for (int i = 0; i < 3; ++i)
	{
		// Check rows
		if (board[i * 3] != Blank && board[i * 3] == board[i * 3 + 1] && board[i * 3 + 1] == board[i * 3 + 2])
			return true;

		// Check columns
		if (board[i] != Blank && board[i] == board[i + 3] && board[i + 3] == board[i + 6])
			return true;
	}

	// Check diagonals
	if (board[0] != Blank && board[0] == board[4] && board[4] == board[8])
		return true;
	if (board[2] != Blank && board[2] == board[4] && board[4] == board[6])
		return true;

	return false;
}

// Checks to see if the board is full; if it is, then it returns true and helps to determine if the game was a draw
bool isBoardFull(Player board[])
{
	for (int i = 0; i < 9; ++i)
	{
		if (board[i] == Blank)
		{
			return false;
		}
	}
	return true;
}

// Function to check if a player has two in a row and returns the index of the value
int hasTwoInARow(Player board[], Player player)
{
	// Check rows and columns
	for (int i = 0; i < 3; ++i)
	{
		// Check rows
		if (board[i * 3] == player && board[i * 3 + 1] == player && board[i * 3 + 2] == Blank)
			return i * 3 + 2;
		if (board[i * 3] == player && board[i * 3 + 1] == Blank && board[i * 3 + 2] == player)
			return i * 3 + 1;
		if (board[i * 3] == Blank && board[i * 3 + 1] == player && board[i * 3 + 2] == player)
			return i * 3;

		// Check columns
		if (board[i] == player && board[i + 3] == player && board[i + 6] == Blank)
			return i + 6;
		if (board[i] == player && board[i + 3] == Blank && board[i + 6] == player)
			return i + 3;
		if (board[i] == Blank && board[i + 3] == player && board[i + 6] == player)
			return i;
	}

	// Check diagonals
	if (board[0] == player && board[4] == player && board[8] == Blank)
		return 8;
	if (board[0] == player && board[4] == Blank && board[8] == player)
		return 4;
	if (board[0] == Blank && board[4] == player && board[8] == player)
		return 0;

	if (board[2] == player && board[4] == player && board[6] == Blank)
		return 6;
	if (board[2] == player && board[4] == Blank && board[6] == player)
		return 4;
	if (board[2] == Blank && board[4] == player && board[6] == player)
		return 2;

	return -1;
}

// Function to make a move based on the provided rules in the provided order
int makeMove(Player board[])
{
	// Rule 1: If there is a move that creates two lines of two in a row, play that.
	int check = hasTwoInARow(board, Computer);
	if (check != -1)
	{
		return check;
		// If no immediate winning move for the Computer, proceed to other rules
	}

	// Rule 2: If your opponent has two in a row, play on the remaining square.
	check = hasTwoInARow(board, Human);
	if (check != -1)
	{
		return check;
		// If no immediate winning move for the opponent, proceed to other rules
	}

	// Rule 3: If the center square is free, play there.
	if (board[4] == Blank)
	{
		return 4;
	}

	// Rule 4: If your opponent has played in a corner, play in the opposite corner.
	if (board[0] == Human && board[8] == Blank)
	{
		return 8;
	}
	if (board[2] == Human && board[6] == Blank)
	{
		return 6;
	}
	if (board[6] == Human && board[2] == Blank)
	{
		return 2;
	}
	if (board[8] == Human && board[0] == Blank)
	{
		return 0;
	}

	// Rule 5: If there’s an empty corner, play there.
	for (int i = 0; i < 9; i += 2)
	{
		if (board[i] == Blank && i != 4)
		{
			return i;
		}
	}

	// Rule 6: Otherwise, play on an empty square.
	for (int i = 0; i < 9; ++i)
	{
		if (board[i] == Blank)
		{
			return i;
		}
	}

	return -1; // Error, should not reach here
}

// Function to play the game until one of the players wins
void playGame(Player board[]) {

    while (true) {
        // Human move
        int humanMove;
        cout << "Enter your move (1-9): ";
        cin >> humanMove;
		cout << endl;
        board[humanMove - 1] = Human;
        printBoard(board);
		cout << endl;
        if (checkWinner(board)) {
            cout << "You win!" << endl;
            break;
        }
        if (isBoardFull(board)) {
            cout << "It's a draw!" << endl;
            break;
        }

        // Computer move
        int computerMove = makeMove(board);
        board[computerMove] = Computer;
        cout << "Computer moves to " << computerMove + 1 << "\n" << endl;
        printBoard(board);
		cout << endl;

        if (checkWinner(board)) {
            cout << "Computer wins!\n" << endl;
            break;
        }
        if (isBoardFull(board)) {
            cout << "It's a draw!\n" << endl;
            break;
        }
    }
}

// Main driving function to call the "bones" of the game as needed. 
// Some functions are self regulating like playGame() but others need to be called. 
// This is also where the game baord is initialized. 
int main()
{
	char play = 'Y';
	
	while (tolower(play) == 'y')
	{
		// Initialize the tic-tac-toe board as blanks
		Player board[9] = {Blank, Blank, Blank, Blank, Blank, Blank, Blank, Blank, Blank};
		cout << endl;
		printBoard(board);
		cout << endl;
		playGame(board);
		cout << "Do you want to play again? (Y/N) ";
		cin >> play;
		cout << endl;
	}
	return 0;
}
