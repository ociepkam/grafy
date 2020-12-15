from tkinter import messagebox


def show_on_off(elements, checkbutton_var, states):
    state = states[checkbutton_var.get()]
    for elem in elements:
        elem.configure(state=state)


def try_convert_to_float(value, text):
    try:
        return float(value)
    except ValueError:
        messagebox.showerror(message='{} has to be a number'.format(text))
        return None


def try_convert_to_int(value, text):
    try:
        return int(value)
    except ValueError:
        messagebox.showerror(message='{} has to be an integer'.format(text))
        return None


def try_in_range(value, text, v_min=None, v_max=None):
    if v_min is not None and value <= v_min:
        messagebox.showerror(message="{} can't be lower than {}".format(text, v_min))
        return False
    if v_max is not None and value >= v_max:
        messagebox.showerror(message="{} can't be higher than {}".format(text, v_max))
        return False
    return True


def try_combobox(value, text):
    if value.get() == "":
        messagebox.showerror(message="You have to choose {}.".format(text))
        return False
    return True


def try_button_color(button, origin, text):
    if button["background"] == origin:
        messagebox.showerror(message="You have to choose {} background color".format(text))
        return False
    return True
