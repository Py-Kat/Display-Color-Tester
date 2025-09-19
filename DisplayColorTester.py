import tkinter as tk
import _tkinter


# MAIN WINDOW
window = tk.Tk()
window.title("Display Color Tester!")
window.geometry("420x420")
window.resizable(False, False)
window.config(background="#323232")


#     Default Window Buttons


# Black Window
def set_black():
    black_window = tk.Toplevel(window)
    black_window.title("#000000")
    black_window.geometry("1280x720")
    black_window.resizable(True, True)
    black_window.configure(background="#000000")
    return

black_window_button = tk.Button(
    window,
    text="Black",
    command=set_black,
    font=("Helvetica", 22, "bold")
)
black_window_button.config(
    activebackground="#000000",
    activeforeground="#323232",
    background="#000000",
    foreground="#323232"
)
black_window_button.place(
    relx=0.01,
    rely=0.01,
    anchor="nw"
)


# Grey Window
def set_grey():
    grey_window = tk.Toplevel(window)
    grey_window.title("#7F7F7F")
    grey_window.geometry("1280x720")
    grey_window.resizable(True, True)
    grey_window.configure(background="#7F7F7F")
    return

grey_window_button = tk.Button(
    window,
    text="Grey",
    command=set_grey,
    font=("Helvetica", 22, "bold")
)
grey_window_button.config(
    activebackground="#7F7F7F",
    activeforeground="#323232",
    background="#7F7F7F",
    foreground="#323232"
)
grey_window_button.place(
    relx=0.5,
    rely=0.01,
    anchor="n"
)


# White Window
def set_white():
    white_window = tk.Toplevel(window)
    white_window.title("#FFFFFF")
    white_window.geometry("1280x720")
    white_window.resizable(True, True)
    white_window.configure(background="#FFFFFF")
    return

white_window_button = tk.Button(
    window,
    text="White",
    command=set_white,
    font=("Helvetica", 22, "bold")
)
white_window_button.config(
    activebackground="#FFFFFF",
    activeforeground="#323232",
    background="#FFFFFF",
    foreground="#323232"
)
white_window_button.place(
    relx=0.99,
    rely=0.01,
    anchor="ne"
)


# Red Window
def set_red():
    red_window = tk.Toplevel(window)
    red_window.title("#FF0000")
    red_window.geometry("1280x720")
    red_window.resizable(True, True)
    red_window.configure(background="#FF0000")
    return

red_window_button = tk.Button(
    window,
    text="Red",
    command=set_red,
    font=("Helvetica", 22, "bold")
)
red_window_button.config(
    activebackground="#FF0000",
    activeforeground="#323232",
    background="#FF0000",
    foreground="#323232"
)
red_window_button.place(
    relx=0.01,
    rely=0.25,
    anchor="w"
)


# Green Window
def set_green():
    green_window = tk.Toplevel(window)
    green_window.title("#00FF00")
    green_window.geometry("1280x720")
    green_window.resizable(True, True)
    green_window.configure(background="#00FF00")
    return

green_window_button = tk.Button(
    window,
    text="Green",
    command=set_green,
    font=("Helvetica", 22, "bold")
)
green_window_button.config(
    activebackground="#00FF00",
    activeforeground="#323232",
    background="#00FF00",
    foreground="#323232"
)
green_window_button.place(
    relx=0.5,
    rely=0.25,
    anchor="center"
)


# Blue Window
def set_blue():
    blue_window = tk.Toplevel(window)
    blue_window.title("#0000FF")
    blue_window.geometry("1280x720")
    blue_window.resizable(True, True)
    blue_window.configure(background="#0000FF")
    return

blue_window_button = tk.Button(
    window,
    text="Blue",
    command=set_blue,
    font=("Helvetica", 22, "bold")
)
blue_window_button.config(
    activebackground="#0000FF",
    activeforeground="#323232",
    background="#0000FF",
    foreground="#323232"
)
blue_window_button.place(
    relx=0.99,
    rely=0.25,
    anchor="e"
)


# Yellow Window
def set_yellow():
    yellow_window = tk.Toplevel(window)
    yellow_window.title("#FFFF00")
    yellow_window.geometry("1280x720")
    yellow_window.resizable(True, True)
    yellow_window.configure(background="#FFFF00")
    return

