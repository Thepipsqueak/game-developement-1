import pgzrun
import random
#defining screen size
WIDTH=450
HEIGHT=350
def draw():
    rec=Rect((225,175),(200,50))
    screen.draw.rect(rec,"turquoise")
    re=Rect((125,100),(200,50))
    screen.draw.rect(re,"purple")
    r=Rect((75,200),(200,50))
    screen.draw.rect(r,"lime green")
    rectan=Rect((25,50),(200,50))
    screen.draw.rect(rectan,"white")
pgzrun.go()
