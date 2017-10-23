class MyClass(object):
	def __init__(self):
		self.__x = None

	def set(self, x):
		self.__x = x

	def print_me(self):
		print(self.__x)


if __name__ == '__main__':
	y = MyClass()
	y.set(1)
	y.print_me()

	try:
		y.__MyClass__x = 10
		y.print_me()
	except:
		print('This won\'t work dude 1')

"""
What's the output ?
1. 1 and 1 
2. 1 and 'not working'
3. 1 and 10

"""
