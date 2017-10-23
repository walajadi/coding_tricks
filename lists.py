x = [5,4, 3, 2, 1]
y = sorted(x)
z = list(set(x))

if __name__ == '__main__':
	for i in range(len(y)):
		if y[i] == z[i]:
			print('different')
			break
	print('same')

"""
what's the output ?
1. different and same 
2. same
3. different x 5 and same
4. exceptions raised.
"""
