# whether there is a temporal gap,
# whether there is a spatial gap, and
# whether the second square moves at the same speed as the first square or at a higher speed.
# The program should display the four types of events in succession:
# Michottean launching, launching with a temporal gap, launching with a spatial gap, and triggering.

# Michottean launching
from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name = "Two_squares")


def horizontal_launching(object_left, object_right, tempgap, spatgap, speed):
    # Michottean launching
    # ----------------------------
    object_left.present(clear=True, update=False)
    object_right.present(clear=False, update=True)

    # launching with a temporal gap
    # ----------------------------
    exp.clock.wait(1000)

    step_size = 5

    while object_right.position[0] - object_left.position[0] > 50:
        object_left.move((step_size, 0))
        # to update screen, show new position of left square
        object_left.present(clear=True, update=False)
        object_right.present(clear=False, update=True)

    if tempgap:
        exp.clock.wait(50)

    # Then move the right square
    while object_right.position[0] - object_left.position[0] < 400:
        object_right.move((step_size, 0))
        object_right.present(clear=True, update=False)
        object_left.present(clear=False, update=True)

    # launching with a spatial gap
    # ----------------------------
    object_left.reposition((-400, 0))
    object_right.reposition((0, 0))
    exp.clock.wait(1000)
    object_left.present(clear=True, update=False)
    object_right.present(clear=False, update=True)

    step_size = 5

    if spatgap:
        spartial_gap = 20
    else:
        spartial_gap = 0

    while object_right.position[0] - object_left.position[0] > 50 + spartial_gap:
        object_left.move((step_size, 0))
        object_left.present(clear=True, update=False)
        object_right.present(clear=False, update=True)

    while object_right.position[0] - object_left.position[0] < 400:
        object_right.move((step_size, 0))
        object_right.present(clear=True, update=False)
        object_left.present(clear=False, update=True)

    # triggering
    # if speed, right square moves faster
    # ----------------------------
    object_left.reposition((-400, 0))
    object_right.reposition((0, 0))
    exp.clock.wait(1000)
    object_left.present(clear=True, update=False)
    object_right.present(clear=False, update=True)

    step_size_left = 5
    step_size_right = 15 if speed else 5

    # Move the left square until it touches right
    while object_right.position[0] - object_left.position[0] > 50:
        object_left.move((step_size_left, 0))
        # to update screen, show new position of left square
        object_left.present(clear=True, update=False)
        object_right.present(clear=False, update=True)

    exp.clock.wait(70)

    # Then move the right square
    while object_right.position[0] - object_left.position[0] < 400:
        object_right.move((step_size_right, 0))
        object_right.present(clear=True, update=False)
        object_left.present(clear=False, update=True)
        
    exp.keyboard.wait()


# -----------------------------------

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

square_size = (50, 50)
square_left = stimuli.Rectangle(
    square_size,
    colour=(255, 0, 0),
    position = (-400, 0)
    )

square_right = stimuli.Rectangle(
    square_size,
    colour=(0, 255, 0),
    position = (0, 0)
    )

# Start running the experiment
control.start(subject_id=1)


# horizontal_launching(self, object1, object2, tempgap, spatgap, speed)
#     Return Michottean launching, launching with a temporal gap,
#     launching with a spatial gap, and triggering in succession.
# 
# default: tempgap = True (temparal gap = 50 ms),
#          spatgap = True (spatial gap = 20),
#          speed = True (right square speed = 3 times of left square)
horizontal_launching(square_left, square_right, tempgap=True, spatgap=True, speed=True)

control.end()