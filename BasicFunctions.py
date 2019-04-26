from Deck import *
from Player import *

def hasTwoBig(player):
    hasone = False
    hastwo = False
    hasthem = False
    for card in player.hand:
        if card.suit == "Tarokk" and card.value == 21:
            hasone = True
        if card.suit == "Tarokk" and card.value == 22:
            hastwo = True
    if hasone and hastwo:
        hasthem = True
    return hasthem
def hasPagat(player):
    hasit = False
    for card in player.hand:
        if card.suit == "Tarokk" and card.value == 1:
            hasit = True
    return hasit
def hasSkiz(player):
    hasit = False
    for card in player.hand:
        if card.suit == "Tarokk" and card.value == 22:
            hasit = True
    return hasit
def hasHuszegy(player):
    hasit = False
    for card in player.hand:
        if card.suit == "Tarokk" and card.value == 21:
            hasit = True
    return hasit
def hasHusz(player):
    hasit = False
    for card in player.hand:
        if card.suit == "Tarokk" and card.value == 20:
            hasit = True
    return hasit
def hasTkilenc(player):
    hasit = False
    for card in player.hand:
        if card.suit == "Tarokk" and card.value == 19:
            hasit = True
    return hasit
def hasTnyolc(player):
    hasit = False
    for card in player.hand:
        if card.suit == "Tarokk" and card.value == 18:
            hasit = True
    return hasit
def tarokkCounter(player):
    sum = 0
    for card in player.hand:
        if card.suit == "Tarokk":
            sum+=1
    return sum
