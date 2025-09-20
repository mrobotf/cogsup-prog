# two squares side by side, the left one red, the right one green.
# Leave the fixation cross out. The two squares should be separated by 200 pixels but centered as a whole.
# Present them on-screen until a key is pressed.

# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry

control.set_develop_mode()

exp = design.Experiment(name = "Labeled shapes")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

triangle = stimuli.Shape(
    vertex_list=geometry.vertices_regular_polygon(3, 50),
    colour=(138,43,226),
    position = (-100, 0),
    )

hexagon = stimuli.Shape(
    # side length is 25
    vertex_list=geometry.vertices_regular_polygon(6, 25),
    colour=(255, 255, 0),
    position = (100, 0),
    )

line_triangle = stimuli.Line(  
    start_point = (-100, (25*(3**0.5))/2),
    end_point = (-100, 50+(25*(3**0.5))/2),
    line_width = 3,
    colour = (255, 255, 255)
    )

line_hexagon = stimuli.Line(  
    start_point = (100, (25*(3**0.5))/2),
    end_point = (100, 50+(25*(3**0.5))/2),
    line_width = 3,
    colour = (255, 255, 255)
    )

text_triangle = stimuli.TextLine(
    text = ("triangle"),
    position = (-100, 70+(25*(3**0.5))/2),
    text_colour = (255, 255, 255)
)

text_hexagon = stimuli.TextLine(
    text = ("hexagon"),
    position = (100, 70+(25*(3**0.5))/2),
    text_colour = (255, 255, 255)
)



# Start running the experiment
control.start(subject_id=1)

triangle.present(clear=True, update=False)
hexagon.present(clear=False, update=False)
line_triangle.present(clear=False, update=False)
line_hexagon.present(clear=False, update=False)
text_triangle.present(clear=False, update=False)
text_hexagon.present(clear=False, update=True)


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()