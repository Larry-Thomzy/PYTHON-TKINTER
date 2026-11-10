# Class work: Scrollable Course Catalogue

# Build a desktop application with the following requirements:
# 1. Create a main window with a title and appropriate dimensions.
# 2. Create a Listbox containing at least 30 course names.
# 3. Add a vertical scrollbar to the Listbox.
# 4. Add a Text widget containing a short description of the courses.
# 5. Add a vertical scrollbar to the Text widget.
# 6. Add a button that displays the selected course using a messagebox.

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Scrollable Course Catalogue")
root.geometry("400x300")

head_frame = tk.Frame(root)
head_frame.pack(side=tk.TOP, fill="x")

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

bottom_frame = tk.Frame(main_frame)
bottom_frame.pack(side=tk.BOTTOM, fill="x", pady=10)

left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

label = tk.Label(head_frame, text="Course Catalogue", bg="blue", font = ("Times New Roman", 24, "bold"), fg="white", pady=15)
label.pack(fill="x")

courses = ["Generative AI Specialization",
"Applied Machine Learning",
"Data Science & Analytics",
"Prompt Engineering for ChatGPT",
"Computer Vision Fundamentals",
"Natural Language Processing (NLP)",
"AWS Cloud Practitioner",
"Microsoft Azure Fundamentals",
"Google Cloud Associate Engineer",
"DevOps Engineering with AWS",
"Kubernetes Administration",
"Infrastructure as Code (Terraform)",
"CompTIA Security+",
"Certified Ethical Hacking (CEH)",
"CISSP Certification Prep",
"Cloud Security Essentials",
"Network Defense Operations",
"Digital Forensics & Incident Response",
"Software Development & Web",
"Full-Stack Web Development",
"Python for Everybody",
"Advanced Java Programming",
"React & Modern JavaScript",
"Mobile App Development (iOS/Android)",
"Blockchain & Smart Contracts",
"IT Support & Networking",
"Google IT Support Professional",
"CompTIA A+ Certification",
"CompTIA Network+",
"Linux System Administration",
"Cisco Certified Network Associate (CCNA)",
"IT Project Management"]

scrollbar = tk.Scrollbar(left_frame, orient=tk.VERTICAL)

course_list = tk.Listbox(left_frame, height=30, width=50, selectmode=tk.MULTIPLE, selectbackground="blue", yscrollcommand=scrollbar.set)
course_list.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

for c in courses:
    course_list.insert(tk.END, c)

scrollbar.config(command=course_list.yview)

scrollbar2 = tk.Scrollbar(right_frame, orient=tk.VERTICAL)

text_pane = tk.Text(right_frame, width=100, yscrollcommand=scrollbar2.set)
text_pane.pack(side=tk.LEFT, fill=tk.BOTH)
text_pane.insert(tk.END, "Welcome to the Course Catalogue!\n\n")
text_pane.insert(tk.END, "Explore our available courses in AI, Data Science, Cloud Computing!, Cyber Security, Software \nDevelopment and Networking.\n\n")
text_pane.insert(tk.END, "Enhance your skills. Build your future!")

text_pane.tag_configure("title_head", font=("Times New Roman", 20, "bold"))
text_pane.tag_add("title_head", "1.0", "1.end")
scrollbar2.pack(side=tk.LEFT, fill=tk.Y)


tk.Button(bottom_frame, text="Show Selected Courses", bg="blue", font=("Times New Roman", 16, "bold"), fg="white",).pack(pady=10)



root.mainloop()













