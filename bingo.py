import random
import pygame
pygame.init()
screen=pygame.display.set_mode((800,550))
screen.fill("yellow")
pygame.display.update()
i1=pygame.image.load("OIP.jpg")
i1=pygame.transform.scale(i1,(350,450))
i2=pygame.image.load("OIP.jpg")
i2=pygame.transform.scale(i1,(350,450))
i3=pygame.image.load("bringo.png")
important=pygame.font.SysFont("Science_Gothic",75)
notimportant=pygame.font.SysFont("Science_Gothic",50)
tele=[]
c=0
d=0
while c < 9:
    randy=random.randint(10,99)
    if randy in tele:
        continue
    tele.append(randy)
    c+=1
melee=[]
while d < 9:
    mandy=random.randint(10,99)
    if mandy in tele:
        continue
    melee.append(mandy)
    d+=1
trandy=random.randint(10,99)
#for te in tele:
#class for the player
'''class thumb:
    def __init__(self,earth):
        #self.x=x
       # self.y=y
        self.image=pygame.image.load(earth)
player=thumb("OIP.jpg")'''
anything=True
while anything:
    screen.blit(i1,(30,50))
    screen.blit(i2,(425,50))
    text=important.render("PLAYER",True,"black")
    text2=important.render("BOT",True,"black")
    text3=important.render("VS",True,"black")
    screen.blit(text,(125,510))
    screen.blit(text2,(560,510))
    screen.blit(text3,(380,510))
    numero_uno=important.render(str(tele[0]),True,"black")
    screen.blit(numero_uno,(70,120))
    numero_dos=important.render(str(tele[1]),True,"black")
    screen.blit(numero_dos,(180,120))
    numero_tres=important.render(str(tele[3]),True,"black")
    screen.blit(numero_tres,(290,120))
    numero_cuatro=important.render(str(tele[4]),True,"black")
    screen.blit(numero_cuatro,(70,240))
    numero_cinco=important.render(str(tele[5]),True,"black")
    screen.blit(numero_cinco,(70,370))
    numero_seis=important.render(str(tele[6]),True,"black")
    screen.blit(numero_seis,(180,240))
    numero_siete=important.render(str(tele[7]),True,"black")
    screen.blit(numero_siete,(290,240))
    numero_ocho=important.render(str(tele[8]),True,"black")
    screen.blit(numero_ocho,(180,370))
    numero_nueve=important.render(str(tele[2]),True,"black")
    screen.blit(numero_nueve,(290,370))
    #box2
    munero_uno=important.render(str(melee[0]),True,"black")
    screen.blit(munero_uno,(465,120))
    munero_dos=important.render(str(melee[1]),True,"black")
    screen.blit(munero_dos,(575,120))
    munero_tres=important.render(str(melee[2]),True,"black")
    screen.blit(munero_tres,(685,120))
    munero_cuatro=important.render(str(melee[3]),True,"black")
    screen.blit(munero_cuatro,(465,240))
    munero_cinco=important.render(str(melee[4]),True,"black")
    screen.blit(munero_cinco,(575,240))
    munero_seis=important.render(str(melee[5]),True,"black")
    screen.blit(munero_seis,(685,240))
    munero_siete=important.render(str(melee[6]),True,"black")
    screen.blit(munero_siete,(465,370))
    munero_ocho=important.render(str(melee[7]),True,"black")
    screen.blit(munero_ocho,(575,370))
    munero_nueve=important.render(str(melee[8]),True,"black")
    screen.blit(munero_nueve,(685,370))
    screen.blit(i3,(600,-10))
    importànt=notimportant.render("your random number is:",True,"black")
    screen.blit(importànt,(100,10))
    pygame.draw.rect(screen,"yellow",(480,0,100,50))
    trandyuno=important.render(str(trandy),True,"black")
    screen.blit(trandyuno,(500,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            anything=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            trandy=random.randint(10,99)
            for i in tele:
                if i == trandy:
                    retro=pygame.image.load("tingo.png")
                    screen.blit(retro,(70,120))

    pygame.display.update()
pygame.quit()
