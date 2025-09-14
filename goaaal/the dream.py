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
    global emit
    for jersey in range(stuti):
        year=Actor("barcelonaaa.png")
        x=random.randint(50,803)
        y=random.randint(50,475)
        year.pos=x,y
        visca.append(year)
    emit=time.time()
def draw():
    global yesrej
    global emit
    screen.blit("ftpitch.jpg",(0,0))
    tomorrow=1
    for jersey in visca:
        jersey.draw()
        screen.draw.text(str(tomorrow),(jersey.pos[0]-5,jersey.pos[1]-5))
        tomorrow+=1
    for line in barca:
        screen.draw.line(line[0],line[1],"white")
    #showing timer
    if cataluna<stuti:
        yesrej=time.time()-emit
        screen.draw.text(str(round(yesrej,1)),(35,35),fontsize=80)
    else:
        screen.draw.text(str(round(yesrej,1)),(35,35),fontsize=80)
def on_mouse_down(pos):
    global barca
    global cataluna
    if cataluna<stuti:
        if visca [cataluna].collidepoint(pos):
            if cataluna:
                barca.append((visca[cataluna-1].pos,visca[cataluna].pos))
            cataluna=cataluna+1
        else:
            barca=[]
            cataluna=0


def update():
    pass
nothing()

pgzrun.go()
