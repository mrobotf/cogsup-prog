# two squares side by side, the left one red, the right one green.
# Leave the fixation cross out. The two squares should be separated by 200 pixels but centered as a whole.
# Present them on-screen until a key is pressed.

# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry
from math import tanh, sin, cos, pi

control.set_develop_mode()

exp = design.Experiment(name = "Labeled shapes")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

def polygon(n, side_length=50, colour_object=(255, 255, 255), position_object=(0, 0)):
    if n < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    polygons = {
        3: "triangle",
        4: "square",
        5: "pentagon",
        6: "hexagon",
        7: "heptagon",
        8: "octagon",
        9: "nonagon",
        10: "decagon"
    }
    # circumscribed_circle of the polygon
    radius = side_length/(2*sin(pi/n))
    if n % 2 != 0:
        # odd number, e.g. triangle
        line_start_point = (position_object[0], radius*(1+cos(pi/n))/2)
    else:
        line_start_point = (position_object[0], radius*cos(pi/n))

    if n in polygons:
        object = stimuli.Shape(
            vertex_list=geometry.vertices_regular_polygon(n, side_length),
            colour=colour_object,
            position = position_object,
        )

    line_polygon = stimuli.Line(  
        start_point = line_start_point,
        end_point = (position_object[0], 50+line_start_point[1]),
        line_width = 3,
        colour = (255, 255, 255)
        )

    text_polygon = stimuli.TextLine(
        text = (polygons[n]),
        position = (position_object[0], 70+line_start_point[1]),
        text_colour = (255, 255, 255)
    )
    return object, line_polygon, text_polygon

# the y coordinate of the center is the center of the height
triangle, line_triangle, text_triangle = \
    polygon(3, 50, (138,43,226), (-100, 0))

hexagon, line_hexagon, text_hexagon = \
    polygon(6, 25, (255, 255, 0), (100, 0))

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