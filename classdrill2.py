# Class work: Scrollable Course Catalogue

# Build a desktop application with the following requirements:
# 1. Create a main window with a title and appropriate dimensions.
# 2. Create a Listbox containing at least 30 course names.
# 3. Add a vertical scrollbar to the Listbox.
# 4. Add a Text widget containing a short description of the courses.
# 5. Add a vertical scrollbar to the Text widget.
# 6. Add a button that displays the selected course using a messagebox.

import tkinter as tk
root = tk.Tk()
root.title("Scrollable Course Catalogue")
root.geometry("400x300")

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

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT)

course_list = tk.Listbox(root, height=15, width=20,selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set)
course_list.pack(side=tk.LEFT)

for c in courses:
    course_list.insert(tk.END, c)

scrollbar.config()





