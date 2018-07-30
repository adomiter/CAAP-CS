#this program accepts a speed limit and a clocked speed and either prints a message indicating the speed was legal or prints the amount of the fine, if the speed is illegal
def speed(speed_limit, clocked_speed)
    if clocked_speed > 90:
        if clocked_speed > speed_limit:
            fine= 250 + ((clocked_speed - speed_limit)*5)
            print("Fine amount: $", fine,"")
        else:
            print("This speed is legal.")
    elif: clocked_speed <= 90:
        if clocked_speed > speed_limit:
            fine= 50 + ((clocked_speed - speed_limit)*5)
            print("Fine amount: $", fine,"")
        else:
            print("This speed is legal.")
            
def main():
    speed_limit= int(input("What is the speed limit?"))
    clocked_speed= int(input("What is the clocked speed?"))
    speed(speed_limit, clocked_speed)
main()