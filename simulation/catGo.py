# from trepan.api import debug

# import pdb
# pdb.set_trace()

import runWorld as rw
import drawWorld as dw


# Initialize world (create display)
name = "Cat Go!"
width = 500
height = 500
rw.newDisplay(width, height, name)

# World state will be single x coordinate at left edge of world
initState = 0

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")

# type state -> image (input-output IO)
# state here is the x-coordinate
def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state, height/2))


# We'll update the state on each tick by incrementing the x stateinate
# type state -> state
def updateState(state):
    return(state+1)

# We'll terminate when the x stateinate reaches the screen edge

# type state -> bool
def endState(state):
    if (state >= width):
        return True
    else:
        return False


# For now we'll handle events just logging them to the console
# If user does something, you may want to change state
# state -> event -> state
def handleEvent(state, event):
    return(state)

# Off we go! Start the cat at the left edge, and try for 30 FPS
frameRate = 60
initState = 0
# debug()
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
# runworld is higher order function that calls other functions
