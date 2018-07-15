#this program calculates the minimum number of coins required to give a user change
def change():
    remain=eval(input("What is the total change in dollars? "))
    remain *= 100
    total=0
    dollars = (0.25, 0.10, 0.05, 0.01)
    for i in dollars:
        change, remain = divmod(remain, i*100)
        print("$%s: %s" % (i,int(change)))
        total += change
    print("The total number of coins is %s." % (int(total)))
change()