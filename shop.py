from item import ItemDatabase

def open_shop(player_data):
    while True:
        print("\n--- TOWN SHOP ---")
        print(f"Your Gold: {player_data['gold']}g")
        print("1. Health Potion (15g)")
        print("2. Iron Sword (+5 Attack) (50g)")
        print("3. Magic Scroll: Fireball (75g)")
        print("4. Healing Tome: Heal (60g)")
        print("5. Exit Shop")
        
        choice = input("Choose an item to buy (1-5): ").strip()
        mapping = {
            "1": ("Health Potion", 15),
            "2": ("Iron Sword", 50),
            "3": ("Magic Scroll", 75),
            "4": ("Healing Tome", 60)
        }
        
        if choice == "5":
            break
        elif choice in mapping:
            name, price = mapping[choice]
            if player_data["gold"] >= price:
                player_data["gold"] -= price
                if name in ["Magic Scroll", "Healing Tome"]:
                    s_name = ItemDatabase.ITEMS[name]["skill"]
                    if s_name not in player_data["skills"]:
                        player_data["skills"].append(s_name)
                        print(f"Successfully learned skill: {s_name}!")
                    else:
                        print("You already know this skill! Gold refunded.")
                        player_data["gold"] += price
                else:
                    player_data["inventory"].append(name)
                    print(f"Successfully purchased {name}!")
            else:
                print("Not enough gold!")
        else:
            print("Invalid shop option. Please enter 1-5.")