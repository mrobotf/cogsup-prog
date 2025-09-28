from expyriment import design, control, stimuli
from expyriment.misc.constants import C_BLACK, C_WHITE

control.set_develop_mode()

def hermann_grid(rows=6, cols=6,
                 square_size=80, spacing=20,
                 square_color=C_BLACK, background_color=C_WHITE):
    """
    Display a Hermann grid illusion.

    rows, cols : Number of squares vertically and horizontally.
    square_size : Size of each black square.
    spacing : Space between squares.
    square_color : Color of squares.
    """
    # background_colour is a read-only property,
    # therefore set it inside of the function
    exp = design.Experiment(
        name="Hermann Grid",
        background_colour=background_color
    )
    control.initialize(exp)

    total_width = cols * square_size + (cols - 1) * spacing
    total_height = rows * square_size + (rows - 1) * spacing

    canvas = stimuli.Canvas(size=(total_width, total_height),
                            colour=background_color)

    for row in range(rows):
        for col in range(cols):
            x = -total_width / 2 + square_size / 2 + col * (square_size + spacing)
            y = total_height / 2 - square_size / 2 - row * (square_size + spacing)

            square = stimuli.Rectangle(
                size=(square_size, square_size),
                position=(x, y),
                colour=square_color
            )
            square.plot(canvas)

    canvas.present(clear=True, update=True)
    return exp


if __name__ == "__main__":
    exp = design.Experiment()
    exp = hermann_grid(rows=6, cols=6,
                 square_size=80, spacing=20,
                 square_color=C_BLACK, background_color=C_WHITE)
    
    exp.keyboard.wait()
    control.end()