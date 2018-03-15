import math

def largestPrimeFactor(n):
	i = 2

	while i*i < n:
		while n % i == 0:
			n = n / i
		i = i + 1 
	
	return n

def isPrime(n):
	if n % 2 == 0 and n > 2:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True		

limit = int(input("Enter the limit: "), 10)

n = 1

for i in range(2, limit + 1, 1):
	if isPrime(i):
		n = n * i	
