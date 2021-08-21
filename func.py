def add(n):
	if n<=1:
		return n
	return n+add(n-1)

def factorial(n):
<<<<<<< HEAD
	prod = 1
	for x in range(1,n+1):
		prod*=x
	return prod

if __name__=="__main__":
	print(add(5))
	print(factorial(5))
=======
	if n<=1:
		return n
	return n*factorial(n-1)

if __name__=="__main__":
	print(add(5))
	print("HELLO WORLD")
>>>>>>> recursiveadd
