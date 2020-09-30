# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:09:08 2020

@author: b20030461
"""

import numpy as np
import matplotlib.pyplot as plt

def tutorial():
    #first steps with matrices in python
    a = np.array([1, 2, 3]) # just a simple vector
    print("This is just a simple vector", a)
    b = np.array([[1, 2, 3], [3, 4, 5]])
    print("This is my data type:", type(b))
    print("This is going to be a matrix: ")
    print(b)
    c = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) # Array of complex numbers
    print("This is a matrix of complex numbers: ")
    print(c)
    t= c.shape
    print("This is the shape of the matrix: ", t[0], "rows x ", t[1], "colums" )
    print("****************************")
   
    a = np.array([[0, 1 , 3], [4, 5, 6], [-1, -2, 0]])
    c= np.array([[0, 0 , 1], [7, 3, 2], [1, 8, 6]])
    print("a: ")
    print(a)
    print("c: ")
    print(c)
    
    add = a+c
    print("a + c:")
    print(add)
    
    mult1 = a.dot(c)
    print("a * c: ")
    print(mult1)
    mult2 = c.dot(a)
    print("c*a: ")
    print(mult2)
    print("****************************")
    
    print("a:")
    print(a)
    
    print("transposing the matrix a : ")
    print(a.transpose())
        
    print("power of matrices")
    
    d = a**2
    print("let's do it wrong: ")
    print(d)
    
    e = np.linalg.matrix_power(a, 2)
    print("let's do it right:")
    print(e)
    
    
def ex5_4(t = 1, mi= np.array([30, 0, 0])):
    #this is the fifth exercise from the td2
    l = np.array([[0, 2, 6], [0.4, 0, 0], [0, 0.6, 0]])
    
    if(t==0):
        return mi
    elif(t==1):
        return (l.dot(mi)).astype(int)
    else:
       return  (l.dot(ex5_4(t-1))).astype(int)
   

def ex5_5(n):
    sum_pop = np.array([])
    for i in range(1, n+1):
        sum_pop = (np.append(sum_pop, sum(ex5_4(i))))

    x= np.array(list(range(0, len(sum_pop))))
    plt.plot(x, sum_pop, alpha=0.5)
    #print("sum_pop", sum_pop)
    plt.show(block=True)
    
def ex5_5extra(n): # this is a slightly different problem than the one before
    
    baby = np.array([]) # i am using a different data structure because i need more information about my the age groups
    young = np.array([])
    adult = np.array([])
    total = np.array([])
    
    for i in range(1, n+1):        
        pop = (ex5_4(i))
        baby = np.append(baby, pop[0])
        young = np.append(young, pop[1])
        adult = np.append(adult, pop[2])
        total = np.append(total, sum(pop))
        

    x= np.array(list(range(0, len(total))))
    plt.plot(x, baby, alpha=0.5, color="red")
    plt.plot(x, young, alpha=0.5, color="blue")
    plt.plot(x, adult, alpha=0.5, color="green")
    plt.plot(x, total, alpha=0.5, color="black")
    
    #print("baby", baby)
    #print("young", young)
    #print("adult", adult)
    #print("total", total)
    plt.show(block=True)    
    
    
def main():
    #sum_pop = np.array([])
    
   #print("ex4", ex5_4(t=3))
   ex5_5(15)
   ex5_5extra(15)

        
main()        