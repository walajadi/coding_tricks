

class MyClass(object):

	def _show(self):
		print('show')

	def __notshow(self):
		print('not show')

	def call_notshow(self):
		print(self.__notshow())

class MyClass2(object):

	def __init__(self):
		self.__x = None

	def set(self, x):
		self.__x = x

	def print_me(self):
		print(self.__x)

def new_print_me():
	print(100)


if __name__ == '__main__':
	y = MyClass2()
	setattr(y, 'print_me', new_print_me)
	y.set(10)
	y.print_me()

"""
what's the output ?

1. print_me
2. 10
3. exception raised
4. 100

"""
