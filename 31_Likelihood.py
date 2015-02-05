# -*- coding: utf-8 -*-
"""
An Introduction to Likelihood

@author: jembrown
"""

"""
There are two primary ways to use probability models. Given what we know to be true about an experimental setup, we can make predictions about what we expect to see in an upcoming trial. For this purpose, probability functions are what we need. If R is the outcome of an experiment (i.e., an event) and p is a parameter of the probability function defined for these experimental outcomes, we can write these expectations or predictions as:

P(R|p).

This conditional probability tells us what to expect about the outcomes of our experiment, given knowledge of the underlying probability model. Thus, it is a probability function of R given a value for p (and the model itself).

However, we might also wish to ask what we can learn about p itself, given outcomes of trials that have already been observed. This is the purview of the likelihood. Likelihoods are functions of parameters (or hypotheses, more generally) given some observations. The likelihood function of a parameter value is defined as:

L(p;R) = P(R|p)

Note that this is the same probability statement we saw above. However, in this context we are considering the outcome (R) to be fixed and we're interested in learning about p. Note that the likelihood is sometimes written in several different ways: L(p;R) or L(p) or L(p|R). P(R|p) gives a probability when R is discrete or a probability density when R is continuous. Since likelihoods are only compared for some particular R, we do not need to worry about this distinction. Technically speaking, likelihoods are just said to be proportional to P(R|p), with the constant of proportionality being arbitrary.

There are some very important distinctions between likelihoods and probabilities. First, likelihoods do NOT sum (or integrate) to 1 over all possible values of p. Therefore, the area under a likelihood curve is not meaningful, as it is for probability.

It does not make sense to compare likelihoods across different R. For instance, smaller numbers of observations generally produce higher values of P(R|p), because there are fewer total outcomes.

Likelihood curves provide useful information about different possible values of p. When we are interested in comparing discrete hypotheses instead of continuous parameters, the likelihood ratio is often used:

L(H1;R)     P(R|H1)
-------  =  -------
L(H2;R)     P(R|H2)

Now, let's try using likelihoods to learn about unknown aspects of the process that's producing some data.


---> Inferring p for a binomial distribution <---

First, we'll start by trying to figure out the unknown probability of success associated with a Binom(5,p) random variable. If you want to try this on your own later, the following code will perform draws from a binomial with 5 trials. You can simply change the associated value of p to whatever you'd like. To make the inference blind, have a friend set this value and perform the draws from the Binomial for you, without revealing the value of p that they used.
"""

from scipy.stats import binom

n = 5
p = 0.5 # Change this and repeat

data = binom.rvs(n,p)

"""
For the in-class version of this exercise, I'm going to perform a manual draw from a binomial using colored marbles in a cup. We'll arbitrarily define dark marbles as successes and light marbles as failures.

Record the outcomes here:
dark=1
light=0

Draw 1: 1
Draw 2: 1
Draw 3: 1
Draw 4: 1
Draw 5: 1

Number of 'successes': 

Now record the observed number of succeses as in the data variable below.
"""

data =  5 # Supply observed number of successes here.
numTrials = 5

"""
Since we are trying to learn about p, we define the likelihood function as;

L(p;data) = P(data|p)

If data is a binomially distributed random variable [data ~ Binom(5,p)]

P(data=k|p) = (5 choose k) * p^k * (1-p)^(n-k)

So, we need a function to calculate the binomial PMF. Luckily, you should have just written one and posted it to GitHub for your last exercise. Copy and paste your binomial PMF code below. For now, I will refer to this function as binomPMF(). 
"""

from scipy.stats import binom
from __future__ import division
import scipy
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

#OR
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.binomial.html
#numpy.random.binomial(n, p, k)

"""
Now we need to calculate likelihoods for a series of different values for p to compare likelihoods. There are an infinite number of possible values for p, so let's confine ourselves to steps of 0.05 between 0 and 1.
"""




###Set up a list with all relevant values of p###

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
        
#some weird rounding errors are happening. 
pvals=additive_list(0,1,0.05)
print pvals
#[0, 0.05, 0.1, 0.15000000000000002, 0.2, 0.25, 0.3, 0.35, 0.39999999999999997, 0.44999999999999996, 0.49999999999999994, 0.5499999999999999, 0.6, 0.65, 0.7000000000000001, 0.7500000000000001, 0.8000000000000002, 0.8500000000000002, 0.9000000000000002, 0.9500000000000003, 1.0000000000000002]

###Calculating the likelihood scores for these values of p, in light of the data you've collected###
#L(p;data)=P(data|p)  data=k data~Bin(n,p)  n=5 trials. 
#iterate through list to find LH for each p in list
def LH_for_pval_list(pvals_min=0,pvals_max=1,counter=0.05,n=5,k=5):
    pvals=additive_list(pvals_min,pvals_max,counter)
    LH_list=[]
    for num in pvals:
        x=binom_dist(k,n,num)
        LH_list.append(round(x,5))
    return LH_list
    
