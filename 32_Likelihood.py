
"""
Sometimes it will not be feasible or efficient to calculate the likelihoods for every
value of a parameter in which we're interested. Also, that approach can lead to large
gaps between relevant values of the parameter. Instead, we'd like to have a 'hill
climbing' function that starts with some arbitrary value of the parameter and finds
values with progressively better likelihood scores. This is an ML optimization
function. There has been a lot of work on the best way to do this. We're going to try
a fairly simple approach that should still work pretty well, as long as our likelihood 
surface is unimodal (has just one peak). Our algorithm will be:
(1) Calculate the likelihood for our starting parameter value (we'll call this pCurr)
(2) Calculate likelihoods for the two parameter values above (pUp) and below (pDown)
our current value by some amount (diff). So, pUp=pCurr+diff and pDown=pCurr-diff. To
start, set diff=0.1, although it would be nice to allow this initial value to be set
as an argument of our optimization function.
(3) If either pUp or pDown has a better likelihood than pCurr, change pCurr to this
value. Then repeat (1)-(3) until pCurr has a higher likelihood than both pUp and
pDown.
(4) Once L(pCurr) > L(pUp) and L(pCurr) > L(pDown), reduce diff by 1/2. Then repeat
(1)-(3).
(5) Repeat (1)-(4) until diff is less than some threshold (say, 0.001).
(6) Return the final optimized parameter value.
Write a function that takes some starting p value and observed data (k,n) for a
binomial as its arguments and returns the ML value for p.
To write this function, you will probably want to use while loops. The structure of
these loops is
while (someCondition):
    code line 1 inside loop
    code line 2 inside loop
    
As long as the condition remains True, the loop will continue executing. If the
condition isn't met (someCondition=False) when the loop is first encountered, the 
code inside will never execute.
If you understand recursion, you can use it to save some lines in this code, but it's
not necessary to create a working function.
"""

# Write a function that finds the ML value of p for a binomial, given k and n.

from LH_code import *


#calculate LH score. similar to binom pmf value (binom_dist(k,n,p))
#starting paramater value = pCurr
#p_start = starting parameter value
#diff = starting step size
def ML_robot(k,n,p_start,diff=0.1,cut_off=0.001):
    #set initial parameter value    
    pc=p_start
    #while the diff btw the p values is larger than your cutoff
    while diff>cut_off:
        pu=pc+diff
        pd=pc-diff
        LHc=binom_dist(k,n,pc)
        LHu=binom_dist(k,n,pu)
        LHd=binom_dist(k,n,pd)
        #print LHc,LHu,LHd
        #print pc,pu,pd
        if LHc<LHd:
            pc=pd
            pu+=diff
            pd-=diff
        if LHc<LHu:
            pc=pu
            pu+=diff
            pd-=diff 
        if LHc>LHu and LHc>LHd:
            diff=diff/2
    return LHc,pu




"""
In the exercise above, you tried to find an intuitive cutoff for likelihood ratio
scores that would give you a reasonable interval in which to find the true value of 
p. Now, we will empirically determine one way to construct such an interval. To do 
so, we will ask how far away from the true value of a parameter the ML estimate 
might stray. Use this procedure: (1) start with a known value for p, (2) simulate
a bunch of datasets, (3) find ML parameter estimates for each simulation, and then 
(4) calculate the likelihood ratios comparing the true parameter values and the ML
estimates. When you do this, you will be constructing a null distribution of
likelihood ratios that might be expected if the value of p you picked in (1)
was true. Note that the ML values for these replicates are very often greater than
L(true value of P), because the ML value can only ever be >= L(true value). Once 
you have this distribution, find the likelihood ratio cutoff you need to ensure 
that the probability of seeing an LR score that big or greater is <= 5%. 
"""

# Set a starting, true value for p

trueP = 0.5

# Simulate 1,000 datasets of 200 trials from a binomial with this p
# If you haven't already done so, you'll want to import the binom class from scipy:
# from scipy.stats import binom
# binom.rvs(n,p) will then produce a draw from the corresponding binomial.


real_p=.5
n=200
k=n*real_p


def TrueP(n=200,real_p=0.5,diff=0.1,cut_off=0.001): 
    ML_list=[]
    for x in range(1000):
        #pick a k value according to n and true p
        k=binom.rvs(n,real_p)
        #run a hill climber to find value of p given your "data". returns a tuple [LH,pval]
        ML=ML_robot(k,n,diff,cut_off)
        #append to a list
        append.ML_list(ML)
        maxvals=max(LH_list)
        return maxvals
        

# Calculate likelihood ratios comparing L(trueP) in the numerator to the maximum
# likelihood (ML) in the denominator. Sort the results and find the value
# corresponding to the 95th percentile.



# Now, convert the likelihood ratios (LRs) to -2ln(LRs) values.
# Find the 95th percentile of these values. Compare these values to this table:
# https://people.richland.edu/james/lecture/m170/tbl-chi.html. In particular, look
# at the 0.05 column. Do any of these values seem similar to the one you calculated?
# Any idea why that particular cell would be meaningful?



# Based on your results (and the values in the table), what LR statistic value 
# [-2ln(LR)] indicates that a null value of p is far enough away from the ML value
# that an LR of that size is <=5% probable if that value of p was true?



# Using this cutoff, what interval might you report for the 5- and 20-trial data
# sets above?



# We've talked in previous classes about two ways to interpret probabilities. Which
# interpretation are we using here to define these intervals?