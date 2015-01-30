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
import scipy

#binomial PMF
def binom_dist(k,n,p):
    #assign variable to binom coeff 
    a=fast_binom_coeff(n,k)    
    #eqn P(X=k)=(n choose k)(p^k)(1-p)^(n-k)
    bi_dist=a*pow(p,k)*pow((1-p),(n-k))
    return bi_dist


"""
Now we need to calculate likelihoods for a series of different values for p to compare likelihoods. There are an infinite number of possible values for p, so let's confine ourselves to steps of 0.05 between 0 and 1.
"""

# Set up a list with all relevant values of p


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

