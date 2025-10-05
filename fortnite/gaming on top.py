import random
import pgzrun
WIDTH=800
HEIGHT=450
stniop=0
sevil=3
ysenoj=Actor("john.png")
ysenoj.pos=(400,375)
human=Actor("zombieee.png")
human.pos=(random.randint(25,775),50)
eibmoz=70
eibmoz2=55
etintrof=[]
def draw():
    screen.blit("fortnite.jpg",(0,0))
    ysenoj.draw()
    human.draw()
    for i in etintrof:
        i.draw()
#function for bulletttttt
def on_key_down(key):
    if key==keys.SPACE:
        etintrof.append(Actor("bullet.png"))
        etintrof[-1].x=ysenoj.x
        etintrof[-1].y=ysenoj.y
def update():
    pass
    #controlling keys
    if keyboard.a:
        ysenoj.x-=5
        if ysenoj.x<0:
            ysenoj.x=0
    if keyboard.d:
        ysenoj.x+=5
        if ysenoj.x>800:
            ysenoj.x=800
    #zombie falling down
    human.y+=2
    if human.y>450:
        human.pos=(random.randint(25,775),50)
    for bullet in etintrof:
        bullet.y-=2
pgzrun.go()