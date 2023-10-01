# Import necessary libraries
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
from PIL import Image, ImageTk

# Function to change text color
def change_color():

    color = colorchooser.askcolor(title="pick a color...or else")
    text_area.config(fg=color[1])

# Function to change font style and size
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

# Function to create a new, untitled document
def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

# Function to open an existing text file
def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")

            text_area.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()

# Function to save the current document
def save_file():
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't save file")

        finally:
            file.close()

# Function to cut selected text
def cut():
    text_area.event_generate("<<Cut>>")

# Function to copy selected text
def copy():
    text_area.event_generate("<<Copy>>")

# Function to paste copied/cut text
def paste():
    text_area.event_generate("<<Paste>>")

# Function to show information about the program
def about():
    showinfo("About this program", "This is a basic text editor program written by YOU....")

def quit():
    window.destroy()

# Create the main window
window = Tk()
window.title("Universal Club Text Editor")
file = None

# Set window dimensions and position it in the center of the screen
window_width = 600
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# Initialize variables for font and font size
font_name = StringVar(window)
font_name.set("Open Sans")

font_size = StringVar(window)
font_size.set("20")

# Create a text area widget for editing text
text_area = Text(window, font=(font_name.get(), font_size.get()))

# Add a scrollbar to navigate through the text
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.configure(background="#00A878")
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

# Create a frame for additional options
frame = Frame(window)
frame.grid()

# Create a button to change text color
color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

# Create a dropdown for selecting font family
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

# Create a spinbox to select font size
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# Create a menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Create file menu and its options
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# Create edit menu and its options
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# Create help menu and its options
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Start the Tkinter main loop
window.mainloop()
