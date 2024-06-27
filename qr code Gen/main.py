import tkinter as tk
from tkinter import colorchooser
import qrcode
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1000x600")
root.title("Image Drawing Tool")
root.config(bg="white")

selected_color = "#000000"  # Default color
selected_size = 10  # Default size


def generate_qr():
    global img
    global selected_color, selected_size
    # Getting the URL entered
    url = url_entry.get()
    # Generate the QR code image
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=selected_size,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color=selected_color, back_color="white")

    # Convert PIL image to Tkinter PhotoImage
    img = ImageTk.PhotoImage(qr_image)

    # Clear the canvas
    canvas.delete("all")
    # Place the image on the canvas
    canvas.create_image(375, 300, image=img, anchor=tk.CENTER)


def choose_color():
    global selected_color
    # Open the color chooser dialog
    color_code = colorchooser.askcolor(title="Choose QR Code Color")
    # Get the selected color
    selected_color = color_code[1] if color_code else "#000000"
    # Generate the QR code again with the new color
    generate_qr()


def update_size(entry):
    global selected_size
    try:
        selected_size = int(entry)
        generate_qr()
        return True  # Validation successful
    except ValueError:
        return False  # Validation failed


# Creating the left frame
left_frame = tk.Frame(root, width=200, height=600, bg="#808080")  # Hex color for grey
left_frame.pack(side="left", fill="y")

# Creating a container frame for input widgets
input_frame = tk.Frame(left_frame, bg="#808080")
input_frame.pack(expand=True, pady=50)

# URL Entry in Container Frame
url_label = tk.Label(input_frame, text="URL", bg="#808080", fg="white", font=("Arial", 12))
url_label.grid(row=0, column=0, pady=10)
url_entry = tk.Entry(input_frame)
url_entry.grid(row=1, column=0, padx=10, pady=10)

# Color Chooser in Container Frame
color_button = tk.Button(input_frame, text="Choose Color", bg="#FF9797", command=choose_color)
color_button.grid(row=2, column=0, padx=10, pady=10)

# Size Entry in Container Frame
size_label = tk.Label(input_frame, text="Size", bg="#808080", fg="white", font=("Arial", 12))
size_label.grid(row=3, column=0, pady=10)
size_entry = tk.Entry(input_frame, validate="key")
size_entry.grid(row=4, column=0, padx=10, pady=10)
size_entry.insert(0, selected_size)  # Set default value
size_entry.config(validatecommand=(size_entry.register(update_size), "%P"))  # %P passes the new value in entry

# Submit Button in Container Frame (not used for real-time update now)
submit_button = tk.Button(input_frame, text="Submit", bg="#FF9797", command=generate_qr)
submit_button.grid(row=5, column=0, padx=10, pady=20)

# Creating the canvas
canvas = tk.Canvas(root, width=750, height=600, bg="white")  # Hex color for white
canvas.pack(side="left")

root.mainloop()
