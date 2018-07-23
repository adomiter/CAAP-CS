# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = 0 
name = ""
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	score = Score(name, moves)
	if won:
		leaderboard.update(score)
	print ("\nGame Over.")
	leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name 
		global moves 
		print ("Welcome to the Escape Room:Candyland Version. To exit enter :q at any time. Instead of a time limit, you will only have a certain amount of lives. May the odds ever be in your favor!") 
		name = input("\n Please enter your name: > ") 
		if (name == ':q'):
			exit(1)
		dificulty_level= ""
		while True:
			dificulty_level = str(input("Which difficulty level do you want: easy, medium, or hard: ")) 
			if dificulty_level == "easy" or dificulty_level == "medium" or dificulty_level == "hard":
				break 
			else: 
				print("Incorrect input: choose one of the levels listed")
		a_map = Map('Giant_Gummy_Bears') 
		a_game = Engine(a_map, dificulty_level)
		moves = a_game.play()
		game_over(a_game.won())

play_game()


def test_game():
	test_playgame = game_over()
	test_playgame2 = play_game()
test_game() 