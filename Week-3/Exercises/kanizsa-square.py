from expyriment import design, control, stimuli, misc

control.set_develop_mode()

# Part 1: Global settings
GREY = misc.constants.C_GREY
WHITE = misc.constants.C_WHITE
BLACK = misc.constants.C_BLACK

exp = design.Experiment(name = "Display Edges", background_colour=GREY)
# exp.add_experiment_info(background_colour=GREY)
control.initialize(exp)
width, height = exp.screen.size
side_length = width * 0.25
radius = width * 0.05
width, height = width//2, height//2

# Part 2
rectangle = stimuli.Rectangle(
    size=(side_length, side_length),
    position=(0, 0),
    colour=GREY,
    # line_width=1,
)
circle_lu = stimuli.Circle(
    radius=radius,
    colour=BLACK,
    position=(-side_length/2, side_length/2),
)
circle_ld = stimuli.Circle(
    radius=radius,
    colour=WHITE,
    position=(-side_length/2, -side_length/2),
)
circle_ru = stimuli.Circle(
    radius=radius,
    colour=BLACK,
    position=(side_length/2, side_length/2),
)
circle_rd = stimuli.Circle(
    radius=radius,
    colour=WHITE,
    position=(side_length/2, -side_length/2),
)

# control.start(subject_id=1)

circle_lu.present(clear=True, update=False)
circle_ld.present(clear=False, update=False)
circle_ru.present(clear=False, update=False)
circle_rd.present(clear=False, update=False)
rectangle.present(clear=False, update=True)
exp.keyboard.wait()

control.end()