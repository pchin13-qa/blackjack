#!/usr/bin/env python

# TODO: Make a main Person class, then subclasses of Player and Dealer
class Player():
    def __init__(self,name,deck,maxHand=31):
        self.hand = 0
        self.cards = [ ]
        self.maxHand = maxHand
        self.name = name
        self.bust = False

    def deal(self,deck):
       card = deck.cards.pop(0) 
       # Put aces at end of list because we have to calculate if it's 1 or 11 after all number cards
       if (card == 'A'):
           self.cards.append(card)
       else:
           self.cards.insert(0,card)

    def hit(self,deck):
        self.deal(deck)
        self.calcHand()

    def calcHand(self,quiet=False):
        self.hand = 0
        for c in self.cards:
           if ((c == 'A') and (self.hand > 10)):
               self.hand += 1
           elif ((c == 'A') and (self.hand <= 10)):
               self.hand += 11
           else:
               self.hand += c
        if (quiet == False):
            print('{} has a hand of {} which totals {}.'.format(self.name,self.cards,self.hand))

    # TODO: Version 2.0
    def checkBlackjack(self):
        pass

''' #################################### '''
import random

class Deck():
    def __init__(self):
        self.types = [ value for value in range(2,11) ]
        self.types.extend([10,10,10,"A"])
        self.cards = [ value for i in range(0,4) for value in self.types ]
        self.shuffleDeck()

    # Shuffle deck
    def shuffleDeck(self):
        random.shuffle(self.cards)

    def getDeck(self):
        return self.cards

''' #################################### '''

def play(pers,act):
    if (act == 'hit'):
        pers.hit(deck)
    if (pers.hand > 21):
        print('{} busted with a hand of {} which is greater than 21'.format(pers.name,pers.hand))
        pers.bust = True


# Initialize Deck
deck = Deck()
print(deck.cards)

# Initialize players, deal cards
player1 = Player('Player1',deck)
dealer = Player('Dealer',deck,17)
players = [ player1 ]
allPlayers = players + [ dealer ]

for i in range(0,2):
    for player in allPlayers:
        player.deal(deck)
        player.calcHand(True)

# Player moves
for player in players:
    player.calcHand()
    player.checkBlackjack()

    action = ''
    while ((action != 'stand') and (player.hand <= 21) and (player.hand <= player1.maxHand)):
        action = input('"hit" or "stand": ')
        play(player,action)

# Dealer moves
# TODO: There has got to be a better way to abstract the while loops into another function like play!  Iterate over allPlayers, if busted then remove the player from the list, then check hand values.
# TODO: There has GOT to be a better way to do this instead of if-else statements!
if (player1.bust == True):
    print('Player1 busted, Dealer wins with {}'.format(dealer.hand))
else:
    action = ''
    dealer.calcHand()
    while ((dealer.hand <= 21) and (dealer.hand < dealer.maxHand)):
        play(dealer,'hit')
    if (dealer.bust == True):
        print('Dealer busted, Player1 wins with {}'.format(player1.hand))
    elif (player1.hand > dealer.hand):
        print('Player1 hand is {} which beats the Dealer hand of {}'.format(player1.hand,dealer.hand))
    else:
        print('Dealer hand is {} which beats the Player1 hand of {}'.format(dealer.hand,player1.hand))
