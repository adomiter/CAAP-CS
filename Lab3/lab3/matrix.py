# takes the number of rows and columns and makes a matrix of those dimensions
def make_matrix(r, c):
    matrix = [0] * r
    for i in range(r):
        matrix[i] = [0] * c
    return(matrix)
#makes a matrix with 0s



# takes two matrices and multiplies them returnin the resulting matrix
def matrixmult(a,b):
    if len(a[0]) == len(b):
        mult = make_matrix(len(a), len(b[0]))
        for i in range(len(mult)):
	        for j in range(len(mult[0])):
	            temp_variable = 0
            for n in range(len(b)):
		        result[i][j] += float(a[i][n]) * float(b[n][j])
	return result
    else:
	return []
# because the make_matrix function outputs a matrix with zeros the mult. will be 0 for all values
#tried to hardcode the function and multiply it that way
#This function was taken from this website: https://www.pythoncentral.io/multiply-matrices-python/
#I received help from another student who explained the function to me

# prints the given matrix, mostly for testing purposes

def print_matrix(m):
	print(matrixmult(a,b))

# given a state matrix, and a transition matrix, runs a markov simulation of the game and returns average number of moves.  
def markov_simulation(initial_matrix, transition_matrix, simulation_number):
    value = 0
    for i in range(simulation_number):
        loop = True
        moves = 0
        temporary_matrix = matrixmult(initial_matrix, transition_matrix)
	    while loop == True:
		temp_matrix = matrixmult(temporary_matrix, transition_matrix)
		moves += 1
		if float(temporary_matrix[0][11]) > float(0.99):
		    value += moves
		    loop = False
    return float(value)/simulation_number
    #received help from other students
    #runs a markov simulation
    

#tried hardcoding the function
#init_matrix = [
#        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
 #       ]

#transit_matrix = [
#       [0, 1/6, 1/6, 1/6, 1/6, 1/3, 0, 0, 0, 0, 0, 0],
#      [0, 0, 1/6, 1/6, 1/6, 1/3, 0, 0, 0, 0, 1/6, 0],
#     [0, 0, 0, 1/6, 1/6, 1/3, 1/6, 0, 0, 0, 1/6, 0],
#        [0, 0, 0, 0, 1/6, 1/6, 1/6, 1/6, 1/6, 0, 1/6, 0],
#        [0, 1/6, 0, 0, 0, 1/6, 1/6, 1/6, 1/6, 0, 1/6, 0],
#        [0, 1/6, 0, 0, 0, 0, 1/6, 1/6, 1/6, 1/6, 1/6, 0],
#        [0, 1/6, 0, 0, 1/6, 0, 0, 1/6, 1/6, 1/6, 1/6, 0],
#        [0, 1/6, 0, 0, 1/6, 0, 0, 0, 1/6, 1/6, 1/6, 1/6],
#        [0, 1/6, 0, 0, 1/6, 0, 0, 0, 0, 1/6, 1/6, 1/3],
#        [0, 0, 0, 0, 1/6, 0, 0, 0, 0, 0, 1/6, 2/3],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#    ]
    
    
