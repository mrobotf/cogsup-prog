from expyriment import design, control, stimuli
from expyriment.misc.constants import C_BLACK, C_WHITE, \
                                    C_YELLOW, C_RED, C_GREEN
from expyriment.misc.constants import K_SPACE
from drawing_functions import *
import numpy as np


def make_circles(r):
    gap = 2*r+0.2*r
    positions = [(-(gap / 2 + gap), 0), (-(gap / 2), 0),
                 (gap / 2, 0), (gap / 2 + gap, 0)]
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
    isi_time = to_time(isi)
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
        present_for(exp, circles_left, num_frames=12) # 200 ms
        present_for(exp, [], num_frames=isi)
      
        present_for(exp, circles_right, num_frames=12) # 200 ms
        present_for(exp, [], num_frames=isi)


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
