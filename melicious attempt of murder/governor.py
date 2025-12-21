import random
import pgzrun
WIDTH=800
HEIGHT=500
passion=Rect(0,0,800,75)
confusion=Rect(0,75,600,100)
dead=Rect(25,200,280,130)
earth=Rect(25,350,280,130)
monkey=Rect(320,200,280,130)
stuti=Rect(320,350,280,130)
acid=Rect(625,100,165,200)
spaceship=Rect(625,350,165,130)
wrong=[dead,earth,monkey,stuti,acid,spaceship]
century=6.7
def draw():
    screen.fill("darkviolet")
    screen.draw.filled_rect(passion,"yellow")
    screen.draw.filled_rect(confusion,"white")
    screen.draw.filled_rect(dead,"white")
    screen.draw.filled_rect(earth,"white")
    screen.draw.filled_rect(monkey,("white"))
    screen.draw.filled_rect(stuti,("white"))
    screen.draw.filled_rect(acid,("white"))
    screen.draw.filled_rect(spaceship,("white"))
    #text boxes
    
def update():
    pass
pgzrun.go()