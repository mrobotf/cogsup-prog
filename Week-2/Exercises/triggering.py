# two squares side by side, the left one red, the right one green.
# Leave the fixation cross out. The two squares should be separated by
# 200 pixels but centered as a whole.
# Present them on-screen until a key is pressed.

########################################################
# Once the moving speed of the right square is 3 times
# faster than the left square, it does look like the red
# square caused the green square to move
########################################################

# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings
# of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two_squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# square_size of each square
square_size = (50, 50)

# define properties of square on the left, red, initial position (-400, 0)
square_left = stimuli.Rectangle(
    square_size,
    colour=(255, 0, 0),
    position = (-400, 0)
    )

# define properties of square on the right, green, initial position (0, 0)
square_right = stimuli.Rectangle(
    square_size,
    colour=(0, 255, 0),
    position = (0, 0)
    )

# Start running the experiment
control.start(subject_id=1)

# Present square on the left
square_left.present(clear=True, update=False)

# Present square on the right
square_right.present(clear=False, update=True)

# step size for moving squares, control speed of movement
step_size_left = 5
step_size_right = 15

# Move the left square until it touches right
while square_right.position[0] - square_left.position[0] > 50:
    square_left.move((step_size_left, 0))
    # to update screen, show new position of left square
    square_left.present(clear=True, update=False)
    square_right.present(clear=False, update=True)

exp.clock.wait(70)

# Then move the right square
while square_right.position[0] - square_left.position[0] < 400:
    square_right.move((step_size_right, 0))
    square_right.present(clear=True, update=False)
    square_left.present(clear=False, update=True)
    
exp.clock.wait(1000)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()