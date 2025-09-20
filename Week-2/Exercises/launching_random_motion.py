# have the axis of motion be randomly selected each time from a full circle.
# the red one on a circle with radius size equal to 300px.
# 
# The green square should move toward the red square and launch it upon
# contact.
# The launched object should travel at the same speed and for the same
# amount of time as the green square. 

import random
import math
from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name = "Two_squares")


def horizontal_launching(object_green, object_red, circle, theta):
    # Michottean launching
    # ----------------------------
    circle.present(clear=True, update=False)
    object_green.present(clear=False, update=False)
    object_red.present(clear=False, update=True)

    exp.keyboard.wait()

    step_size = 5
    
    # define the moving direction based on
    # the relative position of two squares
    step_x = math.copysign(
        step_size * math.cos(theta),
        object_red.position[0] - object_green.position[0]
        )
    step_y = math.copysign(
        step_size * math.sin(theta),
        object_red.position[1] - object_green.position[1]
        )
    step = (step_x, step_y)

    # move the green square
    collision, pos_collision = object_green.overlapping_with_stimulus(object_red)
    while not collision:
        object_green.move(step)
        circle.present(clear=True, update=False)
        object_green.present(clear=False, update=False)
        object_red.present(clear=False, update=True)
        collision, pos_collision = object_green.overlapping_with_stimulus(object_red)

    # after collision, move the red square
    # with the same direction and speed
    while abs(object_red.position[0]) < 400:
        object_red.move(step)
        circle.present(clear=True, update=False)
        object_red.present(clear=False, update=False)
        object_green.present(clear=False, update=True)

    exp.keyboard.wait()


# -----------------------------------

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# check the screen size
screen_width, screen_height = exp.screen.size   #  800 600

circle_radius = 300
square_size = (50, 50)

# randomly generate the position of the
# center of the circle and green square
pos_center_x = random.uniform(
    -(screen_width/2-circle_radius),
    screen_width/2 -circle_radius)
pos_center_y = random.uniform(
    -(screen_height/2-circle_radius),
    screen_height/2 -circle_radius)
pos_center = (pos_center_x, pos_center_y)

# randomly generate the position of the red square on the circle
pos_red_x = random.uniform(pos_center_x - circle_radius,
                           pos_center_x + circle_radius)
pos_red_y = random.choice([-1, 1]) \
        * (circle_radius**2 - (pos_red_x - pos_center_x)**2)**0.5 \
        + pos_center_y
pos_red = (pos_red_x, pos_red_y)

circle = stimuli.Circle(
    radius=circle_radius,
    position=pos_center)
square_green = stimuli.Rectangle(
    square_size,
    colour=(0, 255, 0),
    position = pos_center
    )
square_red = stimuli.Rectangle(
    square_size,
    colour=(255, 0, 0),
    position = pos_red
    )

# calculate the angle between the line connecting
# the centers of two squares and the x-axis
theta = math.atan2((pos_center_y - pos_red_y),
                    (pos_center_x - pos_red_x))


# horizontal_launching(self, object1, object2, tempgap, spatgap, speed)
#     Return Michottean launching, launching with a temporal gap,
#     launching with a spatial gap, and triggering in succession.
# 
# default: tempgap = True (temparal gap = 50 ms),
#          spatgap = True (spatial gap = 20),
#          speed = True (red square speed = 3 times of green square)
horizontal_launching(square_green, square_red, circle, theta)

control.end()