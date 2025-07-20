import pgzrun
import random
WIDTH=600
HEIGHT=450
def draw():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    cer=600
    tcer=150
    for i in range (60):
        sir=Rect((0,0),(cer,tcer))
        sir.center=300,225
        screen.draw.rect(sir,(r,g,b))
        cer-=5
        tcer+=5
def update():
    pass
pgzrun.go()
