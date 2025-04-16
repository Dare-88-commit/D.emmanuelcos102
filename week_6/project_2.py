import tkinter as tk
from tkinter import messagebox

admitted = []
not_admitted = []


def check_admission(name, department, jamb_score, credits, interview_passed):
    if department.lower() == "computer science":
        if jamb_score >= 250 and credits >= 5 and interview_passed.lower() == "yes":
            admitted.append(name)
            return f"{name} has been admitted into Computer Science."
        else:
            not_admitted.append(name)
            return f"{name} was not admitted into Computer Science."
    elif department.lower() == "mass communication":
        if jamb_score >= 230 and credits >= 5 and interview_passed.lower() == "yes":
            admitted.append(name)
            return f"{name} has been admitted into Mass Communication."
        else:
            not_admitted.append(name)
            return f"{name} was not admitted into Mass Communication."
    else:
        return "Invalid department entered."


def submit():
    name = name_entry.get().strip()
    department = dept_entry.get().strip()

    try:
        jamb_score = int(jamb_entry.get().strip())
        credits = int(credit_entry.get().strip())
    except ValueError:
        messagebox.showerror(
            "Invalid input", "Please enter valid numbers for JAMB score and credits.")
        return

    interview_passed = interview_entry.get().strip()
    result = check_admission(
        name, department, jamb_score, credits, interview_passed)
    messagebox.showinfo("Result", result)


root = tk.Tk()
root.title("Admission Checker")
root.geometry("400x400")

tk.Label(root, text="Candidate Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Department (Computer Science / Mass Communication):").pack()
dept_entry = tk.Entry(root)
dept_entry.pack()

tk.Label(root, text="JAMB Score:").pack()
jamb_entry = tk.Entry(root)
jamb_entry.pack()

tk.Label(root, text="Number of Credits:").pack()
credit_entry = tk.Entry(root)
credit_entry.pack()

tk.Label(root, text="Did the candidate pass the interview?").pack()
interview_entry = tk.Entry(root)
interview_entry.pack()

tk.Button(root, text="Check Admission", command=submit).pack(pady=20)

root.mainloop()


print("Admitted Candidates:", admitted)
print("Not Admitted Candidates:", not_admitted)
