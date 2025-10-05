from expyriment import design, control, stimuli
from expyriment.misc.constants import C_BLACK, C_WHITE, \
                                    C_YELLOW, C_RED, C_GREEN
from expyriment.misc.constants import K_SPACE
import numpy as np

def load(stims):
    for stim in stims:
        stim.preload()

def present_for(isi):
    # convert isi(frame) to ms
    isi = np.array(isi)
    isi = 2*((isi) * (1000 / 60)) # in case isi == 0
    exp.clock.wait(isi)
    return isi
      
def make_circles(r):
    # TODO set positions based on r
    gap = 2*r+0.2*r
    positions = [(-(gap / 2 + gap), 0), (-(gap / 2), 0), (gap / 2, 0), (gap / 2 + gap, 0)]
    circles = [stimuli.Circle(r, position=pos, colour=C_BLACK)
                for pos in positions]
    return circles, positions

def add_tags(stims, r, positions):
    """
    set color tags postion based on circles' position
    """
    r_tag = 0.1*r
    stims.extend([stimuli.Circle(r_tag, position=pos, colour=col)
                       for pos, col in zip(positions,
                                           [C_YELLOW, C_RED, C_GREEN, C_YELLOW])])
    return stims

def run_trial(r, isi, color_tag):
    circles, positions = make_circles(r)
    isi = present_for(isi)
    if color_tag:
        circles = add_tags(circles, r, positions)
        circles_left = circles[:3] + circles[4:7]
        circles_right = circles[1:4] + circles[5:]
    else:
        circles_left = circles[:3]
        circles_right = circles[1:4]
    

    while True:
        if exp.keyboard.check(K_SPACE): # inside the loop
            break

        for i, c in enumerate(circles_left): # 3 circles on the left
            c.present(clear=(i==0), update=(i==len(circles_left)-1))
        exp.clock.wait(10*(1000 / 60))  # show for 10 frame
        exp.screen.clear()
        exp.screen.update()
        exp.clock.wait(isi)
        for i, c in enumerate(circles_right): # 3 circles on the right
            c.present(clear=(i==0), update=(i==len(circles_right)-1))
        exp.clock.wait(10*(1000 / 60))  # show for 1 frame
        exp.screen.clear()
        exp.screen.update()
        exp.clock.wait(isi)

def ternus():
    # 1. Element motion without color tags (low ISI)
    # 2. Group motion without color tags (high ISI)
    # 3. Element motion with color tags (high ISI)
    trials = [{"r": 70, "isi": 0, "color_tag": False},
              {"r": 70, "isi": 18, "color_tag": False},
              {"r": 70, "isi": 0, "color_tag": True}]

    for trial_params in trials:
        run_trial(**trial_params)
        exp.screen.clear()
        exp.screen.update()

""" Trail starts here """

exp = design.Experiment(name="ternus", background_colour=C_WHITE)

control.set_develop_mode()
control.initialize(exp)

ternus()

control.end()
