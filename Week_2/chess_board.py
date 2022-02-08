class board:
	def __init__(self, board_dimensions=[8, 8]):
		self.board_dimensions = board_dimensions
		self.actual_board = []
	
	# def __str__()
	
	def create_board(self):
		initial_board_instance = self.actual_board
		
		for row in range(self.board_dimensions[0]):
			initial_board_instance.append([])
			for column in range(self.board_dimensions[1]):
				initial_board_instance[-1].append([])
		
		return initial_board_instance
	
if __name__ == "__main__":
	
	my_board = board()
	
	my_board.create_board()