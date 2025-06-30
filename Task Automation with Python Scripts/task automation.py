import tkinter as tk
from tkinter import filedialog, messagebox
import re

def extract_emails(text):
    # Regex pattern to find emails
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return set(re.findall(pattern, text))

def browse_and_extract():
    # Step 1: Select Input File
    input_file = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text files", "*.txt")]
    )
    if not input_file:
        return

    try:
        with open(input_file, 'r') as f:
            text = f.read()
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {e}")
        return

    emails = extract_emails(text)

    if not emails:
        messagebox.showinfo("No Emails Found", "No valid email addresses were found.")
        return

    # Step 2: Select Output File
    output_file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Save Extracted Emails As"
    )
    if not output_file:
        return

    try:
        with open(output_file, 'w') as f:
            for email in sorted(emails):
                f.write(email + '\n')
    except Exception as e:
        messagebox.showerror("Error", f"Could not write to file: {e}")
        return

    messagebox.showinfo("Success", f"✅ {len(emails)} email(s) extracted and saved to:\n{output_file}")

# Setup GUI
root = tk.Tk()
root.title("📧 Email Extractor Tool")
root.geometry("400x200")

label = tk.Label(root, text="Extract Emails from a .txt File", font=("Helvetica", 14))
label.pack(pady=20)

button = tk.Button(root, text="Browse and Extract", command=browse_and_extract, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
button.pack()

root.mainloop()
