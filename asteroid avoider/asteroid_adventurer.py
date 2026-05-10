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
language=10000
lightyear=0
dinosaurs=30
human=1
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
    def planet(self):
        global language
        global lightyear
        humans=pygame.sprite.spritecollide(self,InnocentMassacre,False)
        for i in humans:
            language-=200
            lightyear+=1
            i.rect.x=random.randint(50,750)
            i.rect.y=random.randint(-300,-50)
#class for bob and innocent child jared
class innocents(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=random.randint(3,5)
    def tempest(self):
        self.rect.y+=self.speed


InnocentMassacre=pygame.sprite.Group()
mmi=two(shark,350,350)
for i in range(7):
    ex=random.randint(50,750)
    why=random.randint(-300,-50)
    stuti=random.choice([jared,acneedbob])
    undeservedDEATH=innocents(stuti,ex,why)
    InnocentMassacre.add(undeservedDEATH)
troupe=pygame.sprite.Group()
troupe.add(mmi)
clock=pygame.time.Clock()
#beginning screen
crescent=pygame.font.Font(None,100)
giant=pygame.font.Font(None,100)
for number in ["3","2","1"]:
    screen.fill("white")
    text=crescent.render(number,True,("black"))
    rect=text.get_rect(center=(400,225))
    screen.blit(text,rect)
    pygame.display.update()
    pygame.time.delay(1000)
while iranfromhome_love:
    clock.tick(60)
    dinosaurs-=1
    screen.blit(utahime,(0,0))
    text=giant.render(str(dinosaurs),True,("white"))
    rect=text.get_rect(center=(400,225))
    screen.blit(text,rect)
    text=crescent.render(str(lightyear),True,("white"))
    rect=text.get_rect(center=(725,50))
    screen.blit(text,rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            iranfromhome_love=False
    #key movement
    keys=pygame.key.get_pressed()
    if keys[K_w]and mmi.rect.y>0:
        mmi.carré(-5)
    if keys[K_s]and mmi.rect.y<375:
        mmi.carré(5)
    if keys[K_d]and mmi.rect.x<750:
        mmi.losange(5)
    if keys[K_a]and mmi.rect.x>0:
        mmi.losange(-5)
    #innocents falling down
    for i in InnocentMassacre:
        i.tempest()
        if i.rect.y>450:
            i.rect.y=random.randint(-300,-50)
            i.rect.x=random.randint(50,750)
            i.speed=random.randint(3,5)

    troupe.draw(screen)
    InnocentMassacre.draw(screen)
    mmi.planet()
    pygame.display.update()
pygame.quit()
