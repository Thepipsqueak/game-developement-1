import random
import pygame
pygame.init()
screen=pygame.display.set_mode((800,547))
bg=pygame.image.load("images/bg.jpg")
class Space (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("images/blue.png")
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x-=1
        if key[pygame.K_RIGHT]:
            self.rect.x+=1
class Enemy (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("images/red.png")
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
universe=Space(400,500)
universegroup=pygame.sprite.Group()
universegroup.add(universe)
reverse=pygame.sprite.Group()
for i in range (5):
    read=Enemy(i*160+80,47)
    reverse.add(read)
while True:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    universegroup.draw(screen)
    universegroup.update()
    reverse.draw(screen)
    pygame.display.update()
