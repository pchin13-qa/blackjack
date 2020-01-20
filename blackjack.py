#!/usr/bin/env python

class Player():
    def __init__(self,name,maxHand,deck):
        self.handUpper = 0
        self.handLower = 0
        self.hand = 0
        self.maxHand = maxHand
        self.name = name
        self.bust = False
        # Initiate hand
        ''' TODO: This should not be in the __init__.  Should iterate over each player and give each one a card in order. '''
        for i in range(0,2):
            self.hit(deck) 
        self.checkBlackjack()

    def hit(self,deck):
        card = deck.cards.pop(0)
        ''' Corner case - if you have multiple Aces this won't work, you're likely to go over 21.
            Probably need a list of cards that you re-compute after every hit, and compute all ace values at end. '''
        if ((card == 'A') and (self.hand > 10)):
            self.updateHand(1)
        elif ((card == 'A') and (self.hand <= 10)):
            self.updateHand(11)
        else:
            self.updateHand(card)
        print('Card is {}, {} hand is {}.'.format(card,self.name,self.hand))

    def updateHand(self,card):
        self.hand += card

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

# Initialize players
player1 = Player('Player1',30,deck)
print('{} has a hand of {}.'.format(player1.name,player1.hand))
dealer = Player('Dealer',17,deck)
print('{} has a hand of {}.'.format(dealer.name,dealer.hand))

# Player1 moves
action = ''
while ((action != 'stand') and (player1.hand <= 21) and (player1.hand <= player1.maxHand)):
    action = input('"hit" or "stand": ')
    play(player1,action)

# Dealer moves
# TODO: There has got to be a better way to abstract the while loops into another function like play!
# TODO: There has GOT to be a better way to do this instead of if-else statements!
if (player1.bust == True):
    print('Player1 busted, Dealer wins with {}'.format(dealer.hand))
else:
    action = ''
    while ((dealer.hand <= 21) and (dealer.hand < dealer.maxHand)):
        play(dealer,'hit')
    if (dealer.bust == True):
        print('Dealer busted, Player1 wins with {}'.format(player1.hand))
    elif (player1.hand > dealer.hand):
        print('Player1 hand is {} which beats the Dealer hand of {}'.format(player1.hand,dealer.hand))
    else:
        print('Dealer hand is {} which beats the Player1 hand of {}'.format(dealer.hand,player1.hand))
