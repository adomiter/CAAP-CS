def sumN(n):
	sum=0
	while (n>0):
		sum=sum+n
		n=n-1
	print("The sum of the first n natural numbers is %s." %(sum))

def sumNCubes(n):
	sum=0
	for i in range(1, n+1):
		sum += i**3
	print("The sum of the cubes of the first n natural numbers is %s." %(sum))

def main ():
	n = int(input("Enter a positive integer: "))
	sumN(n)
	sumNCubes(n)
main()