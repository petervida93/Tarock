import pygame, sys
from pygame.locals import *
import pygame.freetype
from Engine import *
import random


pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tarokk')

COLOR = (96, 168, 48)
WHITE = (255, 255, 255)
bright_green =(140,207,127)
black =(0,0,0)
green = (26,148,49)
cardX = 100
cardY = 400
p2CardX = 1020
p2CardY = 10
p3CardX = 250
p3CardY = -50
p4CardX = 10
p4CardY = 10
afterlicit = True
readytoplay = False
cardPlaceX = WINDOW_WIDTH / 2
cardPlaceY = WINDOW_HEIGHT / 4
p1Images = []
p2Images = []
p3Images = []
p4Images = []
drawingList = []
temp = []
partnerTarock = 0

for card in player1.hand:
    card.startposX = cardX
    card.startposY = cardY
    card.positionX = cardX
    card.positionY = cardY
    cardX += 80
    p1Images.append(card)
    drawingList.append(card)
for card in player2.hand:
    card.positionX = p2CardX
    card.positionY = p2CardY
    p2CardY += 40
    p2Images.append(card)
    drawingList.append(card)
for card in player3.hand:
    card.positionX = p3CardX
    card.positionY = p3CardY
    p3CardX += 40
    p3Images.append(card)
    drawingList.append(card)
for card in player4.hand:
    card.positionX = p4CardX
    card.positionY = p4CardY
    p4CardY += 40
    p4Images.append(card)
    drawingList.append(card)
for card in talon.hand:
    card.positionX = cardPlaceX + 5
    card.positionY = cardPlaceY + 10

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def placeCard(player, index):
    card = player.hand[index]
    player.play(index)
    card.positionX = cardPlaceX + 5
    card.positionY = cardPlaceY + 10
def changeCards(player,images,temp,num):
    if player.isStarter:
        index = random.randint(0, len(player.hand) - 1)
        d = findIndex(images, player.hand[index])
        player.hand[index].whichPlayer = num
        temp.append(player.hand[index])
        placeCard(player, index)
        images.__delitem__(d)
    else:
        index = findTheCard(temp, player)
        d = findIndex(images, player.hand[index])
        player.hand[index].whichPlayer = num
        temp.append(player.hand[index])
        placeCard(player, index)
        images.__delitem__(d)
def canPlaceColor(player,temp):
    canplace = False
    for card in player.hand:
        if card.suit == temp[0].suit:
            canplace = True
    return  canplace
def hasTarokk(player):
    has = False
    for card in player.hand:
        if card.suit == "Tarokk":
            has = True
    return has
k=0
player1.isStarter = True
player1.isNextPlayer = True
placedCardNumber = 0
def newGame():
    gameInitialize()
    cardX = 100
    cardY = 400
    p2CardX = 1020
    p2CardY = 10
    p3CardX = 250
    p3CardY = -50
    p4CardX = 10
    p4CardY = 10
    cardPlaceX = WINDOW_WIDTH / 2
    cardPlaceY = WINDOW_HEIGHT / 4
    p1Images.clear()
    p2Images.clear()
    p3Images.clear()
    p4Images.clear()
    drawingList.clear()
    temp.clear()

    for card in player1.hand:
        card.startposX = cardX
        card.startposY = cardY
        card.positionX = cardX
        card.positionY = cardY
        cardX += 80
        p1Images.append(card)
        drawingList.append(card)
    for card in player2.hand:
        card.positionX = p2CardX
        card.positionY = p2CardY
        p2CardY += 40
        p2Images.append(card)
        drawingList.append(card)
    for card in player3.hand:
        card.positionX = p3CardX
        card.positionY = p3CardY
        p3CardX += 40
        p3Images.append(card)
        drawingList.append(card)
    for card in player4.hand:
        card.positionX = p4CardX
        card.positionY = p4CardY
        p4CardY += 40
        p4Images.append(card)
        drawingList.append(card)
    for card in talon.hand:
        card.positionX = cardPlaceX + 5
        card.positionY = cardPlaceY + 10
def drawRectWithText(x,y,width,height,text,chosecolor):
    pygame.draw.rect(DISPLAYSURF, chosecolor, (x, y, width, height))
    smallText = pygame.font.Font("freesansbold.ttf", 16)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    DISPLAYSURF.blit(textSurf, textRect)
