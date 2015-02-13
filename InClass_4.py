# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:31:18 2015

@author: ChatNoir

In-Class Markov Chain Exercise
2.10.15
@author: jembrown
"""
from __future__ import division
import random
import scipy as sp   
import numpy as np
"""
Recall from your reading that any irreducible and aperiodic Markov chain has a 
stationary distribution. To convince ourselves that things will converge for 
such a chain with arbitrary transition probabilities, let's give it a try.

Work in pairs for this. It's more fun to be social.
"""

# Paste your Markov chain simulation function below, where the starting state
# is drawn with uniform probability from all possible states. Remember to also
# copy any import statements or other functions on which your simulator is
# dependent.

def discSamp(events,probs):
    """
    This function samples from a list of discrete events provided in the events
    argument, using the event probabilities provided in the probs argument. 
    These lists must:
        - Be the same length
        - Be in corresponding orders
    Also, the probabilities in probs must sum to 1.
    """
    ranNum = sp.random.random()
    cumulProbs = []
    cumulProbs.extend([probs[0]])
    for i in range(1,len(probs)):
        cumulProbs.extend([probs[i]+cumulProbs[-1]])
    for i in range(0,len(probs)):
        if ranNum < cumulProbs[i]:
           return events[i]
    return None
    
    
def dmcSim(n,st=('a','b'),allProbs=[[0.5,0.5],[0.5,0.5]]):
    #goes through n-1 numbers
    #st is list of events
    #function disc samp, pulls from list of states (st) based on list of probs (which we create in here with probs)
    chain = []
    #divide 1 by number of states for all states you've given it. and assign equal probs to each
    currstate=discSamp(st,[1.0/len(st) for x in st])
    chain.extend(currstate)
    for step in range(1,n):
        #re-assign probs based on curr-state
        probs = allProbs[st.index(currstate)]
        #one row of probs from matrix
        currstate = discSamp(st,probs)
        #find a current state based on the row
        chain.extend(currstate)
    return chain    
    


# Define a 2x2 transition matrix. For fun, don't make all the probabilities
# equal. Also, don't use any 0s or 1s (to make sure the chain is irreducible
# and aperiodic).

tm=[[0.7,0.3],[0.4,0.6]]
st=('a','b')

# Simulate a single chain for three time steps and print the states

dmcSim(3,st,tm)
['b', 'b', 'b']

# Analytically calculate the progression of states for this chain.
# Calculate the probability of observing the state in step 3, given the initial
# state in step 1 (i.e., as if you didn't know the state in step 2).

"""
P(x1=state1, x2=state2, x3=state3)
A= x1
B=[x2,x3]
# so....
P(A)*P(B|A)
P(x1)*P(x2,x3|x1)
P(x1)*P(x2|x1)*P(x3|x2,x1) = give 1st state, prob of state 2 on 1, and state 2 on three
P(x1)*P(x2|x1)*P(x3|x2) -> cannot have prob of x3 on x1 because of markov
"""

P(b,b,b)= 0.5*0.6*0.6 == 0.18
#first one is 0.5 because of uniform distribution
#what if we don't know middle step
P(b,?,b)=(0.5*0.4*0.3)+(0.5*0.6*0.6)== 0.06+0.18 = 0.24
        =P(b,a,b)+P(b,b,b)

#take transition matrix to the n power, it will give you the probabilities
#matrix mulitplication
T^n
T=np.array(tm)


# Now think of the chain progressing in the opposite direction. What is the
# probability of the progression through all 3 states in this direction? How
# does this compare to the original direction?
#this ends up being the same because I started and ended on the same thing. let's see what happens if I start on A and end on B
P(x3)*P(x2|x3)*P(x1|x2)
P(b,?,b)=(0.5*0.4*0.3)+(0.5*0.6*0.6)= 0.06+0.18 = 0.24
=P(b,a,b)+P(b,b,b)

#FORWARD- start on A, end on B
P(a,?,b)=(0.5*0.7*0.3)+(0.5*0.6*0.6)= 0.105+0.18 = 0.285
        =P(a,a,b)+P(a,b,b)
#REVERSE
P(b,?,a)=(0.5*0.4*0.7)+(0.5*0.6*0.4)= 0.139+0.12 = 0.26
        =P(b,a,a)+P(b,b,a)

#these end up being different 


# Try the same "forward" and "reverse" calculations as above, but with this
# transition matrix:
# revMat = [[0.77,0.23],
#           [0.39,0.61]]
# and these starting frequencies for "a" and "b"
# freq(a) = 0.63   freq(b) = 0.37
revMat = [[0.77,0.23],[0.39,0.61]]
tm=np.matrix(revMat)
freqa=0.63
freqb=0.37
draw=random.random()
if draw <= 0.63:
    i=0
elif draw >= 0.37:
    i=1   
print i
def matrixmult(mx,i,j,n):
    mx=np.matrix(mx)
    Tn=mx**n
    prob=(Tn[i,j])
    print "matrix is "+str(Tn)
    return "prob of i -> j is "+str(prob)
    
matrixmult(revMat,i,1,200)


# What is (roughly) true about these probabilities?





# Simulate 1,000 replicates  (or 10K if your computer is fast enough) of 25 
# steps. What are the frequencies of the 2 states across replicates through time?

# NOTE: Here is a function that reports the frequencies of a state through time 
# for replicate simulations. You'll need to do this several times during this exercise.

def mcStateFreqSum(sims,state="a"):
    """
    Pass this function a list of lists. Each individual list should be the
    states of a discrete-state Markov chain through time (and all the same 
    length). It will return a list containing the frequency of one state 
    ("a" by default) across all simulations through time.
    """
    freqs = []
    for i in range(len(sims[0])):  # Iterate across time steps
        stateCount = 0
        for j in range(len(sims)): # Iterate across simulations
            if sims[j][i] == state:
                stateCount += 1
        freqs.extend([float(stateCount)/float(len(sims))])
    return freqs

# Run replicate simulations 



    
# Summarize the frequency of one state through time




# What do you notice about the state frequencies through time? Try another round
# of simulations with a different transition matrix. How do the state freq.
# values change?






# Now, calculate a vector of probabilities for the focal state (e.g., 'a')
# based on the transition matrix directly (not by simulation). How do these
# values compare to the simulated frequencies?










