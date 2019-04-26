import random
import datetime

class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.value = val
        self.path = None
        self.positionX = 0
        self.positionY = 0
        self.startposX = 0
        self.startposY = 0
        self.hasPlaced = False
        self.whichPlayer = 0
        if(self.suit == 'Tarokk'):
            for i in range (1,23):
                if(self.value == i):
                    n = ".png"
                    self.path = 'C:\\Users\\vida1petera20\\PycharmProjects\\Tarock\\Tk\\%d%s' % (i,n)
        elif(self.suit == 'Karo'):
            for i in range(1,6):
                if (self.value == i):
                    n = ".png"
                    self.path = 'C:\\Users\\vida1petera20\\PycharmProjects\\Tarock\\Karo\\%d%s' % (i, n)
        elif (self.suit == 'Kor'):
            for i in range(1, 6):
                if (self.value == i):
                    n = ".png"
                    self.path = 'C:\\Users\\vida1petera20\\PycharmProjects\\Tarock\\Kor\\%d%s' % (i, n)
        elif (self.suit == 'Treff'):
            for i in range(1, 6):
                if (self.value == i):
                    n = ".png"
                    self.path = 'C:\\Users\\vida1petera20\\PycharmProjects\\Tarock\\Treff\\%d%s' % (i, n)
        else:
            for i in range(1, 6):
                if (self.value == i):
                    n = ".png"
                    self.path = 'C:\\Users\\vida1petera20\\PycharmProjects\\Tarock\\Pikk\\%d%s' % (i, n)
    def show(self):
        if(self.suit == "Tarokk"):
            print("{} erteku {}".format(self.value,self.suit))
        else:
            print("{} {}".format(self.suit,self.value))
class Deck:
    def __init__(self):
        self.cards = []
        self.buildDeck()
    def buildDeck(self):
        for s in ["Karo","Kor","Treff","Pikk"]:
            for v in range(1,6):
                self.cards.append(Card(s,v))
        for t in["Tarokk"]:
            for v in range(1,23):
                self.cards.append(Card(t,v))
    def show(self):
        for c in self.cards:
            c.show()
    def shuffle(self):
        shuffled_cards = random.shuffle(self.cards)
        return shuffled_cards
    def drawCard(self):
        return self.cards.pop()
