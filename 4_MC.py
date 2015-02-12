"""
Exercise 4
Discrete-time Markov chains
@author: jembrown
"""

# -*- coding: utf-8 -*-

from __future__ import division
import random
import scipy as sp   

"""
In this exercise, we will explore Markov chains that have discrete state spaces
and occur in discrete time steps. To set up a Markov chain, we first need to 
define the states that the chain can take over time, known as its state space.
To start, let's restrict ourselves to the case where our chain takes only two
states. We'll call them A and B.
"""

states=(A,B)
# Create a tuple that contains the names of the chain's states


"""
The behavior of the chain with respect to these states will be determined by 
the probabilities of taking state A or B, given that the chain is currently in 
A and B. Remember that these are called conditional probabilities (e.g., the 
probability of going to B, given that the chain is currently in state A is 
P(B|A).)

We record all of these probabilities in a transition matrix. Each row
of the matrix records the conditional probabilities of moving to the other
states, given that we're in the state associated with that row. In our example
row 1 will be A and row 2 will be B. So, row 1, column 1 is P(A|A); row 1, 
column 2 is P(B|A); row 2, column 1 is P(A|B); and row 2, column 2 is P(B|B). 
All of the probabilities in a ROW need to sum to 1 (i.e., the total probability
associated with all possibilities for the next step must sum to 1, conditional
on the chain's current state).

In Python, we often store matrices as "lists of lists". So, one list will be 
the container for the whole matrix and each element of that list will be 
another list corresponding to a row, like this: mat = [[r1c1,r1c2],[r2c1,r2c2]]. 
We can then access individual elements use two indices in a row. For instance,
mat[0][0] would return r1c1. Using just one index returns the whole row, like
this: mat[0] would return [r1c1,r1c2].

Define a transition matrix for your chain below. For now, keep the probabilties
moderate (between 0.2 and 0.8).
"""

# Define a transition probability matrix for the chain with states A and B
#statematrix=[[r1c1,r1c2],[r2c1,r2c2]]
state_matrix=[[0.3,0.7],[0.6,0.4]]
# Try accessing a individual element or an individual row 
# Element
PAB=state_matrix[1][0]
print PAB

# Row
RowB=state_matrix[1]
print RowB


"""
Now, write a function that simulates the behavior of this chain over n time
steps. To do this, you'll need to return to our earlier exercise on drawing 
values from a discrete distribution. You'll need to be able to draw a random
number between 0 and 1 (built in to scipy), then use your discrete sampling 
function to draw one of your states based on this random number.
"""

# Import scipy U(0,1) random number generator
#?
# Paste or import your discrete sampling function

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
    result=(type1, type2)
    return result

# Write your Markov chain simulator below. Record the states of your chain in 
# a list. Draw a random state to initiate the chain.
#input is the state matrix 
#check RT's for reverse time and recursion example

def twostateMC(state_matrix,num_steps):
    #list state space, then randomly pick a state to start with    
    states=('A', 'B')
    init_state=random.choice(states)    
    state_list=[]
    for x in range(num_steps):
        x=random.random()
        currstate=init_state
        if currstate =='A':
            if x <= 0.3:
                state_list.append('A')
                currstate='A'
            if 0.3 < x <= 1:
                state_list.append('B')
                currstate='B'
        if currstate == 'B':
            if x <= 0.6:
                state_list.append('A')
                currstate='A'
            if 0.6 < x <= 1:
                state_list.append('B')
                currstate='B'
    return state_list
    
    
def dmcSim(n,st=('a','b'),allProbs=):
    #goes through n-1 numbers
    #st is list of events
    #function disc samp, pulls from list of states (st) based on list of probs (which we create in here with probs)
    chain = []
    #divide 1 by number of states for all states you've given it. and assign equal probs to each
    currstate=discSamp(st,[1.0/len(st) for x in st])
    for step in range(1,n):
        #re-assign probs based on curr-state
        probs = allProbs[st.index(currstate)]
        #one row of probs from matrix
        currstate = discSamp(st,probs)
        #find a current state based on the row
        chain.extend(currstate)
    return chain   

# Run a simulation of 10 steps and print the output.

twostateMC(state_matrix,10)    
                
['B', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'B', 'B']
                


# ----> Try to finish the above lines before Tues, Feb. 10th <----

# Now try running 100 simulations of 100 steps each. How often does the chain
# end in each state? How does this change as you change the transition matrix?

tm=[[0.3,0.7],[0.4,0.6]]
st=('a','b')

endA_list=[]
endB_list=[]
laststatelist=[]
for x in range(100):
    run=dmcSim(100,st,tm)
    laststate=run[len(run)-1]
    laststatelist.append(laststate)
#print laststatelist
endA=laststatelist.count('a')
endA_list.append(endA)
endB=laststatelist.count('b')
endB_list.append(endB)
print "number of times ending in A" + str(endA_list)
#33,35,44
print "number of times ending in B" + str(endB_list)
#66,65,56

tm=[[0.1,0.9],[0.5,0.5]]
A= 37, 25, 29, 34
B= 62, 75, 71, 66

# Try defining a state space for nucleotides: A, C, G, and T. Now define a 
# transition matrix with equal probabilities of change between states.

eq_nuc_mat=[[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25]]
bp_st=('a','c','g','t')

         
laststatelist=[]
for x in range(100):
    run=dmcSim(100,bp_st,eq_nuc_mat)
    laststate=run[len(run)-1]
    laststatelist.append(laststate)
print laststatelist
endA=laststatelist.count('a')
print endA
endC=laststatelist.count('c')
print endC   
endT=laststatelist.count('t')
print endT
endG=laststatelist.count('g')
print endG       
         
         
  
         
# Again, run 100 simulations of 100 steps and look at the ending states. Then
# try changing the transition matrix.
        


uneq_nuc_mat=[[0.1,0.2,0.3,0.4],[0.4,0.3,0.2,0.1],[0.1,0.2,0.3,0.4],[0.4,0.3,0.2,0.1]]
     
laststatelist=[]
for x in range(100):
    run=dmcSim(100,bp_st,uneq_nuc_mat)
    laststate=run[len(run)-1]
    laststatelist.append(laststate)
print laststatelist
endA=laststatelist.count('a')
print endA
endC=laststatelist.count('c')
print endC   
endT=laststatelist.count('t')
print endT
endG=laststatelist.count('g')
print endG    
