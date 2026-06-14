import random
import pygame
pygame.init()
screen=pygame.display.set_mode((800,547))
bg=pygame.image.load("images/bg.jpg")
cat=3
class Space (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("images/blue.png")
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x>0:
            self.rect.x-=5
        if key[pygame.K_RIGHT] and self.rect.x<730:
            self.rect.x+=5
class Enemy (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("images/red.png")
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
    def update(self):
        global cat
        self.rect.y+=1
        if self.rect.y>547:
            cat-=1
            self.kill()
universe=Space(400,500)
universegroup=pygame.sprite.Group()
universegroup.add(universe)
reverse=pygame.sprite.Group()
for i in range (5):
    read=Enemy(i*160+80,47)
    reverse.add(read)
clock=pygame.time.Clock()
while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    universegroup.draw(screen)
    universegroup.update()
    reverse.draw(screen)
    reverse.update()
    pygame.display.update()
