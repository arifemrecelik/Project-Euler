def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

limit = int(input("Enter the fibonacci limit: "), 10)
result = 0
i = 2

while (fib(i) < limit):
	if fib(i) % 2 == 0:
		result += fib(i)	
	i += 1

print(result)				