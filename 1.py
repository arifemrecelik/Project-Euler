x = int(input("Enter the number: "), 10)
result = 0

for i in range(1,x):
	if i % 3 == 0:
		result += i
	elif i % 5 == 0:
		result += i

print(result)		