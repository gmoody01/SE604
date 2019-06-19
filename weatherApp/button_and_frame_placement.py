##############################################################
# From youtube @ https://www.youtube.com/watch?v=D8-snVfekto
# How to Program a GUI Application (with Python Tkinter)!
# Good source for Doc is at:
#   https://www.tutorialspoint.com/python/python_gui_programming.htm
#
##############################################################

import tkinter as tk

HEIGHT = 700
WIDTH = 800


# Tkinter needs a root window
#Everything in the app goes between the above and the root.mainloop() line
root = tk.Tk()

# Create a canvas size, and then pack the geometry into root
# pack manages the geometry of the widgets
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

# Create a frame within the canvas. Rel width is in %
frame = tk.Frame(root, bg = 'blue')
frame.place(relx = 0.05, rely = 0.05, relwidth= 0.9, relheight= 0.9)

# Create a test button in the canvas
button = tk.Button(root, text = "Test button")
button.pack()

# Create a test button inside the frame
button = tk.Button(frame, text = "Test button 2")
button.pack()

# Add an label field in the frame
label = tk.Label(frame, text = "This is a label", bg = 'yellow')
label.pack(side = 'right')

# Add a label that uses an entry in the frame
entry = tk.Entry(frame, bg = 'green')
entry.pack()

root.mainloop()

