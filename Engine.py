from BasicFunctions import *

player1 = Player("Player 1", 1)
player2 = Player("Player 2", 2)
player3 = Player("Player 3", 3)
player4 = Player("Player 4", 4)
talon = Player("Talon",5)
PLAYERS = [player1,player2,player3,player4]
GAMENUM = 0
ROUNDNUM = 0
MONDASOK = ["Négy király", "Dupla játék", "Tuletroá", "Centrum", "Kismadár", "Nagymadár", "Pagátkismadár", "Saskismadár",
            "Királykismadár","Pagát ulti", "Sas ulti","Király ulti","Pagát uhu", "Sas uhu","Király uhu",
            "Párosfácan", "Volát", "Huszonegyes fogás", "Színcsalád", "Három király", "Káró", "Kőr", "Treff", "Pikk"]

def findTarokk(player):
    index = 0
    findThat = False
    for i in range(len(player.hand)):
        if player.hand[i].suit == "Tarokk":
            index = i
            findThat = True
            break
    if findThat:
        return index
    else:
        return 0
def findTheCard(temp, player):
    index = 0
    findThat = False
    for i in range(len(player.hand)):
        if temp[0].suit == player.hand[i].suit:
            index = i
            findThat = True
            break
    if findThat == False:
        if temp[0].suit == "Tarokk":
            index = 0
        else:
            index = findTarokk(player)
            if findTarokk(player) == 0:
                index = 0
    return index

def findIndex(list,card):
    index = 0
    for i in range(len(list)):
        if card.suit == list[i].suit and card.value == list[i].value:
            index = i
            break
    return index
def tempShow(temp):
    for c in temp:
        c.show()
def whosNextPlayer(temp):
    nextplayer = 0
    if temp[0].suit == temp[1].suit and temp[1].suit == temp[2].suit and temp[2].suit == temp[3].suit:
        maxvalue = 0
        for i in range(0,4):
            if temp[i].value > maxvalue:
                maxvalue = temp[i].value
                nextplayer = temp[i].whichPlayer
    else:
        maxvalue2 = 0
        for i in range(0,4):
            if temp[i].suit == "Tarokk" and temp[i].value > maxvalue2:
                maxvalue2 = temp[i].value
                nextplayer = temp[i].whichPlayer
    return nextplayer

############ INICIALIZALAS ###########


def gameInitialize():
    deck = Deck()
    deck.shuffle()
    print("A pakli megkeverve")
    for i in range(0,6):
        talon.draw(deck)
    for i in range(0,5):
        player1.draw(deck)
        player2.draw(deck)
        player3.draw(deck)
        player4.draw(deck)
    for i in range(0,4):
        player1.draw(deck)
        player2.draw(deck)
        player3.draw(deck)
        player4.draw(deck)
    print("A lapook kiosztva")
    for p in PLAYERS:
        p.sortingCards(p.hand)
def gameCounter(roundcounter, gamenumber):
    if roundcounter == 9:
        gamenumber+=1
    return gamenumber
########### LICITALAS ###########

def orderOfBidding(startingplayer):
    licitOrder = []
    if startingplayer == PLAYERS[0]:
        licitOrder.append(PLAYERS[0])
        licitOrder.append(PLAYERS[1])
        licitOrder.append(PLAYERS[2])
        licitOrder.append(PLAYERS[3])
    elif startingplayer == PLAYERS[1]:
        licitOrder.append(PLAYERS[1])
        licitOrder.append(PLAYERS[2])
        licitOrder.append(PLAYERS[3])
        licitOrder.append(PLAYERS[0])
    elif startingplayer == PLAYERS[2]:
        licitOrder.append(PLAYERS[2])
        licitOrder.append(PLAYERS[3])
        licitOrder.append(PLAYERS[0])
        licitOrder.append(PLAYERS[1])
    else:
        licitOrder.append(PLAYERS[3])
        licitOrder.append(PLAYERS[0])
        licitOrder.append(PLAYERS[1])
        licitOrder.append(PLAYERS[2])
    return licitOrder

