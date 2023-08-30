import tkinter as tk
from tkinter import ttk, PhotoImage
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image, ImageTk

# Character data stored as dictionaries
character_info = [
    {"name": "Aether", "image": "picture/Aether_Icon.png"},
    {"name": "Albedo", "image": "picture/Albedo_Icon.png"},
    {"name": "Alhaitham", "image": "picture/Alhaitham_Icon.png"},
    {"name": "Arataki Itto", "image": "picture/Arataki_Itto_Icon.png"},
    {"name": "Baizhu", "image": "picture/Baizhu_Icon.png"},
    {"name": "Beidou", "image": "picture/Beidou_Icon.png"},
    {"name": "Cyno", "image": "picture/Cyno_Icon.png"},
    {"name": "Diluc", "image": "picture/Diluc_Icon.png"},
    {"name": "Eula", "image": "picture/Eula_Icon.png"},
    {"name": "Ganyu", "image": "picture/Ganyu_Icon.png"},
    {"name": "Hu Tao", "image": "picture/Hu_Tao_Icon.png"},
    {"name": "Kaedehara Kazuha", "image": "picture/Kaedehara_Kazuha_Icon.png"},
    {"name": "Kamisato Ayaka", "image": "picture/Kamisato_Ayaka_Icon.png"},
    {"name": "Kamisato Ayato", "image": "picture/Kamisato_Ayato_Icon.png"},
    {"name": "Kaveh", "image": "picture/Kaveh_Icon.png"},
    {"name": "Keqing", "image": "picture/Keqing_Icon.png"},
    {"name": "Klee", "image": "picture/Klee_Icon.png"},
    {"name": "Lumine", "image": "picture/Lumine_Icon.png"},
    {"name": "Lyney", "image": "picture/Lyney_Icon.png"},
    {"name": "Nahida", "image": "picture/Nahida_Icon.png"},
    {"name": "Nilou", "image": "picture/Nilou_Icon.png"},
    {"name": "Ningguang", "image": "picture/Ningguang_Icon.png"},
    {"name": "Raiden Shogun", "image": "picture/Raiden_Shogun_Icon.png"},
    {"name": "Razor", "image": "picture/Razor_Icon.png"},
    {"name": "Sangonomiya Kokomi", "image": "picture/Sangonomiya_Kokomi_Icon.png"},
    {"name": "Shikanoin Heizou", "image": "picture/Shikanoin_Heizou_Icon.png"},
    {"name": "Tartaglia", "image": "picture/Tartaglia_Icon.png"},
    {"name": "Tighnari", "image": "picture/Tighnari_Icon.png"},
    {"name": "Venti", "image": "picture/Venti_Icon.png"},
    {"name": "Wanderer", "image": "picture/Wanderer_Icon.png"},
    {"name": "Yae Miko", "image": "picture/Yae_Miko_Icon.png"},
    {"name": "Yanfei", "image": "picture/Yanfei_Icon.png"},
    {"name": "Yelan", "image": "picture/Yelan_Icon.png"},
    {"name": "Yoimiya", "image": "picture/Yoimiya_Icon.png"},
    {"name": "Xiao", "image": "picture/Xiao_Icon.png"},
    {"name": "Zhongli", "image": "picture/Zhongli_Icon.png"},
    # Add more characters as needed
]

characters = []

for info in character_info:
    character = {
        "name": info["name"],
        "image": info["image"],
        "CR": "",
        "WeaCR": "",
        "CD": "",
        "WeaCD": ""
    }
    characters.append(character)

current_character_index = 0
select_character_button = None
calculator_frame_visible = False  # Flag to control the visibility of the calculator frame
    
def update_view():
    if calculator_frame_visible:
        banner_label.pack_forget()  # Hide the banner
        start_button.pack_forget()   # Hide the start button
        calculator_frame.pack()      # Show the calculator frame
    else:
        banner_label.pack()
        start_button.pack()

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
                crit_message_label.config(text=character["name"] + "'s Crit Value is enough, go do a Spiral Abyss!")
            else:
                crit_message_label.config(text="")

        except ValueError:
            result_label.config(text="Invalid input. Please check your values.")
            crit_value_label.config(text="")
    else:
        result_label.config(text="Please fill in all the input fields.")
        crit_value_label.config(text="")
        crit_message_label.config(text="")  # Clear the crit message

def start_calculator():
    banner_label.pack_forget()  # Hide the banner
    start_button.pack_forget()   # Hide the start button
    calculator_frame.pack()      # Show the calculator frame
  
def update_select_button_state(event=None):
    selected_character = character_selection.get()
    if selected_character and selected_character in character_names:
        select_character_button.config(state="normal")
    else:
        select_character_button.config(state="disabled")

def on_search_bar_change(event):
    search_text = character_selection.get().lower()
    matching_names = [name for name in character_names if search_text in name.lower()]
    character_selection.set_completion_list(matching_names)
    
    update_select_button_state()
    
def select_character():
    global current_character_index
    current_character_index = character_names.index(character_selection.get())
    update_character()
    select_character_button.config(state="disabled")
    crit_message_label.config(text="")  # Clear the crit message
    character_selection.set("")  # Clear the search box

def next_character():
    global current_character_index
    current_character_index = (current_character_index + 1) % len(characters)
    update_character()

def previous_character():
    global current_character_index
    current_character_index = (current_character_index - 1) % len(characters)
    update_character()
    
root = tk.Tk()
root.title("Character Crit Value Calculator")
root.geometry("700x925")  # Set the window's fixed width and height
root.resizable(False, False)  # Disable resizing in both directions


# Load and display the Genshin Impact banner
banner_image = Image.open("picture/Genshin_Impact_logo.png")
banner_image = banner_image.resize((650, 270), Image.LANCZOS)
banner_photo = ImageTk.PhotoImage(banner_image)
banner_label = tk.Label(root, image=banner_photo)
banner_label.image = banner_photo
banner_label.pack()

root.iconbitmap("tray_large.ico")
image = PhotoImage(file="picture/scara.png")
image_label = tk.Label(root, image=image)
image_label.pack()

# Create a "Start" button to initiate the calculator
start_button = tk.Button(root, text="Start Calculator", command=start_calculator, font=("Trebuchet MS", 14))
start_button.pack()

# Create a frame to hold the calculator widgets
calculator_frame = tk.Frame(root)

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

calculate_button = tk.Button(root, text="Calculate Crit Value / Save", command=calculate_crit_value, font=("Trebuchet MS", 16, "bold"))
calculate_button.pack(pady=10)

# Bind the "Return" key press event to the calculate_crit_value function
root.bind("<Return>", calculate_crit_value)

result_label = tk.Label(root, text="", font=("Trebuchet MS", 20))
result_label.pack()

crit_value_label = tk.Label(root, text="", font=("Trebuchet MS", 24, "bold"))
crit_value_label.pack()

crit_message_label = tk.Label(root, text="", font=("Trebuchet MS", 16))
crit_message_label.pack()

# Create an AutocompleteCombobox for character selection
character_names = [info["name"] for info in character_info]
character_selection = AutocompleteCombobox(root, font=("Open Sans", 12))
character_selection.set_completion_list(character_names)
character_selection.pack()

# Bind the search bar's text variable to the callback function
character_selection.bind("<<ComboboxSelected>>", update_select_button_state)
character_selection.bind("<KeyRelease>", on_search_bar_change)


# Create "Select Character" button
select_character_button = tk.Button(root, text="Select Character", command=select_character, font=("Trebuchet MS", 14))
select_character_button.pack(side="right", padx=10)
select_character_button.config(state="disabled")  # Initially disabled

# Create a frame to hold the navigation buttons
navigation_frame = tk.Frame(root)
navigation_frame.pack(pady=10)

# Create "Previous Character" button
previous_character_button = tk.Button(navigation_frame, text="Previous Character", command=previous_character, font=("Trebuchet MS", 14))
previous_character_button.pack(side="left", padx=10)

# Create "Next Character" button
next_character_button = tk.Button(navigation_frame, text="Next Character", command=next_character, font=("Trebuchet MS", 14))
next_character_button.pack(side="right", padx=10)

# Pack the navigation frame after the "Select" button
navigation_frame.pack(pady=5)

update_character()  # Initial character update

# Initialize the view
update_view()

root.mainloop()