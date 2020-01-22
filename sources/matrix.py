from psychopy import visual
from sources.arrow import Arrow


class Matrix:
    def __init__(self, win, pos, config, v, e, answers):
        self.v = []
        self.k = []
        self.pos = pos
        self.answers = answers
        for elem in v:
            point = visual.Circle(win, radius=config["v_size"], lineColor=config["v_color"],
                                  fillColor=config["v_color"], pos=self.set_pos(pos, elem, config))
            self.v.append([elem, point])
        for elem in e:
            arrow = Arrow(win=win, color=config["arrow_color"],
                          arrow_length=config["arrow_length"],
                          arrow_width=config["arrow_width"],
                          start=self.set_pos(pos, elem[0], config),
                          end=self.set_pos(pos, elem[1], config),
                          shorter=config["arrow_shorter"])
            self.k.append(arrow)

    def set_auto_draw(self, log):
        for v in self.v:
            v[1].setAutoDraw(log)
        for k in self.k:
            k.setAutoDraw(log)

    @staticmethod
    def set_pos(pos, i, config):
        x = pos[0]
        y = pos[1]
        if i in [0, 3, 6]:
            x -= config["FIG_OFFSET"]
        elif i in [2, 5, 8]:
            x += config["FIG_OFFSET"]
        if i in [0, 1, 2]:
            y += config["FIG_OFFSET"]
        elif i in [6, 7, 8]:
            y -= config["FIG_OFFSET"]
        return [x, y]

    def mark_answer(self, v_nr, color):
        for elem in self.v:
            if elem[0] == v_nr:
                elem[1].color = color
