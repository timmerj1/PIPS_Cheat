"""
Assignment 3.2P Programming in Psychological Science
Jeroen Timmerman 12033685
"""

import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

## Q3.2P.1

"""
Simulate uniformly distributed data between -10 and 10 and show them in a 
plt.boxplot() using matplotlib. Now create a sns.violinplot() with “jittered” 
data points using sns.stripplot() with the same data using the seaborn package.
Make sure you can see the data points!

Which one do you find more insightful for your data?
"""

random_uniform_data = np.random.uniform(-10, 10, 100)

plt.figure()
plt.boxplot(random_uniform_data)
plt.savefig("Py_uniform_boxplot.png", dpi = 300)

plt.figure()
sns.violinplot(random_uniform_data)
sns.stripplot(random_uniform_data)
plt.savefig("Py_uniform_violin_jitter.png", dpi = 300)

# I found the boxplot more readable than the violinplot by itself, but the
# jitterplot portion of the violin plot was quite insightful as it really looked
# like a uniform box.

## Q3.2P.2

"""
The day that the titanic sank, was a bad day in many ways. Using an informative 
plot, check whether a passenger’s age was associated with their chance of 
survival.

TIP: When reading in the titanic csv file please do not use a path pointing to a
location on your computer like “documents/titanic.csv” but rather read the data
directly from the web (e.g., here https://shorturl.at/bhuJS). Otherwise it
doesn’t work on the laptop of your TA’s.
"""

TITANIC_DATA_LINK = ("https://raw.githubusercontent.com/hannesrosenbusch/"
                     "schiphol_class/master/titanic.csv")
titanic_data = pd.read_csv(TITANIC_DATA_LINK)
titanic_data = titanic_data.dropna(subset='Age')
titanic_data['Age'] = titanic_data['Age'].astype(int)
survival = titanic_data.groupby('Age')[['Survived']].mean().reset_index()

slope, intercept = np.polyfit(survival['Age'], survival['Survived'], 1)

survival.plot.scatter(x = 'Age', y = 'Survived')
plt.plot(survival['Age'], slope*survival['Age'] + intercept)
plt.savefig("Py_titanic_survival.png", dpi = 300)

## Q3.2P.3

"""
Load the tips dataset from the seaborn package. Make a scatter plot with 
total_bill on the x axis and tip on the y axis. Add a regression line to the 
plot. Label your x-axis and y-axis with the variable names in large font size.
"""

tips_data = sns.load_dataset('tips')
slope, intercept = np.polyfit(tips_data['total_bill'], tips_data['tip'], 1)

tips_data.plot.scatter('total_bill', 'tip')
plt.plot(tips_data['total_bill'], slope * tips_data['total_bill'] + intercept)
plt.xlabel('Total Bill', fontsize = 20)
plt.ylabel('Tips', fontsize = 20)
plt.savefig("Py_tips_scatter.png", dpi = 300)

## Q3.2P.4

"""
Let’s analyze the quality of diamonds. Make two subplots next to each other.
Plot a heatmap showing all the correlations between the numeric variables in the
diamonds dataset from seaborn. Next to the heatmap, add a kdeplot with carat on
the x axis and price on the y axis.
"""

diamonds_data = sns.load_dataset('diamonds')

fig, ax = plt.subplots(1, 2)
sns.heatmap(diamonds_data.select_dtypes(include = "number").corr(), ax = ax[0])
sns.kdeplot(diamonds_data, x = 'carat', y = 'price', ax=ax[1])
plt.savefig("Py_diamonds.png", dpi = 300)

## Q3.2P.5

"""

Define a function my_plots that takes a string as input (i.e., it has one
argument) and generates a plot. If the string is “eww” it generates a confusing,
non-informative plot. If the string is “yay” it prints a clear, informative
plot. All other inputs lead to reminders that the function should be either used
with “eww” or “yay”.
"""

def my_plots(yay_or_eww: str):
    """This function shows an informative plot when input is "yay", and an 
    uninformative plot when input is "eww"."""
    x = np.random.normal(100,15,100)
    y = 0.5 * x + 30 + np.random.standard_normal(100)
    plot = plt.figure()
    if yay_or_eww.casefold() == "eww":
        plt.bar(x, y + np.random.normal(0,50,100))
        return plot
    elif yay_or_eww.casefold() == "yay":
        plt.scatter(x,y) 
        plt.plot(x, 0.5 * x + 30)
        plt.title('Simulation y = 0.5x + 30 + E')
        plt.xlabel('x')
        plt.ylabel('y')
        return plot
    else:
        warnings.warn('Function should either be used with "eww" or "yay"')
        return plot

my_plots("YAY")
plt.savefig("Py_yay.png", dpi = 300)

## Q3.2P.6

# Old bad code
import numpy as np
import random
import time

# Deck has to be defined outside of class because otherwise ranks and suits are not callable to get deck
ranks = [str(i) for i in range(2,11)] + ["J","Q","K", "A"]
suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
deck = [i + j for i in ranks for j in suits]

