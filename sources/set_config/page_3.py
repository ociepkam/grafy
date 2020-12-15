from tkinter.ttk import Separator
from sources.set_config.tkinter_elements import *
from sources.set_config.utils import *
from sources.set_config.alerts import *


def page_3():
    def choose_background_color():
        return choose_button_color(background_button_color, title="Choose background color")

    def choose_vertices_color():
        return choose_button_color(vertices_button_color, title="Choose vertices color")

    def choose_edges_color():
        return choose_button_color(edges_button_color, title="Choose edges color")

    def alerts():
        global information
        # ------------------ Visual ------------------ #
        if not try_button_color(background_button_color, orig_button_background, "background color"):
            return None
        txt_size = try_convert_to_int(text_size.get(), "Text size")
        if not try_in_range(txt_size, "Text size", v_min=0):
            return None
        if not try_button_color(edges_button_color, orig_button_background, "edges color"):
            return None

        l_graph_position_x = try_convert_to_int(left_graph_position_x.get(), "Left graph x position")
        if l_graph_position_x is None:
            return None
        l_graph_position_y = try_convert_to_int(left_graph_position_y.get(), "Left graph y position")
        if l_graph_position_y is None:
            return None

        r_graph_position_x = try_convert_to_int(right_graph_position_x.get(), "Right graph x position")
        if r_graph_position_x is None:
            return None
        r_graph_position_y = try_convert_to_int(right_graph_position_y.get(), "Right graph y position")
        if r_graph_position_y is None:
            return None

        v_size = try_convert_to_int(vertices_size.get(), "Vertices size")
        if not try_in_range(v_size, "Vertices size", v_min=0):
            return None

        v_distance = try_convert_to_int(vertices_distance.get(), "Distance between vertices")
        if not try_in_range(v_distance, "Distance between vertices", v_min=0):
            return None

        e_v_gap = try_convert_to_int(gap_between_edges_and_vertices.get(), "Gap between edges and vertices")
        if not try_in_range(e_v_gap, "Gap between edges and vertices", v_min=0):
            return None

        a_length = try_convert_to_int(arrowhead_length.get(), "Arrowhead length")
        if not try_in_range(a_length, "Arrowhead length", v_min=0):
            return None

        a_width = try_convert_to_int(arrowhead_width.get(), "Arrowhead width")
        if not try_in_range(a_width, "Arrowhead width", v_min=0):
            return None

        # ------------------ Other ------------------- #
        b_n_trails = try_convert_to_int(break_after_n_trials.get(), "Provide break after n trials")
        if not try_in_range(b_n_trails, "Provide break after n trials", v_min=0):
            return None

        information = {
            # Feedback text
            "correct_answer": correct_answer.get(),
            "incorrect_answer": incorrect_answer.get(),
            "no_answer": no_answer.get(),
            "press_space_message": press_space_message.get(),
            # Visual
            "background_color": background_button_color["background"],
            "text_size": txt_size.get(),
            "vertices_color": vertices_button_color["background"],
            "edges_color": edges_button_color["background"],
            "left_graph_position": [l_graph_position_x, l_graph_position_y],
            "right_graph_position": [r_graph_position_x, r_graph_position_y],
            "vertices_size": v_size,
            "vertices_distance": v_distance,
            "gap_between_edges_and_vertices": e_v_gap,
            "arrowhead_length": a_length,
            "arrowhead_width": a_width,
            # Other
            "break_after_n_trials": b_n_trails,
            "exit_key": exit_key
        }

        window.destroy()

    global information
    information = None

    window = create_window("Set config", 550, 680)

    # -------------- Feedback text --------------- #

    insert_text(text="", column=5, row=0, size=1, win=window)
    insert_text(text="Feedback text", column=0, row=1, size=14, columnspan=6, win=window)

    insert_text(text="Correct answer:", column=0, row=3, columnspan=6, win=window, sticky="W")
    correct_answer = insert_entry(column=0, row=4, width=5, sticky="EW", win=window, columnspan=6)

    insert_text(text="Incorrect answer:", column=0, row=5, columnspan=6, win=window, sticky="W")
    incorrect_answer = insert_entry(column=0, row=6, width=5, sticky="EW", win=window, columnspan=6)

    insert_text(text="No answer:", column=0, row=7, columnspan=6, win=window, sticky="W")
    no_answer = insert_entry(column=0, row=8, width=5, sticky="EW", win=window, columnspan=6)

    insert_text(text="Press space message:", column=0, row=9, columnspan=6, win=window, sticky="W")
    press_space_message = insert_entry(column=0, row=10, width=5, sticky="EW", win=window, columnspan=6)

    # ------------------ Visual ------------------ #
    insert_text(text="Visual", column=0, row=11, columnspan=6, win=window, size=14)

    insert_text(text="Background:", column=0, row=12, columnspan=6, win=window, sticky="W")
    background_button_color = insert_button(text="Choose color", column=0, row=12, command=choose_background_color,
                                            size=12, win=window, columnspan=6)

    insert_text(text="Text size (px):", column=0, row=13, columnspan=2, win=window, sticky="W")
    text_size = insert_entry(column=2, row=13, width=5, sticky="E", win=window, columnspan=1)

    insert_text(text="Vertices color:", column=0, row=14, columnspan=6, win=window, sticky="W")
    vertices_button_color = insert_button(text="Choose color", column=0, row=14, command=choose_vertices_color,
                                          size=12, win=window, columnspan=6)

    insert_text(text="Edges color:", column=0, row=15, columnspan=6, win=window, sticky="W")
    edges_button_color = insert_button(text="Choose color", column=0, row=15, command=choose_edges_color,
                                       size=12, win=window, columnspan=6)

    insert_text(text="x:", column=2, row=16, win=window, sticky="W", columnspan=1)
    left_graph_position_x = insert_entry(column=2, row=16, width=5, sticky="E", win=window, columnspan=1)
    insert_text(text="y:", column=3, row=16, win=window, sticky="W", columnspan=1)
    left_graph_position_y = insert_entry(column=3, row=16, width=5, sticky="E", win=window, columnspan=1)
    insert_text(text="Left graph position:", column=0, row=16, columnspan=6, win=window, sticky="W")

    insert_text(text="x:", column=2, row=17, win=window, sticky="W", columnspan=1)
    right_graph_position_x = insert_entry(column=2, row=17, width=5, sticky="E", win=window, columnspan=1)
    insert_text(text="y:", column=3, row=17, win=window, sticky="W", columnspan=1)
    right_graph_position_y = insert_entry(column=3, row=17, width=5, sticky="E", win=window, columnspan=1)
    insert_text(text="Right graph position:    ", column=0, row=17, columnspan=6, win=window, sticky="W")

    insert_text(text="Vertices size:", column=0, row=18, columnspan=6, win=window, sticky="W")
    vertices_size = insert_entry(column=2, row=18, width=5, sticky="E", win=window, columnspan=1)

    insert_text(text="Distance between vertices:", column=0, row=19, columnspan=6, win=window, sticky="W")
    vertices_distance = insert_entry(column=2, row=19, width=5, sticky="E", win=window, columnspan=1)

    insert_text(text="Gap between edges and vertices:", column=0, row=20, columnspan=6, win=window, sticky="W")
    gap_between_edges_and_vertices = insert_entry(column=2, row=20, width=5, sticky="E", win=window, columnspan=1)

    insert_text(text="Arrowhead length:", column=0, row=21, columnspan=6, win=window, sticky="W")
    arrowhead_length = insert_entry(column=2, row=21, width=5, sticky="E", win=window, columnspan=1)

    insert_text(text="Arrowhead width:", column=0, row=22, columnspan=6, win=window, sticky="W")
    arrowhead_width = insert_entry(column=2, row=22, width=5, sticky="E", win=window, columnspan=1)

    # ------------------ Other ------------------- #
    insert_text(text="Other", column=0, row=23, columnspan=6, win=window, size=14)

    insert_text(text="Provide break after n trials:", column=0, row=24, columnspan=6, win=window, sticky="W")
    break_after_n_trials = insert_entry(column=2, row=24, width=5, sticky="E", win=window, columnspan=1)

    insert_text(text="Exit key:", column=0, row=25, columnspan=6, win=window, sticky="W")
    exit_key = insert_entry(column=2, row=25, width=5, sticky="E", win=window, columnspan=1)

    save_button = insert_button(text="  Save  ", column=0, row=30, command=alerts, size=12, win=window, columnspan=6)
    orig_button_background = save_button['background']

    window.mainloop()
    return information