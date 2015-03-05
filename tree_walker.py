# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 10:37:09 2015

@author: ChatNoir
"""
from __future__ import division
import random
import scipy as sp
from scipy.linalg import expm
from scipy import array
import numpy as np

class Markov(object):
    
    def __init__(self,q=[[-0.75,0.25,0.25,0.25],
                        [0.25,-0.75,0.25,0.25],
                        [0.25,0.25,-0.75,0.25],
                        [0.25,0.25,0.25,-0.75]],chainLen=10,stateSpace=['a','c','g','t'],nSims=1,longV=100):
        self.q=q #Q indicates a np.array. q is a list of lists
        self.chainLen=chainLen #total times
        self.stateSpace=stateSpace
        self.nSims=nSims
        self.longV=longV
        self.chain=[]
        self.waitTimes=[]
        self.simulate()
        self.makeQarray()
        
    def makeQarray(self):
        Q=sp.array(self.q)
        return Q
        
    def stationaryFreq(self):
        Q=self.makeQarray()
        statFreqmat=sp.linalg.expm(Q*self.longV) #exponentiate to a very large number to get stationary freqs
        #theoretically put in a check here to make sure all numbers in a column are almost identicle. 
        statFreqA=statFreqmat[0,1] #store each stationary frequency
        statFreqC=statFreqmat[1,0]
        statFreqG=statFreqmat[2,0]
        statFreqT=statFreqmat[3,0]
        statFreq=[statFreqA,statFreqC,statFreqG,statFreqT] #these are your big pi stationary freq values for the q matrix
        return statFreq       
        
        
    def discSamp(self,probs):
        """
        @author: JeremyBrown
        This function samples from a list of discrete events provided in the events
        argument, using the event probabilities provided in the probs argument. 
        These lists must:
            - Be the same length
            - Be in corresponding orders
        Also, the probabilities in probs must sum to 1.
        """
        ranNum = sp.random.random() #create an empty list. create an additive list that has the cum probs. ex: 0.25, 0.5, 0.74 1
        cumulProbs = []
        cumulProbs.extend([probs[0]])
        for i in range(1,len(probs)):
            cumulProbs.extend([probs[i]+cumulProbs[-1]])  # creates a CDF list.
        for i in range(0,len(probs)):   #numerical CDF graph
            if ranNum < cumulProbs[i]:    #iterates elements of a list to find where ranNum fits on CDF
               return self.stateSpace[i] #state space will always be same. 
        return None     #if none of the above happens. return nothing. 
      

    def qii(self,row): 
        """
        returns the negative number in the row as a positive number
        """
        for i in row:
            if i < 0:
                return -i
                
    def simulate(self):
        #Q=self.makeQarray()
        for n in range(self.nSims):
            qi=self.discSamp(self.stationaryFreq()) #pull a starting state from the stationary frequencies
            #print qi
            self.chain.extend(qi)  #add state to the markov chain
            while sum(self.waitTimes) < self.chainLen:
                qiRow=self.q[self.stateSpace.index(qi)] #pull the row corresponding to state qi
                #print qiRow
                l=self.qii(qiRow) #pull qii from row of state qi
                #print l
                wait=random.expovariate(l) #pull waiting time
                #print wait
                self.waitTimes.append(wait)
                #print self.waitTimes#add to list
                conditionalProbs=[qij/l for qij in qiRow] #conditional probabilities
                for i in conditionalProbs:
                    if i == -1:
                        conditionalProbs[conditionalProbs.index(i)]=0
                qi=self.discSamp(conditionalProbs) #sample new state from qi row, based on condProbs,
                self.chain.extend(qi) # create new qii
        return self.chain, self.waitTimes
            
    def margProbs(self,branch_len):
        """
        marginalizes over a lenght of time
        multiple substitutions over that time are assumed
        large values passed to this will create stationary frequencies
        """
        marg=sp.linalg.expm(self.Q*branch_len)
        return marg
        
    def calcHistProb(self,stateHist,timeHist):
        statFreq=self.stationaryFreq()
        states_totalProb=[]
        states_totalProb.extend(self.statFreq[self.stateSpace.index(stateHist[0])])
        for count in range(len(stateHist)-1):
            i=
           iRow=self.q[self.stateSpace.index(count)]
           qj=qiRow[self.stateSpace.index(count+1)]
           
           def calcHistProb(self, states, timevals):

            
          def stateProb(self):
""" Calculates the probabilities across all waiting
times and nucleotide states in the chain
"""
if len(self.chain) == 0:
return "chain is empty"
if len(self.tProblist) == 0:
return "run the tProb function, the transition probability matrix is empty"
list = []
# multiply all of the waiting times together, except the last value
sum = 1
for i in self.times[:-1]:
sum *= i
# not sure about this. Do I need to convert these waiting times to a probability? and how?
list.extend(self.times[:-1])
# multiply all of the chain transition probabilities together
# except the first value
for a, b in zip(self.chain, self.chain[1:]):
curr = self.stateSpace.index(b)
prev = self.stateSpace.index(a)
#print curr, prev
#val = self.tProb()[prev, curr]
val = self.tProblist[prev, curr]
sum *= val
list.append(val)
# calculates the probability of the first state in the chain
row = self.margProb(chainLength=100)[0]
firstProb = row[self.stateSpace.index(self.chain[0])]
sum *= firstProb
list.append(firstProb)
# just need to figure out the last value (1 - cdf (t last))
y = 1.0 - (norm.cdf(self.times[-1]))
sum *= y
list.append(y)

            