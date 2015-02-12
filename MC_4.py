# -*- coding: utf-8 -*-
"""
MC Hw

functions only. need to wrap up a bunch of these into fuctions. for now they are just comments. 
"""
from __future__ import division
import random
import scipy as sp    

"""
My version failed

state_matrix=[[0.3,0.7],[0.6,0.4]]

#input is the state matrix 
def twostateMC(state_matrix,num_steps):
    #list state space, then randomly pick a state to start with    
    states=('A', 'B')
    #draw random state from U(0,1) to start chain
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
"""          
   
#the following is Jeremy's version

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


# Now try running 100 simulations of 100 steps each. How often does the chain
# end in each state? How does this change as you change the transition matrix?

#tm=[[0.1,0.9],[0.5,0.5]]
#st=('a','b')

"""
NEED to wrap this in a fuction"
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



# Try defining a state space for nucleotides: A, C, G, and T. Now define a 
# transition matrix with equal probabilities of change between states.


eq_nuc_mat=[[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25]]
bp_st=('a','c','g','t')
         
# Again, run 100 simulations of 100 steps and look at the ending states. Then
# try changing the transition matrix.
         
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
"""