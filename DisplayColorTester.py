import tkinter as tk

# MAIN WINDOW
window = tk.Tk()
window.title("Display Color Tester!")
window.geometry("420x420")
window.resizable(True, True)
window.config(background="#323232")


#     Windows


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
    font=("Helvetica", 20, "bold")
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
    font=("Helvetica", 20, "bold")
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
    font=("Helvetica", 20, "bold")
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
    font=("Helvetica", 20, "bold")
)
red_window_button.config(
    activebackground="#FF0000",
    activeforeground="#323232",
    background="#FF0000",
    foreground="#323232"
)
red_window_button.place(
    relx=0.01,
    rely=0.5,
    anchor="w"
)

# Green Window Button
green_window_button = tk.Button(
    window,
    text="Green",
    command=set_green,
    font=("Helvetica", 20, "bold")
)
green_window_button.config(
    activebackground="#00FF00",
    activeforeground="#323232",
    background="#00FF00",
    foreground="#323232"
)
green_window_button.place(
    relx=0.49,
    rely=0.5,
    anchor="center"
)

# Blue Window Button
blue_window_button = tk.Button(
    window,
    text="Blue",
    command=set_blue,
    font=("Helvetica", 20, "bold")
)
blue_window_button.config(
    activebackground="#0000FF",
    activeforeground="#323232",
    background="#0000FF",
    foreground="#323232"
)
blue_window_button.place(
    relx=0.99,
    rely=0.5,
    anchor="e"
)


# Labels


# Version Number Label
version_label = tk.Label(
    window,
    text="v1.0",
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