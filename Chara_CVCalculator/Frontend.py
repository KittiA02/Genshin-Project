# frontend.py
import tkinter as tk
from tkinter import ttk, PhotoImage
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image, ImageTk
from Backend import controller

# Create Tkinter GUI as you did before, but only include the UI code
# ...

# Use controller methods to interact with backend logic
def update_character():
    global current_character_index
    selected_character = character_selection.get()

    for index, character in enumerate(characters):
        if character["name"] == selected_character:
            current_character_index = index
            break

    character = characters[current_character_index]

    crit_rate_entry.delete(0, tk.END)
    crit_rate_entry.insert(0, character["CR"])

    weapon_crit_rate_entry.delete(0, tk.END)
    weapon_crit_rate_entry.insert(0, character["WeaCR"])

    crit_damage_entry.delete(0, tk.END)
    crit_damage_entry.insert(0, character["CD"])

    weapon_crit_damage_entry.delete(0, tk.END)
    weapon_crit_damage_entry.insert(0, character["WeaCD"])

    image = PhotoImage(file=character["image"])
    image_label.config(image=image)
    image_label.image = image

    title_namelabel.config(text=character["name"])

    title_label.config(text="Crit Value Calculator")

    # Update crit value label
    calculate_crit_value()

def calculate_crit_value(event=None):
    global current_character_index
    character = characters[current_character_index]

    crit_rate = crit_rate_entry.get()
    weapon_crit_rate = weapon_crit_rate_entry.get()
    crit_damage = crit_damage_entry.get()
    weapon_crit_damage = weapon_crit_damage_entry.get()

    if crit_rate and weapon_crit_rate and crit_damage and weapon_crit_damage:
        try:
            character["CR"] = float(crit_rate)
            character["WeaCR"] = float(weapon_crit_rate)
            character["CD"] = float(crit_damage)
            character["WeaCD"] = float(weapon_crit_damage)

            NewCR = ((character["CR"] - (5.0 + character["WeaCR"])) * 2.0)
            NewCD = (character["CD"] - (50.0 + character["WeaCD"]))

            CritValue = NewCR + NewCD

            result_label.config(text="Character Crit Value:", font=("Trebuchet MS", 20))
            crit_value_label.config(text=f"{CritValue:.1f}", font=("Trebuchet MS", 24, "bold"))
            
            if 0.0 <= CritValue < 90.0:
                crit_message_label.config(text="Your character's Crit Value is too low.")
            elif 90.0 <= CritValue < 150.0:
                crit_message_label.config(text="Your character's Crit Value is decent.")
            elif 150.0 <= CritValue < 180.0:
                crit_message_label.config(text="Your character's Crit Value is moderate.")
            elif 180.0 <= CritValue < 200.0:
                crit_message_label.config(text="Your character's Crit Value is good!")
            elif CritValue >= 200.0:
                crit_message_label.config(text="Your character's Crit Value is enough, go do a Spiral Abyss!")
            else:
                crit_message_label.config(text="")

        except ValueError:
            result_label.config(text="Invalid input. Please check your values.")
            crit_value_label.config(text="")
    else:
        result_label.config(text="Please fill in all the input fields.")
        crit_value_label.config(text="")
        

def previous_character():
    global current_character_index
    current_character_index = (current_character_index - 1) % len(characters)
    update_character()
    
def next_character():
    global current_character_index
    if next_character_button["text"] == "Select Character":
        update_character()
        next_character_button["text"] = "Next Character"
    else:
        current_character_index = (current_character_index + 1) % len(characters)
        update_character()
        if current_character_index == len(characters) - 1:
            next_character_button["text"] = "Select Character"

def on_character_selection(event):
    update_character()
    
    # Set the combobox value again to ensure it's responsive after button presses
    character_selection.set(character_names[current_character_index])
    
root = tk.Tk()
root.title("Character Crit Value Calculator")

root.iconbitmap("tray_large.ico")
image = PhotoImage(file="picture/scara.png")
image_label = tk.Label(root, image=image)
image_label.pack()

# Set the window's fixed width and height
fixed_window_width = 650
fixed_window_height = 900

root.geometry(f"{fixed_window_width}x{fixed_window_height}")

# Disable resizing in both directions
root.resizable(False, False)

title_namelabel = tk.Label(root, font=("Trebuchet MS", 18))
title_namelabel.pack(pady=10)

title_label = tk.Label(root, font=("Trebuchet MS", 24, "bold"))
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

crit_message_label = tk.Label(root, text="", font=("Trebuchet MS", 16))
crit_message_label.pack()

# Create a list of character names
character_names = [info["name"] for info in character_info]

# Create an AutocompleteCombobox for character selection
character_selection = AutocompleteCombobox(root, font=("Open Sans", 12))
character_selection.set_completion_list(character_names)
character_selection.pack()
character_selection.bind("<<ComboboxSelected>>", on_character_selection)

# Set the initial selection and trigger the event
character_selection.set(character_names[0])
on_character_selection(event=None)

# Create a frame to hold the navigation buttons
navigation_frame = tk.Frame(root)
navigation_frame.pack(pady=10)

# Create "Previous Character" button
previous_character_button = tk.Button(navigation_frame, text="Previous Character", command=previous_character, font=("Trebuchet MS", 14))
previous_character_button.pack(side="left", padx=10)

# Create "Next Character" button
next_character_button = tk.Button(navigation_frame, text="Select/Next Character", command=next_character, font=("Trebuchet MS", 14))
next_character_button.pack(side="left", padx=10)

# Pack the navigation frame after the "Select" button
navigation_frame.pack(pady=5)

update_character()  # Initial character update

root.mainloop()
