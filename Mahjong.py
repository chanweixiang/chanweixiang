import pygame
import math
import random
import tkinter as tk

# setup display
pygame.init()
WIDTH, HEIGHT = 1200, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Singapore Mahjong Huat Ar!")

# restart button variables
RADIUS = 10
startx = 820
starty = 50
drawx = 940
drawy = 50
gangx = 700
gangy = 20
undox = 700
undoy = 50
hux = 580
huy = 50
pongx = 580
pongy = 20
throwx =820
throwy = 20


# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 20)
HOST_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images.
images = []
for i in range(148):
    image = pygame.image.load("mj" + str(i) + ".png")
    images.append(image)

# game variables
mahjong_status = 0
# draw phase
game_status = 0
host_status = 1
boss_status = 1
wind_status = 1



# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

#cardorder
cardorder = list(range(0, 148))
special = list(range(0, 12))
player2hand = []
player3hand = []
player4hand = []
front2card = []
front3card = []
front4card = []
playerhand = []
player1handcard = 13
player2handcard = 13
player3handcard = 13
player4handcard = 13
frontcard = []
selected = []
selected2 = []
selected3 = []
selected4 = []
new = []

cardnumber = 0
centerpool = []

#set up Player1
P1WIDTH, P1HEIGHT = (50,500)
#starting hand
CWIDTH, CHEIGHT = (80,86)
#P1 card width and height
F1WIDTH, F1HEIGHT = (50,435)
#front card
FWIDTH,FHEIGHT = (60,65)
#Front card width and height

#set up center Pool
C1WIDTH, C1HEIGHT = (110,80)
#center Pool Card width and height
C2WIDTH, C2HEIGHT = (60,65)

#set up player 2
P2WIDTH, P2HEIGHT = (1180,30)
F2WIDTH, F2HEIGHT = (1147,30)

#set up player 3
P3WIDTH, P3HEIGHT = (160,0)
F3WIDTH, F3HEIGHT = (160,20)

#Set up player 4
P4WIDTH, P4HEIGHT = (0,30)
F4WIDTH, F4HEIGHT = (20,30)

#Player 2,3,4 card
P2CWIDTH, P2CHEIGHT = (20,30)
P3CWIDTH, P3CHEIGHT = (30,20)
P4CWIDTH, P4CHEIGHT = (20,30)

#Player 2,3,4 front card
F234WIDTH, F234HEIGHT = (30,33)

