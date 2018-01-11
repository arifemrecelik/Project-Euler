def isPrime(n):
	temp = int(n/2) + 1	

	if n==2:
		return True

	for i in range(2, temp+1):
		if n % i == 0:
			return False

	return True

def largestPrimeFactor(n):
	i = 2

	while i*i < n:
		while n % i == 0:
			n = n / i
		i = i + 1 
	
	print(n)

print(largestPrimeFactor(600851475143))