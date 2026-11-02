
# A frame is a container used to group and organize widgets inside a window.
# Think of a Frame as a box inside your application window. You can place labels,
# buttons, entry fields, and other widgets inside that box.

# For example when creating a login form, you can put the username field, and
#  login button inside one Frame.


# For Instance, you can use separate frames for a login form, 
# navigation buttons, and a registration form.


# Why do we use Frames?

# To organize widgets into separate sections.
# To create cleaner application layouts.
# To manage groups of widgets independently.
# To make complex interfaces easier to structure.


# Creating A Frame
import tkinter as tk

root = tk.Tk()
root.title("Frame Widget")
root.geometry("400x300")

frame = tk.Frame(root, bg="lightblue", width=550, height=750)
frame.pack(pady=20)

# frame.pack_propagate(False)

root.mainloop()