# Andrea Domiter
# Lab3

from random import randint

# global variable of chutes and ladders
# remenber to let your function know you're using this variable with 'global'
chutes_ladders = {4 : 7,
					8 : 15,
					12 : 2,
					14: 6}

# Rolls a die of six sides and returns the result
def roll_die():
	return randint(1,6)

# makes a game (just a list) of the given dimensions
def makeGame(w, l):
    game_board = []
    for i in range((w*l)):
        game_board.append(i+1)
    print(game_board)

# checks if given square is a chutes or ladders
def is_chutes_ladders(d):
    global chutes_ladders
    for i in chutes_ladders:
        if i == d:
            return True
    return False

# function to make and play a game
def play_game(mode, w, l):
    
        
    if mode == 1:

        w = int(input("Enter a width: "))
        l = int(input("Enter a length: "))
        makeGame(w, l)
        players = int(input("How many players?: "))
        state = []
        for i in range(players):
            players_name= input("What is player %s's name?" %(i+1))
            state.append({"Player":players_name, "Player_State":1,"Moves":0})
        print(state)
        gameover = False
        while gameover == False:
            for player in range(players):
                print("It is Player",player+1,"'s turn")
                roll = input("Press enter to roll the die")
                die = roll_die()
                print("You rolled a",die,".")
                state[player]['Player_State'] += die
                state[player]['Moves'] += 1
                print("You are now in",state[player]['Player_State'],".")
                if state[player]['Player_State'] in chutes_ladders:
                    state[player]['Player_State'] = chutes_ladders[state[player]['Player_State']]
                if state[player]['Player_State'] > (w*l):
                    gameover == True
                    state[player]['Player_State'] == w*l
                    print("player " + str(player +1) + ": you won!")
                    gameover= True
                    break
  
    else:
        makeGame(w, l)
        position = 1
        moves = 0
        while position < (w*l):
            position += roll_die()
            moves += 1
            if position in chutes_ladders:
                position = chutes_ladders[position]              
            if position >= (w*l):
                print(moves,"moves")
                break

#play_game()

# Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average
#def sim(l,w):
#       makeGame(w, l)
#        position = 1
#       moves = 0
#        while position < (w*l):
#           position += roll_die()
#            moves += 1
#            if position in chutes_ladders:
#                position = chutes_ladders[position]              
#            if position >= (w*l):
#                print(moves,"moves")
#                break

def simulate_game():
    w = int(input("Enter a width: "))
    l = int(input("Enter a length: "))
    times= int(input("How many times do you want to run the game?"))
    sums= []
    for i in range(times):
        sums.append(play_game(2,l,w))
        return sums
    print("The average number of moves it takes to win is",sum(sums)/ len(sums),"moves.")

simulate_game()
    

    