import sys


fibCache = {0:0, 1:1}


def fibonacci(n):
	if fibCache.has_key(n):
		return fibCache[n]
	else:
		fibCache[n] = fibonacci(n-1) + fibonacci(n-2)
	return fibCache[n] 

def main():
	sum = 0
	i = 0
	while(1):
		fib = fibonacci(i)
		if fib > 4000000:
			break
		if fib % 2 == 0:
			print fib		
			sum += fib
		i += 1

	print "the sum is:"
	print sum


if __name__ == "__main__":
	main()