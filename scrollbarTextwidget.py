import tkinter as tk
root = tk.Tk()
root.title("Scrollable Text")
root.geometry("400x300")

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_box = tk.Text(root, yscrollcommand=scrollbar.set)
text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
text_box.insert("1.0", "Neither Femi nor Adeola nor Faruk got it right, Moyosore bailed them all but she kinda cheated \n Neither Femi nor Adeola nor Faruk got it right, Moyosore bailed them all but she kinda cheated \n Neither Femi nor Adeola nor Faruk got it right, Moyosore bailed them all but she kinda cheated \n Neither Femi nor Adeola nor Faruk got it right, Moyosore bailed them all but she kinda cheated \n Neither Femi nor Adeola nor Faruk got it right, Moyosore bailed them all but she kinda cheated \n Neither Femi nor Adeola nor Faruk got it right, Moyosore bailed them all but she kinda cheated \n Neither Femi nor Adeola nor Faruk got it right, Moyosore bailed them all but she kinda cheated")
scrollbar.config(command=text_box.yview)

root.mainloop()