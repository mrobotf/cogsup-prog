from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
from expyriment.misc.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE


""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
# Pass in a list of string variable names: This will give the names of your columns
exp.add_data_variable_names(["side", 'key', "radius", 'coordinate'])
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

def make_text(side='L'):
    heading = 'Blind spot'
    if side == 'L':
        text = 'Cover your right eye. Fixate on the fixation. Press 1/2 to reduce/enlarge the size of the circle. Press keyboard arrows to control circle position. When you are done, press space to move on'
    else:
        text = 'Cover your left eye. Fixate on the fixation. Press 1/2 to reduce/enlarge the size of the circle. Press keyboard arrows to control circle position. When you are done, press space to move on'
    t = stimuli.TextScreen(heading, text)
    return t

""" Experiment """
def run_trial(side):
    text = make_text(side)
    text.present()
    exp.keyboard.wait()

    if side == 'L':
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    elif side == 'R':
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[-300, 0])
    fixation.preload()

    radius = 75
    circle = make_circle(radius)

    fixation.present(True, False)
    circle.present(False, True)

    pos = circle.position
    while 1:
        key, rt = exp.keyboard.wait()
        if key == K_DOWN:
            circle.position = (pos[0], pos[1]-10)
        elif key == K_UP:
            circle.position = (pos[0], pos[1]+10)
        elif key == K_LEFT:
            circle.position = (pos[0]-10, pos[1])
        elif key == K_RIGHT:
            circle.position = (pos[0]+10, pos[1])
        elif key == ord('1'):
            circle = make_circle(0.9*radius, pos)
            radius = circle.radius
        elif key == ord('2'):
            circle = make_circle(1.1*radius, pos)
            radius = circle.radius
        elif key == K_SPACE:
            break
        
        fixation.present(True, False)
        circle.present(False, True)
        pos = circle.position
    
        # Exercise 2B
        exp.data.add([side, key, circle.radius, circle.position]) # Can be condition, reaction times, responses, anything!

    # Exercise 2A
    # At the end of your run_trial function, store any data you want in exp.data
    # exp.data.add([side, circle.radius, circle.position[0], circle.position[1]]) # Can be condition, reaction times, responses, anything!

    # exp.keyboard.wait()

control.start(subject_id=1)

side = 'R'
run_trial(side)
    
control.end()