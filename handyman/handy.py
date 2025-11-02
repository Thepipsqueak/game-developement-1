import random
import pgzrun
WIDTH=800
HEIGHT=450
sloot=["glue.png","hammer.png","mesuringtape.png","scissor.png","screw.png","screwdriver.png","wrench.png"]
#variables
emag=False
incomplete=False
downgrade=1
lluf=14
walmart=None
dictionnary=[]
def draw():
    screen.blit("mechanism.jpg",(0,0))
#function for falling item
def loot(xtra):
    global walmart
    target=[]
    walmart=random.choice(sloot)
    correct=random.choices([i for i in sloot if i !=walmart],k=xtra)
    trong=[walmart]+correct
    random.shuffle(trong)
    galaxie=WIDTH/(len(trong)+1)
    for i,img in enumerate(trong):
        planet=Actor(img)
        planet.active=True
        planet.x=(i+1)*galaxie
        planet.y=0
        target.append(planet)
        
def update():
    pass
pgzrun.go()