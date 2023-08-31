# backend.py

from Frontend import on_character_selection


class CharacterController:
    def __init__(self, character_info):
        self.characters = []
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

for info in CharacterController.character_info:
    character = {
        "name": info["name"],
        "image": info["image"],
        "CR": "",
        "WeaCR": "",
        "CD": "",
        "WeaCD": ""
    }
    characters.append(character)

    def update_character():
        global current_character_index
        selected_character = on_character_selection.get()

    for index, character in enumerate(characters):
        if character["name"] == selected_character:
            current_character_index = index
            break

    character = characters[current_character_index]

    # Update crit value label
    calculate_crit_value()

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

    def get_character_info(self, character_index):
        # Get character's current information
        return character_info

# Initialize the controller
controller = CharacterController(character_info)
