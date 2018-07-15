#computes the nth Fibonacci number where n is a value input by the user 
def fib1(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fib1(n-1)+fib1(n-2)
    

def main():
    nth_term=eval(input("What is the value of n where n is the nth Fibonacci number? "))
    print("If n= %s then the result is %s." % (nth_term, fib1(nth_term))) 
main()    
