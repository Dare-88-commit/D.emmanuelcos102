import tkinter as tk
from tkinter import messagebox


def calculate_delivery_fee(location, weight):
    if location.lower() == "ibeju-lekki":
        if weight >= 10:
            return 5000
        else:
            return 3500
    elif location.lower() == "epe":
        if weight >= 10:
            return 10000
        else:
            return 5000
    else:
        return None


def show_result():
    location = location_entry.get().strip()
    try:
        weight = float(weight_entry.get().strip())
    except ValueError:
        messagebox.showerror(
            "Invalid input", "Please enter a valid number for weight.")
        return

    fee = calculate_delivery_fee(location, weight)

    if fee is not None:
        messagebox.showinfo(
            "Delivery Fee", f"The delivery fee to {location.title()} for {weight}kg is ₦{fee:,}")
    else:
        messagebox.showerror(
            "Invalid location", "Please enter a valid location (Ibeju-Lekki or Epe).")


root = tk.Tk()
root.title("Delivery Fee Calculator")
root.geometry("400x250")

tk.Label(root, text="Enter Location (Ibeju-Lekki or Epe):").pack(pady=5)
location_entry = tk.Entry(root)
location_entry.pack()

tk.Label(root, text="Enter Package Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Button(root, text="Calculate Fee", command=show_result).pack(pady=20)

root.mainloop()
