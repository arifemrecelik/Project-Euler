import math

result = 0

def isPrime(n):
	if n % 2 == 0 and n > 2:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True	

limit = int(input("Enter the limit: "), 10)

for i in range(1,limit):
	if isPrime(i):
		result += i

print(result-1)		