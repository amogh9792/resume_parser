import tkinter as tk
from tkinter import filedialog, messagebox

def upload_resume(parse_resume_func):
    """Upload resume and parse its details."""
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file_path:
        return

    job_desc = job_entry.get("1.0", tk.END).strip()
    if not job_desc:
        messagebox.showerror("Error", "Please enter a job description.")
        return

    result = parse_resume_func(file_path, job_desc)
    result_text.set(result)

def start_gui(parse_resume_func):
    """Create a user-friendly GUI for the resume parser."""
    global job_entry, result_text

    root = tk.Tk()
    root.title("AI Resume Parser with ML Ranking")
    root.geometry("500x600")

    tk.Label(root, text="Enter Job Description:").pack()
    job_entry = tk.Text(root, height=5, width=50)
    job_entry.pack()

    tk.Button(root, text="Upload Resume (PDF)", command=lambda: upload_resume(parse_resume_func)).pack()
    result_text = tk.StringVar()
    tk.Label(root, textvariable=result_text, justify="left", wraplength=450).pack()

    root.mainloop()
