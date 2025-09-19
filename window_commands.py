import tkinter as tk

# MAIN MENU WINDOW
window = tk.Tk()
window.title("Display Color Tester!")
window.geometry("420x420")
window.resizable(False, False)
window.config(background="#323232")


# Black Window
def set_black():
    black_window = tk.Toplevel(window)
    black_window.title("The Color Black!")
    black_window.geometry("1280x720")
    black_window.resizable(True, True)
    black_window.configure(background="#000000")
    return


# Grey Window
def set_grey():
    grey_window = tk.Toplevel(window)
    grey_window.title("The Color Grey!")
    grey_window.geometry("1280x720")
    grey_window.resizable(True, True)
    grey_window.configure(background="#7F7F7F")


# White Window
def set_white():
    white_window = tk.Toplevel(window)
    white_window.title("The Color White!")
    white_window.geometry("1280x720")
    white_window.resizable(True, True)
    white_window.configure(background="#FFFFFF")
    return


# Red Window
def set_red():
    red_window = tk.Toplevel(window)
    red_window.title("The Color Red!")
    red_window.geometry("1280x720")
    red_window.resizable(True, True)
    red_window.configure(background="#FF0000")
    return


# Green Window
def set_green():
    green_window = tk.Toplevel(window)
    green_window.title("The Color Green!")
    green_window.geometry("1280x720")
    green_window.resizable(True, True)
    green_window.configure(background="#00FF00")
    return


# Blue Window
def set_blue():
    blue_window = tk.Toplevel(window)
    blue_window.title("The Color Blue!")
    blue_window.geometry("1280x720")
    blue_window.resizable(True, True)
    blue_window.configure(background="#0000FF")
    return


# Yellow Window
def set_yellow():
    yellow_window = tk.Toplevel(window)
    yellow_window.title("The Color Yellow!")
    yellow_window.geometry("1280x720")
    yellow_window.resizable(True, True)
    yellow_window.configure(background="#FFFF00")
    return


# Pink Window
def set_pink():
    pink_window = tk.Toplevel(window)
    pink_window.title("The Color Pink!")
    pink_window.geometry("1280x720")
    pink_window.resizable(True, True)
    pink_window.configure(background="#FF00FF")
    return


# Cyan Window
def set_cyan():
    cyan_window = tk.Toplevel(window)
    cyan_window.title("The Color Cyan!")
    cyan_window.geometry("1280x720")
    cyan_window.resizable(True, True)
    cyan_window.configure(background="#00FFFF")
    return