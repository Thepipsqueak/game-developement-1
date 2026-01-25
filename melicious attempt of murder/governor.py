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
wrong=[dead,earth,monkey,stuti]
century=30
football=0
rage=False
pokemon=0
smart=0
paper="nature.txt"
hold=[]
gitgud=False
def draw():
    if gitgud == True:
        screen.fill("white")
        screen.draw.text(f"congratulations! You acctually got good...\n AT NOTHING!!!your score is {football}",(50,225),fontsize=50,color=("black"))
    elif rage == True:
        screen.fill("black")
        screen.draw.text(f"Git Gud!:Your score is {football}",(175,225),fontsize=60,color=("white"))
    else:
        screen.fill("darkviolet")
        screen.draw.filled_rect(passion,"yellow")
        screen.draw.filled_rect(confusion,"white")
        screen.draw.filled_rect(dead,"white")
        screen.draw.filled_rect(earth,"white")
        screen.draw.filled_rect(monkey,("white"))
        screen.draw.filled_rect(stuti,("white"))
        screen.draw.filled_rect(acid,("yellow"))
        screen.draw.filled_rect(spaceship,("yellow"))
        #text boxes
        screen.draw.textbox('skip',spaceship,color=("black"),)
        screen.draw.textbox("Time:\n"+str(century),acid,color=("black"))
        child="welcome to the ultimate test of knowledge to test if you are smart"
        child=child+f"Q:{pokemon} of {smart}"
        screen.draw.textbox(child,passion,color=("black"))
        screen.draw.textbox(question[0],confusion,color=("black"))
        screen.draw.textbox(question[1],dead,color=("black"))
        screen.draw.textbox(question[2],earth,color=("black"))
        screen.draw.textbox(question[3],monkey,color=("black"))
        screen.draw.textbox(question[4],stuti,color=("black"))
#checking if answer is correct
def headphones():
    global century,football,question,hold
    football+=1
    if len(hold)>0:
        question=stutii()
        century=30
    else:
        stressed()
#checking if you lost
def me():
    global question,century,rage,football,child
    century=0
    rage=True
# check if you win
def stressed():
    global gitgud,rage
    gitgud=True
    rage=False



def on_mouse_down(pos):
    i=1
    for necessity in wrong:
        if necessity.collidepoint(pos):
            if i == int(question[5]):
                headphones()
            else:
                me()
        i+=1
    if spaceship.collidepoint(pos):
        school()

# function for skipping
def school():
    global question, century
    if hold and rage != True:
        question=stutii()
        century=30
    else:
        me()

    
def update():
    pass   
    microsoft()
#function for timer
def backstory():
    global century
    if century>0:
        century-=1
# function for marquee box
def microsoft():
    passion.x-=3
    if passion.right<0:
        passion.left=800
#function for reading the file
def xbox():
    global smart,pokemon,hold
    synonyme=open(paper,"r")
    for i in synonyme:
        hold.append(i)
        smart+=1
    synonyme.close()
def stutii ():
    global pokemon
    pokemon+=1
    return hold.pop(0).split(",")
clock.schedule_interval(backstory,1)  
xbox()
question=stutii()   
pgzrun.go()
