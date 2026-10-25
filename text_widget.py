# The Text widget is used to accept and display multiple lines of text. 
# Unlike Entry, which accepts a single line, Text is suitable for 
# descriptions, comments, and messages.

# Creating a text Widget 

import tkinter as tk

root = tk.Tk()
root.title("Text Widget")
root.geometry("400x300")


result_label = tk.Label(root, text="")
text_box = tk.Text(root, height=5, width=30)
text_box.pack(pady=10)

# Retrieving Text


def show_text():
    message = text_box.get("1.0", tk.END)
    result_label.config(text=message)

def clear():
    text_box.delete("1.0", tk.END)

tk.Button(root, text="Show Text", command=show_text).pack()
tk.Button(root, text="Clear Text", command=clear).pack()

result_label.pack(pady=10)





# Use .get("1.0", tk.END) to retrieve the text entered by the user.
# Understanding get("1.0", tk.END)
# - "1.0" — starts at line 1, character position 0.
# - tk.END — specifies the end of the text.
# - .get() — retrieves the text between those positions.

# Inserting Text
# Use .insert() to add text to the widget.
# text_box.insert("1.0", "Enter your message here")

# This case, "1.0" specifies where the text should be inserted.

# Clearing the Text Widget
# Use .delete("1.0", tk.END) to remove all text.


root.mainloop()

# Class work
# Build a Feedback Form with the following features:
# 1. A label displaying “Enter Your Feedback”.
# 2. A Text widget for multiline input.
# 3. A Submit button that displays the submitted feedback in a label.
# 4. A Clear button that removes all text from the Text widget.







