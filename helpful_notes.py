"""
DEFAULT VALUES 
"""
#you can do a def like this
def myfunction(x=1,y=2):
  do things in this function
#this will mean that if the user just run the function as:
myfunction()
#it will automatically run the funtion with the default values of 1 and 2

"""
Append vs Extend
"""
append:
#this just adds the whole list
x = [1, 2, 3]
x.append([4, 5])
print (x)
gives you: [1, 2, 3, [4, 5]]

extend:
#this takes the list and adds each independant element of the old list to the new one. 
x = [1, 2, 3]
x.extend([4, 5])
print (x)
gives you: [1, 2, 3, 4, 5]

"""
Recursion- check advanced python book
"""
#calling function from within function
def factorial(num):
	#set bound so that it doesn't go below 1
	if num !=1:
		return num*factorial(num-1)
	elif num == 1:
		return 1
	else:
		return -1
		#return negative to show it's failed

"""
IMPORTING short cuts
"""
import numpy as np 
#now every time you call numpy you can just use np instead. so instead of numpy.matrix you can write np.matrix

"""
OH CRAP LISTS
"""
a=[]
b=a
b.append('cat')
print(a)
['test']

#wtf??? gaaahhh!!!! so a and b become synonyms. you can redefine b and a will stay the same