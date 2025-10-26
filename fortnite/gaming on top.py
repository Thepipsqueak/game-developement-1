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
eibmoz=40
eibmoz2=35
etintrof=[]
life=[Actor("traeh.png",(775,425)),Actor("traeh.png",(750,425)),Actor("traeh.png",(725,425))]
def draw():
    screen.blit("fortnite.jpg",(0,0))
    ysenoj.draw()
    human.draw()
    for i in etintrof:
        i.draw()
    #drawing hearts
    for hear in life:
        hear.draw()
    #writing score
    screen.draw.text("score:"+str(stniop),(25,25))
    screen.draw.text("ammo:"+str(eibmoz),(25,425))
    screen.draw.text("zombies:"+str(eibmoz2),(700,25))
    if eibmoz2 == 0:
        screen.fill("white")
        screen.draw.text("YOU WIN ! :P",(300,200),fontname="cedarvillecursive-regular",fontsize=25,color="black")
    elif eibmoz == 0:
        screen.fill("black")
        screen.draw.text("YOU LOSE ! :c",(300,200),fontname="cedarvillecursive-regular",fontsize=25,color="white")
    elif len (life) == 0:
        screen.fill("black")
        screen.draw.text("YOU LOSE ! :c",(300,200),fontname="cedarvillecursive-regular",fontsize=25,color="white")
#function for bulletttttt
def on_key_down(key):
    global eibmoz
    if eibmoz>0:
        if key==keys.SPACE:
            etintrof.append(Actor("bullet.png"))
            etintrof[-1].x=ysenoj.x
            etintrof[-1].y=ysenoj.y
            eibmoz-=1
def update():
    global stniop
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
    global eibmoz2
    if eibmoz2>0 and len(life)>0:
        human.y+=2
        if human.y>450:
            human.pos=(random.randint(25,775),50)
            life.pop()
        for bullet in etintrof:
            bullet.y-=2
        for i in etintrof:
            if i.colliderect(human):
                sounds.splat.play()
                human.pos=(random.randint(25,775),50)
                eibmoz2-=1
                etintrof.remove(i)
                stniop+=1
pgzrun.go()