class hand:
    ranks = ranks
    suits = suits
    deck = deck
    payouts = {"Royal Flush": 800,
               "Straight Flush": 50,
               "Four of a Kind": 25,
               "Full House": 9,
               "Flush": 6,
               "Straight": 4,
               "Three of a Kind": 3,
               "Two Pair": 0,
               "Pair": 0,
               "High Card": 0}
    
    def __init__(self, cards: list):
        self.cards = cards
        self.suits = [i[-1] for i in cards]
        self.ranks = [i[:-1] for i in cards]
    def is_flush(self):
        return len(set(self.suits)) == 1
    def is_straight(self):
        index = sorted([hand.ranks.index(i) for i in self.ranks])
        return index == [*range(min(index),max(index))]
    def is_straightflush(self):
        return self.is_straight() and self.is_flush()
    def is_fullhouse(self):
        return len(set(self.suits)) == 2
    def is_onepair(self):
        return len(set(self.ranks)) == len(self.ranks) - 1
    def is_fourofakind(self):
        return len(set(self.ranks)) == 2
    def is_twopairs(self):
        duplicates = [i for i in self.ranks if self.ranks.count(i) > 1]
        return len(duplicates) == 2
    def is_threeofakind(self):
        duplicates = [i for i in self.ranks if self.ranks.count(i) == 3]
        return len(duplicates) == 2
    def is_royalflush(self):
        isroyal = set(self.ranks) == set(hand.ranks[-5:])
        return isroyal and self.is_flush()
    def evaluatecombination(self):
        if self.is_royalflush():
            return "Royal Flush"
        elif self.is_straightflush():
            return "Straight Flush"
        elif self.is_fourofakind():
            return "Four of a Kind"
        elif self.is_fullhouse():
            return "Full House"
        elif self.is_flush():
            return "Flush"
        elif self.is_straight():
            return "Straight"
        elif self.is_threeofakind():
            return "Three of a Kind"
        elif self.is_twopairs():
            return "Two Pair"
        elif self.is_onepair():
            return "Pair"
        else:
            return "High Card"

def play():
    """
    Play a game of video poker.
    Payouts as defined by hand.payouts:
    Royal Flush: 800,
    Straight Flush: 50,
    Four of a Kind: 25,
    Full House: 9,
    Flush: 6,
    Straight: 4,
    Three of a Kind: 3,
    Two Pair: 0,
    Pair: 0,
    High Card: 0
    """

    keepplaying = True # To initiate the while loop to play
    wallet = float(input("What's in your Wallet? \n"))
    time.sleep(0.5) # To make the code run less instantaneous, makes it feel more natural.

    while keepplaying == True and wallet > 0:
        bet = float(input(f"\nIn wallet: {wallet:.2f}\nWhat are you betting?\nBet value: "))
        if bet > wallet:
            print("You don't have that kind of money. Bet less or come back when you have some more money in your wallet.")
            break

        cards = hand(random.sample(hand.deck, k = 5))
        combination = cards.evaluatecombination()
        value = bet * hand.payouts[combination]
        outcome = value - bet
        wallet += outcome
        time.sleep(0.5)

        print(f"Your cards:\n{cards.cards}\n{combination}!\n")
        time.sleep(0.5)

        if outcome < 1:
            print(f"You lost: {outcome:.2f}\nNow in your wallet: {wallet:.2f}")
        else:
            print(f"You won: {outcome:.2f}\nNow in your wallet: {wallet:.2f}")
        if wallet == 0:
            print("You're out of Money! Come back some other time!")
            break
        time.sleep(0.5)

        keepplaying = bool(float(input("Enter 1 if you want to keep playing, otherwise enter 0:\n")))
        time.sleep(0.5)

# New good code
"""
Module providing a function to play poker games, as well as a handy class for 
cards and checking poker hands.
"""
import random
import time

# Deck has to be defined outside of class because otherwise ranks and suits are
# not callable to get deck
ranks = [str(i) for i in range(2,11)] + ["J","Q","K", "A"]
suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
deck = [i + j for i in ranks for j in suits]

