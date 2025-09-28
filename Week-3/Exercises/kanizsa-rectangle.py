from expyriment import design, control, stimuli
from expyriment.misc.constants import C_BLACK, C_WHITE, C_GREY

control.set_develop_mode()

def kanizsa_rectangle(aspect_ratio=1.0, rect_scale=0.25, circle_scale=0.05):
    """
    Display a Kanizsa-rectangle illusion.

    aspect_ratio : Width / Height of the rectangle
    rect_scale : Scaling factor for rectangle size relative to screen width.
    circle_scale : Scaling factor for inducing circle radius relative to screen width.
    """


    screen_w, screen_h = exp.screen.size

    rect_height = screen_w * rect_scale
    rect_width = rect_height * aspect_ratio

    # Circle radius scaled separately
    radius = screen_w * circle_scale

    rectangle = stimuli.Rectangle(
        size=(rect_width, rect_height),
        position=(0, 0),
        colour=C_GREY
    )

    half_w, half_h = rect_width / 2, rect_height / 2

    circle_lu = stimuli.Circle(radius=radius, colour=C_BLACK,
                               position=(-half_w, half_h))
    circle_ld = stimuli.Circle(radius=radius, colour=C_WHITE,
                               position=(-half_w, -half_h))
    circle_ru = stimuli.Circle(radius=radius, colour=C_BLACK,
                               position=(half_w, half_h))
    circle_rd = stimuli.Circle(radius=radius, colour=C_WHITE,
                               position=(half_w, -half_h))

    circle_lu.present(clear=True, update=False)
    circle_ld.present(clear=False, update=False)
    circle_ru.present(clear=False, update=False)
    circle_rd.present(clear=False, update=False)
    rectangle.present(clear=False, update=True)

    exp.keyboard.wait()
    control.end()


if __name__ == "__main__":
    exp = design.Experiment(
        name="Kanizsa-Rectangle",
        background_colour=C_GREY
    )
    control.initialize(exp)
    # Wide rectangle, medium size, medium circles
    kanizsa_rectangle(aspect_ratio=2.0, rect_scale=0.25, circle_scale=0.05)
