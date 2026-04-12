import pygame
from pygame.locals import*
import random
pygame.init()
screen=pygame.display.set_mode((800,450))
utahime=pygame.image.load("whoaaaa.jpg")
iranfromhome_love=True
shark=pygame.image.load("asteroid.png")
jared=pygame.image.load("innocent_child_Jared.png")
acneedbob=pygame.image.load("bob.png")
class two (pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def losange(self,sonic):
        self.rect.x+=sonic
    def carré(self,flash):
        self.rect.y+=flash
#class for bob and innocent child jared
class innocents(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


mmi=two(shark,350,350)
ex=random.randint(50,750)
undeservedDEATH=innocents(jared,ex,50)
xe=random.randint(50,750)
inloveBOB=innocents(acneedbob,xe,50)
troupe=pygame.sprite.Group()
troupe.add(mmi)
InnocentMassacre=pygame.sprite.Group()
InnocentMassacre.add(undeservedDEATH)
InnocentMassacre.add(inloveBOB)
clock=pygame.time.Clock()
while iranfromhome_love:
    clock.tick(60)
    screen.blit(utahime,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            iranfromhome_love=False
    #key movement
    keys=pygame.key.get_pressed()
    if keys[K_w]:
        mmi.carré(-2)
    if keys[K_s]:
        mmi.carré(2)
    if keys[K_d]:
        mmi.losange(2)
    if keys[K_a]:
        mmi.losange(-2)
    troupe.draw(screen)
    InnocentMassacre.draw(screen)

    pygame.display.update()
pygame.quit()
