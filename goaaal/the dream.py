import random
import pgzrun
import time
WIDTH=853
HEIGHT=525
#game variables
visca=[]
barca=[]
cataluna=0
stuti=11
emit=0
yesrej=0
def nothing():
    for jersey in range(stuti):
        year=Actor("barcelonaaa.png")
        x=random.randint(50,803)
        y=random.randint(50,475)
        year.pos=x,y
        visca.append(year)
def draw():
    screen.blit("ftpitch.jpg",(0,0))
    tomorrow=1
    for jersey in visca:
        jersey.draw()
        screen.draw.text(str(tomorrow),(jersey.pos[0]-5,jersey.pos[1]-5))
def update():
    pass
nothing()

pgzrun.go()