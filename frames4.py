# Nesting Frames
# A Frame can contain another Frame
# 
# This is called nesting, and it allows you to build more complex layouts.
# 
# For example, a login form might have:
#  A main Frame.
#  A smaller Frame for the username.
# Another Frame for the password.
# A separate Frame for the buttons.

import tkinter as tk

root = tk.Tk()
root.title("Nested Frames")
root.geometry("400x300")

main_frame = tk.Frame(root, bg="lightgray", padx=20, pady=20)
main_frame.pack(pady=30)

inner_frame = tk.Frame(main_frame, bg="lightblue", padx=20, pady=20)
inner_frame.pack()

label = tk.Label(inner_frame, text="Inside the Inner Frame", bg="lightblue")
label.pack()
root.mainloop()


# Project: Simple Login Interface
# Create a Tkinter application with the following requirements:
# Main Window
# Title: Login System
# Dimensions: 400x350
# Header Frame
# Background color: dark blue.
# Contains a Label displaying USER LOGIN.
# The Label's text color must be white.
# Form Frame
# Contains a Label displaying Username.
# Contains an Entry widget for the username.
# Contains a Label displaying Password.
# Contains an Entry widget for the password.
# The password Entry must hide typed characters using show="*".
# Button Frame
# Contains a Login button.
# Contains a Clear button.
# Additional Requirements
# Use three separate Frames.
# Place each widget inside the appropriate Frame.
# Use padding to improve the layout.
# The Clear button must clear both Entry widgets.
# The Login button must display an informational message using messagebox.showinfo().

