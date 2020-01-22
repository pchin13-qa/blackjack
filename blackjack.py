#!/usr/bin/env python

# TODO: Make a main Person class, then subclasses of Player and Dealer
class Player():
    def __init__(self,name,deck,maxHand=21):
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
        allPlayers.remove(pers)


# Initialize Deck
deck = Deck()
print(deck.cards)

# Initialize players, deal cards
player1 = Player('Player1',deck)
player2 = Player('Player2',deck)
dealer = Player('Dealer',deck,17)
players = [ player1, player2 ]
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
    while ((action != 'stand') and (player.hand <= player1.maxHand)):
        action = input('"hit" or "stand": ')
        play(player,action)

# Dealer moves
dealer.calcHand()
dealer.checkBlackjack()

if ( len(allPlayers) == 1):
    print('All players busted, Dealer wins with {}.'.format(dealer.hand))
    exit()
else:
    # TODO: There has got to be a better way to abstract the while loops into another function like play!  
    action = ''
    while (dealer.hand < dealer.maxHand):
        play(dealer,'hit')

# Get winner out of all players who haven't busted.
winner = ''
winning_hand = 0
for player in allPlayers:
    # This does not deal well with ties between Players
    if ((player.hand > winning_hand) or ((player.hand == winning_hand) and (player.name == 'Dealer'))):
        winner = player.name
        winning_hand = player.hand

print('{} is the winner with a hand of {}'.format(winner,winning_hand))