def deal():
    global cardorder
    global playerhand
    global special
    global cardnumber
    global game_status
    global mahjong_status
    global player1handcard
    global player2handcard
    global player3handcard
    global player4handcard
    global host_status
    global wind_status
    
    if wind_status ==5:
        wind_status = 1
    
    if host_status == 1:
        player1handcard += 1
        
    if host_status == 2:
        player2handcard += 1
    
    if host_status == 3:
        player3handcard += 1
    
    if host_status == 4:
        player4handcard += 1

    if game_status == 0:
       #deal player 1        
        while len(playerhand) < player1handcard :
            playerhand.append(cardorder[cardnumber])
            new.append(cardorder[cardnumber])
            cardnumber += 1
     
        check = 0
        for i in range(len(playerhand)):
            for s in special:
                if (playerhand[i] == s):
                    frontcard.append(playerhand[i])
                    playerhand [i] = 'empty'
                    check += 1
              
        if (check != 0):
            for i in range(check):
                playerhand.remove('empty')  
            
            while len(playerhand) < player1handcard :
                playerhand.append(cardorder[cardnumber])            
                new.append(cardorder[cardnumber])
                cardnumber += 1
    
        if len(playerhand) == player1handcard:
             check = 0
             for i in range(len(playerhand)):
                 for s in special:
                     if (playerhand[i] == s):
                         frontcard.append(playerhand[i])
                         playerhand [i] = 'empty'
                         check += 1
              

             if (check != 0):
                for i in range(check):
                            playerhand.remove('empty')  
            
                while len(playerhand) < player1handcard :
                    playerhand.append(cardorder[cardnumber])            
                    new.append(cardorder[cardnumber])
                    cardnumber += 1
        #dealplayer 2
        while len(player2hand) < player2handcard :
            player2hand.append(cardorder[cardnumber])
            cardnumber += 1
     
        check = 0
        for i in range(len(player2hand)):
            for s in special:
                if (player2hand[i] == s):
                    front2card.append(player2hand[i])
                    player2hand [i] = 'empty'
                    check += 1
              
        if (check != 0):
            for i in range(check):
                player2hand.remove('empty')  
            
            while len(player2hand) < player2handcard :
                player2hand.append(cardorder[cardnumber])            
                cardnumber += 1
    
        if len(player2hand) == player2handcard:
             check = 0
             for i in range(len(player2hand)):
                 for s in special:
                     if (player2hand[i] == s):
                         front2card.append(player2hand[i])
                         player2hand [i] = 'empty'
                         check += 1
              

             if (check != 0):
                for i in range(check):
                            player2hand.remove('empty')  
            
                while len(player2hand) < player2handcard :
                    player2hand.append(cardorder[cardnumber])            
                    cardnumber += 1
        #deal player 3
        while len(player3hand) < player3handcard :
            player3hand.append(cardorder[cardnumber])
            cardnumber += 1
     
        check = 0
        for i in range(len(player3hand)):
            for s in special:
                if (player3hand[i] == s):
                    front3card.append(player3hand[i])
                    player3hand [i] = 'empty'
                    check += 1
              
        if (check != 0):
            for i in range(check):
                player3hand.remove('empty')  
            
            while len(player3hand) < player3handcard :
                player3hand.append(cardorder[cardnumber])            
                cardnumber += 1
    
        if len(player3hand) == player3handcard:
             check = 0
             for i in range(len(player3hand)):
                 for s in special:
                     if (player3hand[i] == s):
                         front3card.append(player3hand[i])
                         player3hand [i] = 'empty'
                         check += 1
              

             if (check != 0):
                for i in range(check):
                            player3hand.remove('empty')  
            
                while len(player3hand) < player3handcard :
                    player3hand.append(cardorder[cardnumber])            
                    cardnumber += 1
        #deal player 4
        while len(player4hand) < player4handcard :
            player4hand.append(cardorder[cardnumber])
            cardnumber += 1
     
        check = 0
        for i in range(len(player4hand)):
            for s in special:
                if (player4hand[i] == s):
                    front4card.append(player4hand[i])
                    player4hand [i] = 'empty'
                    check += 1
              
        if (check != 0):
            for i in range(check):
                player4hand.remove('empty')  
            
            while len(player4hand) < player4handcard :
                player4hand.append(cardorder[cardnumber])            
                cardnumber += 1
    
        if len(player4hand) == player4handcard:
             check = 0
             for i in range(len(player4hand)):
                 for s in special:
                     if (player4hand[i] == s):
                         front4card.append(player4hand[i])
                         player4hand [i] = 'empty'
                         check += 1
              

             if (check != 0):
                for i in range(check):
                            player4hand.remove('empty')  
            
                while len(player4hand) < player4handcard :
                    player4hand.append(cardorder[cardnumber])            
                    cardnumber += 1
        
        mahjong_status += 1     
        game_status = 1
        draw()
        play()                    


