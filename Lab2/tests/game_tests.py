# importing package to be able to run the tests
from nose.tools import *
# Here you should import all the modules/classes you want to test
from game.scores import Score
from leaderboard import Leaderboard
from death import Death
import scenes as S
from map import Map
from random import randint


# define a function like these for each class/module you test.
def test_scores():
    test_score = Score("andrea", 1)
    if ("andrea" == test_score.get_name()):
    	print("it works")
    else:
    	raise ValueError("Doesn't work")

test_scores()

def test_leaderboard():
    test_board = Leaderboard
    test_board.print_board()
    test_board.update(Score("andrea", 45))
    test_board.print_board()

tests()

def test_death():
    test_death = Death()

test_death()


def test_scenes():
    test_scene1=GiantGummyBears()
    test_scene1.enter()
    test_scene1.action()
    test_scene1.exit_scene()

    test_scene2=CandyHouse()
    test_scene2.enter()
    test_scene2.action()
    test_scene2.exit_scene()

    test_scene3=TheLiquid()
    test_scene3.enter()
    test_scene3.action()
    test_scene3.exit_scene()

    test_scene4=NewHome()
    test_scene4.enter()
    test_scene4.action()
    test_scene4.exit_scene()

test_scenes()

def test_game():
	test_playgame = game_over()
	test_playgame2 = play_game()
test_game() 

def test_map():
	test_maps = Map()
	test_maps.__init__()
	test_maps.next_scene()
	test_maps.opening_scene()

test_map()
# etc...