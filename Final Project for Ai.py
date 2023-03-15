#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random #to get a random number for guessing
import math
import winsound #for adding sound


# In[6]:



lower = int(input("Enter Lower bound(0<):- ")) #we will take input for lower number (from my side,it is better to take the input manually,even i added the requirement according to the question) )
 
upper = int(input("Enter Upper bound(>100):- ")) #input for higest number
 


x = random.randint(lower, upper) # generating random number between(the number which will be guessed)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n") #according to the difference of number ,will make a range of guessing
 

count = 0-10 #according to question we should consider as a game so, added the the how many times we tried for guessing.it will show the result after the right guess
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
 
    # taking guessing number as input
    guess = int(input("Can you please guess a number?:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations, you made it in ",
              count, " try")
        #duration = 4000  # Set Duration To 1000 ms == 1 second #i tried to make it little bit longer using duration,but failed to make it long
        winsound.PlaySound("*", winsound.SND_ALIAS)
        break ## Once guessed, loop will break
    elif x > guess:
        print("You guessed too small!")
        frequency = 2500  # Set Frequency To 2500 Hertz(how loud it will be)
        duration = 2000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    elif x < guess:
        print("You Guessed too high!")
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 4000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
 
# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")


# In[ ]:




