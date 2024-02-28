import pgzrun
import random

#creating title of game window
TITLE = "Good Shot"

#setting width and height of game window
WIDTH = 500
HEIGHT = 500

#creating a variable to store a message
message = ""

#creating actors-actors are game objects
alien = Actor("alien")
alien.pos=50,50

#creating function draw
#this is automatically called by system. instructions that we want continuously repeated are written in function draw
#function draw is an endless loop which keeps repeating until code is running
def draw() :
    screen.clear()
    screen.fill(color=(128,0,0))
    screen.draw.text(message,center=(400,10),fontsize=30)
    #instruction to draw alien on screen
    alien.draw()

#creating a function to change alien position
def place_alien() :
    alien.x = random.randint(50,WIDTH-50)
    alien.y = random.randint(50,HEIGHT-50)

def on_mouse_down(pos) :
    if alien.collidepoint(pos):
        message = "Good Shot!"
        place_alien()
    
    else :
        message = "you missed"

place_alien()


#function must be called to start processing
pgzrun.go()