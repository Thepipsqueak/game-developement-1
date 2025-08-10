import pgzrun
import random
WIDTH=800
HEIGHT=500
mes=""
# creating an actor
mot=Actor("cutie pie.png")
def draw():
    screen.blit("try to find me heeheehee",(0,0))
    screen.draw.text(mes,center=(400,50),fontsize=25)
    mot.draw()
def update():
    pass
def stuti():
    mot.x=random.randint(0,800)
    mot.y=random.randint(0,500)
stuti()
#mouse event
def on_mouse_down(pos):
    global mes
    if mot.collidepoint(pos):
        stuti()
        mes="You found him!!!but...can you do it again??"
    else:
        mes="WRONG!!!!!Try again...if you can that is..."
pgzrun.go()