def gainingCard(order,actuallicit):
   if actuallicit == 3:
       if order[0].winBidding:
           order[0].gainingCard = 3
           order[1].gainingCard = 1
           order[2].gainingCard = 1
           order[3].gainingCard = 1
       elif order[1].winBidding:
           order[1].gainingCard = 3
           order[2].gainingCard = 1
           order[3].gainingCard = 1
           order[0].gainingCard = 1
       elif order[2].winBidding:
           order[2].gainingCard = 3
           order[3].gainingCard = 1
           order[0].gainingCard = 1
           order[1].gainingCard = 1
       else:
           order[3].gainingCard = 3
           order[0].gainingCard = 1
           order[1].gainingCard = 1
           order[2].gainingCard = 1
   elif actuallicit == 2:
       if order[0].winBidding:
           order[0].gainingCard = 2
           order[1].gainingCard = 2
           order[2].gainingCard = 1
           order[3].gainingCard = 1
       elif order[1].winBidding:
           order[1].gainingCard = 2
           order[2].gainingCard = 2
           order[3].gainingCard = 1
           order[0].gainingCard = 1
       elif order[2].winBidding:
           order[2].gainingCard = 2
           order[3].gainingCard = 2
           order[0].gainingCard = 1
           order[1].gainingCard = 1
       else:
           order[3].gainingCard = 2
           order[0].gainingCard = 2
           order[1].gainingCard = 1
           order[2].gainingCard = 1
   elif actuallicit == 1:
       if order[0].winBidding:
           order[0].gainingCard = 1
           order[1].gainingCard = 2
           order[2].gainingCard = 2
           order[3].gainingCard = 1
       elif order[1].winBidding:
           order[1].gainingCard = 1
           order[2].gainingCard = 2
           order[3].gainingCard = 2
           order[0].gainingCard = 1
       elif order[2].winBidding:
           order[2].gainingCard = 1
           order[3].gainingCard = 2
           order[0].gainingCard = 2
           order[1].gainingCard = 1
       else:
           order[3].gainingCard = 1
           order[0].gainingCard = 2
           order[1].gainingCard = 2
           order[2].gainingCard = 1
   else:
       if order[0].winBidding:
           order[0].gainingCard = 0
           order[1].gainingCard = 2
           order[2].gainingCard = 2
           order[3].gainingCard = 2
       elif order[1].winBidding:
           order[1].gainingCard = 0
           order[2].gainingCard = 2
           order[3].gainingCard = 2
           order[0].gainingCard = 2
       elif order[2].winBidding:
           order[2].gainingCard = 0
           order[3].gainingCard = 2
           order[0].gainingCard = 2
           order[1].gainingCard = 2
       else:
           order[3].gainingCard = 0
           order[0].gainingCard = 2
           order[1].gainingCard = 2
           order[2].gainingCard = 2

def searchPartner(partnertarock,player):
    for card in player1.hand:
        if card.suit == "Tarokk" and card.value == partnertarock:
            player.partnerNumber = 1
            player1.partnerNumber = player.position
            break
    for card in player2.hand:
        if card.suit == "Tarokk" and card.value == partnertarock:
            player.partnerNumber = 2
            player2.partnerNumber = player.position
            break
    for card in player3.hand:
        if card.suit == "Tarokk" and card.value == partnertarock:
            player.partnerNumber = 3
            player3.partnerNumber = player.position
            break
    for card in player4.hand:
        if card.suit == "Tarokk" and card.value == partnertarock:
            player.partnerNumber = 4
            player4.partnerNumber = player.position
            break
    return player.partnerNumber
def isMondasIn(mondas,mondasok):
    isin = False
    for m in mondasok:
        if mondas == m:
            isin = True
            break
    return  isin
def getMondasok(mondasok,partnertarock):
    mondasokback = []
    pnumber = searchPartner(partnertarock,player1)
    partnerplayer = 0
    if pnumber == 1:
        partnerplayer = player1
    if pnumber == 2:
        partnerplayer = player2
    if pnumber == 3:
        partnerplayer = player3
    if pnumber == 4:
        partnerplayer = player4
    if partnertarock == 20:
        if isMondasIn("Négy király", mondasok):
            if hasHuszegy(partnerplayer) or hasSkiz(partnerplayer):
                mondasokback.append("Tuletroá")
            if hasTnyolc(partnerplayer) and tarokkCounter(partnerplayer) >=7:
                mondasokback.append("Dupla játék")
        if isMondasIn("Dupla játék", mondasok):
            if hasHuszegy(partnerplayer) or hasSkiz(partnerplayer):
                mondasokback.append("Tuletroá")
            if hasTkilenc(partnerplayer):
                mondasokback.append("Négy király")
        if isMondasIn("Tuletroá",mondasok):
            if hasTkilenc(partnerplayer):
                mondasokback.append("Négy király")
            if hasTnyolc(partnerplayer) and tarokkCounter(partnerplayer) >=7:
                mondasokback.append("Dupla játék")





