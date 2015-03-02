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
                        [0.25,0.25,0.25,-0.75]],chainLen=10,stateSpace=('a','c','g','t'),nSims=1,longV=100):
        self.q=q #Q indicates a np.array. q is a list of lists
        self.chainLen=chainLen #total times
        self.stateSpace=stateSpace
        self.nSims=nSims
        self.longV=longV
        self.chain=[]
        self.waitTimes=[]
        self.simulate()
        
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
      
    """
    returns the negative number in the row as a positive number
    """
    def qii(self,row):  
        for i in row:
            if i < 0:
                return -i
                
    def simulate(self):
        Q=self.makeQarray()
        for n in range(self.nSims):
            qi=self.discSamp(self.stationaryFreq()) #pull a starting state from the stationary frequencies
            print qi
            self.chain.extend(qi)  #add state to the markov chain
            while sum(self.waitTimes) < self.chainLen:
                qiRow=q[self.stateSpace.index(qi)] #pull the row corresponding to state qi
                print qiRow
                l=self.qii(qiRow) #pull qii from row of state qi
                print l
                wait=random.expovariate(l) #pull waiting time
                print wait
                self.waitTimes.extend(wait) #add to list
                conditionalProbs=[qij/l for qij in qiRow] #conditional probabilities
                for x in conditionalProbs == -1:
                    conditionalProbs[x]=0
                if conditionalProbs[qi] == 0: #add check here to make sure qii/qii==0
                    qi=self.discSamp(conditionalProbs) #sample new state from qi row, create new qi
                    self.chain.extend(qi)
                else:
                    print "qii value is incorrect, something is wrong"
            if len(self.chain)==len(self.waitTimes):
                return self.chain, self.waitTimes
            else:
                print "you have unequal lists for wait times and chain states"
                    
                
cha1=Markov()
print cha1       
