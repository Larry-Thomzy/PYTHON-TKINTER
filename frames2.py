# Placing Widgets Inside a Frame

# This is one of the most important things to understand about Frames.
# Instead of placing every widget directly inside the main window, you can place related widgets inside a Frame.

import tkinter as tk
app = tk.Tk()
app.title("Widgets Inside a Frame")
app.geometry("400x300")
app.config(bg="pink")

frame = tk.Frame(app, bg="lightblue", width=500, height=500, padx=20, pady=20)
frame.pack(pady=30)
frame.pack_propagate(False)

label = tk.Label(frame, text="Welcome to Tkinter")
label.pack()

button =tk.Button(frame, text="Click Me")

button.pack(pady=10)



app.mainloop()