LHk5=LH_for_pval_list()
print LHk5

def simple_dot_plot(xnums, ynums, xlabel, ylabel, data_label):
    plt.plot(xnums, ynums, 'ro',label=data_label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
 

simple_dot_plot(pvals, LHk5,"possible p values","Likelihood","Likelihood values")

# Find the maximum likelihood value of p (at least, the max in this set)

max_LH=max(LHk5)
print max_LH
#max LH is 1


# What is the strength of evidence against the most extreme values of p (0 and 1)?

#for p of 0 =0.0
print LHk5[0]
#for p of 1 = 1.0
print LHk5[(len(pvals)-1)]

# Calculate the likelihood ratios comparing each value (in the numerator) to the max value (in the denominator)
#input is list of LHs and corresponding list of pvals
def LRT(LH,pvals):
    max_LH=max(LH)
    LRT_list=[]
    for num in LH:
        LRT=num/max_LH
        LRT_list.append(round(LRT,5))
    return LRT_list
    
LRT(LHk5,pvals)
#[0.0, 0.0, 1e-05, 8e-05, 0.00032, 0.00098, 0.00243, 0.00525, 0.01024, 0.01845, 0.03125, 0.05033, 0.07776, 0.11603, 0.16807, 0.2373, 0.32768, 0.44371, 0.59049, 0.77378, 1.0]



#re-running with k=4

LHk4=LH_for_pval_list(0,1,0.05,5,4)
print LHk4
#[0.0, 3e-05, 0.00045, 0.00215, 0.0064, 0.01465, 0.02835, 0.04877, 0.0768, 0.11277, 0.15625, 0.20589, 0.2592, 0.31239, 0.36015, 0.39551, 0.4096, 0.3915, 0.32805, 0.20363, 0.0]

max_LH=max(LHk4)
print max_LH
#0.4096

#for p of 0 =0.0
print LHk4[0]
#for p of 1 = 0.0
print LHk4[(len(pvals)-1)]

simple_dot_plot(pvals, LHk4,"possible p values","Likelihood","Likelihood values")

LRTk4=LRT(LHk4,pvals)
#[0.0, 7e-05, 0.0011, 0.00525, 0.01563, 0.03577, 0.06921, 0.11907, 0.1875, 0.27532, 0.38147, 0.50266, 0.63281, 0.76267, 0.87927, 0.9656, 1.0, 0.95581, 0.8009, 0.49714, 0.0]


index=LRTk4.index(max(LRTk4))
print index
max_p=pvals[index]
print max_p
#0.8

#My interval:

pval_interval=LRTk4[(index-1):(index+2)]
print pval_interval
#[0.75, 0.8, 0.85]

LRT_interval=LRTk4[(index-1):(index+2)]
print LRT_interval
#[0.9656, 1.0, 0.95581]


"""
m = max(a)
>>> [i for i, j in enumerate(a) if j == m]
"""

"""
Now let's try this all again, but with more data. This time, we'll use 20 draws from our cup of marbles.
"""

data = 12# Supply observed number of successes here.
numTrials = 20


# Calculate the likelihood scores for these values of p, in light of the data you've collected

#LH_for_pval_list(pvals_min=0,pvals_max=1,counter=0.05,n=5,k=5)
LHk12n20=LH_for_pval_list(0,1,0.05,20,12)
print LHk12n20
#[0.0, 0.0, 0.0, 0.0, 9e-05, 0.00075, 0.00386, 0.01356, 0.0355, 0.07273, 0.12013, 0.1623, 0.17971, 0.16135, 0.1144, 0.06089, 0.02216, 0.00459, 0.00036, 0.0, 0.0]

# Find the maximum likelihood value of p (at least, the max in this set)

max_LH=max(LHk12n20)
print max_LH
#0.17971

index=LHk12n20.index(max(LHk12n20))
print index
max_p=pvals[index]
print max_p
#0.6


# What is the strength of evidence against the most extreme values of p (0 and 1)?

#for p of 0 =0.0
print LHk12n20[0]
#for p of 1 = 0.0
print LHk12n20[(len(pvals)-1)]

# Calculate the likelihood ratios comparing each value (in the numerator) to the max value (in the denominator)

LRTk12n20=LRT(LHk12n20,pvals)
print LRTk12n20
#[0.0, 0.0, 0.0, 0.0, 0.0005, 0.00417, 0.02148, 0.07545, 0.19754, 0.40471, 0.66847, 0.90312, 1.0, 0.89784, 0.63658, 0.33882, 0.12331, 0.02554, 0.002, 0.0, 0.0]

index=LRTk12n20.index(max(LRTk12n20))
print index

p_interval=pvals[(index-1):(index+2)]
print p_interval
#[0.55, 0.6, 0.65]

LRT_interval=LRTk12n20[(index-1):(index+2)]
print LRT_interval
#[0.90312, 1.0, 0.89784]

# When is the ratio small enough to reject some values of p?
good question!!

