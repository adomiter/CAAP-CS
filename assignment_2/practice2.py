#this program accepts a quiz score as an input and uses a decision structure to calculate the corresponding grade and uses a decision structure to calculate the corresponding grade

def quiz_score(score):
    if score == 5:
        print("A")
    elif score == 4:
        print("B")
    elif score == 3:
        print("C")
    elif score == 2:
        print("D")
    else:
        print("F")
        
def main():
    score = int(input("What is the quiz score?"))
    quiz_score(score)
main()