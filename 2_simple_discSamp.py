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

from __future__ import division
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
    #print "there are",type1,"sites of type 1 and ",type2,"sites of type 2"
    result=(type1, type2)
    return result

sampling_seq(400)
#t is number of trials/repeats
#n is the number of sites in one trial
def repeat(t,n):
    results=[]
    #make a list to fill with trial results
    for num in range(t):
        x=sampling_seq(n)
        #this will return a tuple of number of sites with type 1, type two
        type1=x[0]
        type2=x[1]
        #calculate the percent of each type of site divided by total
        frac_type1=type1/n
        frac_type2=type2/n
        trial=(type1,type2, frac_type1, frac_type2)
        results.append(trial)
    return results
    

import matplotlib.pyplot as plt
#wrapping in a fuction that takes t-number of trials. n-number of sites. site_type- which site you want to make a histogram of. and 
def make_graph(t,n,site_type,bin_num):
    if site_type == "type1":
        z=2
    elif site_type == "type2":
        z=3
    else:
        print "not a valid site type, please enter type1 or type2"
    #run t times with n bp per sequence
    run=repeat(t,n)
    #making a list of just probabilities of whatever type you input
    type_list=[x[z] for x in run]
    #return type_list
    #plotting said list in histogram
    plt.hist(type_list, bins = bin_num)
    plt.ylabel('number of trials')
    plt.xlabel('number of sites with choosen type in sequence')
    plt.show()

make_graph(100,400,"type1",20)



prob_type=[]
run=repeat(100,400)
print run
prob_type=[x[2] for x in run]
print prob_type
    

def make_PMF(t,n,site_type,p,bin_num):
    if site_type == "type1":
        z=0
    elif site_type == "type2":
        z=1
    else:
        print "not a valid site type, please enter type1 or type2"
    #run t times with n bp per sequence
    run=repeat(t,n)
    type_list=[x[z] for x in run]
    PMF_type1=[]
    for num in type_list:
        bd=binom_dist(num,n,p)
        PMF_type1.append(bd)
    plt.hist(type_list, bins = bin_num)
    plt.ylabel('number of trials')
    plt.xlabel('PMF value')
    plt.show()

make_PMF(10000,400,"type1",0.5,20)
make_graph(10000,400,"type1",20)

