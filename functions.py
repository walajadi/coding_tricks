def my_func(a, b, *args, **kwargs):

	if a is None:
		print 'a'

	if b is None:
		print 'b'

	if args :
		print 'args'

	if kwargs:
		print 'kwargs'


my_func(None, 5, 10, 20)

"""
What's the output ?
1. a, b, args, kwargs.
2. a, args
3. a, args, kwargs 
"""