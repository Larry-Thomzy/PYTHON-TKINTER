import tkinter as tk
app = tk.Tk()
app.title("Using Place")
app.geometry("400x300")

tk.Label(app, text="Welcome").place(x=150, y=50)
tk.Button(app, text="Login").place(x=260, y=100)

app.mainloop()