chosecolor = []
aktualisMondas = []
clicked = 0
passing = False
for i in range (0,30):
    chosecolor.append(bright_green)
while True:
    muz = pygame.mouse.get_pos()
    #print(muz[0], "  ", muz[1])
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        if e.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if not readytoplay:
                if not passing:
                    if 200<= mx <=240 and 160<=my<=160+30 and partnerTarock == 0:
                        partnerTarock = 20
                        chosecolor[0] = green
                    elif 200<=mx<=240 and 195<my<=195+30 and partnerTarock == 0:
                        partnerTarock = 19
                        chosecolor[1] = green
                    elif 200<=mx<=240 and 230<my<=230+30 and partnerTarock == 0:
                        partnerTarock = 18
                        chosecolor[2] = green
                    elif 200<=mx<=240 and 265<my<=265+30 and partnerTarock == 0:
                        partnerTarock = 17
                        chosecolor[3] = green
                    elif 200<=mx<=240 and 300<my<=300+30 and partnerTarock == 0:
                        partnerTarock = 16
                        chosecolor[4] = green
                    elif 840<=mx<=940 and 15<=my<=45:
                        chosecolor[26] = green
                        aktualisMondas.append(MONDASOK[20])
                    elif 840 <= mx <= 940 and 50 <= my <= 80:
                        chosecolor[27] = green
                        aktualisMondas.append(MONDASOK[21])
                    elif 840 <= mx <= 940 and 85 <= my <= 115:
                        chosecolor[28] = green
                        aktualisMondas.append(MONDASOK[22])
                    elif 840 <= mx <= 940 and 120 <= my <= 150:
                        chosecolor[29] = green
                        aktualisMondas.append(MONDASOK[23])
                    elif 500<=mx<=650 and 350<my<=370 and clicked>=1:
                        for i in range(len(chosecolor)):
                            chosecolor[i] = bright_green
                            clicked = 0
                            passing = True
                            getMondasok(aktualisMondas,partnerTarock)
                    for i in range (0,4):
                        for j in range (0,5):
                            if 280+i*175<= mx <=280+165+i*175 and 160+j*35<= my <=160+30+j*35:
                                chosecolor[i*5+j+6] = green
                                aktualisMondas.append(MONDASOK[i*5+j])
                                for i in range(len(aktualisMondas)):
                                    print(aktualisMondas[i])
                                clicked+=1
                #else:
                    #IDE JÖN A PASSZOLÁS UTÁNI DOLOG

            else: #EZ A LICITÁLÁS UTÁNI EGÉR INTERAKCIÓ
                if cardPlaceX <= mx <= cardPlaceX+100 and cardPlaceY <= my <= cardPlaceY+200:
                    for i in range(len(temp)):
                        temp[i].positionX = cardPlaceX-400+80*i
                elif 800 <= mx <= 900 and 200 <= my <=230:
                    for i in range(len(temp)):
                        temp[i].positionX = cardPlaceX +5
                elif 800 <= mx <= 900 and 240 <= my <= 270:
                    temp.clear()
                elif 800 <= mx <= 900 and 280 <= my <= 310 and len(player2.hand) == 0 and len(player3.hand) == 0 and len(player4.hand) == 0:
                    newGame()
                else:
                    if player1.isNextPlayer:
                        if player1.isStarter:
                            for i in range(len(p1Images)):
                                if (p1Images[i].startposX <= mx <= p1Images[i].startposX + 100
                                        and p1Images[i].startposY <= my <= p1Images[i].startposY + 200):
                                    p1Images[i].positionX = cardPlaceX + 5
                                    p1Images[i].positionY = cardPlaceY + 10
                                    index = findIndex(p1Images, p1Images[i])
                                    p1Images[i].whichPlayer = 1
                                    temp.append(p1Images[i])
                                    p1Images.__delitem__(index)
                                    player1.play(index)
                                    player1.isNextPlayer = False
                                    player2.isNextPlayer = True
                                    placedCardNumber += 1
                                    break
                        else:
                            if canPlaceColor(player1,temp):
                                for i in range(len(p1Images)):
                                    if (p1Images[i].startposX <= mx <= p1Images[i].startposX + 100
                                            and p1Images[i].startposY <= my <= p1Images[i].startposY + 200
                                            and p1Images[i].suit == temp[0].suit):
                                        p1Images[i].positionX = cardPlaceX + 5
                                        p1Images[i].positionY = cardPlaceY + 10
                                        index = findIndex(p1Images, p1Images[i])
                                        p1Images[i].whichPlayer = 1
                                        temp.append(p1Images[i])
                                        p1Images.__delitem__(index)
                                        player1.play(index)
                                        player1.isNextPlayer = False
                                        player2.isNextPlayer = True
                                        placedCardNumber += 1
                                        break
                            else:
                                if hasTarokk(player1):
                                    for i in range(len(p1Images)):
                                        if (p1Images[i].startposX <= mx <= p1Images[i].startposX + 100
                                                and p1Images[i].startposY <= my <= p1Images[i].startposY + 200
                                                and p1Images[i].suit == "Tarokk"):
                                            p1Images[i].positionX = cardPlaceX + 5
                                            p1Images[i].positionY = cardPlaceY + 10
                                            index = findIndex(p1Images, p1Images[i])
                                            p1Images[i].whichPlayer = 1
                                            temp.append(p1Images[i])
                                            p1Images.__delitem__(index)
                                            player1.play(index)
                                            player1.isNextPlayer = False
                                            player2.isNextPlayer = True
                                            placedCardNumber += 1
                                            break
                                else:
                                    for i in range(len(p1Images)):
                                        if (p1Images[i].startposX <= mx <= p1Images[i].startposX + 100
                                                and p1Images[i].startposY <= my <= p1Images[i].startposY + 200):
                                            p1Images[i].positionX = cardPlaceX + 5
                                            p1Images[i].positionY = cardPlaceY + 10
                                            index = findIndex(p1Images, p1Images[i])
                                            p1Images[i].whichPlayer = 1
                                            temp.append(p1Images[i])
                                            p1Images.__delitem__(index)
                                            player1.play(index)
                                            player1.isNextPlayer = False
                                            player2.isNextPlayer = True
                                            placedCardNumber += 1
                                            break

        if e.type == KEYDOWN:
            if e.key == K_SPACE and player2.isNextPlayer:
                changeCards(player2,p2Images,temp,2)
                player2.isNextPlayer = False
                player3.isNextPlayer = True
                placedCardNumber += 1
            elif e.key == K_SPACE and player3.isNextPlayer:
                changeCards(player3, p3Images, temp, 3)
                player3.isNextPlayer = False
                player4.isNextPlayer = True
                placedCardNumber += 1
            elif e.key == K_SPACE and player4.isNextPlayer:
                changeCards(player4,p4Images,temp,4)
                player4.isNextPlayer = False
                player1.isNextPlayer = True
                placedCardNumber += 1
    if placedCardNumber == 4:
        nextp = whosNextPlayer(temp)
        if nextp == 1:
            player1.isNextPlayer = True
            player1.isStarter = True
            player2.isStarter = False
            player2.isNextPlayer = False
            player3.isStarter = False
            player3.isNextPlayer = False
            player4.isStarter = False
            player4.isNextPlayer = False
        elif nextp == 2:
            player2.isNextPlayer = True
            player2.isStarter = True
            player3.isStarter = False
            player3.isNextPlayer = False
            player4.isStarter = False
            player4.isNextPlayer = False
            player1.isNextPlayer = False
            player1.isStarter = False
        elif nextp == 3:
            player3.isNextPlayer = True
            player3.isStarter = True
            player4.isStarter = False
            player4.isNextPlayer = False
            player1.isNextPlayer = False
            player1.isStarter = False
            player2.isNextPlayer = False
            player2.isStarter = False
        else:
            player4.isNextPlayer = True
            player4.isStarter = True
            player1.isNextPlayer = False
            player1.isStarter = False
            player2.isNextPlayer = False
            player2.isStarter = False
            player3.isStarter = False
            player3.isNextPlayer = False
        placedCardNumber = 0


    ########### KIRAJZOLÁS ############

    drawingList = p1Images+p2Images+p3Images+p4Images+temp
    DISPLAYSURF.fill(WHITE)
    placeImg = pygame.image.load('placeofcard.png')
    if readytoplay:
        DISPLAYSURF.blit(placeImg, (cardPlaceX, cardPlaceY))
        mouse = pygame.mouse.get_pos()
        #CARD BACK BUTTON
        if 800<=mouse[0] <=900 and 200<=mouse[1]<=230:
            pygame.draw.rect(DISPLAYSURF, bright_green, (800, 200, 100 , 30))
        else:
            pygame.draw.rect(DISPLAYSURF, green, (800, 200, 100, 30))
        smallText = pygame.font.Font("freesansbold.ttf", 16)
        textSurf, textRect = text_objects("Card Back", smallText)
        textRect.center = ((800 + (100 / 2)), (200 + (30 / 2)))
        DISPLAYSURF.blit(textSurf, textRect)
        #NEXT ROUND BUTTON
        if 800<=mouse[0] <=900 and 240<=mouse[1]<=270:
            pygame.draw.rect(DISPLAYSURF, bright_green, (800, 240, 100 , 30))
        else:
            pygame.draw.rect(DISPLAYSURF, green, (800, 240, 100, 30))
        smallText2 = pygame.font.Font("freesansbold.ttf", 16)
        textSurf2, textRect2 = text_objects("Next Round", smallText2)
        textRect2.center = ((800 + (100 / 2)), (240 + (30 / 2)))
        DISPLAYSURF.blit(textSurf2, textRect2)
        # NEW GAME BUTTON
        if 800<=mouse[0] <=900 and 280<=mouse[1]<=310:
            pygame.draw.rect(DISPLAYSURF, bright_green, (800, 280, 100 , 30))
        else:
            pygame.draw.rect(DISPLAYSURF, green, (800, 280, 100, 30))
        smallText3 = pygame.font.Font("freesansbold.ttf", 16)
        textSurf3, textRect3 = text_objects("New Game", smallText3)
        textRect3.center = ((800 + (100 / 2)), (280 + (30 / 2)))
        DISPLAYSURF.blit(textSurf3, textRect3)
        #AKTUÁLIS JÁTÉKOS BUTTON
        if player1.isNextPlayer:
            le = pygame.image.load('le.png')
            DISPLAYSURF.blit(le,(400,300))
        elif player2.isNextPlayer:
            jobb = pygame.image.load('jobb.png')
            DISPLAYSURF.blit(jobb,(900,300))
        elif player3.isNextPlayer:
            fel = pygame.image.load('fel.png')
            DISPLAYSURF.blit(fel, (400, 200))
        elif player4.isNextPlayer:
            bal = pygame.image.load('bal.png')
            DISPLAYSURF.blit(bal, (200, 200))
    else:
        drawRectWithText(200,160,40,30,"XX", chosecolor[0])
        drawRectWithText(200,195,40,30,"XIX", chosecolor[1])
        drawRectWithText(200,230,40,30,"XVIII", chosecolor[2])
        drawRectWithText(200,265,40,30,"XVII", chosecolor[3])
        drawRectWithText(200,300,40,30,"XVI", chosecolor[4])
        drawRectWithText(500,350,150,30,"Passz", chosecolor[5])
        for i in range (0,5):
            drawRectWithText(280,160+i*35,165,30,MONDASOK[i], chosecolor[i+6])
        for i in range (0,5):
            drawRectWithText(455, 160 + i * 35, 165, 30, MONDASOK[i+5], chosecolor[i+11])
        for i in range (0,5):
            drawRectWithText(630, 160 + i * 35, 165, 30, MONDASOK[i+10], chosecolor[i+16])
        for i in range(0, 5):
            drawRectWithText(805, 160 + i * 35, 165, 30, MONDASOK[i + 15], chosecolor[i+21])
        for i in range(0,4):
            drawRectWithText(840,15+i*35,100,30,MONDASOK[i+20],chosecolor[i+26])


    for i in range(len(drawingList)):
        d1 = pygame.image.load(drawingList[i].path)
        DISPLAYSURF.blit(d1,(drawingList[i].positionX, drawingList[i].positionY))


    pygame.display.update()
    fpsClock.tick(FPS)