## Q1.2P.1

## another_array = np.zeros((2, 4, 6))

"""
(a) This python code produces an error that the name ‘np’ is not defined. What line of code did I need to import numpy before this line or at the beginning of my Python script?
"""

import numpy as np
another_array = np.zeros((2, 4, 6))

"""
(b) Return the last element of the first dimension using the Python shortcut for a last element, the first element of the second dimension, and the 3rd element of the 3rd dimension.
"""
# instructions were a bit unclear. Do I get a single element:
another_array[-1,0,2]
# or do I get 3 seperate elements:
another_array[-1,:,:]
another_array[:,0,:]
another_array[:,:,2] #?

## Q1.2P.2

another_array = np.zeros((2, 4, 6))
new_array = another_array
new_array[1, 2, 2] = 1
print(another_array[1, 2, 2])
# What went wrong in this code? How is this different from R? How can we make a true new copy of the numpy array?

"""
another_array was affected by the changes made to new_array, as they are stored with the same id / in the same place. In R, they would be stored as seperate variables, so another_array would remain the same when new_array is changed. To make a true new copy, use .copy():
"""
another_array = np.zeros((2, 4, 6))
new_array = another_array.copy()
new_array[1, 2, 2] = 1
print(another_array[1, 2, 2])

## Q1.2P.3

"""
Note that the iPython terminal is a specific interactive terminal program that will save Python variables in a workspace like R. Other Windows, Mac, and Linux terminals can run Python scripts but are not as interactive.

Try copying some code and then pasting it into a iPython terminal using the magic function %paste. Does the %paste function work in a Python script? Why or why not?
"""

"""
Done. You use %paste to paste code that was copied to the clipboard, it does not work in a python script. Of course, if you are working with a python script, you can just copy and paste as you normally would. It's just with terminals that you can't always copy and paste straight into the terminals. It is not needed in python scripts, but it is needed when wanting to run lines of code in a terminal.
"""

## Q1.2P.4

"""
What are the magic functions in the iPython terminal to change the working directory, print the current working directory, list the contents of the working directory, and to list current workspace variables?
"""

"""
Change current directory: %cd
Print the current working directory: %pwd
List the contents of the working directory: %ls
List current workspace variables: %who_ls
"""

## Q1.2P.5

"""
What is the command that can be run in a terminal or iPython terminal to install the package pip-install-test?
"""

# pip install pip-install-test


## Q1.2P.6

sample_scores = np.array([1, 6, 7, 8, 9, np.nan])
print(np.var(sample_scores))
# This returns nan, why? Can you compute the mean with the missing value removed? Check ?np.var

# Because there is an np.nan in the array. To compute the variance with the missing value removed, you can use:
print(np.nanvar(sample_scores))
# and for the mean:
print(np.nanmean(sample_scores))

## Q1.2P.7 

"""
Make a 3 dimensional array of 4 by 3 by 5 with all elements as missing values.
"""

missing_array = np.ndarray(shape=(4,3,5))
missing_array[:] = np.nan
print(missing_array)

## Q1.2P.8

"""
Refer to problem Q.1.1.31 in Assignment 1.1. Import the EuroNumbers_data.csv file into Python as a
Python dictionary. Note that one method is to use pandas.read_csv with one additional step. 
"""

import pandas as pd
EuroNumbers = pd.read_csv("EuroNumbers_data.csv", sep=";", decimal=",")
print(EuroNumbers.head())

# How can you return the variables or keys of this dictionary in Python?
EuroNumbers.keys()

## Q1.2P.9

# We used this data to simulate the speed of R and Python on various operations.
np.random.seed(1234) # Set the random seed
speed_sec = np.zeros(10)
sim_speed = np.random.uniform(size=5) # Speed simulation in seconds
speed_sec[0:5] = sim_speed * np.random.uniform(low=0.5, high=10, size=5)
speed_sec[5:10] = sim_speed

"""
Make the following pandas.DataFrame without typing out the first two variables. You can use the variable
speed_sec for the last variable. Note that you can first make a Python dictionary before converting to a
pandas.DataFrame.

language code_type speed
0 R forloop1 0.591724
1 R forloop2 1.944967
2 R forloop3 3.553380
3 R forloop4 7.541267
4 R forloop5 6.880447
5 Python forloop1 0.191519
6 Python forloop2 0.622109
7 Python forloop3 0.437728
8 Python forloop4 0.785359
9 Python forloop5 0.779976
"""

speeds = {
    "language": ["R"] * 5 + ["Python"] * 5,
    "code_type": ["forloop" + str(i) for i in range(1,6)] * 2,
    "speed": speed_sec
}

df = pd.DataFrame(speeds)
print(df)

## Q1.2P.10

"""
Take and retake the Python Psychology Research Masters Self Diagnosis Tool of the Programming preparatory
paddling pool until you achieve a score of 85% or more (if you haven’t already). Write a brief review about
the self diagnosis tool, about what you learned (if anything) using the self diagnosis tool, and your final score
(2 to 4 sentences in total). Include your text as a comment in your solution script for these assignments.
"""

"""
I already took it in the summer. It was fine, but it ways way easier than the R self-diagnosis tool. I'm quite used to R, whereas I'm not as good with python. And yet, for the self-diagnosis tool I had 14 out of 14 for the python one first try. Also I think that it goes over some things that I would never use, like ' '.join(os.listdir(os.getcwd())), which is something that doesn't seem that useful to know by heart.
"""
