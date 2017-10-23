from threading import RLock

lock = RLock()

def fac_recursive(n):
	lock.acquire()
	if n == 1:
		return n
	else:
		return n * fac_recursive(n-1)

if __name__ == '__name__':
	print fac_recursive(5)

"""
what's the output ?
1. 120
2. code blocked to due to the lock in the second recursion
3. after the lock, it prints 120
4. Exception raised

"""