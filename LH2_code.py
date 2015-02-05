# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 12:40:17 2015

@author: ChatNoir
"""

from LH_code import *
from scipy.stats import binom

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

ML_robot(60,100,0.2,0.1)


real_p=.5

ML_list=[]

LH_list=[]

k=binom.rvs(n,p)