def draw():
    global centerpool
    global player2hand
    global player3hand
    global player4hand
    global playhand  
    global new
    global wind_status
    global host_status
    win.fill(WHITE)

    # draw title (currently dont want title)
    # text = TITLE_FONT.render("Mahjong Time", 1, BLACK)
    # win.blit(text, (10, 10))

    # draw buttons
    pygame.draw.circle(win, BLACK, (startx, starty), RADIUS, 3)
    text = LETTER_FONT.render("Restart", 1, BLACK)
    win.blit(text, (startx + RADIUS, starty - RADIUS))
    
    pygame.draw.circle(win, BLACK, (drawx, drawy), RADIUS, 3)
    text = LETTER_FONT.render("Draw", 1, BLACK)
    win.blit(text, (drawx + RADIUS, drawy - RADIUS))
    
    pygame.draw.circle(win, BLACK, (gangx, gangy), RADIUS, 3)
    text = LETTER_FONT.render("AnGang", 1, BLACK)
    win.blit(text, (gangx + RADIUS, gangy - RADIUS))
    
    pygame.draw.circle(win, BLACK, (undox, undoy), RADIUS, 3)
    text = LETTER_FONT.render("Undo", 1, BLACK)
    win.blit(text, (undox + RADIUS, undoy - RADIUS))
    
    pygame.draw.circle(win, BLACK, (hux, huy), RADIUS, 3)
    text = LETTER_FONT.render("Hu", 1, BLACK)
    win.blit(text, (hux + RADIUS, huy - RADIUS))
    
    pygame.draw.circle(win, BLACK, (pongx, pongy), RADIUS, 3)
    text = LETTER_FONT.render("ChiPongGang", 1, BLACK)
    win.blit(text, (pongx + RADIUS, pongy - RADIUS))
    
    pygame.draw.circle(win, BLACK, (throwx, throwy), RADIUS, 3)
    text = LETTER_FONT.render("Throw", 1, BLACK)
    win.blit(text, (throwx + RADIUS, throwy - RADIUS))
    
    #draw host
    if boss_status == 1:
        text = HOST_FONT.render("P1 Host", 1, BLACK)
        win.blit(text, (0, 0))
    
    if boss_status == 2:
        text = HOST_FONT.render("P2 Host", 1, BLACK)
        win.blit(text, (0, 0))
    
    if boss_status == 3:
        text = HOST_FONT.render("P3 Host", 1, BLACK)
        win.blit(text, (0, 0))
    
    if boss_status == 4:
        text = HOST_FONT.render("P4 Host", 1, BLACK)
        win.blit(text, (0, 0))
    
    #draw wind
    if wind_status == 1:
        win.blit(pygame.transform.scale(images[132],(40,42)), (110, 0))
    
    if wind_status == 2:
        win.blit(pygame.transform.scale(images[136],(40,42)), (110, 0)) 
 
    if wind_status == 3:
        win.blit(pygame.transform.scale(images[140],(40,42)), (110, 0))
    
    if wind_status == 4:
        win.blit(pygame.transform.scale(images[144],(40,42)), (110, 0))
        
    
    # draw player card
    sselfcards = sorted(playerhand)
    lengthPlayerhand = len(playerhand)
    if len(playerhand) > 0:
        for i in range(lengthPlayerhand):
            win.blit(images[sselfcards[i]], (P1WIDTH+CWIDTH* i , P1HEIGHT))
    # draw front card        
    lengthFrontCard = len(frontcard)
    if lengthFrontCard > 0:
        for i in range(lengthFrontCard):
            win.blit(pygame.transform.scale(images[frontcard[i]], (FWIDTH, FHEIGHT)), (F1WIDTH + FWIDTH * i, F1HEIGHT))

    #draw player 2 card
    lengthp2hand = len(player2hand)
    if lengthp2hand > 0:
        for i in range(lengthp2hand):
            pygame.draw.rect(win,GREEN,(P2WIDTH,P2HEIGHT*(i+1),P2CWIDTH,P2CHEIGHT),0)
    if lengthp2hand > 0:
        for i in range(lengthp2hand):
            pygame.draw.rect(win,BLACK,(P2WIDTH,P2HEIGHT*(i+1),P2CWIDTH,P2CHEIGHT),1)
     
    lengthP2FrontCard = len(front2card)
    if lengthP2FrontCard > 0:
        for i in range(lengthP2FrontCard):
            win.blit(pygame.transform.rotate(pygame.transform.scale(images[front2card[i]],(F234WIDTH,F234HEIGHT)),-90), (F2WIDTH, F2HEIGHT + F234WIDTH * i))        
    
    
    #draw player 3 card
    lengthp3hand = len(player3hand)
    if lengthp3hand > 0:
        for i in range(lengthp3hand):
            pygame.draw.rect(win,GREEN,(P3WIDTH+P3CWIDTH*(i),P3HEIGHT,P3CWIDTH,P3CHEIGHT),0)
    if lengthp3hand > 0:
        for i in range(lengthp3hand):
            pygame.draw.rect(win,BLACK,(P3WIDTH+P3CWIDTH*(i),P3HEIGHT,P3CWIDTH,P3CHEIGHT),1)
     
    lengthP3FrontCard = len(front3card)
    if lengthP3FrontCard > 0:
        for i in range(lengthP3FrontCard):
            win.blit(pygame.transform.rotate(pygame.transform.scale(images[front3card[i]],(F234WIDTH,F234HEIGHT)),180), (F3WIDTH+F234WIDTH*i, F3HEIGHT))    

            
    #draw player 4 card
    lengthp4hand = len(player4hand)
    if lengthp4hand > 0:
        for i in range(lengthp4hand):
            pygame.draw.rect(win,GREEN,(P4WIDTH,P4HEIGHT*(i+1),P4CWIDTH,P4CHEIGHT),0)
    if lengthp4hand > 0:
        for i in range(lengthp4hand):
            pygame.draw.rect(win,BLACK,(P4WIDTH,P4HEIGHT*(i+1),P4CWIDTH,P4CHEIGHT),1)
     
    lengthP4FrontCard = len(front4card)
    if lengthP4FrontCard > 0:
        for i in range(lengthP4FrontCard):
            win.blit(pygame.transform.rotate(pygame.transform.scale(images[front4card[i]],(F234WIDTH,F234HEIGHT)),90), (F4WIDTH, F4HEIGHT + F234WIDTH * i))    


    # draw center pool        
    lengthcenterpool = len(centerpool)
    if lengthcenterpool > 0 :
        for i in range(0,lengthcenterpool):
            if i < 16:
                win.blit(pygame.transform.scale(images[centerpool[i]], (C2WIDTH, C2HEIGHT)), (C1WIDTH + C2WIDTH * i, C1HEIGHT))
    if lengthcenterpool > 15 :
        for i in range(16,lengthcenterpool):
            if i <32:
                win.blit(pygame.transform.scale(images[centerpool[i]], (C2WIDTH, C2HEIGHT)), (C1WIDTH + C2WIDTH * (i-16), C1HEIGHT + C2HEIGHT))
    if lengthcenterpool > 31 :
        for i in range(32,lengthcenterpool):
            if i <48:
                win.blit(pygame.transform.scale(images[centerpool[i]], (C2WIDTH, C2HEIGHT)), (C1WIDTH + C2WIDTH * (i-32), C1HEIGHT + C2HEIGHT*2))
    if lengthcenterpool > 47 :
        for i in range(48,lengthcenterpool):
            if i <64:
                win.blit(pygame.transform.scale(images[centerpool[i]], (C2WIDTH, C2HEIGHT)), (C1WIDTH + C2WIDTH * (i-48), C1HEIGHT + C2HEIGHT*3))
    if lengthcenterpool > 63 :
        for i in range(64,lengthcenterpool):
            win.blit(pygame.transform.scale(images[centerpool[i]], (C2WIDTH, C2HEIGHT)), (C1WIDTH + C2WIDTH * (i-64), C1HEIGHT + C2HEIGHT*4))
    
    #draw rect
    pygame.draw.rect(win,BLACK,(P1WIDTH,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*2,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*3,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*4,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*5,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*6,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*7,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*8,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*9,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*10,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*11,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*12,P1HEIGHT,CWIDTH,CHEIGHT),1)
    pygame.draw.rect(win,BLACK,(P1WIDTH+CWIDTH*13,P1HEIGHT,CWIDTH,CHEIGHT),1)
    
    #suggested text
    if host_status == 2 and len(player2hand) == 14:
        text = LETTER_FONT.render("Player 2 Throw", 1, BLACK)
        win.blit(text, (600, 400))
    
    elif host_status == 2 and len(player2hand) == 13:
        text = LETTER_FONT.render("Player 3 Draw", 1, BLACK)
        win.blit(text, (600, 400))
    
    elif host_status == 3 and len(player3hand) == 14:
        text = LETTER_FONT.render("Player 3 Throw", 1, BLACK)
        win.blit(text, (600, 400))
    
    elif host_status == 3 and len(player3hand) == 13:
        text = LETTER_FONT.render("Player 4 Draw", 1, BLACK)
        win.blit(text, (600, 400))
    
    elif host_status == 4 and len(player4hand) == 14:
        text = LETTER_FONT.render("Player 4 Throw", 1, BLACK)
        win.blit(text, (600, 400))
    
    elif host_status == 4 and len(player4hand) == 13:
        text = LETTER_FONT.render("Player 1 Draw", 1, BLACK)
        win.blit(text, (600, 400))
        
    elif host_status == 1:
        text = LETTER_FONT.render("Player 1 Throw", 1, BLACK)
        win.blit(text, (600, 400))
    
    
    
    
    pygame.display.update()
   
