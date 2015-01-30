# -*- coding: utf-8 -*-
"""
An Introduction to Likelihood

@author: jembrown
"""

from scipy.stats import binom
from __future__ import division
import scipy

n = 5
p = 0.5 # Change this and repeat

data = binom.rvs(n,p)
data =  5 # Supply observed number of successes here.
numTrials = 5

#binomial PMF
def binom_dist(k,n,p):
    #assign variable to binom coeff 
    a=fast_binom_coeff(n,k)    
    #eqn P(X=k)=(n choose k)(p^k)(1-p)^(n-k)
    bi_dist=a*pow(p,k)*pow((1-p),(n-k))
    return bi_dist

# Set up a list with all relevant values of p
def additive_list(min=0,max=1):
    add=0.5
    

# Calculate the likelihood scores for these values of p, in light of the data you've collected


# Find the maximum likelihood value of p (at least, the max in this set)


# What is the strength of evidence against the most extreme values of p (0 and 1)?


# Calculate the likelihood ratios comparing each value (in the numerator) to the max value (in the denominator)



"""
Now let's try this all again, but with more data. This time, we'll use 20 draws from our cup of marbles.
"""

data =   # Supply observed number of successes here.
numTrials = 20


# Calculate the likelihood scores for these values of p, in light of the data you've collected



# Find the maximum likelihood value of p (at least, the max in this set)


# What is the strength of evidence against the most extreme values of p (0 and 1)?



# Calculate the likelihood ratios comparing each value (in the numerator) to the max value (in the denominator)


# When is the ratio small enough to reject some values of p?

