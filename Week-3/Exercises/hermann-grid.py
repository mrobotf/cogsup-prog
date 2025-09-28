from expyriment import design, control, stimuli
from expyriment.misc.constants import C_BLACK, C_WHITE

control.set_develop_mode()

def hermann_grid(rows=6, cols=6,
                 square_size=80, spacing=20,
                 square_color=C_BLACK):
    """
    Display a Hermann grid illusion.

    rows, cols : Number of squares vertically and horizontally.
    square_size : Size of each black square (pixels).
    spacing : Space between squares (pixels).
    square_color : Color of squares (default black).
    background_color : Background color of screen (default white).
    """

    total_width = cols * square_size + (cols - 1) * spacing
    total_height = rows * square_size + (rows - 1) * spacing

    for row in range(rows):
        for col in range(cols):
            # Center of each square
            x = -total_width / 2 + square_size / 2 + col * (square_size + spacing)
            y = total_height / 2 - square_size / 2 - row * (square_size + spacing)

            square = stimuli.Rectangle(
                size=(square_size, square_size),
                position=(x, y),
                colour=square_color
            )
            square.present(clear=False, update=False)

    exp.screen.update()

    exp.keyboard.wait()
    control.end()


if __name__ == "__main__":
    exp = design.Experiment(
        name="Hermann Grid",
        background_colour=C_WHITE
    )
    control.initialize(exp)
    hermann_grid(rows=6, cols=6,
                 square_size=80, spacing=20,
                 square_color=C_BLACK)
