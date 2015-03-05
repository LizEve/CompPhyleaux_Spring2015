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

q=[[-0.75,0.25,0.25,0.25],[0.25,-0.75,0.25,0.25],[0.25,0.25,-0.75,0.25],[0.25,0.25,0.25,-0.75]]
chainLen=10
stateSpace=['a','c','g','t']
nsims=1
longV=100
Q=sp.array(q)
chain=[]
waitTimes=[]
print q.range()
qi='a'
qiRow=q[stateSpace.index(qi)]
l=0.75
x=[qij/l for qij in qiRow]
print x
print qiRow
conditionalProbs=[qij/l for qij in qiRow]
print conditionalProbs

for i in conditionalProbs:
    if i == -1:
         conditionalProbs[conditionalProbs.index(i)]=0

print conditionalProbs


def margProbs(branch_len):
    marg=sp.linalg.expm(Q*branch_len)
    return marg

margProbs(5)


def makeQarray(q):
    Q=sp.array(q)
    return Q
        
Q=makeQarray(q)

statFreqmat=sp.linalg.expm(Q*longV)    
statFreq=[]
statFreqA=statFreqmat[0,1]
statFreqC=statFreqmat[1,0]
statFreqG=statFreqmat[2,0]
statFreqT=statFreqmat[3,0]
statFreq.append([statFreqA,statFreqC,statFreqG,statFreqT])
        
def stationaryFreq(Q,longV):

    statFreqmat=sp.linalg.expm(Q*longV)
    statFreqA=statFreqmat[0,1]
    statFreqC=statFreqmat[1,0]
    statFreqG=statFreqmat[2,0]
    statFreqT=statFreqmat[3,0]
    statFreq=[statFreqA,statFreqC,statFreqG,statFreqT]
    return statFreq       

statFreq=stationaryFreq(Q,longV)
print statFreq
statFreq=[]
stateHist=['t', 'g', 'c', 't', 'c', 'a', 'c', 'a', 'c']
timeHist=[0.30128339968394346, 0.4838314807043198, 4.0934644738405375, 2.879742835201872, 0.901128743239807, 0.2756532847403307, 0.5581161157285621, 1.091560978118395]
print stateHist[0]
print statFreq[stateSpace.index(stateHist[0])]
print statFreq[1]

qi=stateHist.index[i]
j=i+1
qj=stateHist.index[j]

for count in range(len(stateHist)):
    print count
    i=stateHist[count]
    print i
    j=stateHist[count+1]
    print i,j
    print count
    print i
    qiRow=Q[stateSpace.index(i)]
    print qiRow
    #j=stateHist.index[]
    qij=qiRow[count+1]
    print qij
    count+=1
    print count
    
    #j=qiRow[stateSpace.index(j)]
    

def calcHistProb(self,stateHist,timeHist):
        totalProb=[]
        for i in stateHist:
            totalProb.extend(self.stationaryFreq[self.stateSpace[statHist[0]]])
  
def discSamp(probs):
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
           return statespace[i] #state space will always be same. 
    return None     #if none of the above happens. return nothing. 
  
def qii(row):  
    for i in row:
        if i < 0:
            return -i
qi='a'
qiRow=Q[stateSpace.index(qi)]
print qiRow
diag=qii(qiRow)
print diag

def simulate(Q,nsims,statFreq,stateSpace,chain,waitTimes):
    for n in range(nsims):
        qi=discSamp(statFreq) #pull a starting state from the stationary frequencies
        chain.extend(qi)  #add state to the markov chain
        while sum(waitTimes) < chainLen:
            qiRow=Q[stateSpace.index(qi)] #pull the row corresponding to state qi
            l=qii(qiRow) #pull qii from row of state qi
            wait=random.expovariate(l) #pull waiting time
            waitTimes.extend(wait) #add to list
            conditionalProbs=[qij/qii for qij in qiRow] #conditional probabilities
            if conditionalProbs[0] == -1: #add check here to make sure qii/qii==0
                qi=discSamp(conditionalProbs) #sample new state from qi row, create new qi
                schain.extend(qi)
            else:
                print "qii value is incorrect, something is wrong"
        if len(chain)==len(waitTimes):
            return chain, waitTimes
        else:
            print "you have unequal lists for wait times and chain states"

x=simulate(Q,nsims,statFreq,stateSpace,chain,waitTimes)






































freq


class Markov(object):
    
class DiscMark(Markov):

class ContMark(Markov):

    def __init__(self,Q[[-0.75,0.25,0.25,0.25],
                        [0.25,-0.75,0.25,0.25],
                        [0.25,0.25,-0.75,0.25],
                        [0.25,0.25,0.25,-0.75]],v=10,statespace=(a,t,g,c),nsims=1,states,time):
        # to make the chain:  q matrix, branch lenght, state space,         
        self.Q=Q
        self.v=v
        self.statespace=statespace
        self.nsims=nsims
        # store the chain: states and waiting times
        self.states=[]
        self.time=[]
        # make sure len(chain)=len(wait)
        #maybe you always want to simulate
        self.simulate()
        
    def simulate(self):
        for i in frange(nsims):
        
    def stateTime(self):
        #time in each state
    
    def endFreqs(self):
        #freq of ending in each state
    
    
#could also make this class input states and times, and then you would want to calc the frequenceies of each state
    def calcHistProb(self):
        #calculate prob of seeing entire history
        #calc prob for each state
    
    def calcMargProb(self):
        #calculate prob of ending given beginning. 
        #this is based on e^Qv info
        #built into scipy scipy.linalg.expm(Q*v) -> Q needs to be an array. take a list of list and make it an array. 
    
    
    
    
def discSamp(events,probs):
        """
        @author: JeremyBrown
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
        print cumulProbs
        for i in range(1,len(probs)):
            cumulProbs.extend([probs[i]+cumulProbs[-1]])
            print cumulProbs
        for i in range(0,len(probs)):
            if ranNum < cumulProbs[i]:
               return events[i]
        return None    
        
q=[[-0.75,0.25,0.25,0.25],[0.25,-0.75,0.25,0.25],[0.25,0.25,-0.75,0.25],[0.25,0.25,0.25,-0.75]]
Q=np.array(q)   
         
a= Q[0]
def qii(row):  
        for i in row:
            if i < 0:
                return -i
print qii(a)
            
            
stateSpace=('a','c','g','t')

def stationaryFreq(Q,longV):
        #exponentiate to a very large number ot get stationary freqs
        statFreqmat=sp.linalg.expm(Q*longV)
        #theoretically put in a check here to make sure all numbers in a column are almost identicle. 
        statFreqA=statFreqmat[0,1]
        statFreqC=statFreqmat[1,0]
        statFreqG=statFreqmat[2,0]
        statFreqT=statFreqmat[3,0]
        statFreq=[statFreqA,statFreqC,statFreqG,statFreqT]
        return statFreq

stationaryFreq(Q,100)
print sp.linalg.expm(q*100)
print statFreqmat
q*100
l=qii(q[stateSpace.index(qi)])
qi='a'
print l

qiRow=Q[stateSpace.index(qi)]
diag=qii(a)
print qiRow/diag
print qiRow