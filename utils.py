# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import *
import scipy.integrate as integrale



def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	
	try :
		return factorial(n)
		
		
	except :
		raise ValueError

	
	

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + c = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	try :
		x1 = (-b + sqrt(b**2-4*a*c))/2*a
		x2 = (-b - sqrt(b**2-4*a*c))/2*a
		return x1, x2
		
		
	except :
		raise ValueError
def func(x):
	return x**2

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' andrr
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	try: 
		func = lambda x:eval(function)
		result = integrale.quad(func,lower,upper)
		return result
	except:
		raise ValueError

if __name__ == '__main__':
	print(fact(7))
	print(roots(1, 6, 1))
	print(integrate('x**2', -1, 1))