class Hand:
    """Class representing cards and card hands"""
    ranks = ranks
    suits = suits
    deck = deck
    payouts = {"Royal Flush": 800,
               "Straight Flush": 50,
               "Four of a Kind": 25,
               "Full House": 9,
               "Flush": 6,
               "Straight": 4,
               "Three of a Kind": 3,
               "Two Pair": 0,
               "Pair": 0,
               "High Card": 0}
    def __init__(self, cards: list):
        self.cards = cards
        self.suits = [i[-1] for i in cards]
        self.ranks = [i[:-1] for i in cards]
    def is_flush(self):
        """Checks whether a hand is flush, so if all suits are the same."""
        return len(set(self.suits)) == 1
    def is_straight(self):
        """Checks whether a hand is straight, so if the card ranks are ascending
        by one."""
        index = sorted([Hand.ranks.index(i) for i in self.ranks])
        return index == [*range(min(index),max(index))]
    def is_straightflush(self):
        """Checks whether a hand is a straight flush."""
        return self.is_straight() and self.is_flush()
    def is_fullhouse(self):
        """Checks whether a hand is a full house."""
        return len(set(self.suits)) == 2
    def is_onepair(self):
        """Checks whether a hand has one pair."""
        return len(set(self.ranks)) == len(self.ranks) - 1
    def is_fourofakind(self):
        """Checks whether a hand has four of a kind."""
        return len(set(self.ranks)) == 2
    def is_twopairs(self):
        """Checks whether a hand has two pairs."""
        duplicates = [i for i in self.ranks if self.ranks.count(i) > 1]
        return len(duplicates) == 2
    def is_threeofakind(self):
        """Checks whether a hand has three of a kind"""
        duplicates = [i for i in self.ranks if self.ranks.count(i) == 3]
        return len(duplicates) == 2
    def is_royalflush(self):
        """Checks whether a hand is a royal flush"""
        isroyal = set(self.ranks) == set(Hand.ranks[-5:])
        return isroyal and self.is_flush()
    def evaluatecombination(self):
        """Evaluates what poker hand you have."""
        if self.is_royalflush():
            return "Royal Flush"
        elif self.is_straightflush():
            return "Straight Flush"
        elif self.is_fourofakind():
            return "Four of a Kind"
        elif self.is_fullhouse():
            return "Full House"
        elif self.is_flush():
            return "Flush"
        elif self.is_straight():
            return "Straight"
        elif self.is_threeofakind():
            return "Three of a Kind"
        elif self.is_twopairs():
            return "Two Pair"
        elif self.is_onepair():
            return "Pair"
        else:
            return "High Card"

def play():
    """
    Play a game of video poker.
    Payouts as defined by Hand.payouts:
    Royal Flush: 800,
    Straight Flush: 50,
    Four of a Kind: 25,
    Full House: 9,
    Flush: 6,
    Straight: 4,
    Three of a Kind: 3,
    Two Pair: 0,
    Pair: 0,
    High Card: 0
    """

    keepplaying = True # To initiate the while loop to play
    wallet = float(input("What's in your Wallet? \n"))
    time.sleep(0.5) # To make the gameplay feel more natural.

    while keepplaying is True and wallet > 0:
        bet = float(input(f"\nIn wallet: {wallet:.2f}\nWhat are you betting?"\
                          "\nBet value: "))
        if bet > wallet:
            print("You don't have that kind of money. Bet less or come back "\
                  "when you have some more money in your wallet.")
            break

        cards = Hand(random.sample(Hand.deck, k = 5)) # create random hand
        combination = cards.evaluatecombination()
        value = bet * Hand.payouts[combination]
        outcome = value - bet
        wallet += outcome
        time.sleep(0.5)

        print(f"Your cards:\n{cards.cards}\n{combination}!\n")
        time.sleep(0.5)

        if outcome < 1:
            print(f"You lost: {outcome:.2f}\nNow in your wallet: {wallet:.2f}")
        else:
            print(f"You won: {outcome:.2f}\nNow in your wallet: {wallet:.2f}")
        if wallet == 0:
            print("You're out of Money! Come back some other time!")
            break
        time.sleep(0.5)

        keepplaying = bool(float(input("Enter 1 if you want to keep playing, "\
                                       "otherwise enter 0:\n")))
        time.sleep(0.5)

## Q3.2P.7

"""
Many conventions and style guidelines for Python code are universally accepted.
However, sometimes there is controversy about “the best way to do things”. Find
one of these issues and state in two brief sentences which side you are on.
"""

# I think one controversy is the max 80 character rule
# (https://www.reddit.com/r/Python/comments/csyoge/pep8_line_length_at_80_is_very_strange/)
# (https://pythonsway.it/pep8-style-controversy/)
# In many cases, breaking certain strings to span multiple lines does not make 
# that much sense, for example the link I used for Q3.2P.2, or the reddit link 
# above. I feel like in most IDEs you can just use line wrapping anyway which I 
# honestly prefer over both options. 

## Q3.2P.8

"""
Michael is a sloppy Python coder: https://github.com/mdnunez/pyhddmjags/blob/master/pyhddmjagsutils.py 
Choose one of his functions to improve by using a pylint and creating better 
variable names and comments. Explain what you did to change his code to PEP8 and
discuss how else you improved his code. If his old code was already perfect 
explain why.
"""

def shape_stan_samples(samples_in: dict):
    """For each value in dictionary not starting with '_', moves first two 
    axes of shape to last two positions in shape. If there are only two axes,
    an extra dimension is added."""
    result = {} # To store reshaped samples in
    for key in samples_in.keys():
        if key[0] != '_':
            possamps = samples_in[key]
            # Move first 2 axes to the end:
            bettersamps = np.moveaxis(possamps,(0,1), (-2,-1))
            if len(bettersamps.shape) == 2:
                # Increase number of axes:
                reshapedsamps = np.reshape(bettersamps, (1,) +\
                                           bettersamps.shape[0:2])
                result[key] = reshapedsamps
            else:
                result[key] = bettersamps
    return result
