# importing random int maker module
from random import randint

# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
	quips = ["Unfortunately, you died."
			"Try again.",
			"Wow, I didn't know someone could be so bad at this.",
			"You dead",
			"Better luck next time."
            ]

	def enter(self):
		print (Death.quips[randint(0, len(self.quips)- 1)])
		return 'died'


def test_death():
    test_death = Death()

test_death()