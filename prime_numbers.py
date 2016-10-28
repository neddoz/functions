import math

for num in range(0,101):
    if is_prime(num):
        print(num)

def is_prime(n):
	if n<2:
		return false
	elif
	    for i in range(2, int(math.sqrt(n)) + 1):
	        if n % i == 0:
	            return False
    return True