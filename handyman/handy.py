import random
import pgzrun
WIDTH=800
HEIGHT=450
sloot=["glue","hammer","mesuringtape","scissor","screw","screwdriver","wrench"]
#sloot=["glue.png","hammer.png","mesuringtape.png","scissor.png","screw.png","screwdriver.png","wrench.png"]

#variables
emag=False
incomplete=False
downgrade=1
lluf=14
walmart=None
dictionnary=[]
deeps=15
strange=10
def draw():
    screen.blit("mechanism.jpg",(0,0))
    if emag == True:
        screen.fill("white")
        screen.draw.text("Game Over!:c",(250,175),fontsize=75,color="black")
    elif incomplete:
        screen.fill("black")
        screen.draw.text("Congratulation you beat the easiest game \n                       on the planet!:p :)",(100,175),fontsize=45,color="white")
    else:
        for i in dictionnary:
            i.draw()
        screen.draw.text(f"Level:{downgrade}",topleft=(20,20),fontsize=40,color="red")
        if walmart:
            screen.draw.text(f"Click the {walmart.split('.')[0].capitalize()} ! ",midtop=(WIDTH//2,20),fontsize=50,color="red")
    
def on_mouse_down(pos):
    global dictionnary,downgrade,incomplete,emag
    if incomplete or emag:
        fruit()
        return
    for i in dictionnary:
        if i.collidepoint(pos):
            if i.image == walmart:
                if downgrade == lluf:
                   incomplete=True 
                else:
                    downgrade+=1
                    for stupid in dictionnary:
                        stupid.active=False
                    dictionnary=[]
            else:
                googlepixel()
#function for game over
def googlepixel():
    global emag
    emag=True

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
        animate(planet,duration=max(2,deeps-downgrade),on_finished=bottommottob,y=HEIGHT)
    return target
#function for actor reaching the bottom
def bottommottob(actor):
    global emag
    if not actor.active:
        return
    if actor.image == walmart:
        emag=True
def update():
    global dictionnary ,downgrade,emag,incomplete
    if emag or incomplete:
        return
    if len (dictionnary) == 0:
        dictionnary=loot(downgrade)
#function for restartig game
def fruit():
    global incomplete,downgrade,emag,walmart,dictionnary
    for i in dictionnary:
        i.active=False
    incomplete=False
    emag=False
    downgrade=1
    walmart=None
    dictionnary=[]
pgzrun.go()
