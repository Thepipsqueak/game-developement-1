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
century=30
football=0
rage=False
pokemon=0
smart=0
paper="nature.txt"
hold=[]
def draw():
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
    
def update():
    pass   
    microsoft()
def backstory():
    global century
    if century>0:
        century-=1
def microsoft():
    passion.x-=3
    if passion.right<0:
        passion.left=800
#function for reading the file
def xbox():
    global smart,pokemon,hold
    synonyme=open(paper,"r")
clock.schedule_interval(backstory,1)        
pgzrun.go()
