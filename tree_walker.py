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
import math
import operator
import functools

class Markov(object):
    
    def __init__(self,q=[[-0.75,0.25,0.25,0.25],
                        [0.25,-0.75,0.25,0.25],
                        [0.25,0.25,-0.75,0.25],
                        [0.25,0.25,0.25,-0.75]],chainLen=2,stateSpace=['a','c','g','t'],nSims=1):
        self.q=q #Q indicates a np.array. q is a list of lists
        self.chainLen=chainLen #total times
        self.stateSpace=stateSpace
        self.nSims=nSims
        self.chains=[] #a list of character history lists across simulations
        self.waitTimes=[] #a list of wait time lists across simulations
        self.multChains=[] # paired character histories and wait times across simulations
        self.startStates=[] # start states across simulations
        self.endStates=[] #end states across simulations
        self.Q=self.makeQarray() #automatically make a Q matrix that is a sci py array of the q matrix
        self.LHlist=[]

    #def make a Q array out of r and pi values      
        
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
        
    def indexStatespace(self,stateSpace):
        """
        creates a state space that is numbers instead of letters
        """
        numStates=[]
        for state in stateSpace:
            index=stateSpace.index(state)
            numStates.append(index)
        return numStates 

    def qii(self,qi): 
        """
        returns the negative number in the row as a positive number
        """
        qiRow=self.q[self.stateSpace.index(qi)]
        for i in qiRow:
            if i < 0:
                return -i
                
    def makeQarray(self):
        Q=sp.array(self.q)
        return Q
        
    def stationaryFreq(self):
        """
        creates stationary frequencies 
        """
        statFreqmat=sp.linalg.expm(self.Q*100) #exponentiate to a very large number to get stationary freqs
        #theoretically put in a check here to make sure all numbers in a column are almost identicle. 
        statFreqA=statFreqmat[0,1] #store each stationary frequency
        statFreqC=statFreqmat[1,0]
        statFreqG=statFreqmat[2,0]
        statFreqT=statFreqmat[3,0]
        statFreq=[statFreqA,statFreqC,statFreqG,statFreqT] #should round these numbers off 
        return statFreq       
        
                
    def simulate(self):
        """
        simulates character history along a branch, starting with a base pulled from the stationary frequencies
        returns a list of character histories and waiting times, in that order
        each time simulator is run it appends the appropriate lists to the chain history and wait times
        the result is that when multsims is run, chains and waitTimes will also be added to and be callable. 
        also added to list of starting and ending states
        """
        ch=[] #create localized chain and wait time to allow for multiple sims
        wT=[]
        qi=self.discSamp(self.stationaryFreq()) #pull a starting state from the stationary frequencies
        self.startStates.append(qi)        
        #print qi
        ch.extend(qi)  #add state to the markov chain
        while sum(wT) < self.chainLen:
            qiRow=self.q[self.stateSpace.index(qi)]
            l=self.qii(qi) #pull qii from row of state qi
            #print l
            wait=random.expovariate(l) #pull waiting time from exponendial distribution, lambda=l=|qii|
            #print wait
            if wait+sum(wT) < self.chainLen: #only add another time if it doesn't go over the total length
                wT.append(wait) #add to list
                #print wT
                conditionalProbs=[qij/l for qij in qiRow] #conditional probabilities
                for i in conditionalProbs:
                    if i == -1:
                        conditionalProbs[conditionalProbs.index(i)]=0
                qi=self.discSamp(conditionalProbs) #sample new state from qi row, based on condProbs,
                ch.extend(qi) # create new qii and add state to list 
                #print ch
            elif wait+sum(wT) >= self.chainLen: #if adding another time will extend it past the branch length, just add a length that covers the rest of the time. 
                last_time=self.chainLen-sum(wT)
                #print 
                wT.append(last_time)
                #print 
                conditionalProbs=[qij/l for qij in qiRow] #conditional probabilities
                for i in conditionalProbs:
                    if i == -1:
                        conditionalProbs[conditionalProbs.index(i)]=0
                last_qi=self.discSamp(conditionalProbs) 
                ch.extend(last_qi)
                self.endStates.append(last_qi)
                #print ch   
        self.waitTimes.append(wT)
        self.chains.append(ch)
        pair=[ch,wT]
        return ch,wT,pair
        
    def multSims(self):
        #if you want to re-set every time you run multiple chains
        #self.chain=[]
        #self.waitTimes=[]
        #self.multSims=[]
        for n in range(self.nSims):
            sim=self.simulate()
            self.multChains.append(sim[2])
        return self.multChains  #returned as a list of lits. lists of paired chains and wait times 
       

    """
    would like to make the following it's own subclass. 
    need to learn more about classes before i do that. 
    class MrkvStats(Markov):
        
        def __init__(self):
            super(MrkvStats, self).__init__(self)    
            self.Q=self.makeQarray()
            self.LHlist=[]
    """
    
    def calcHistProb(self,stateHist,timeHist):
        """
        P(i)*P(j|i)*P(t)..... etc
        P(i)=stationary prob of P(i)
        P(j|i)=|(qij/qii)|
        P(t)=-qii*e^(qii*t)
        P(no change before last time)=1-(1-e^-qii*x)
        """
        Q=self.makeQarray()
        statFreq=self.stationaryFreq() #store stationary freqs
        totalProb=[]
        totalProb.append(statFreq[self.stateSpace.index(stateHist[0])])   #start list with initial probability from stationary frequencies 
        for monkey in range(len(stateHist)-1):
            qij=Q[self.stateSpace.index(stateHist[monkey]),self.stateSpace.index(stateHist[(monkey+1)])] #iterate through index in state histories. pass each state and its following state to state space, get an index of the state from there, then find it in the q matrix 
            totalProb.append(qij)
            x=timeHist[monkey]
            qii=-Q[self.stateSpace.index(stateHist[monkey]),self.stateSpace.index(stateHist[(monkey)])]
            pdf = qii * math.exp(-qii * x) #returns the PDF of the waiting time based on the state
            totalProb.append(pdf)
        lastqii=-Q[self.stateSpace.index(stateHist[-1]),self.stateSpace.index(stateHist[-1])]
        lastTimeP=math.exp(-lastqii * timeHist[-1]) # 1-cdf. cdf= 1- e^-qii*x
        totalProb.append(lastTimeP)
        LH=functools.reduce(operator.mul, totalProb, 1)
        return LH
                 
    def margProbMatrix(self,V):
        """
        marginalizes over a length of time
        multiple substitutions over that time are assumed
        large values passed to this will create stationary frequencies
        """
        marg=sp.linalg.expm(self.Q*V)
        return marg
        
    def margProb(self,start,end,V):
        """
        takes a starting value and an ending value
        uses the branch length you gave the Markov class and returns the likelihood aka marg prob for those values
        """
        matrix=self.margProbMatrix(V)
        LH=matrix[self.stateSpace.index(start),self.stateSpace.index(end)]
        return LH
    
    def LHMultSites(self):
        """
        automatically uses lists of starts and end states that were stored from the multiple simulations
        not sure if i want to change this to accept other input for the start and end lists
        """
        if len(self.endStates) != len(self.startStates):
            print "something went wrong! lists are different lenghts. this should be impossible, but you managed it. congrats?"
        else:
            for num in range(len(self.startStates)):
                start=self.startStates[num]
                end=self.endStates[num]
                LH=self.margProb(start,end,self.chainLen)
                self.LHlist.append(LH)        

    def totalLH(self):
        total=functools.reduce(operator.mul, self.LHlist, 1)
        return total
            
    def LHBranchCalc(self,V):
        """
        similar to LH MultSites but this requires V input
        output is single number
        """
        if len(self.endStates) != len(self.startStates):
            print "something went wrong! lists are different lenghts. this should be impossible, but you managed it. congrats?"
        else:
            branchLH=1
            for num in range(len(self.startStates)):
                start=self.startStates[num]
                end=self.endStates[num]
                LH=self.margProb(start,end,V)
                branchLH*=LH
            return branchLH   
        
    """
    a=Markov(nSims=5)
    a.multSims()
    a.margProbMulti()
    print a.totaLH()
    """
    """
    def branchEst(self,start,end,initV,diff=0.1,cutOff=0.001,maxBranch=20):
        LH=totalLH()
        if LH==0:
            print "you need to run margProbMult() to create likelihoods for your sites"
        else:
            currV=initV
            for num in range(len(self.startStates)):
                
     """
        #print pc
        #while the diff btw the p values is larger than your cutoff
        #while diff>cut_off:
        #   pu=pc+diff
        #   pd=pc-diff
        #    LHc=binom_dist(k,n,pc)
        #    LHu=binom_dist(k,n,pu)
        #    LHd=binom_dist(k,n,pd)
            #print LHc,LHu,LHd
            #print pc,pu,pd
        #    if LHc<LHd:
        #        pc=pd
        #        pu+=diff
        #        pd-=diff
        #    elif LHc<LHu:
        #        pc=pu
        #        pu+=diff
        #        pd-=diff 
        #    elif LHc>LHu and LHc>LHd: #could also just put else
        #        diff=diff/2
        #return [LHc,pc] 
                
       
       


"""       
     =================================                
            currLH=1
            for i in 1,2,....,nsites:
                currLH*=LH of site i
          
            #initV=currV
            #for element in startStates (if multiple sites)
                #calc current likelihood of initV- marginalize Q over V. get qij
            #calc LH for currV-diff
            #calc LH for currV+diff
            #make sure that branch lengths stay above 0
            #while(diff>thresh):
                #if (upLH > currLH):
                    #currV=branchEst(upV,diff,thresh)
                #elif(downLH>currLH):
                    #currV=branchEst(downV,diff,thresh)
                #diff *=0.5
                #currLH = LHcalc(currV)
                #calc LH for currV-diff
                #calc LH for currV+diff
            #return currV & currLH
        
        def ML_robot(k,n,diff=0.1,cut_off=0.001):
        #set initial parameter value    
        pc=random.random()
        #print pc
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
            elif LHc<LHu:
                pc=pu
                pu+=diff
                pd-=diff 
            elif LHc>LHu and LHc>LHd: #could also just put else
                diff=diff/2
        return [LHc,pc]
        
        
        #create object for note
        #create object for tree
        #figure out how to store 
"""