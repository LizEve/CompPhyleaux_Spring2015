*** Discrete Sampling Practice ***

---> Creating useful functions <---
"""
(1) Write a function that multiplies all consecutively decreasing numbers between a maximum and a minimum supplied as arguments. (Like a factorial, but not necessarily going all the way to 1). This calculation would look like:  max * max-1 * max-2 * ... * min
"""
import time

import random

from __future__ import division

import matplotlib.pyplot as plt
#basically a factorial calculation between two numbers
def multip_range(max,min):
    total = 1 #set total to 1, not zero
    if min <= 0 or max <=0: #make sure your range doesnt equal zero
        print "your range contains the number 0 and will therefor return zero"
    else:
        for num in range(max,min-1,-1): #this works because the second argument is non-inclusive, so even if it's 0 then it will work
            total *= num #multiply all numbers together
        return total   

"""
(2) Using the function you wrote in (1), write a function that calculates the binomial coefficient (see Definition 1.4.12 in the probability reading). Actually, do this twice. The first time (2a) calculate all factorials fully. Now re-write the function and cancel as many terms as possible so you can avoid unnecessary multiplication (see the middle expression in Theorem 1.4.13).
"""

#a
def binom_coeff(n,k):
    #assigning each variable for clarity
    nk=(n-k) 
    n1=multip_range(n,1)
    #there is also a factorial function that you could use here. 
    k1=multip_range(k,1)
    #bionom_coeff equation
    binom = n1/(nk*k1)
    return binom 

#using the equation = (n*(n-1)*(n-2)...(n-k+1))/k!
#n is total number of trials
#k is number of successes
#this function cancles out a lot of factorials. 
def fast_binom_coeff(n,k):
    k1=multip_range(k,1)
    max=n
    min=(n-k+1)
    top=multip_range(max,min)
    f_binom = top/k1
    return f_binom 


"""
(3) Try calculating different binomial coefficients using both the functions from (2a) and (2b) for different values of n and k. Try some really big values there is a noticeable difference in speed between the (2a) and (2b) function. Which one is faster? By roughly how much?
"""
def time_func(n,k):
	start1=time.time()
	fast_binom_coeff(n,k)
	end1=time.time()
	total=end1-start1
	print "wow that was fast! it only took",total,"seconds"
	start2=time.time()
	binom_coeff(n,k)
	end2=time.time()
	total=end2-start2
	print "wow you are still here. that took",total,"seconds"

fast_binom_coeff(10000,2)
#takes seconds
    
binom_coeff(1000000,2)
#takes over two minutes (then I stopped it)

"""
(4) Use either function (2a) or (2b) to write a function that calculates the probability of k successes in n Bernoulli trials with probability p. This is called the Binomial(n,p) distribution. See Theorem 3.3.5 for the necessary equation. [Hint: pow(x,y) returns x^y (x raised to the power of y).]
"""
#binomial PMF
def binom_dist(k,n,p):
    #assign variable to binom coeff 
    a=fast_binom_coeff(n,k)    
    #eqn P(X=k)=(n choose k)(p^k)(1-p)^(n-k)
    bi_dist=a*pow(p,k)*pow((1-p),(n-k))
    return bi_dist
#OR
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.binomial.html
numpy.random.binomial(n, p, k)

"""
(5) Now write a function to sample from an arbitrary discrete distribution. This function should take two arguments. The first is a list of arbitrarily labeled events and the second is a list of probabilities associated with these events. Obviously, these two lists should be the same length.
"""
#events- a list of random events
#probs- the probability for each event. must add up to zero
#this pulls events randomly, with no basis on it's probabilities
def arb_disc_dist(events,probs):
    #zip together the two lists into a tuple
    event_probs=zip(events,probs)
    #randomly select a tuple. event and prob tuple. later we will parse out the event name and the probability
    evprobtupe=random.choice(event_probs)
    event=evprobtupe[0]
    prob=evprobtupe[1]
    #print event
    #print prob
    print "the probability of you eating a",event,"is",prob
 
events1=["magnet", "water bottle", "headphones", "sofa", "thermostat", "floor"]


arb_disc_dist(events1,probs1)