yellow_window_button = tk.Button(
    window,
    text="Yellow",
    command=set_yellow,
    font=("Helvetica", 22, "bold")
)
yellow_window_button.config(
    activebackground="#FFFF00",
    activeforeground="#323232",
    background="#FFFF00",
    foreground="#323232"
)
yellow_window_button.place(
    relx=0.01,
    rely=0.42,
    anchor="w"
)


# Pink Window
def set_pink():
    pink_window = tk.Toplevel(window)
    pink_window.title("#FF00FF")
    pink_window.geometry("1280x720")
    pink_window.resizable(True, True)
    pink_window.configure(background="#FF00FF")
    return

pink_window_button = tk.Button(
    window,
    text="Pink",
    command=set_pink,
    font=("Helvetica", 22, "bold")
)
pink_window_button.config(
    activebackground="#FF00FF",
    activeforeground="#323232",
    background="#FF00FF",
    foreground="#323232"
)
pink_window_button.place(
    relx=0.5,
    rely=0.42,
    anchor="center"
)


# Cyan Window
def set_cyan():
    cyan_window = tk.Toplevel(window)
    cyan_window.title("#00FFFF")
    cyan_window.geometry("1280x720")
    cyan_window.resizable(True, True)
    cyan_window.configure(background="#00FFFF")
    return


cyan_window_button = tk.Button(
    window,
    text="Cyan",
    command=set_cyan,
    font=("Helvetica", 22, "bold")
)
cyan_window_button.config(
    activebackground="#00FFFF",
    activeforeground="#323232",
    background="#00FFFF",
    foreground="#323232"
)
cyan_window_button.place(
    relx=0.99,
    rely=0.42,
    anchor="e"
)


# Close
close_button = tk.Button(
    window,
    text="Close",
    command=window.destroy,
    font=("Helvetica", 10, "bold")
)
close_button.config(
    activebackground="#FF0000",
    activeforeground="#7F7F7F",
    background="#7F7F7F",
    foreground="#FF0000"
)
close_button.place(
    relx=0.99,
    rely=0.99,
    anchor="se"
)


# Custom Colored Window
def custom_color():
    user_color = color_input.get()
    custom_window = tk.Toplevel(window)
    custom_window.geometry("1280x720")
    custom_window.resizable(True, True)
    try:
        custom_window.title(f"#{user_color}")
        custom_window.configure(background=f"#{user_color}")
    except _tkinter.TclError:
        custom_window.title("No Color Was Chosen!")
        custom_window.configure(background=f"#000000")
        no_color_label = tk.Label(
            custom_window,
            text="Please input a HEX VALUE!",
            font=("Helvetica", 40, "bold")
        )
        no_color_label.config(
            background="#000000",
            foreground="#FF0000"
        )
        no_color_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
    return


custom_window_button = tk.Button(
    window,
    text="Open",
    command=custom_color,
    font=("Helvetica", 12, "bold")
)
custom_window_button.config(
    activebackground="#7F7F7F",
    activeforeground="#323232",
    background="#7F7F7F",
    foreground="#323232"
)
custom_window_button.place(
    relx=0.5,
    rely=0.85,
    anchor="s"
)


#     Labels


# Version Number
version_label = tk.Label(
    window,
    text="v1.1",
    font=("Helvetica", 14, "bold")
)
version_label.config(
    background="#323232",
    foreground="#4E0096"
)
version_label.place(
    relx=0.01,
    rely=0.99,
    anchor="sw"
)


# Custom Input
custom_input_label = tk.Label(
    window,
    text="Custom Color",
    font=("Helvetica", 14, "bold")
)
custom_input_label.config(
    background="#323232",
    foreground="#000000"
)
custom_input_label.place(
    relx=0.5,
    rely=0.68,
    anchor="s"
)


# Hex Indicator
hashtag_label = tk.Label(
    window,
    text="#",
    font=("Helvetica", 14, "bold")
)
hashtag_label.config(
    background="#323232",
    foreground="#000000"
)
hashtag_label.place(
    relx=0.375,
    rely=0.75,
    anchor="s"
)


#     Entries


color_input = tk.Entry(
    window,
    width=7,
    font=("Helvetica", 14, "bold")
)
color_input.place(
    relx=0.5,
    rely=0.75,
    anchor="s"
)

# START PROGRAM
window.mainloop()