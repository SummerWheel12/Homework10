import random
from skill import get_skill_object
from colorama import Fore, Style

class CombatPlayer:
    def __init__(self, player_data):
        self.data = player_data
        self.username = player_data["username"]
        self.hp = player_data["hp"]
        self.max_hp = player_data["max_hp"]
        self.level = player_data["level"]
        self.attack = 8 + (self.level * 2)
        if "Iron Sword" in player_data["inventory"]:
            self.attack += 5

    def sync_back(self):
        self.data["hp"] = self.hp
        self.data["max_hp"] = self.max_hp
        self.data["level"] = self.level

def handle_inventory(player_data):
    while True:
        print("\n--- INVENTORY ---")
        print(f"Gold: {player_data['gold']}g")
        if not player_data["inventory"]:
            print("Your inventory is empty.")
            break
        
        for i, item in enumerate(player_data["inventory"], 1):
            print(f"{i}. {item}")
        
        choice = input("Select item number to consume (or 0 to exit): ").strip()
        if choice == "0":
            break
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(player_data["inventory"]):
                item = player_data["inventory"][idx]
                if item == "Health Potion":
                    player_data["hp"] = min(player_data["max_hp"], player_data["hp"] + 25)
                    player_data["inventory"].pop(idx)
                    print("You consumed a Health Potion and restored 25 HP!")
                else:
                    print("This item cannot be consumed directly.")
            else:
                print("Invalid inventory selection.")
        else:
            print("Please enter a valid number.")

def start_combat(player_data, monster):
    p = CombatPlayer(player_data)
    print(Fore.RED + f"\n[!] A wild {monster.name} appeared!" + Style.RESET_ALL)

    while monster.hp > 0 and p.hp > 0:
        p.sync_back()
        print(f"\n{p.username} HP: {p.hp}/{p.max_hp} | {monster.name} HP: {monster.hp}/{monster.max_hp}")
        print("1. Basic Attack")
        print("2. Use Skill")
        print("3. Use Potion")
        
        choice = input("Choose combat action (1-3): ").strip()
        
        if choice == "1":
            dmg = random.randint(p.attack - 2, p.attack + 2)
            monster.hp -= dmg
            print(f"You strike {monster.name} for {dmg} damage.")
        elif choice == "2":
            print("Skills:", player_data["skills"])
            s_name = input("Enter skill name to cast: ").strip()
            if s_name in player_data["skills"]:
                skill_obj = get_skill_object(s_name)
                msg = skill_obj.use(p, monster)
                print(msg)
            else:
                print("Unknown skill! Turn skipped.")
        elif choice == "3":
            if "Health Potion" in player_data["inventory"]:
                player_data["inventory"].remove("Health Potion")
                p.hp = min(p.max_hp, p.hp + 25)
                print("Drank Health Potion! Restored 25 HP.")
            else:
                print("No Health Potions in inventory!")
                continue
        else:
            print("Invalid move! Monster attacks.")

        if monster.hp > 0:
            m_dmg = random.randint(monster.attack - 1, monster.attack + 1)
            p.hp -= m_dmg
            print(Fore.YELLOW + f"{monster.name} hits you back for {m_dmg} damage." + Style.RESET_ALL)

    player_data["hp"] = max(0, p.hp)

    if p.hp <= 0:
        print(Fore.RED + "\nYou have been defeated... Returning to town with half HP." + Style.RESET_ALL)
        player_data["hp"] = player_data["max_hp"] // 2
        return False
    else:
        print(Fore.GREEN + f"\nYou defeated {monster.name}!" + Style.RESET_ALL)
        gold_gain, loot = monster.drop_loot()
        player_data["gold"] += gold_gain
        player_data["xp"] += monster.xp_reward
        for item in loot:
            player_data["inventory"].append(item)
        print(f"Gained {monster.xp_reward} XP and {gold_gain} Gold!")

        if player_data["xp"] >= player_data["level"] * 50:
            player_data["level"] += 1
            player_data["max_hp"] += 15
            player_data["hp"] = player_data["max_hp"]
            print(Fore.CYAN + f"\n*** LEVEL UP! You are now level {player_data['level']}! ***" + Style.RESET_ALL)

        return True