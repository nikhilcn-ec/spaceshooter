#hii
import pygame
import random
import math
from pygame import mixer


#intialize pygames
pygame.init()




score=0

#setting a screen display
screen=pygame.display.set_mode((800,700))


#setting title and logo
pygame.display.set_caption("space invaders")
logo=pygame.image.load("logo.png")
pygame.display.set_icon(logo)



out={"out1":0,"out2":0}


bg=pygame.image.load("space.jpg")


#bgm
mixer.music.load("bgs.mp3")
mixer.music.play(-1)


#player image loading and dimensions
playerimg=pygame.image.load("player.png")
px=360
py=560
px_c=0



# multiple enemy image loading and dimensions
enemyimg=[]
ex=[]
ey=[]
ex_c=[]
ey_c=[]
no_enemy=4



enemyimg=[]
ex=[]
ey=[]
ex_c=[]
ey_c=[]
no_enemy=4

#enemy img and values appending
for i in range(no_enemy):
    enemyimg.append(pygame.image.load("enemy.png"))
    ex.append(random.randint(0,672))
    ey.append(random.randint(5,300))
    ex_c.append(1)
    ey_c.append(80)

bulletimg=pygame.image.load("bullet.png")
bx=0
by=560
bx_c=0
by_c=7
b_state = "ready"

if score>=10 & score<=20:
    ey_c
font=pygame.font.Font("freesansbold.ttf",32)
tx=10
ty=10

font1=pygame.font.Font("freesansbold.ttf",64)


score=0
def show_sc(x,y):
    sc=font.render("Score:"+str(score),True,(0,255,0))
    screen.blit(sc,(x,y))

def game_over():
    g=font1.render("GAME OVER",True,(255,255,255))
    screen.blit(g,(200,350))
    pygame.display.update()


def player(x,y):
    screen.blit(playerimg, (x, y))

def enemy(x,y,i):
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x,y):
    global b_state 
    b_state="fire"
    screen.blit(bulletimg, (x+50, y)) 


def iscollision(ex,ey,bx,by):
    d=math.sqrt((math.pow(ex-bx,2)) + (math.pow(ey-by,2)))
    if d<57:
        return True
    else:
        return False

def isout(ex,ey,px,py):
    d=math.sqrt((math.pow(ex-px,2)) + (math.pow(ey-py,2)))
    if d<67:
        return 1
    else:
        return 

window=True
while window:
    screen.fill((0,0,0))
    screen.blit(bg, (0, 0)) 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            window=False
    

    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            px_c= -1
        if event.key==pygame.K_RIGHT:
            px_c= 1
        if event.key==pygame.K_UP:
            if b_state =="ready":
                b_sound=mixer.Sound("shot.mp3")
                b_sound.play()
                bx=px
                fire_bullet(bx,by)           
    if event.type==pygame.KEYUP:  
        if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
            px_c= 0 

    px=px + px_c
    if px<=0:
       px=0
    elif px>=672:
       px=672
    for i in range(no_enemy):
        global out1,out2
        v=isout(ex[i],ey[i],px,py)
        out.update({"out1":v})
        if 1 in out.values():
            for i in range(no_enemy):
                ey[i]=2000  
            out.update({"out2":1})
            game_over()
            break
                   
            

        ex[i]=ex[i]+ex_c[i]
        if ex[i]<=0:
            ex_c[i]=0.6
            ey[i]=ey_c[i]+ey[i]
        elif ex[i]>=672:
            ex_c[i]=-0.6
            ey[i]=ey_c[i]+ey[i]

        col=iscollision(ex[i],ey[i],bx,by)
        if col:
            ex[i]=random.randint(0,672)
            ey[i]=random.randint(5,300)
            by=560
            b_state="ready"
            score=score+1





        enemy(ex[i],ey[i],i)    




    if by<=50:
        by=560
        b_state="ready"
    if b_state == "fire":
        fire_bullet(bx,by)
        by=by-by_c
    


            
    show_sc(tx,ty)
    player(px,py)    
    pygame.display.update()        