def play():
    global game_status
    global mahjong_status
    global cardorder
    global cardnumber
    global playerhand
    global centerpool
    global new
    global selected
    global selected2
    global selected3
    global selected4
    global player1handcard
    global player2handcard
    global player3handcard
    global player4handcard
    global choice
    global host_status
    global boss_status
    global wind_status
    
    draw()
    pygame.display.update()
    if mahjong_status != 1:
        for i in range(len(playerhand)):
            for n in new:
                if (sorted(playerhand)[i] == n):
                    new_text = TITLE_FONT.render("New", 1, BLACK)
                    win.blit(new_text, (P1WIDTH + (CWIDTH * (i)), 550))
                    pygame.display.update()
                    
        
        
    while game_status == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    game_status = 0
                    if host_status == 1:
                        host_status += 1
                        player1handcard -=1
                        deal()
                    elif host_status ==2:
                        player2handcard -= 1
                        host_status += 1
                    elif host_status ==3:
                        player3handcard -= 1
                        host_status += 1
                        
                    elif host_status ==4:
                        player4handcard -= 1
                        host_status = 1
                    
                    deal()            
                
                elif event.key == pygame.K_t:
                    for i in range(len(selected)):
                        centerpool.append(selected[i])          
                        playerhand.remove(selected[i])
                    new.clear()
                    selected.clear()
                    
                    if host_status == 2:
                        selected2.append(player2hand[random.randint(1,len(player2hand))-1])
                        centerpool.append(selected2[0])
                        player2hand.remove(selected2[0])
                        selected2.clear()
                        play()
                    
                    elif host_status == 3:
                        selected3.append(player3hand[random.randint(1,len(player3hand))-1])
                        centerpool.append(selected3[0])
                        player3hand.remove(selected3[0])
                        selected3.clear()
                        play()
                    
                    elif host_status == 4:
                        selected4.append(player4hand[random.randint(1,len(player4hand))-1])
                        centerpool.append(selected4[0])
                        player4hand.remove(selected4[0])
                        selected4.clear()
                        play()
                    
                    elif host_status == 1:
                        host_status += 1
                        player1handcard -= 1
                        game_status = 0
                        deal()      

                    
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                
                positionCardThrow = 1000
                
                for i in range(1,15):
                    if (P1WIDTH + CWIDTH * i > m_x > P1WIDTH + CWIDTH *(i-1)) and (P1HEIGHT + CHEIGHT > m_y > P1HEIGHT):
                        positionCardThrow = i - 1
                
                #restart button
                if startx + RADIUS > m_x > startx and starty + RADIUS > m_y > starty:
                    random.shuffle(cardorder)
                    playerhand.clear()
                    player2hand.clear()
                    player3hand.clear()
                    player4hand.clear()
                    frontcard.clear()
                    front2card.clear()
                    front3card.clear()
                    front4card.clear()
                    game_status = 0
                    cardnumber = 0
                    mahjong_status = 0
                    player1handcard = 13
                    player2handcard = 13
                    player3handcard = 13
                    player4handcard = 13
                    boss_status = 1
                    wind_status = 1
                    host_status = 1
                    centerpool.clear()
                    new.clear()
                    deal()
                
  
                #draw button
                if drawx + RADIUS > m_x > drawx and drawy + RADIUS > m_y > drawy:
                    game_status = 0
                    if host_status == 1:
                        host_status += 1
                        player1handcard -=1
                        deal()
                    elif host_status ==2:
                        player2handcard -= 1
                        host_status += 1
                    elif host_status ==3:
                        player3handcard -= 1
                        host_status += 1
                        
                    elif host_status ==4:
                        player4handcard -= 1
                        host_status = 1
                    
                    deal()                   
                                    
                #bye screen    
                elif positionCardThrow != 1000:
                    new.clear()
                    selected.append(sorted(playerhand)[positionCardThrow])
                    bye_text = TITLE_FONT.render("Bye", 1, BLACK)
                    win.blit(bye_text, (P1WIDTH + (CWIDTH * (positionCardThrow)), 550))
                    pygame.display.update()
                    
                #throw button
                elif throwx + RADIUS > m_x > throwx and throwy + RADIUS > m_y > throwy:
                    for i in range(len(selected)):
                        centerpool.append(selected[i])          
                        playerhand.remove(selected[i])
                    new.clear()
                    selected.clear()
                    
                    if host_status == 2:
                        selected2.append(player2hand[random.randint(1,len(player2hand))-1])
                        centerpool.append(selected2[0])
                        player2hand.remove(selected2[0])
                        selected2.clear()
                        play()
                    
                    elif host_status == 3:
                        selected3.append(player3hand[random.randint(1,len(player3hand))-1])
                        centerpool.append(selected3[0])
                        player3hand.remove(selected3[0])
                        selected3.clear()
                        play()
                    
                    elif host_status == 4:
                        selected4.append(player4hand[random.randint(1,len(player4hand))-1])
                        centerpool.append(selected4[0])
                        player4hand.remove(selected4[0])
                        selected4.clear()
                        play()
                    
                    elif host_status == 1:
                        host_status += 1
                        player1handcard -= 1
                        game_status = 0
                        deal()                
                #pong button
                elif pongx + RADIUS > m_x > pongx and pongy + RADIUS > m_y > pongy:
                    for i in range(len(selected)):
                        frontcard.append(selected[i])        
                        playerhand.remove(selected[i])
                    frontcard.append(centerpool[len(centerpool)-1])
                    centerpool.remove(centerpool[len(centerpool)-1])
                    player1handcard -= 3
                    game_status = 0
                    if host_status != 4:
                        host_status = 1
                        new.clear()
                        selected.clear()
                        deal()
                        
                    elif host_status ==4:
                        player4handcard -= 1
                        host_status = 1
                        selected.clear()   
                        deal()
                    
                #gang button
                elif gangx + RADIUS > m_x > gangx and gangy + RADIUS > m_y > gangy:
                    print("selected len is",len(selected))
                    print(selected)
                    if len(selected) == 4:
                        player1handcard -= 4
                    elif len(selected) == 1:
                        player1handcard -= 1
                    for i in range(len(selected)):
                        frontcard.append(selected[i])          
                        playerhand.remove(selected[i])
                    game_status = 0
                    new.clear()
                    selected.clear()
                    deal()
                #undo button
                elif undox + RADIUS > m_x > undox and undoy + RADIUS > m_y > undoy:
                    game_status = 0
                    new.clear()
                    selected.clear()
                    deal()
                
                #hu button
                elif hux + RADIUS > m_x > hux and huy + RADIUS > m_y > huy:
                    root.mainloop()
                   #1,4,2,3 what to do if different player hu
                    if choice == "Player 1":
                        random.shuffle(cardorder)
                        playerhand.clear()
                        player2hand.clear()
                        player3hand.clear()
                        player4hand.clear()
                        frontcard.clear()
                        front2card.clear()
                        front3card.clear()
                        front4card.clear()
                        game_status = 0
                        cardnumber = 0
                        mahjong_status = 0
                        player1handcard = 13
                        player2handcard = 13
                        player3handcard = 13
                        player4handcard = 13
                        centerpool.clear()
                        new.clear()
                        if boss_status == 1:
                            host_status = 1
                            deal()
                        if boss_status == 4:
                            boss_status = 1
                            host_status = 1
                            wind_status += 1
                            deal()
                        if boss_status == 2 or boss_status ==3:
                            boss_status += 1
                            host_status = boss_status
                            deal()
                        pygame.display.update()
                     
                    elif choice == "Player 4":
                        random.shuffle(cardorder)
                        playerhand.clear()
                        player2hand.clear()
                        player3hand.clear()
                        player4hand.clear()
                        frontcard.clear()
                        front2card.clear()
                        front3card.clear()
                        front4card.clear()
                        game_status = 0
                        cardnumber = 0
                        mahjong_status = 0
                        player1handcard = 13
                        player2handcard = 13
                        player3handcard = 13
                        player4handcard = 13
                        centerpool.clear()
                        new.clear()
                        if boss_status == 4:
                            host_status = 4
                            deal()
                        if boss_status == 1:
                            boss_status = 2
                            host_status = 2
                            deal()
                        if boss_status == 2 or boss_status ==3:
                            boss_status += 1
                            host_status = boss_status
                            deal()
                        pygame.display.update()                   
                    
                    elif choice == "Player 2":
                        random.shuffle(cardorder)
                        playerhand.clear()
                        player2hand.clear()
                        player3hand.clear()
                        player4hand.clear()
                        frontcard.clear()
                        front2card.clear()
                        front3card.clear()
                        front4card.clear()
                        game_status = 0
                        cardnumber = 0
                        mahjong_status = 0
                        player1handcard = 13
                        player2handcard = 13
                        player3handcard = 13
                        player4handcard = 13
                        centerpool.clear()
                        new.clear()
                        if boss_status == 2:
                            host_status = 2
                            deal()
                        if boss_status == 4:
                            boss_status = 1
                            host_status = 1
                            wind_status += 1
                            deal()
                        if boss_status == 1 or boss_status ==3:
                            boss_status += 1
                            host_status = boss_status
                            deal()
                        pygame.display.update()           
                    
                    elif choice == "Player 3":
                        random.shuffle(cardorder)
                        playerhand.clear()
                        player2hand.clear()
                        player3hand.clear()
                        player4hand.clear()
                        frontcard.clear()
                        front2card.clear()
                        front3card.clear()
                        front4card.clear()
                        game_status = 0
                        cardnumber = 0
                        mahjong_status = 0
                        player1handcard = 13
                        player2handcard = 13
                        player3handcard = 13
                        player4handcard = 13
                        centerpool.clear()
                        new.clear()
                        if boss_status == 3:
                            host_status = 3
                            deal()
                        if boss_status == 4:
                            boss_status = 1
                            host_status = 1
                            wind_status += 1
                            deal()
                        if boss_status == 2 or boss_status ==1:
                            boss_status += 1
                            host_status = boss_status
                            deal()
                        pygame.display.update()
                    
                    elif choice == "No Hu":
                        random.shuffle(cardorder)
                        playerhand.clear()
                        player2hand.clear()
                        player3hand.clear()
                        player4hand.clear()
                        frontcard.clear()
                        front2card.clear()
                        front3card.clear()
                        front4card.clear()
                        game_status = 0
                        cardnumber = 0
                        mahjong_status = 0
                        player1handcard = 13
                        player2handcard = 13
                        player3handcard = 13
                        player4handcard = 13
                        centerpool.clear()
                        new.clear()
                        host_status = boss_status
                        deal()
                        pygame.display.update()
