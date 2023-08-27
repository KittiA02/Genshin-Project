import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def calculate_crit_value(event=None):
    try:
        CR = float(crit_rate_entry.get())
        WeaCR = float(weapon_crit_rate_entry.get())
        CD = float(crit_damage_entry.get())
        WeaCD = float(weapon_crit_damage_entry.get())

        NewCR = ((CR - (5.0 + WeaCR)) * 2.0)
        NewCD = (CD - (50.0 + WeaCD))

        CritValue = NewCR + NewCD

        result_label.config(text="\nCharacter Crit Value:", font=("Trebuchet MS", 20, "bold"))
        crit_value_label.config(text=f"\n{CritValue:.1f}\n", font=("Trebuchet MS", 24, "bold"))
    except ValueError:
        result_label.config(text="Invalid input. Please check your values.")
        crit_value_label.config(text="")

root = tk.Tk()
root.title("Character Crit Value Calculator")

root.iconbitmap("tray_large.ico")
image = PhotoImage(file="scara.png")  # Replace "image.png" with your image file's name or path
image_label = tk.Label(root, image=image)
image_label.pack()

title_label = tk.Label(root, text="Crit Value Calculator", font=("Trebuchet MS", 24, "bold"))
title_label.pack(pady=10)

crit_rate_label = tk.Label(root, text="Enter character's Crit Rate:", font=("Open Sans", 13))
crit_rate_label.pack()
crit_rate_entry = tk.Entry(root, justify="center", font=("Open Sans", 12))
crit_rate_entry.pack()

weapon_crit_rate_label = tk.Label(root, text="Enter character weapon's Crit Rate. If not available, type 0:", font=("Open Sans", 13))
weapon_crit_rate_label.pack()
weapon_crit_rate_entry = tk.Entry(root, justify="center", font=("Open Sans", 12))
weapon_crit_rate_entry.pack()

crit_damage_label = tk.Label(root, text="Enter character's Crit Damage:", font=("Open Sans", 13))
crit_damage_label.pack()
crit_damage_entry = tk.Entry(root, justify="center", font=("Open Sans", 12))
crit_damage_entry.pack()

weapon_crit_damage_label = tk.Label(root, text="Enter character weapon's Crit Damage. If not available, type 0:", font=("Open Sans", 13))
weapon_crit_damage_label.pack()
weapon_crit_damage_entry = tk.Entry(root, justify="center", font=("Open Sans", 12))
weapon_crit_damage_entry.pack()

calculate_button = tk.Button(root, text="Calculate Crit Value", command=calculate_crit_value, font=("Trebuchet MS", 16, "bold"))
calculate_button.pack(pady=10)

# Bind the "Return" key press event to the calculate_crit_value function
root.bind("<Return>", calculate_crit_value)

result_label = tk.Label(root, text="", font=("Trebuchet MS", 20))
result_label.pack()

crit_value_label = tk.Label(root, text="", font=("Trebuchet MS", 24, "bold"))
crit_value_label.pack()

root.mainloop()
