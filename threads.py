from threading import RLock
import _thread
import time

lock = RLock()

def fac_recursive(n):
	lock.acquire()
	if n == 1:
		return n
	else:
		return n * fac_recursive(n-1)

def print_time(thread_name, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print("{} : {}".format(thread_name, time.ctime(time.time())) )




# if __name__ == '__name__':
	# print fac_recursive(5)

	"""
	what's the output ?
	1. 120
	2. code blocked to due to the lock in the second recursion
	3. after the lock, it prints 120
	4. Exception raised

	"""
try:
	_thread.start_new_thread(print_time, ("Thread-1", 2))
	_thread.start_new_thread(print_time, ("Thread-2", 4))
except:
	print("Error: unable to start thread")

while True:
	pass

