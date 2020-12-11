from tkinter import IntVar, messagebox, END, StringVar
from tkinter.ttk import Separator
from sources.set_config.tkinter_elements import *


def page_1():
    global information, session_type
    information = None
    window = create_window("Set config", 550, 680)
    session_type = IntVar()

    def session():
        if session_type.get() == 1:
            state_list = ["normal", "disabled"]
        elif session_type.get() == 2:
            state_list = ["disabled", "normal"]
        else:
            raise Exception("Problem with session radiobutton")

        for elem in [predefined_test_list, randomize_trials_order, randomize_graphs]:
            elem.configure(state=state_list[0])
        if session_type.get() == 1:
            predefined_test_list.config(state="readonly")

        for elem in [choose_factor_levels, no_of_edges, edges_3, edges_4, edges_5, crossed_edges,
                     graphs_with_crossed, graphs_without_crossed_edges, types_of_target_vertices, direct, mixed,
                     indirect, trials_per_cell_text, trials_per_cell, n_of_trials_text]:
            elem.configure(state=state_list[1])

    def change_n_of_trials(new):
        n_of_trials.configure(state="normal")
        n_of_trials.delete(0, END)
        n_of_trials.insert(0, new)
        n_of_trials.configure(state="disabled")

    def calcutale_n_of_trials():
        if any([edges_3_var.get(), edges_4_var.get(), edges_5_var.get()]) and \
           any([graphs_with_crossed_var.get(), graphs_without_crossed_edges_var.get()]) and \
           any([direct_var.get(), mixed_var.get(), indirect_var.get()]):
            try:
                n = sum([edges_3_var.get(), edges_4_var.get(), edges_5_var.get()]) * \
                    sum([graphs_with_crossed_var.get(), graphs_without_crossed_edges_var.get()]) * \
                    sum([direct_var.get(), mixed_var.get(), indirect_var.get()]) * \
                    int(trials_per_cell.get())
                change_n_of_trials(n)
            except:
                change_n_of_trials("?")
        else:
            change_n_of_trials("?")

    def alerts():
        global information, session_type
        if predefined_training.get() == "":
            messagebox.showerror(message="You have to choose predefined training.")
            return None

        try:
            temp = float(training_accuracy.get())
        except:
            messagebox.showerror(message='Required training accuracy has to be a number')
            return None
        if not 0 <= temp <= 1:
            messagebox.showerror(message='Required training accuracy has to be in range [0, 1]')
            return None

        try:
            temp = int(training_attempts.get())
        except:
            messagebox.showerror(message='Required training accuracy has to be an integer')
            return None
        if temp < 0:
            messagebox.showerror(message='Required training accuracy can\'t be a negative number')
            return None

        if session_type.get() == 1:
            if predefined_test_list.get() == "":
                messagebox.showerror(message="You have to choose predefined test.")
                return None
        elif session_type.get() == 2:
            if not any([edges_3_var.get(), edges_4_var.get(), edges_5_var.get()]):
                messagebox.showerror(message="Choose at least one of \"No. of edges\"")
                return None
            if not any([graphs_with_crossed_var.get(), graphs_without_crossed_edges_var.get()]):
                messagebox.showerror(message="Choose at least on of \"Crossed edges\"")
                return None
            if not any([direct_var.get(), mixed_var.get(), indirect_var.get()]):
                messagebox.showerror(message="Choose at least one of \"Types of target vertices\"")
                return None
            try:
                temp = int(trials_per_cell.get())
            except:
                messagebox.showerror(message='No. of trials per cell has to be an integer')
                return None
            if temp <= 0:
                messagebox.showerror(message='No. of trials per cell has to be a positive number')
                return None
        else:
            messagebox.showerror(message="You have to choose \"Predefined test\" or \"Randomized experiment\".")
            return None

        session_type = "Predefined test" if session_type == 1 else "Randomized experiment"

        information = {
                        # Training
                        "predefined_training": predefined_training.get(),
                        "training_accuracy": float(training_accuracy.get()),
                        "training_attempts": int(training_attempts.get()),
                        "feedback_var": feedback_var.get(),
                        # Session type
                        "session_type": session_type,
                        # Predefined test
                        "predefined_test": predefined_test_list.get(),
                        "randomize_trials_order": randomize_trials_order_var.get(),
                        "randomize_graphs": randomize_graphs_var.get(),
                        # Randomized experiment
                        "no_of_edges": {"3": edges_3_var.get(),
                                        "4": edges_4_var.get(),
                                        "5": edges_5_var.get()},
                        "crossed_edges": {"graphs_with_crossed": graphs_with_crossed_var.get(),
                                          "graphs_without_crossed_edges": graphs_without_crossed_edges_var.get()},
                        "types_of_target_vertices": {"direct": direct_var.get(),
                                                     "mixed": mixed_var.get(),
                                                     "indirect": indirect_var.get()},
                        "trials_per_cell": int(trials_per_cell.get()),
                        "n_of_trials": n_of_trials.get()
                        }

        window.destroy()

    insert_text(text="", column=0, row=0, size=1, win=window)
    insert_text(text="Training session", column=0, row=1, size=14, columnspan=6, win=window)
    insert_text(text="", column=0, row=2, size=1, win=window)
    Separator(window, orient='horizontal').place(x=0, y=40, relwidth=1, height=2)

    insert_text(text="Select predefined training:", column=0, row=3, sticky="W", win=window)
    predefined_training = insert_combobox(column=2, row=3, values=(1, 2, 3), sticky="W", win=window)

    insert_text(text="Required training accuracy:", column=0, row=4, sticky="W", win=window)
    training_accuracy = insert_entry(column=2, row=4, width=5, sticky="W", win=window)

    insert_text(text="Select predefined attempts:", column=0, row=5, sticky="W", win=window)
    training_attempts = insert_entry(column=2, row=5, width=5, sticky="W", win=window)

    insert_text(text="Feedback:", column=0, row=6, sticky="W", win=window)
    feedback, feedback_var = insert_checkbutton(text="", column=2, row=6, sticky="W", win=window)

    # -------------- Experimental session -------------- #

    insert_text(text="", column=0, row=7, size=1, win=window)
    Separator(window, orient='horizontal').place(x=0, y=155, relwidth=1, height=2)
    insert_text(text="Experimental session", column=0, row=8, size=14, columnspan=6, win=window)
    insert_text(text="", column=0, row=9, size=1, win=window)

    Separator(window, orient='horizontal').place(x=0, y=197, relwidth=1, height=2)
    Separator(window, orient='vertical').place(relx=0.5, y=197, width=1, height=420)

    # ---------------- Predefined test ----------------- #
    predefined_test = insert_radiobutton(text="Predefined test", column=0, row=10, selector=session_type,
                                         value=1, size=12, columnspan=3, command=session, win=window)
    insert_text(text="", column=0, row=11, size=1, win=window)
    predefined_test_list = insert_combobox(column=0, row=12, values=(1, 2, 3), columnspan=3, win=window)
    insert_text(text="", column=0, row=13, size=1, win=window)
    randomize_trials_order, randomize_trials_order_var = insert_checkbutton(text="Randomize trials order", columnspan=3,
                                                                            row=14, column=0, sticky="W", win=window)
    randomize_graphs, randomize_graphs_var = insert_checkbutton(text="Randomize graphs", column=0, row=15, columnspan=3,
                                                                sticky="W", win=window)

    # -------------- Randomized experiment ------------- #
    randomized_experiment = insert_radiobutton(text="Randomized experiment", column=3, row=10, selector=session_type,
                                               value=2, size=12, columnspan=3, command=session, win=window)
    choose_factor_levels = insert_text(text="Choose factor levels (max 3x2x3):", column=3, row=12, columnspan=3,
                                       sticky="W", size=12, win=window)

    no_of_edges = insert_text(text="No. of edges:", column=3, row=14, columnspan=3, sticky="W", win=window)
    edges_3, edges_3_var = insert_checkbutton(text="3", column=3, row=15, columnspan=1, sticky="W",
                                              win=window, command=calcutale_n_of_trials)
    edges_4, edges_4_var = insert_checkbutton(text="4", column=3, row=15, columnspan=2, sticky="E",
                                              win=window, command=calcutale_n_of_trials)
    edges_5, edges_5_var = insert_checkbutton(text="5", column=3, row=15, columnspan=3, sticky="E",
                                              win=window, command=calcutale_n_of_trials)

    insert_text(text="", column=0, row=16, size=1, win=window)

    crossed_edges = insert_text(text="Crossed edges:", column=3, row=17, columnspan=3, sticky="W", win=window)
    graphs_with_crossed, graphs_with_crossed_var = insert_checkbutton(text="Graphs with crossed", column=3, row=18,
                                                                      columnspan=3, sticky="W", win=window,
                                                                      command=calcutale_n_of_trials)
    graphs_without_crossed_edges, graphs_without_crossed_edges_var = insert_checkbutton(text="Graphs without crossed edges",
                                                                                        column=3, row=19, columnspan=3,
                                                                                        sticky="W", win=window,
                                                                                        command=calcutale_n_of_trials)

    insert_text(text="", column=0, row=20, size=1, win=window)

    types_of_target_vertices = insert_text(text="Types of target vertices:", column=3, row=21,
                                           columnspan=3, sticky="W", win=window)
    direct, direct_var = insert_checkbutton(text="Direct", column=3, row=22, columnspan=3, sticky="W",
                                            win=window, command=calcutale_n_of_trials)
    mixed, mixed_var = insert_checkbutton(text="Mixed", column=3, row=23, columnspan=3, sticky="W",
                                          win=window, command=calcutale_n_of_trials)
    indirect, indirect_var = insert_checkbutton(text="Indirect", column=3, row=24, columnspan=3, sticky="W",
                                                win=window, command=calcutale_n_of_trials)

    insert_text(text="", column=0, row=25, size=1, win=window)

    trials_per_cell_text = insert_text(text="No. of trials per cell:", column=3, row=26,
                                       columnspan=2, sticky="W", win=window)
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: calcutale_n_of_trials())
    trials_per_cell = insert_entry(column=5, row=26, width=5, columnspan=1, sticky="W", win=window, textvariable=sv)

    n_of_trials_text = insert_text(text="Total n of trials:", column=3, row=27, columnspan=2, sticky="W", win=window)
    n_of_trials = insert_entry(column=5, row=27, width=5, columnspan=1, sticky="W", win=window)
    change_n_of_trials("?")

    Separator(window, orient='horizontal').place(x=0, y=617, relwidth=1, height=2)

    # --------- Experimental session disabled ---------- #
    for elem in [predefined_test_list, randomize_trials_order, randomize_graphs, choose_factor_levels, no_of_edges,
                 edges_3, edges_4, edges_5, crossed_edges, graphs_with_crossed,
                 graphs_without_crossed_edges, types_of_target_vertices, direct, mixed, indirect,
                 trials_per_cell_text, trials_per_cell, n_of_trials_text, n_of_trials]:
        elem.configure(state="disabled")

    insert_text(text="", column=0, row=29, size=12, win=window)
    next_page = insert_button(text="  Next  ", column=3, row=30, command=alerts, size=12,
                              win=window, columnspan=1, sticky="W")
    window.mainloop()

    return information
