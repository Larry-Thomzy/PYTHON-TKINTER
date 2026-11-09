# TKINTER SCROLLBAR WIDGET
# A SCROLLBAR IS A tKINTER WIDGET THAT ALLOWS USERS TO NAVIGATE THROUGH CONTENT
# THAT IS TOO LARGE TO FIT INSIDE THE VISIBLE AREA OF ANOTHER WIDGET.

import tkinter as tk
root = tk.Tk()
root.title("Scrollbar Widget")
root.geometry("400x300")

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()
