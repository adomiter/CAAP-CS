# imports random madule form library
from random import randint

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class GiantGummyBears(Scene):
	
	name = 'Giant_Gummy_Bears'

	def enter(self):
		print("The Giant Gummy Bears of Candyland have invaded your town. As mayor, it is up to you to save your people.")
		print("You have limited reserves of food and water. Also, you have no weapons.")
		return self.action()
		
		
	def action(self):
		print ("What will you do?")
		print ("1. Feed the Giant Gummy Bears your last supply of food and water")
		print ("2. Try to make peace through conversing with their leaders")
		print ("3. Take your people and escape")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Oh no, you don't have enough food or water to satisfy their hunger.")
			print ("It is too late to turn back now.")
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Unfortunately, you do not speak their language and insult the leader.")
			print ("Their leader is angry and sends his men after you.")
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("Lucky for you, you all made it out in time before the Giant Gummy Bears noticed.")
			print ("The Giant Gummy Bears have successfully taken over your town though.")
			return self.exit_scene('Candy_House') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class CandyHouse(Scene):
	
	name = 'Candy_House'

	def enter(self):
		print ("You and your people have been walking for days and have finished your supply of food and water. It is not long before the hunger becomes unbearable and the dehydration kicks in.")
		print ("Luckily, you have stumbled upon a house made of what seems to be candy. The gate is wide open and you walk up to the front door. Oh no! It's locked.")
		return self.action()

	def action(self):
		print ("However, there's a keypad lock on the door.")
		print ("If you get the code wrong 10 times, then the door closes forever and you will have to keep walking.")
		code = [randint(0,9), randint(0,9), randint(0,9)]
		guesses = 0
		# loop to check three random integers, one at a time
		for i in range(3):
			print ("Enter digit %d." % (i+1))
			guess = input("[keypad]> ")
			if guess == ':q':
				return self.exit_scene(guess)
			try:
			   guess = int(guess)
			except ValueError:
			   print("That's not an int!")
			   return self.exit_scene(self.name)
			while int(guess) != code[i] and guesses <10:
				print ("BZZZZEDDD!")
				guesses += 1
				guess =input("[keypad]> ")
				if guess == ':q':
					return self.exit_scene(guess)
				try:
				   guess = int(guess)
				except ValueError:
				   print("That's not an int!")
				   guess = -1
		
		if guesses < 10:
			print ("The door opens and your people cheer.")
			print ("Now, you need to explore the house. You send your bravest people into the house to investigate.")
			return self.exit_scene('the_liquid')
		else:
			print ("The lock buzzes one last time and then you hear a latch open above you.")
			print ("A bag of flour falls on your head and you hit the steps.")
			return self.exit_scene('death') # raise ValueError ('todo')

	def exit_scene(self, outcome):
		return outcome 
			
class TheLiquid(Scene):
	
	name ='the_liquid'

	def enter(self):
		print ("Your bravest people have entered the house. It is completely empty. They discover that the walls inside are made of candy and all kinds of sweets.")
		print ("They move into the kitchen and discover jars of liquid in the refrigerator.")
		print ("There are 5 jars. They call you in and wait for your orders.")
		return self.action()
	
	def action(self):
		print ("What will you do?")
		print ("1. Choose 1 jar and have everyone take a sip from it")
		print ("2. Pour a little liquid from each jar onto the plants outside")
		print ("3. Eat the candy walls and get out of there")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Uh oh, you don't realize that the jar you chose contains a chemical that turns people into zombies.")
			print ("The first 5 people to drink from it become zombies and turn on the rest of you. You run, but they are too quick.")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("Hooray! You discover that four of the jars contain a chemical that kills the plants, but the last one has water.")
			print ("Each one of you take a sip from the jar and continue on your journey.") 
			return self.exit_scene('new_home') 
		elif int(choice) == 3:
			print ("Shooters! The candy walls are poisonous as well! You become fatally ill.")
			print ("The disease spreads quickly and the rest of your people become sick also.")
			return self.exit_scene('death')
		else:
			print ("Error 404! Choose an option or type :q to end game") 
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome 

class NewHome(Scene):
	
	name = 'new_home'

	def enter(self):
		print ("You and your people walk for 3 hours and come to a crossroads. There are 5 different roads you can take. It is dark and you can't see down the roads. Only one will lead you to paradise. The other 4 will lead you to the homes of the killer Giant Gummy Bears.")
		print ("Everyone looks at you to make a decision.")
		return self.action()


	def action(self):
		print ("There's 5 roads, which one do you take?")
		good_road = randint(1,5)
		guess = input("[road ")

		if guess == ':q':
			return self.exit_scene(guess)
		try:
		   guess = int(guess)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)
		   
		if int(guess) != good_road:
			print ("You walk down road %s."% guess)
			print ("You are only a mile down the road when you see eyes looking at you.")
			return self.exit_scene('death')
		else:
			print ("You walk down road %s."% guess)
			print ("You walk for hours until the sun rises. The light reveals a clearing with a waterfall running through it. This is your new home.")
			return self.exit_scene('finished')

	def exit_scene(self, outcome):
		return outcome 



