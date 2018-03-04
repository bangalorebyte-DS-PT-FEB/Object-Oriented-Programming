#!usr/bin/env python3.6
__author__ = 'udaykeith'

"""The first method that all classes should provide is the constructor.
 The constructor defines the way in which data objects are created. To create a Fraction object,
 we will need to provide two pieces of data, the numerator and the denominator. In Python, 
 the constructor method is always called __init__ (two underscores before and after init)"""

def gcd(m,n):
   		while m%n != 0:
   			oldm = m
   			oldn = n
   			m = oldn
   			n = oldm%oldn
   		return n

class Fraction:
	# instantiate two data types, numerator and denominator	
    def __init__(self,top,bottom):
    	# The notation self.num in the constructor defines the fraction
    	# object to have an internal data object called num as part of its state
        self.num = top
        self.den = bottom
    def show(self):
    	print(self.num,"/",self.den)

    def __str__(self):
    	return str(self.num)+"/"+str(self.den)	
    #okay, lets look at some behaviour, can we add the two Fractions
	#myfraction = Fraction(3,5) #instantiate class
	#myfraction_2 = Fraction (4,2)# specify which behavior to implement
	#print(myfraction + myfraction_2)

    #the problem is that the “+” operator does not understand the Fraction operands.
    #We can fix this by providing the Fraction class with a 
    #method that overrides the addition method.

 
    def __add__(self,otherfraction):
   		newnum = self.num*otherfraction.den + self.den*otherfraction.num
   		newden = self.den*otherfraction.den 
   		common = gcd(newnum,newden)
   		return Fraction(newnum//common,newden//common)
    
    def __sub__(self,otherfraction):
      newnum = self.num*otherfraction.den - self.den*otherfraction.num
      newden = self.den*otherfraction.den 
      common = gcd(newnum,newden)
      return Fraction(newnum//common,newden//common)

    def __mul__(self,otherfraction):
      newnum = self.num*otherfraction.num 
      newden = self.den*otherfraction.den 
      common = gcd(newnum,newden)
      return Fraction(newnum//common,newden//common)

    def __eq__(self, otherfraction):
      firstnum = self.num * otherfraction.den
      secondnum = otherfraction.num * self.den

      return firstnum == secondnum

    def __truediv__(self, otherfraction):
      newnum = self.num*otherfraction.den 
      newden = self.den*otherfraction.num 
      common = gcd(newnum,newden)
      return Fraction(newnum//common,newden//common)
      
    def __lt__(self,otherfraction):
      firstnum = self.num * otherfraction.den
      secondnum = otherfraction.num * self.den

      return firstnum < secondnum
    
    def __gt__(self,otherfraction):
      firstnum = self.num * otherfraction.den
      secondnum = otherfraction.num * self.den

      return firstnum > secondnum


x = Fraction(3,5)
y = Fraction(4,6)
print(x==y)

# Are we happy with this? Is this the best factoring?

