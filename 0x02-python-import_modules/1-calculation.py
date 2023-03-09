#!/usr/bin/python3

if __name__ == "__main__":
	""" print the sum, sub, mil and div od 10 by 5 """
	from calculator_1 import add, sub, div, mul

	a = 10
	b = 5

	print("{} + {} = {}".format(a, b, add(a, b)))
	print("{} - {} = {}".format(a, b, sub(a, b)))
	print("{} / {} = {}".format(a, b, div(a, b)))
	print("{} * {} = {}".format(a, b, mul(a, b)))
