import random
import pygame
pygame.init()
screen=pygame.display.set_mode((800,550))
screen.fill("yellow")
pygame.display.update()
#class for the player
class thumb:
    def __init__(self,earth):
        #self.x=x
       # self.y=y
        self.image=pygame.image.load(earth)
player=thumb("OIP.jpg")
anything=True
while anything:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            anything=False
    player.draw(screen)
    pygame.display.update()
    
pygame.quit()
