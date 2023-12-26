game_over = False
size = 3
board = [[0 for x in range(size)] for y in range(size)]
def print_board():
	for i in range(len(board)):
		print(board[i])
	return board
def check_win():
	global game_over
	if board[row][0]==board[row][1]==board[row][2]== turn:
		print('player {} you win!!!'.format(turn))
		game_over = True
	elif board[0][col]==board[1][col]==board[2][col]== turn:
		print('player {} you win!!!'.format(turn))
		game_over = True
	elif board[0][0] == board[1][1] == board[2][2] == turn:
		print('player {} you win!!!'.format(turn))
		game_over = True
	elif board[2][0] == board[1][1] == board[0][2] == turn:
		print('player {} you win!!!'.format(turn))
		game_over = True
				
turn = 0
print_board()
while not game_over:
	try:
		if turn == 0:
			row = int(input('player 1 select your row: ')) - 1
			col = int(input('player 1 select your collum: ')) - 1
		else:
			row = int(input('player 2 select your row: ')) -1
			col = int(input('player 2 select your collum: ')) -1
		if board[row][col] == 0:
			turn += 1
			board[row][col] = turn
			check_win()
			print_board()
			turn %= 2
		else:
			print("you can't chose that spot please try again")
	except IndexError:
		print('please type a interger from 1-3')
	except ValueError:
		print('please type a interger from 1-3')
