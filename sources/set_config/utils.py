from tkinter import colorchooser


def show_on_off(elements, checkbutton_var, states):
    state = states[checkbutton_var.get()]
    for elem in elements:
        elem.configure(state=state)


def choose_button_color(button, title):
    color_code = colorchooser.askcolor(title=title)
    button['background'] = color_code[1]
    if sum(color_code[0]) < 100:
        button['foreground'] = 'white'
    else:
        button['foreground'] = 'black'
    return color_code[1]
