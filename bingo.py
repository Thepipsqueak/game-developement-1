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
important=pygame.font.SysFont("Science_Gothic",75)
tele=[]
for i in range(9):
    randy=random.randint(10,99)
    tele.append(randy)
melee=[]
for i in range(9):
    mandy=random.randint(10,99)
    melee.append(mandy)
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            anything=False
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
    pygame.display.update()
pygame.quit()
