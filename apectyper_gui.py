import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def run_apec():
    input_file = filedialog.askopenfilename(title="Select FASTA file", filetypes=[("FASTA files", "*.fa *.fasta")])
    if not input_file:
        return

    output_dir = filedialog.askdirectory(title="Select output directory")
    if not output_dir:
        return

    # Build the command
    cmd = ["./APECtyper.sh", "-f", input_file, "-o", output_dir]

    try:
        subprocess.run(cmd, check=True)
        messagebox.showinfo("Success", f"APECtyper ran successfully!\nOutput directory: {output_dir}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while running the command:\n{e}")

# Simple GUI
root = tk.Tk()
root.title("APECtyper GUI")

run_button = tk.Button(root, text="Run APECtyper", command=run_apec, width=30, height=2)
run_button.pack(pady=20)

root.mainloop()
