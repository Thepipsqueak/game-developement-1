import pgzrun
import time
import random
WIDTH=1000
HEIGHT=425
retro=Actor("harry potttter.png")
retro.pos=100,212
orter=Actor("happy rn.png",(950,212))
def draw():
    screen.blit("qk.jpg",(0,0))
    retro.draw()
    orter.draw()
def update():
    pass

pgzrun.go()