#Jeremy's code
def discSamp(events, probs):
	#pick random number
	ranNum = scipy.random.random()
	#open an empty list
	cumulProbs=[]
	#start by adding the first element
	cumulProbs.extend([probs[0]])
	#for elements in the range of your list after the first one[0]
	for i in range(1,leng(probs)):
		#add the probability of i plus the probability of the previous one in the list you are making cumulProbs
		cumulProbs.extend([probs[i]+cumulProbs[-1]])
	#now for all numbers in a lenght
	for i in range(0,len(probs)):
		if ranNum < cumulProbs[i]:
			return events[i]
	return None

"""
---> Sampling sites from an alignment <---

Imagine that you have a multiple sequence alignment with two kinds of sites. One type of site pattern supports the monophyly of taxon A and taxon B. The second type supports the monophyly of taxon A and taxon C.

(6) For an alignment of 400 sites, with 200 sites of type 1 and 200 of type 2, sample a new alignment (a new set of site pattern counts) with replacement from the original using your function from (5). Print out the counts of the two types.
"""
#bootstrapping

import random
#n represents the number of sites
def sampling_seq(n):
	#open list
    new_seq=[]
    #for the number of bp in the sequence, pick a random number. if its <0.5 append #1 to list, else append #2
    for bp in range(n):
        x=random.random()
        if x <= 0.5:
            new_seq.append(1)
        else:
            new_seq.append(2)
    type1=new_seq.count(1)
    type2=new_seq.count(2)
    print "there are",type1,"sites of type 1 and ",type2,"sites of type 2"
    result=(type1, type2)
    #this is a tuple, but could be a list. doesn't matter. just want to be able to pull both numbers out of results 
    return result

sampling_seq(400)
            


"""
(7) Repeat (6) 100 times and store the results in a list.
"""
#t is number of trials/repeats
#n is the number of sites in one trial
def repeat(t,n):
    results=[]
    #make a list to fill with trial results
    for num in range(t):
        x=sampling_seq(n)
        #this will return a tuple of number of sites with type 1, type two
        type1=x[0]
        type2=x[1]
        #calculate the percent of each type of site divided by total
        frac_type1=type1/n
        frac_type2=type2/n
        trial=(type1,type2, frac_type1, frac_type2)
        results.append(trial)
    return results

"""
(8) Of those 100 trials, summarize how often you saw particular proportions of type 1 vs. type 2. 
"""
#wrapping in a fuction that takes 
#t-number of trials. 
#n-number of sites. 
#site_type- which site you want to make a histogram of. type1 or type2
#bin_num- number of bins in your histogram

def make_graph(t,n,site_type,bin_num):
    if site_type == "type1":
        z=2
    elif site_type == "type2":
        z=3
    else:
        print "not a valid site type, please enter type1 or type2"
    #run t times with n bp per sequence
    run=repeat(t,n)
    #making a list of whatever type you input
    type_list=[x[z] for x in run]
    #return type_list
    #plotting said list in histogram
    plt.hist(type_list, bins = bin_num)
    plt.ylabel('number of trials')
    plt.xlabel('number of bp of choosen type in sequence')
    plt.show()

make_graph(100,400,"type1",20)
make_graph(100,400,"type2",20)

#would like to make both graphs at once but my graphing skills in python need a lot of work

"""
(9) Calculate the probabilities of the proportions you saw in (8) using the binomial probability mass function (PMF) from (4).
"""

#wrapping in a fuction that takes 
#t-number of trials. 
#n-number of sites. 
#p-probability of your site type
#site_type- which site you want to make a histogram of. type1 or type2
#bin_num- number of bins in your histogram
def make_PMF(t,n,site_type,p,bin_num):
    if site_type == "type1":
        z=0
    elif site_type == "type2":
        z=1
    else:
        print "not a valid site type, please enter type1 or type2"
    #run t times with n bp per sequence
    run=repeat(t,n)
    type_list=[x[z] for x in run]
    PMF_type1=[]
    for num in type_list:
        bd=binom_dist(num,n,p)
        PMF_type1.append(bd)
    plt.hist(type_list, bins = bin_num)
    plt.ylabel('number of trials')
    plt.xlabel('PMF value')
    plt.show()



(10) Compare your results from (8) and (9).

make_PMF(10000,400,"type1",0.5,20)
make_graph(10000,400,"type1",20)



(11) Repeat 7-10, but use 10,000 trials.
















