#!/usr/bin/env python

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

    def moves(self,deck):
        action = ''
        while ((action != 'stand') and (self.hand <= self.maxHand)):
            action = input('"hit" or "stand": ')
            self.play(action,deck)

    def play(self,act,deck):
        if (act == 'hit'):
            self.hit(deck)
        if (self.hand > 21):
            print('{} busted with a hand of {} which is greater than 21'.format(self.name,self.hand))
            self.bust = True

    # TODO: Version 2.0
    def checkBlackjack(self):
        pass


class Dealer(Player):
    def __init__(self,name,deck,maxHand=17):
        Player.__init__(self,name,deck,maxHand)

    def moves(self,deck):
        while (self.hand <= self.maxHand):
            self.play('hit',deck)


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


# Initialize Deck
deck = Deck()
print(deck.cards)

# Initialize players, deal cards
player1 = Player('Player1',deck)
player2 = Player('Player2',deck)
dealer = Dealer('Dealer',deck,17)
players = [ player1, player2 ]
allPlayers = players + [ dealer ]
validPlayers = [ ]

for i in range(0,2):
    for player in allPlayers:
        player.deal(deck)
        player.calcHand(True)

# Player moves, then add player to validPlayers if didn't bust.
for player in players:
    player.calcHand()
    player.checkBlackjack()
    player.moves(deck)
    if (player.bust == False):
        validPlayers.append(player)

# Dealer moves if needed
dealer.calcHand()
dealer.checkBlackjack()

if ( len(validPlayers) == 0):
    print('All players busted, Dealer wins with {}.'.format(dealer.hand))
    exit()
else:
    dealer.moves(deck)


# Get winners out of all players who haven't busted.
for player in validPlayers:
    if ((player.hand > dealer.hand) or (dealer.bust == True)):
        print('{} beats the dealer with a hand of {}.'.format(player.name,player.hand))
    else:
       print('Dealer beats {} with a hand of {}.'.format(player.name,dealer.hand))
