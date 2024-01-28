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
