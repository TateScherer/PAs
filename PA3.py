# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:37:55 2024

@author: Tate
"""

import numpy as np
#%% Question 4
four = np.poly1d([2,3,0,1])
print(four)
print(four(2))
#%% Question 5
five = np.poly1d([1,0,1])
five2 = np.polyder(five)
print(five2(1))
#%%
def newtonMthd(x, n, count): # x = user entered polynomial, n is desired start number
    poly = np.poly1d(x) # initializes polynomial
    der = np.polyder(poly) # initializes derivative
    
    i = n - (poly(n) / der(n))
    
    if abs(i - n) < .001:
        return i
    else:
        n = i # n is now assigned the i value
        count += 1
        print(f"x_{count} = {i}")
        return newtonMthd(x, n, count) # recursive part

#%%
def main():
    inputstring = input("Input your polynomial in [x, y, z] format: ")
    x = [float(coefficient) for coefficient in inputstring.split(",")]
    n = int(input("Enter desired starting number: "))
    count = 0

    answer = newtonMthd(x, n, count)
    print(np.poly1d(x).roots)
main()
