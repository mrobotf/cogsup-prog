from expyriment import design, control, stimuli, misc

control.set_develop_mode()

# Part 1: Global settings
rectangle_colour = misc.constants.C_RED

exp = design.Experiment(name = "Display Edges")
control.initialize(exp)
width, height = exp.screen.size
width_r = (width * 0.25) // 2
width, height = width//2, height//2

# Part 2
rectangle_lu = stimuli.Rectangle(
    size=(width_r*2, width_r*2),
    colour=rectangle_colour,
    position=(-width+width_r, height-width_r),
    line_width=1,
)
rectangle_ru = stimuli.Rectangle(
    size=(width_r*2, width_r*2),
    colour=rectangle_colour,
    position=(width-width_r, height-width_r),
    line_width=1,
)
rectangle_rd = stimuli.Rectangle(
    size=(width_r*2, width_r*2),
    colour=rectangle_colour,
    position=(width-width_r, -height+width_r),
    line_width=1,
)
rectangle_ld = stimuli.Rectangle(
    size=(width_r*2, width_r*2),
    colour=rectangle_colour,
    position=(-width+width_r, -height+width_r),
    line_width=1,
)

# control.start(subject_id=1)

rectangle_ld.present(clear=True, update=False)
rectangle_lu.present(clear=False, update=False)
rectangle_ru.present(clear=False, update=False)
rectangle_rd.present(clear=False, update=True)
exp.keyboard.wait()

control.end()