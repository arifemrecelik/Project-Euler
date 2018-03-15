import math

result1 = 0
result2 = 0
finalResult = 0

limit = int(input("Enter the limit: "), 10)

for i in range(1, limit+1):
	result1 += i**2

for i in range(1, limit+1):
	result2 += i
result2 *= result2	

finalResult = result2 - result1
print (finalResult)	