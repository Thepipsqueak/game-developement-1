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
important=pygame.font.SysFont("Science_Gothic",52)
n1=random.randint(1,99)

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
    pygame.display.update()

pygame.quit()
