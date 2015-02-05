# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 12:40:17 2015

@author: ChatNoir
"""

from LH_code import *
from scipy.stats import binom
import random

#calculate LH score. similar to binom pmf value (binom_dist(k,n,p))
#starting paramater value = pCurr
#p_start = starting parameter value
#diff = starting step size
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
        if LHc<LHu:
            pc=pu
            pu+=diff
            pd-=diff 
        if LHc>LHu and LHc>LHd:
            diff=diff/2
    return [LHc,pc]

x=ML_robot(60,100)
print x


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
        ML_list.append(ML)
        return ML_list
        


TrueP()










