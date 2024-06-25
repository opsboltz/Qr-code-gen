import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("1000x600")
root.title("Image Drawing Tool")
root.config(bg="white")

# Creating the left frame
left_frame = tk.Frame(root, width=200, height=600, bg="#808080")  # Hex color for grey
left_frame.pack(side="left", fill="y")

# Creating the canvas
canvas = tk.Canvas(root, width=750, height=600, bg="white")  # Hex color for white
canvas.pack(side="left")

# Creating the entry widget inside the canvas
url_entry = tk.Entry(left_frame)
url_entry.pack(pady=240, padx=50)

# Creating the submit button inside the left frame
submit_button = tk.Button(left_frame, text="Submit", bg="#FF9797")
submit_button.pack(pady=0, padx=50)

root.mainloop()
