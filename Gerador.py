def fib(max):
	x, y = 1, 1
	while  x < max:
		yield x
		x, y = x, x + y

gen = fib(10)
'''
print(next(gen)
print(next(gen)
print(next(gen)
print(next(gen)
print(next(gen)'''

for i in gen:
	print(i, end='')