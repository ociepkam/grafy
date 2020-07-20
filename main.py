import atexit
from psychopy import visual, event, core # , logging
from os.path import join
import csv
import random

from sources.experiment_info import experiment_info
from sources.load_data import load_config, load_trials, replace_polish
from sources.screen import get_screen_res, get_frame_rate
from sources.show_info import show_info, show_image
from sources.trial import trial

part_id, part_sex, part_age, date = experiment_info()
NAME = "{}_{}_{}".format(part_id, part_sex[:1], part_age)
RAND = str(random.randint(100, 999))

RESULTS = list()
RESULTS.append(["ORDER", "NR", 'EXPERIMENT', "FEED",
                "LEFT_ANS", "RIGHT_ANS",
                'LEFT_ACC', "RIGHT_ACC", "ACC",
                "LEFT_RT", "RIGHT_RT", 'RT',
                "VA", "EA", "VB", "EB", "left", "right", "NV", "NE", "Bidirectional", "Type",
                "Crossed_edges", "Block", "A_to_B_relation"])


@atexit.register
def save_beh():
    with open(join('results', '{}_{}.csv'.format(NAME, RAND)), 'w') as f:
        beh_writer = csv.writer(f)
        beh_writer.writerows(RESULTS)


def prepare_result(i, info, answers, rt, acc, exp, A_to_B_relation):
    return [i, info["NR"], exp, info["FEED"],
            # "LEFT_ANS", "RIGHT_ANS",
            answers["left"], answers["right"],
            # 'LEFT_ACC', "RIGHT_ACC", "ACC",
            acc["left"], acc["right"], acc["left"] and acc["right"],
            # "LEFT_RT", "RIGHT_RT", 'RT',
            rt["left"], rt["right"], max(rt["left"], rt["right"]) if rt["left"] and rt["right"] else None,
            # "VA", "EA", "VB", "EB", "left", "right",
            info["VA"], info["EA"], info["VB"], info["EB"], info["left"], info["right"],
            # "NV", "NE" "Bidirectional", "Type",
            info["NV"], info["NE"], info["Bidirectional"], info["Type"],
            info["Crossed_edges"], info["Block"], A_to_B_relation]


config = load_config()
file_name = config['trials']
data_train, data_exp = load_trials(file_name)

SCREEN_RES = get_screen_res()

window = visual.Window(SCREEN_RES, fullscr=True, monitor='testMonitor', units='pix', color='Gainsboro')
FRAMES_PER_SEC = get_frame_rate(window)
mouse = event.Mouse(visible=True)

clock_image = visual.ImageStim(win=window, image=join('images', 'clock.png'), interpolate=True,
                               size=config['CLOCK_SIZE'], pos=config['CLOCK_POS'])

mouse_info = visual.ImageStim(win=window, image=join('images', 'mouse_info.PNG'), interpolate=True,
                               size=130, pos=[-60, -250])

answers_colors = config["answers_colors"]

pos_feedb = visual.TextStim(window, text=replace_polish(config["pos_feedb"]), color='black', height=25, pos=(0, -120))
neg_feedb = visual.TextStim(window, text=replace_polish(config["neg_feedb"]), color='black', height=25, pos=(0, -120))
no_feedb = visual.TextStim(window, text=replace_polish(config["no_feedb"]), color='black', height=25, pos=(0, -120))
feedb = {"pos": pos_feedb, "neg": neg_feedb, "no": no_feedb}

break_time = visual.TextStim(window, text=replace_polish("Masz pół minuty przerwy. Nie odchodź od komputera"),
                          color='black', height=config['TEXT_SIZE'], pos=(0, 0))


# TRAINING
mean_acc = 0
training_nr = 0
while mean_acc < config["min_training_acc"]:

    # INSTRUCTIONS:
    # show_info(window, join('.', 'messages', "instruction1.txt"), text_size=config['TEXT_SIZE'],
    #           screen_width=SCREEN_RES[0], key=config["exit_key"])
    show_image(window, 'instruction1.png', SCREEN_RES, key=config["exit_key"])
    show_image(window, 'instruction2.png', SCREEN_RES, key=config["exit_key"])
    show_image(window, 'instruction3.png', SCREEN_RES, key=config["exit_key"])
    show_image(window, 'instruction4.png', SCREEN_RES, key=config["exit_key"])
    show_image(window, 'instruction5.png', SCREEN_RES, key=config["exit_key"])

    mean_acc = 0
    i = 1
    training_nr += 1
    for info in data_train:
        idx_info = visual.TextStim(window, color='black', pos=(500, 400), height=50,
                                   text=i)
        answers, rt, acc, A_to_B_relation = trial(window, config, answers_colors, info, mouse,
                                 clock_image, feedb, mouse_info, idx_info)

        RESULTS.append(prepare_result(i, info, answers, rt, acc, "train", A_to_B_relation))
        i += 1
        mean_acc += 1 if acc["left"] and acc["right"] else 0
    if i > 1:
        mean_acc /= (i - 1)
    else:
        break
    if mean_acc < config["min_training_acc"] and training_nr == config['max_training_attempts']:
        show_info(window, join('.', 'messages', "end.txt"), text_size=config['TEXT_SIZE'], screen_width=SCREEN_RES[0])
        exit(1)
    if mean_acc < config["min_training_acc"]:
        show_info(window, join('.', 'messages', "training_info.txt"),
                  text_size=config['TEXT_SIZE'], screen_width=SCREEN_RES[0])

# EXPERIMENT
show_info(window, join('.', 'messages', "instruction2.txt"), text_size=config['TEXT_SIZE'],
          screen_width=SCREEN_RES[0], key=config["exit_key"])

i = 1
for c, block in enumerate(data_exp):
    for info in block:
        idx_info = visual.TextStim(window, color='black', pos=(500, 400), height=50,
                                   text=i)
        answers, rt, acc, A_to_B_relation = trial(window, config, answers_colors, info,
                                 mouse, clock_image, feedb, mouse_info, idx_info)
        RESULTS.append(prepare_result(i, info, answers, rt, acc, "exp", A_to_B_relation))
        i += 1

        if i == config['break_after_n_trials']:
            show_info(window, join('.', 'messages', "break.txt"), text_size=config['TEXT_SIZE'] + 25,
                      screen_width=SCREEN_RES[0], key=config["exit_key"], color='green')

    if c + 1 == 3:
        show_info(window, join('.', 'messages', "end.txt"), text_size=config['TEXT_SIZE'], screen_width=SCREEN_RES[0])


