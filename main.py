import atexit
from psychopy import visual, event  # , logging
from os.path import join
import csv
import random

from sources.experiment_info import experiment_info
from sources.load_data import load_config, load_trials, replace_polish
from sources.screen import get_screen_res, get_frame_rate
from sources.show_info import show_info
from sources.trail import trial

part_id, part_sex, part_age, date = experiment_info()
NAME = "{}_{}_{}".format(part_id, part_sex[:1], part_age)
RAND = str(random.randint(100, 999))
# logging.LogFile(join('.', 'results', 'logging', NAME + '_' + RAND + '.log'), level=logging.INFO)

RESULTS = list()
RESULTS.append(['IDX', "NR", 'EXPERIMENTAL', "FEED",
                "LEFT_ANS", "RIGHT_ANS",
                'LEFT_ACC', "RIGHT_ACC", "ACC",
                "LEFT_RT", "RIGHT_RT", 'RT',
                "VA", "KA", "VB", "KB", "left", "right", "NV", "NK", "Dwustronna", "TYP", "Koment"])


@atexit.register
def save_beh():
    # logging.flush()
    with open(join('results', 'behavioral', 'beh_{}_{}.csv'.format(NAME, RAND)), 'w') as f:
        beh_writer = csv.writer(f)
        beh_writer.writerows(RESULTS)


def prepare_result(i, info, answers, rt, acc, exp):
    #      'IDX', "NR"  'EXPERIMENTAL', "FEED",
    return [i, info["NR"], exp, info["FEED"],
            # "LEFT_ANS", "RIGHT_ANS",
            answers["left"], answers["right"],
            # 'LEFT_ACC', "RIGHT_ACC", "ACC",
            acc["left"], acc["right"], acc["left"] and acc["right"],
            # "LEFT_RT", "RIGHT_RT", 'RT',
            rt["left"], rt["right"], max(rt["left"], rt["right"]) if rt["left"] and rt["right"] else None,
            # "VA", "KA", "VB", "KB", "left", "right",
            info["VA"], info["KA"], info["VB"], info["KB"], info["left"], info["right"],
            # "NV", "NK" "Dwustronna", "TYP", "Koment"
            info["NV"], info["NK"], info["Dwustronna"], info["TYP"], info["Koment"]]


config = load_config()
data_train, data_exp = load_trials()
if config["train_trials_randomize"]:
    random.shuffle(data_train)
if config["exp_trials_randomize"]:
    random.shuffle(data_exp)

SCREEN_RES = get_screen_res()
window = visual.Window(SCREEN_RES, fullscr=True, monitor='testMonitor', units='pix', color='Gainsboro')
FRAMES_PER_SEC = get_frame_rate(window)
mouse = event.Mouse(visible=True)

clock_image = visual.ImageStim(win=window, image=join('images', 'clock.png'), interpolate=True,
                               size=config['CLOCK_SIZE'], pos=config['CLOCK_POS'])

answers_colors = random.sample(config["answers_colors"], 2) if config["randomize_answers_colors"] \
    else config["answers_colors"]

pos_feedb = visual.TextStim(window, text=replace_polish(config["pos_feedb"]), color='black', height=40, pos=(0, -200))
neg_feedb = visual.TextStim(window, text=replace_polish(config["neg_feedb"]), color='black', height=40, pos=(0, -200))
no_feedb = visual.TextStim(window, text=replace_polish(config["no_feedb"]), color='black', height=40, pos=(0, -200))
feedb = {"pos": pos_feedb, "neg": neg_feedb, "no": no_feedb}

# TRAINING
mean_acc = 0
while mean_acc < config["min_training_acc"]:
    show_info(window, join('.', 'messages', "instruction1.txt"), text_size=config['TEXT_SIZE'],
              screen_width=SCREEN_RES[0], key=config["exit_key"])
    # show_image(window, 'instruction.png', SCREEN_RES, , key=config["exit_key"])
    mean_acc = 0
    i = 1
    for info in data_train:
        answers, rt, acc = trial(window, config, answers_colors, info, mouse, clock_image, feedb)

        RESULTS.append(prepare_result(i, info, answers, rt, acc, "train"))
        i += 1
        mean_acc += 1 if acc["left"] and acc["right"] else 0
    if i > 1:
        mean_acc /= (i - 1)
    else:
        break

# EXPERIMENT
show_info(window, join('.', 'messages', "instruction2.txt"), text_size=config['TEXT_SIZE'],
          screen_width=SCREEN_RES[0], key=config["exit_key"])

i = 1
for info in data_exp:
    answers, rt, acc = trial(window, config, answers_colors, info, mouse, clock_image, feedb)
    RESULTS.append(prepare_result(i, info, answers, rt, acc, "exp"))
    i += 1

show_info(window, join('.', 'messages', "end.txt"), text_size=config['TEXT_SIZE'],
          screen_width=SCREEN_RES[0], key=config["exit_key"])