root = tk.Tk()

# Create a Tkinter variable
tkvar = tk.StringVar(root)

# options
choices = ['Player 1','Player 2','Player 3','Player 4','No Hu']
tkvar.set('Player 1') # set the default option

def on_selection(value):
    global choice
    choice = value  # store the user's choice
    root.quit()  # close window

popupMenu = tk.OptionMenu(root, tkvar, *choices, command=on_selection)
tk.Label(root, text="Who hu le?").grid(row=0, column=0)
popupMenu.grid(row=1, column =0)


# Do whatever you want with the user's choice after closing the window
# print('You have chosen %s' % choice)


def main():
    global mahjong_status
    global cardorder
    global cardnumber
    global game_status
    global centerpool
    global player1handcard
    global player2handcard
    global player3handcard
    global player4handcard
    global host_status
    global boss_status
    global wind_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                if startx + RADIUS > m_x > startx and starty + RADIUS > m_y > starty:
                    random.shuffle(cardorder)
                    playerhand.clear()
                    player2hand.clear()
                    player3hand.clear()
                    player4hand.clear()
                    frontcard.clear()
                    front2card.clear()
                    front3card.clear()
                    front4card.clear()
                    game_status = 0
                    cardnumber = 0
                    player1handcard = 13
                    player2handcard = 13
                    player3handcard = 13
                    player4handcard = 13
                    boss_status = 1
                    wind_status = 1
                    centerpool.clear()
                    host_status = 1
                    mahjong_status = 0
                     

                    
    
        deal()

while True:
    
    main()
pygame.quit()