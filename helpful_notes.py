#DEFAULT VALUES 
#you can do a def like this
def myfunction(x=1,y=2):
  do things in this function
#this will mean that if the user just run the function as:
myfunction()
#it will automatically run the funtion with the default values of 1 and 2

#Append vs Extend
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
