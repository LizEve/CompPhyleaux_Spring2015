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

import random



def arb_disc_dist(events,probs):
    #zip together the two lists into a tuple
    event_probs=zip(events,probs)
    #randomly select a tuple. event and prob tuple. later we will parse out the event name and the probability
    evprobtupe=random.choice(event_probs)
    event=evprobtupe[0]
    prob=evprobtupe[1]
    #print event
    #print prob
    print "the probability of you eating a",event,"is",prob
 
events1=["magnet", "water bottle", "headphones", "sofa", "thermostat", "floor"]
probs1=[0.2,0.3,0.5,0.6,0.1,0.4]

arb_disc_dist(events1,probs1)

import random
#n represents the number of sites
def sampling_seq(n):
    new_seq=[]
    for bp in range(n):
        x=random.random()
        if x <= 0.5:
            new_seq.append(1)
        else:
            new_seq.append(2)
    type1=new_seq.count(1)
    type2=new_seq.count(2)
    print "there are",type1,"sites of type 1 and ",type2,"sites of type 2"
    result=(type1, type2)
    print result[0]

sampling_seq(400)

def repeat(t,n):
	results=[]
	for num in range(t):
		x=sampling_seq(n)
		type1=x[0]
		type2=x[1]
		trial=(type1,type2)