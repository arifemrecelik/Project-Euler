def isPalindrome(n):
	if str(n) == str(n)[::-1]:
		return True
	return False

n = 0

for i in range(999, 99, -1):
	for j in range(i, 99, -1):
		x = i * j
		if x > n:
			if isPalindrome(x):
				n = x

print(n)				