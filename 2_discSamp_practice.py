# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 17:32:12 2015

@author: ChatNoir
"""
from __future__ import division

def multip_range(max,min):
    total = 1 #set total to 1, not zero
    if min <= 0 or max <=0: #make sure your range doesnt equal zero
        print "your range contains the number 0 and will therefor return zero"
    else:
        for num in range(max,min-1,-1): #this works because the second argument is non-inclusive, so even if it's 0 then it will work
            total *= num #multiply all numbers together
        return total        
        


def binom_coeff(n,k):
    #assigning each variable for clarity
    nk=(n-k) 
    n1=multip_range(n,1)
    k1=multip_range(k,1)
    #bionom_coeff equation
    binom = n1/(nk*k1)
    return binom 

    
def fast_binom_coeff(n,k):
    k1=multip_range(k,1)
    max=n
    min=(n-k+1)
    top=multip_range(max,min)
    f_binom = top/k1
    return f_binom 
   
   
fast_binom_coeff(4,2)
    
  
binom_coeff(4,2)

def binom_dist(k,n,p):
    #assign variable to binom coeff 
    a=fast_binom_coeff(n,k)    
    #eqn P(X=k)=(n choose k)(p^k)(1-p)^(n-k)
    bi_dist=a*pow(p,k)*pow((1-p),(n-k))
    return bi_dist
    
binom_dist(2,4,0.1)

    
