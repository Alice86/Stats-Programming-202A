# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


""" arithmetics """
print 2 + 2
print 50 - 5*6
print (50 - 5.0*6) / 4
print 8 / 5.0
print 8 / 5
# power **
5**2

""" floating vs int """
# operators with mixed type operands convert the integer operand to floating point

# int / int -> int
print 17 / 3
# int / float -> float
print 17 / 3.0 
# the % operator returns the remainder of the division
print 17 % 3
# print and combine string and arithmetics
print '5 * 3 + 2 = ', 5 * 3 + 2

"""" variables """
width = 20
height = 5 * 9
width * height
print 'width * height =', width * height

""" Lists """
# most versatil, comma-separated values (items) between square brackets
# might contain items of different types, but usually of the same type.
squares = [1, 4, 9, 16, 25]
print squares

""" Indexing, slicing, modification, length """
# Indexing from 0
# Indices may also be negative, to start counting from the right
# -0 is the same as 0, negative indices start from -1.
print squares[0]
print squares[-3] 

# slicing, obtain a sublist of items. 
# defaults: omitted first index defaults to 0, omitted second index defaults to the size of the list
print squares[0:2] # items from position 0 (included) to 2 (excluded) 
print squares[:3] # items from the beginning to position 3 (excluded print squares[-3:] # slicing returns a new list
print squares[:]

# Modification & appending: mutable type
# the item in position 0
cubes = [1, 8, 27, 65, 125] # something’s wrong here, the cube of 4 is 64, not 65! cubes[3] = 6
print cubes
# append() method:
cubes.append(216) # add the cube of 6 
cubes.append(7 ** 3) # and the cube of 7 print cubes

# len()
print len(cubes)

""" Nesting """
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print x
print x[0]
print x[0][1]

""" Loop: while, if, for """
# Fibonacci series
# a = 0
# b = 1
#while (b<10) {
#  print (b)
#  c=a; a=b; b=b+c } 
a, b = 0,1 # multiple assignment: variables a and b simultaneously get new values
while b<10: 
# standard comparison operators the same as in C: < (less than), > (greater than), == (equal to), 
# <= (less than or equal to), >= (greater than or equal to) and != (not equal to).
    # The body of the loop must be indented by the same amount.
    print b
    a, b = b, a+b 
    # expressions on the right-hand side evaluated first before any of the assignments take place
    # right-hand side expressions are evaluated from the left to the right.

# The condition may also be a string or list value
# anything with a non-zero length is true, empty sequences are false; 
# like in C, any non-zero integer value is true; zero is false.


#x = 42
#if (x < 0) {
#  x=0
#  print ("Negative changed to zero")
#} else if (x == 0) {
#  print ("Zero")
#} else if (x == 1) {
#  print ("Single")
#} else {
#  print ("More") } 
    
# elif is short for “else if”, useful to avoid excessive indentation.
x = 42
if x < 0:
    x=0
    print 'Negative changed to zero' 
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'

# Pascal: always iterating over an arithmetic progression of numbers 
# C: giving the user the ability to define both the iteration step and halting condition
# Python: iterates over the items of any sequence (a list or a string), 
#        in the order that they appear in the sequence
# Measure some strings:
#words = c("cat", "window", "defenestrate")
#for (w in words) {
#  print (list (w, nchar(w))) } / print (w); print (nchar(w)) }
words = ['cat', 'window', 'defenestrate' ] 
for w in words:
    print w, len(w)
    
# range(): iterate over a sequence of numbers
print range(10)
print range(5, 10)
print range(0, 10, 3)

for x in range(-10, -100, -30):
    print x

""" Functions """
# create a function that writes the Fibonacci series to an arbitrary boundary n:
def fib(n):
    result=[]
    a, b = 0,1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
# Store the result into a variable.
fib_200 = fib(200)
print fib_200

""" vectors and matrices """
# numpy: fundamental package for scientific computing, already included in the Anaconda distribution.
# start import first. 
import numpy as np
# vector
x = np.array([1,2,3]) 
x
print x
# matrix
y = np.array([[2,3],[4,5]])
print y
# a range of numbers in a vector 
np.arange(10)
## array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) start from 0

#lists commands for MATLAB, R, and Python: http://mathesaurus.sourceforge.net/matlab-python-xref.pdf
