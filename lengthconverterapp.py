import tkinter as tk
from tkinter import messagebox
def convert_to_cm():
    try:
        inches = float(entry_inch.get())
        cm = inches * 2.54
        label_result.config(text=f"{cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
root = tk.Tk()
root.title("Inch to Centimeter Converter")
root.geometry("300x200")
label_title = tk.Label(root, text="Inches to Centimeters", font=("Arial", 14))
label_title.pack(pady=10)
entry_inch = tk.Entry(root, width=20)
entry_inch.pack(pady=5)
btn_convert = tk.Button(root, text="Convert", command=convert_to_cm)
btn_convert.pack(pady=10)
label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.pack(pady=10)
root.mainloop()