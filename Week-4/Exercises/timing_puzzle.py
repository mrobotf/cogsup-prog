from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

t0 = exp.clock.time
fixation.present()

# exp.clock.time execulation time much less than 1ms
# can be ignored
t1 = exp.clock.time

# fixation present for 1 second
exp.clock.wait(1000 - (t1 - t0))

t2 = exp.clock.time

# to show fixation was present for 1 second
fix_duration = (t2 - t0)/1000

text.present()

exp.clock.wait(1000)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()