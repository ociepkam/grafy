import time
from psychopy import event, core, visual

from sources.matrix import Matrix
from sources.check_exit import check_exit


def trial(window, config, answers_colors, info, mouse, clock_image, feedb, mouse_info, idx_info):
    response_clock = core.Clock()

    a = Matrix(win=window, pos=config["MATRIX_1_POS"], config=config, v=info["VA"], k=info["KA"], answers=None)
    a.mark_answer(v_nr=info["left"][0], color=answers_colors[0])
    a.mark_answer(v_nr=info["right"][0], color=answers_colors[1])
    b = Matrix(win=window, pos=config["MATRIX_2_POS"], config=config, v=info["VB"], k=info["KB"], answers=None)
    press_space_msg = visual.TextStim(window, text=u'Przyci\u015Bnij spacje', color='red', height=25, pos=(0, -400))
    a.set_auto_draw(True)
    b.set_auto_draw(True)
    window.callOnFlip(response_clock.reset)
    event.clearEvents()
    mouse_info.setAutoDraw(True)
    if config["show_idx"]:
        idx_info.setAutoDraw(True)
    window.flip()

    click = {"left": False, "right": False}
    answers = {"left": None, "right": None}
    rt = {"left": None, "right": None}
    while response_clock.getTime() < config["trial_time"] and not (click["left"] and click["right"]):
        for idx, point in b.v:
            if not click["left"] and mouse.isPressedIn(point, buttons=[0]):
                rt["left"] = response_clock.getTime()
                b.mark_answer(idx, color=answers_colors[0])
                window.flip()
                time.sleep(config["click_show_time"])
                b.mark_answer(idx, color=config["v_color"])
                window.flip()
                click["left"] = True
                answers["left"] = idx
            elif not click["right"] and mouse.isPressedIn(point, buttons=[2]):
                rt["right"] = response_clock.getTime()
                b.mark_answer(idx, color=answers_colors[1])
                window.flip()
                time.sleep(config["click_show_time"])
                b.mark_answer(idx, color=config["v_color"])
                window.flip()
                click["right"] = True
                answers["right"] = idx
        if config["trial_time"] - response_clock.getTime() < config['SHOW_CLOCK']:
            clock_image.setAutoDraw(True)
        check_exit()
        window.flip()
    clock_image.setAutoDraw(False)

    acc = {"left": answers["left"] == info["left"][1], "right": answers["right"] == info["right"][1]}

    if info["FEED"]:
        b.mark_answer(info["left"][1], color=answers_colors[0])
        b.mark_answer(info["right"][1], color=answers_colors[1])
        if not click["left"] or not click["right"]:
            feedb["no"].setAutoDraw(True)
        elif acc["left"] and acc["right"]:
            feedb["pos"].setAutoDraw(True)
        else:
            feedb["neg"].setAutoDraw(True)
        window.flip()

        if config["feedback_time"] > 0:
            time.sleep(config["feedback_time"])
        elif config["feedback_time"] == -1:
            press_space_msg.setAutoDraw(True)
            window.flip()
            event.waitKeys(keyList=['f7', 'space'])

    a.set_auto_draw(False)
    b.set_auto_draw(False)
    mouse_info.setAutoDraw(False)
    idx_info.setAutoDraw(False)
    press_space_msg.setAutoDraw(False)
    for k, v in feedb.items():
        v.setAutoDraw(False)

    window.flip()
    time.sleep(config["wait_time"])


    return answers, rt, acc
