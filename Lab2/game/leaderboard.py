# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 10
	board = []

	def __init__(self):
		for i in range(self.size):
			self.board.append(Score("player", i))

	# prints the leaderboard
	def print_board(self):
		print("High Scores:")
		print()
		for entry in self.board:
			player = entry.get_name()
			score = entry.get_score()
			print(player+ ": ", score)

	# checks if given score should be in the leaderboard
	def update(self, score):
		i=0
		newScore = score.get_score()
		newName = score.get_name()
		for entry in self.board:
			if (score.get_score() >= entry.get_score()):
				self.board[i].set_score(newScore)
				self.board[i].set_name(newName)
				break
			i += 1

	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank


