from expyriment import design, control, stimuli
from expyriment.misc.constants import C_RED, C_BLUE, C_GREEN, C_YELLOW, C_WHITE, C_BLACK, K_r, K_b, K_g, K_o
import random
import itertools


""" Constants """
KEYS = [K_r, K_b, K_g, K_o]
TRIAL_TYPES = ["Match","Mismatch"]
WORDS = ['red', 'blue', 'green', 'yellow']

COLOR_KEY_MAPPING = {
    "red": K_r,
    "blue": K_b,
    "green": K_g,
    "orange": K_o
}

N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16

INSTR_START = """
In this task, you have to indicate whether the meaning of a word and the color of its font match. \n
Respond to the COLOUR the word is written in:

R = RED\n
B = BLUE\n
G = GREEN\n
O = ORANGE

Press SPACE to continue.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """ Good job! You got it right. """
FEEDBACK_INCORRECT = """ That was incorrect. """

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    print('test_timed_draw')
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

def derangements(lst):
    # Create all distinctive permutations
    ders = [] 
    for perm in itertools.permutations(lst):
        if all(ob != perm[idx] for idx, ob in enumerate(lst)):
            ders.append(perm)
    return ders

def create_block_trials():
    # Create equal number of match and mismatch trials
    trials = []
    trials_per_type = N_TRIALS_IN_BLOCK // 2
    
    # Create match trials
    for _ in range(trials_per_type):
        word = random.choice(WORDS)
        trials.append(("match", word, word))
    
    # Create mismatch trials
    for _ in range(trials_per_type):
        word = random.choice(WORDS)
        color = random.choice([c for c in WORDS if c != word])
        trials.append(("mismatch", word, color))
    
    # Shuffle the trials
    random.shuffle(trials)
    return trials

def create_all_trials():
    # Create all possible trials
    blocks = []
    for block_id in range(1, N_BLOCKS + 1):
        block_trials = []
        # Add matching trials (word matches color)
        for word in WORDS:
            block_trials.append({
                "block_id": block_id,
                "trial_id": len(block_trials) + 1,
                "trial_type": "match",
                "word": word,
                "color": word
            })
        # Add mismatching trials (word differs from color)
        for word in WORDS:
            other_colors = [c for c in WORDS if c != word]
            color = random.choice(other_colors)
            block_trials.append({
                "block_id": block_id,
                "trial_id": len(block_trials) + 1,
                "trial_type": "mismatch",
                "word": word,
                "color": color
            })
        block_trials = block_trials * 2
        random.shuffle(block_trials)
        for i, trial in enumerate(block_trials, 1):
            trial["trial_id"] = i
        blocks.append(block_trials)
    return blocks


""" Global settings """
exp = design.Experiment(name="Balanced Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

N_BLOCKS=16
N_TRIALS_IN_BLOCK
PERMS=derangements(WORDS) 

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

""" Experiment """
def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stimuli.TextLine(text=word, text_colour=color)
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait()
    # print('key:', key)
    correct = True if (key == COLOR_KEY_MAPPING[color]) else False
    feedback = feedback_correct if correct else feedback_incorrect
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])
    present_for(feedback, t=1000)


control.start(subject_id=1)

blocks = create_all_trials()

present_instructions(INSTR_START)
for block_id in range(1, N_BLOCKS + 1):
    # Generate and run balanced block trials
    block_trials = create_block_trials()
    for trial_id, (trial_type, word, color) in enumerate(block_trials):
        run_trial(block_id, trial_id, trial_type, word, color)
    
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)
present_instructions(INSTR_END)

control.end()