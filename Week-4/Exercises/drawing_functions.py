from expyriment import design, control, stimuli
import random

def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(stims):
    # Have draw return its execution time & use that inside display
    t0 = exp.clock.time
    for i, stim in enumerate(stims):
        # includes edge cases:
        # 1. empty list
        # 2. only one stimulus
        stim.present(clear=(i==0), update=(i==len(stims)-1))
    return exp.clock.time - t0
    # return the time it took to draw

def present_for(stims, t=1000):
    td = timed_draw(stims)
    exp.clock.wait(t - td)


""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemneted correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()