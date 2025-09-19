import tkinter as tk
from functions import (
    window,
    set_black,
    set_grey,
    set_white,
    set_red,
    set_green,
    set_blue,
    set_yellow,
    set_pink,
    set_cyan
)


#     Buttons


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

# Black Window Button
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

# Grey Window Button
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

# White Window Button
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

# Red Window Button
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

# Green Window Button
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

# Blue Window Button
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

# Yellow Window Button
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

# Pink Window Button
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

# Cyan Window Button
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


# Labels


# Version Number Label
version_label = tk.Label(
    window,
    text="v1.1",
    font=("Helvetica", 14, "bold")
)
version_label.config(
    background="#323232",
    foreground="#4E0096",
)
version_label.place(
    relx=0.01,
    rely=0.99,
    anchor="sw"
)

# START PROGRAM
window.mainloop()