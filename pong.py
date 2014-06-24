from __future__ import division
from visual import *
import math
'''
Building a game of Pong. Two paddles, one ball, some physics and a score.
'''
# Setting the scene up
def pause():
    while True:
        rate(30)
        if scene.mouse.events:
            m = scene.mouse.getevent()
            if m.click == 'left': return
        elif scene.kb.keys:
            k = scene.kb.getkey()
            return

scene.height = 600
scene.width = 800
scene.autocenter = False
scene.background = color.black

# Paddles and the ball
left = box(pos=(-20,0,0), length=1, height = 5, width = 2.5, color = (10,10,10))
right = box(pos=(20,0,0), length=1, height = 5, width = 2.5, color = (10,10,10))

ball = sphere(pos=(0,0,0), radius=0.4, color=(255,0,0))

# The math
v = 50 # ball velocity
theta = 0 # ball angle with horizontal
(x,y) = (0,0) # ball position
ly = 0 # left paddle position
ry = 0 # right paddle position
t = 0 # time
dt = 0.0005

## Max angle = 0.3587 rad
game = True

while game:
    rate(1/dt)
    t = t + dt
    
    # Move paddles
    if scene.kb.keys:
        key = scene.kb.getkey()
        if key == 'down':
            ry -= 0.5
        elif key == 'up':
            ry += 0.5
        elif key == 's':
            ly -= 0.5
        elif key == 'w':
            ly += 0.5
        elif key == ' ':
            pause()
        right.pos = (20,ry,0)
        left.pos = (-20,ly,0)

    # Keep paddles within bounds
    if abs(ry) >= 12 or abs(ly) >= 12:
        if ry >= 12:
            ry = 12
        elif ly >= 12:
            ly = 12
        elif ry <= 12:
            ry = -12
        elif ly <= 12:
            ly = -12

    if (abs(round(ry - y)) < 3 or abs(round(ly - y)) < 3) and abs(round(x)) == 19:
        y_hit = y
        
    # Ball bounce
    if abs(round(y)) == 15:
        l_1 = abs(x + 19)
        h_1 = (y_hit + 15)
        if l_1 > 0:
            theta = math.atan(l_1/h_1)
        else:
            theta = - (math.pi/2 - math.atan(l_1/h_1))
    # Paddle hit
    if (round(ry - y) == 1) and (round(x) == 19):
        theta = 0.12
    elif round(ly - y) == -1 and (round(x) == -19):
        theta = 0.12
    elif round(ry - y) == 2 and (round(x) == 19):
        theta = 0.28
    elif round(ly - y) == -2 and round(x) == -19:
        theta = 0.30
    elif round(ry - y) == -1 and (round(x) == 19):
        theta = -0.14
    elif round(ly - y) == 1 and round(x) == -19:
        theta = -0.14
    elif round(ry - y) == -2  and (round(x) == 19):
        theta = -0.27
    elif round(ly - y) == 2 and (round(x) == -19):
        theta = -0.25
    elif round(ry - y) == 0 and round(x) == 19:
        theta = 0
    elif round(ly-y) == 0 and round(x) == -19:
        theta = 0

    # Keeping the ball in bounds
    if abs(x) > 19:
        if x > 19:
            v = -1*v
        else:
            v = abs(v)
    
    x += v * cos(theta) * dt
    y += v * sin(theta) * dt        
    ball.pos = (x,y,0)
    
    # Know when the game is over
    if ((round(ry-y) > 3 or round(ry-y) < -3)) and x > 19:
        label(pos=(0,0,0), text="Left wins",align='center',height=10)
        break
    elif ((round(ly-y) > 3 or round(ly-y) < -3)) and x < -19:
        label(pos=(0,0,0), text="Right wins",align='center',height=10)
        break

    if abs(y) > 19:
        label(pos=(0,0,0),text="The game has broken. Who you gonna call?",height=10)
        break
    
