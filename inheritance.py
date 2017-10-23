
class A(object):
	def __init__(self):
		print('A constructor')

class B(A):
	def __init__(self):
		print('B constructor')
		super(B, self).__init__()

class C(A):
	def __init__(self):
		print('C constructor')
		super(C, self).__init__()

class D(C, B):
	def __init__(self):
		print('D constructor')
		super(D, self).__init__()

if __name__ == '__main__':
	d = D()


"""
What's the output ?
1. D constructor
C constructor
B constructor
A constructor

2. D constructor
B constructor
C constructor
A constructor

3. D constructor

4. D constructor
C constructor
"""