# two squares side by side, the left one red, the right one green.
# Leave the fixation cross out. The two squares should be separated by 200 pixels but centered as a whole.
# Present them on-screen until a key is pressed.

# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name = "Two_squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

square_size = (50, 50)
square_left = stimuli.Rectangle(
    square_size,
    colour=(100, 0, 0),
    position = (-100, 0)
    )

square_right = stimuli.Rectangle(
    square_size,
    colour=(0, 100, 0),
    position = (100, 0)
    )

# Start running the experiment
control.start(subject_id=1)

square_left.present(clear=True, update=False)
square_right.present(clear=False, update=True)


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()