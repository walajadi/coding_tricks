from abc import ABCMeta, abstractmethod

class A(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.items = []

	@abstractmethod
	def add_items(self, x):
		pass


class B(A):
	def add_item(self, x):
		self.items.append(x)

if __name__ == '__main__':
	b = B()
	b.add_item('foo')
	a = A()

"""
what happen?

1. Exception at 'a' creation.
2. Exception at 'b' creation.
3. Exception when adding element to b.
4. b.items equal to [1]
"""
