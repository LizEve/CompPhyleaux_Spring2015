# -*- coding: utf-8 -*-
"""
Likelihood

stripped down to functions and hastags
"""

from scipy.stats import binom
from __future__ import division
import random
import matplotlib.pyplot as plt

#basically a factorial calculation between two numbers
def multip_range(max,min):
    total = 1 #set total to 1, not zero
    if min <= 0 or max <=0: #make sure your range doesnt equal zero
        print "your range contains the number 0 and will therefor return zero"
    else:
        for num in range(max,min-1,-1): #this works because the second argument is non-inclusive, so even if it's 0 then it will work
            total *= num #multiply all numbers together
        return total  

#def fast_binom_coeff(n,k):
#k=number of successes or sets
#n=number of trials

def fast_binom_coeff(n,k):
    k1=multip_range(k,1)
    max=n
    min=(n-k+1)
    top=multip_range(max,min)
    f_binom = top/k1
    return f_binom 

#binomial PMF def binom_dist(k,n,p):
#k=number of successes or sets
#n=number of trials
#p=probability of success
def binom_dist(k,n,p):
    a=fast_binom_coeff(n,k)  #assign variable to binom coeff 
    bi_dist=a*pow(p,k)*pow((1-p),(n-k)) #eqn P(X=k)=(n choose k)(p^k)(1-p)^(n-k)
    return bi_dist #returns a single number



#creates a list of numbers between lower and upper, stepping by the number add 
#lower=lower number
#upper=upper number
#add= the amount you want to count by
def additive_list(lower=0,upper=1,add=0.05):     
    count=[] #open a list to fill with numbers
    count.append(lower) #start by adding the lower number to the list
    while lower < upper: #as long as the lower number is less than the upper number add your counter, and add to list
        lower += add
        count.append(round(lower,5))   #rounding down to avoid weird python rounding number
    else:
        return count
        
#LIKELIHOOD:: iterate through list of p values, given n & k, returns LH values. assuming X~Bin(n,k)
#L(p;data)=P(data|p)  data=k data~Bin(n,p)  n=5 trials. 
def LH_for_pval_list(pvals_min=0,pvals_max=1,step=0.05,n=5,k=5):
    pvals=additive_list(pvals_min,pvals_max,step) #making list of p values
    LH_list=[]
    for num in pvals: #for each p value input n and k and output a 
        x=binom_dist(k,n,num) #input each p value into binom dist
        LH_list.append(round(x,5)) #rounding here
    return LH_list
    

#makes graphs
def simple_dot_plot(xnums, ynums, xlabel, ylabel, data_label):
    plt.plot(xnums, ynums, 'ro',label=data_label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
 
##retriving LH values from LH-list and then corresponding pvals(need to work on getting pvals part)
 
#maximum likelihood value of p 
max_LH=max(LH_list)
#max_pval=pvals

#for p of 0 =0.0
LH_list[0]
#for p of 1 = 1.0
LH_list[(len(pvals)-1)]

# LRT for each LH value, input list of LH and pvals
def LRT(LH,pvals):
    max_LH=max(LH) #find max
    LRT_list=[]
    for num in LH:
        LRT=num/max_LH
        LRT_list.append(round(LRT,5))
    return LRT_list
    
