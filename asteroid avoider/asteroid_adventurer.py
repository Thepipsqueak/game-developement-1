import pygame
from pygame.locals import*
import random
pygame.init()
screen=pygame.display.set_mode((800,450))
utahime=pygame.image.load("whoaaaa.jpg")
iranfromhome_love=True
shark=pygame.image.load("asteroid.png")
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
mmi=two(shark,350,350)
troupe=pygame.sprite.Group()
troupe.add(mmi)
while iranfromhome_love:
    screen.blit(utahime,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            iranfromhome_love=False
    #key movement
    keys=pygame.key.get_pressed()
    if keys[K_w]:
        mmi.carré(-7)
    troupe.draw(screen)

    pygame.display.update()
pygame.quit()