def wantToBiddingMore(player,actuallicit,order):
    want = False
    if hasTwoBig(player):
        want = True
    if hasPagat(player) and not hasHusz(player) and not hasTkilenc(player):
        want = True
    if gainingCard(order,actuallicit) == 1:
        want = True
    if hasSkiz(player) and tarokkCounter(player) >=5:
        want = True
    if hasHuszegy(player) and tarokkCounter(player) >=7:
        want = True
    if hasHuszegy(player) and tarokkCounter(player)<=4 and gainingCard(order,actuallicit) == 2:
        want = False
    return want

def cardBidding():
    order = []
    gamenum = gameCounter(ROUNDNUM,GAMENUM)
    licit = 0
    if gamenum % 4 == 0:
        order = orderOfBidding(player1)
    if gamenum % 4 == 1:
        order = orderOfBidding(player2)
    if gamenum % 4 == 2:
        order = orderOfBidding(player3)
    if gamenum % 4 == 3:
        order = orderOfBidding(player4)

    if order[0].canLicit(order[0].hand):
        licit = 3                                                                       #HÁRMAS
        print("--HARMAS--")
        order[0].winBidding = True
        if order[1].canLicit(order[1].hand) and wantToBiddingMore(order[1],licit,order):
            licit = 3                                                                   #TARTOM
            print("--TARTOM--")
            order[0].winBidding = False
            order[1].winBidding = True
            if order[2].canLicit(order[2].hand) and wantToBiddingMore(order[2],licit,order):
                licit = 2                                                               #KETTES PASSZ
                print("--KETTES--")
                order[1].winBidding = False
                order[2].winBidding = True
            elif order[3].canLicit(order[3].hand) and wantToBiddingMore(order[3],licit,order):
                licit = 2
                print("--KETTES--")
                order[1].winBidding = False                                             #KETTES PASSZ
                order[3].winBidding = True
            else:
                if wantToBiddingMore(order[0],licit, order):
                    licit = 2                                                           #KETTES
                    print("--KETTES--")
                    order[1].winBidding = False
                    order[0].winBidding = True
                    if wantToBiddingMore(order[1],licit,order):
                        licit = 2                                                       #TARTOM
                        print("--TARTOM--")
                        order[1].winBidding = True
                        order[0].winBidding = False
                        if wantToBiddingMore(order[0],licit,order):
                            licit = 1                                                   #EGYES
                            print("--EGYES--")
                            order[0].winBidding = True
                            order[1].winBidding = False
                            if wantToBiddingMore(order[1],licit,order):
                                licit = 1                                               #TARTOM
                                print("--TARTOM--")
                                order[1].winBidding = True
                                order[0].winBidding = False
                                if wantToBiddingMore(order[0],licit,order):
                                    licit = 0                                           #SZÓLÓ
                                    print("--SZÓLÓ--")
                                    order[0].winBidding = True
                                    order[1].winBidding = False
                                    if wantToBiddingMore(order[1],licit,order):
                                        licit = 0                                       #TARTOM
                                        print("--TARTOM--")
                                        order[1].winBidding = True
                                        order[0].winBidding = False

                else:
                    licit = 3
                    order[0].winBidding = False
                    order[1].winBidding = True
        elif order[1].canLicit(order[1].hand) and wantToBiddingMore(order[1],licit,order):
            licit = 3                                                                   #HÁRMAS
            order[1].winBidding = True
            if order[2].canLicit(order[2].hand) and wantToBiddingMore(order[2],licit,order):
                licit = 3                                                               #TARTOM
                order[1].winBidding = False
                order[2].winBidding = True
                if order[3].canLicit(order[3].hand) and wantToBiddingMore(order[3],licit,order):
                    licit = 2                                                           #KETTES PASSZ
                    order[2].winBidding = False
                    order[3].winBidding = True
                elif order[0].canLicit(order[0].hand) and wantToBiddingMore(order[0],licit,order):
                    licit = 2
                    order[2].winBidding = False                                         #KETTES PASSZ
                    order[0].winBidding = True
                else:
                    if wantToBiddingMore(order[1],licit,order):
                        licit = 2                                                       #KETTES
                        order[2].winBidding = False
                        order[1].winBidding = True
                        if wantToBiddingMore(order[2],licit,order):
                            licit = 2                                                   #TARTOM
                            order[2].winBidding = True
                            order[1].winBidding = False
                            if wantToBiddingMore(order[1],licit,order):
                                licit = 1                                               #EGYES
                                order[1].winBidding = True
                                order[2].winBidding = False
                                if wantToBiddingMore(order[2],licit,order):
                                    licit = 1                                           #TARTOM
                                    order[2].winBidding = True
                                    order[1].winBidding = False
                                    if wantToBiddingMore(order[1],licit,order):
                                        licit = 0                                       #SZÓLÓ
                                        order[1].winBidding = True
                                        order[2].winBidding = False
                                        if wantToBiddingMore(order[2],licit,order):
                                            licit = 0                                   #TARTOM
                                            order[2].winBidding = True
                                            order[1].winBidding = False
        elif order[2].canLicit(order[2].hand) and wantToBiddingMore(order[2],licit,order):
            licit = 3                                                                   #HÁRMAS
            order[2].winBidding = True
            if order[3].canLicit(order[3].hand) and wantToBiddingMore(order[3],licit,order):
                licit = 3                                                               #TARTOM
                order[2].winBidding = False
                order[3].winBidding = True
                if order[0].canLicit(order[0].hand) and wantToBiddingMore(order[0],licit,order):
                    licit = 2                                                           #KETTES PASSZ
                    order[3].winBidding = False
                    order[0].winBidding = True
                elif order[1].canLicit(order[1].hand) and wantToBiddingMore(order[1],licit,order):
                    licit = 2
                    order[3].winBidding = False                                         #KETTES PASSZ
                    order[1].winBidding = True
                else:
                    if wantToBiddingMore(order[2],licit,order):
                        licit = 2                                                       #KETTES
                        order[3].winBidding = False
                        order[2].winBidding = True
                        if wantToBiddingMore(order[3],licit,order):
                            licit = 2                                                   #TARTOM
                            order[3].winBidding = True
                            order[2].winBidding = False
                            if wantToBiddingMore(order[2],licit,order):
                                licit = 1                                               #EGYES
                                order[2].winBidding = True
                                order[3].winBidding = False
                                if wantToBiddingMore(order[3],licit,order):
                                    licit = 1                                           #TARTOM
                                    order[3].winBidding = True
                                    order[2].winBidding = False
                                    if wantToBiddingMore(order[2],licit,order):
                                        licit = 0                                       #SZÓLÓ
                                        order[2].winBidding = True
                                        order[3].winBidding = False
                                        if wantToBiddingMore(order[3],licit,order):
                                            licit = 0                                   #TARTOM
                                            order[3].winBidding = True
                                            order[2].winBidding = False
        elif order[3].canLicit(order[3].hand) and wantToBiddingMore(order[3],licit,order):
            licit = 3                                                                   #HÁRMAS
            order[3].winBidding = True
            if order[0].canLicit(order[0].hand) and wantToBiddingMore(order[0],licit,order):
                licit = 3                                                               #TARTOM
                order[3].winBidding = False
                order[0].winBidding = True
                if order[1].canLicit(order[1].hand) and wantToBiddingMore(order[1],licit,order):
                    licit = 2                                                           #KETTES PASSZ
                    order[0].winBidding = False
                    order[1].winBidding = True
                elif order[2].canLicit(order[2].hand) and wantToBiddingMore(order[2],licit,order):
                    licit = 2
                    order[0].winBidding = False                                         #KETTES PASSZ
                    order[2].winBidding = True
                else:
                    if wantToBiddingMore(order[3],licit,order):
                        licit = 2                                                       #KETTES
                        order[0].winBidding = False
                        order[3].winBidding = True
                        if wantToBiddingMore(order[0],licit,order):
                            licit = 2                                                   #TARTOM
                            order[0].winBidding = True
                            order[3].winBidding = False
                            if wantToBiddingMore(order[3],licit,order):
                                licit = 1                                               #EGYES
                                order[3].winBidding = True
                                order[0].winBidding = False
                                if wantToBiddingMore(order[0],licit,order):
                                    licit = 1                                           #TARTOM
                                    order[0].winBidding = True
                                    order[3].winBidding = False
                                    if wantToBiddingMore(order[3],licit,order):
                                        licit = 0                                       #SZÓLÓ
                                        order[3].winBidding = True
                                        order[0].winBidding = False
                                        if wantToBiddingMore(order[0],licit,order):
                                            licit = 0                                   #TARTOM
                                            order[0].winBidding = True
                                            order[3].winBidding = False
    return licit

########### MAIN ###########
gameInitialize()
