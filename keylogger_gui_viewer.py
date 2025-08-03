import tkinter as tk
from tkinter import filedialog

def load_log():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, "r") as f:
            content = f.read()
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, content)

root = tk.Tk()
root.title("📝 Keylog Viewer")
root.geometry("600x400")

tk.Button(root, text="Open Keylog File", command=load_log).pack(pady=10)

text_box = tk.Text(root, wrap=tk.WORD)
text_box.pack(expand=True, fill=tk.BOTH)

root.mainloop()
