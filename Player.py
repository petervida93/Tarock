
class Player:
    def __init__(self,name, position):
        self.name = name
        self.hand = []
        self.isNextPlayer = False
        self.isStarter = False
        self.position = position
        self.hasPlacedCard = False
        self.winBidding = False
        self.wantBiddingMore = False
        self.gainingCard = 0
        self.partnerNumber = 0
    def draw(self,deck):
        self.hand.append(deck.drawCard())
    def showHand(self):
        s=self.name
        print("## - " +s)
        for card in self.hand:
            card.show()
    def play(self, index):
        self.hand.__delitem__(index)
    def getFirstTarokk(self,hand):
        index = 0
        for i in range(len(self.hand)):
            if(self.hand[i].suit == 'Tarokk'):
                index = i
                break
        return index
    def licit(self,number):
        return number
    def canLicit(self,hand):
        licit = False
        for card in hand:
            if (card.suit == "Tarokk"):
                if(card.value == 1 or card.value == 21 or card.value == 22):
                    licit = True
                    break
        return licit
    def sortingCards(self,hand):
        pikkek = []
        treffek = []
        karok = []
        korok = []
        tarokkok = []
        for card in hand:
            if(card.suit == "Pikk"):
                pikkek.append(card)
            if(card.suit == "Treff"):
                treffek.append(card)
            if(card.suit == "Karo"):
                karok.append(card)
            if(card.suit == "Kor"):
                korok.append(card)
            if(card.suit == "Tarokk"):
                tarokkok.append(card)
        pikkek = sorted(pikkek,key=lambda card: card.value)
        treffek = sorted(treffek,key=lambda card: card.value)
        karok = sorted(karok,key=lambda card: card.value)
        korok = sorted(korok,key=lambda card: card.value)
        tarokkok = sorted(tarokkok,key=lambda card: card.value)
        self.hand = pikkek+treffek+karok+korok+tarokkok

