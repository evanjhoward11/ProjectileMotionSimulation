import vpython as vp
import math, time

#Inputs/Constants
g = -9.81
v1 = 15
theta1 = 45
h = 0

#Calculate components of velocity
vx1 = v1 * math.cos(math.radians(abs(theta1)))
vy1 = v1 * math.sin(math.radians(abs(theta1)))

#Ball's size, starting position, color, trail
ball_radius = 0.5
y1 = ball_radius + h
ball_pos = vp.vector(0,y1,0)
ball = vp.sphere(pos=ball_pos, radius=ball_radius, color=vp.color.red, make_trail=True)

#While loop initial conditions/constants
y = ball_radius
t = 0
dt = 0.01

#While the height is greater than/equal to ball's radius, calculate the ball's height
#Run 1st while loop to find length of platform, don't change ball's position
while y >= ball_radius:
  y = (g / (2 * vx1 ** 2)) * (t ** 2) + (vy1 / vx1) * t + y1
  t = t + dt

#Platform's dimensions, position, color
#Platform length is determined by 1st loop, is +/- ball radius on each either end
length = t + ball_radius * 2
thickness = 1
ground_size = vp.vector(length,thickness,2)
ground_pos = vp.vector(length/2-ball_radius,-thickness/2,0)
ground = vp.box(pos=ground_pos, size=ground_size, color=vp.color.green)

#Run 2nd while loop to change ball's position
vp.canvas()
t = 0
time.sleep(.3)
while ball.pos.y >= ball_radius:
  vp.rate(1000)
  
  y = (g / (2 * vx1 ** 2)) * (t ** 2) + (vy1 / vx1) * t + y1
  ball.pos = vp.vector(t,y,0)
  
  t = t + dt
