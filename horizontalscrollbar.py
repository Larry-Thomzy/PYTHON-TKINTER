# A Horizontal Scrollbar allows users to move through content from left to right


import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

scrollbar = tk.Scrollbar(root, orient = tk.HORIZONTAL)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

text_box = tk.Text(root, wrap=tk.NONE, xscrollcommand=scrollbar.set)
text_box.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=text_box.xview)

root.mainloop()



# Class work: Scrollable Course Catalogue

# Build a desktop application with the following requirements:
# 1. Create a main window with a title and appropriate dimensions.
# 2. Create a Listbox containing at least 30 course names.
# 3. Add a vertical scrollbar to the Listbox.
# 4. Add a Text widget containing a short description of the courses.
# 5. Add a vertical scrollbar to the Text widget.
# 6. Add a button that displays the selected course using a messagebox.
