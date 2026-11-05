from colorama import init
from database import register_user, login_user, save_game_data
from map import MAPS, render_map
from npc import talk_to_npc
from quest import check_quests
from shop import open_shop
from combat import start_combat, handle_inventory
from monster import Goblin, Slime, Orc, Skeleton, Boss
import random

init(autoreset=True)

def print_story_intro():
    print("========================================")
    print("   CHRONICLES OF ETHERIA: TERMINAL RPG  ")
    print("========================================")
    print("Darkness has descended upon Safe Haven.")
    print("The Shadow Demon Lord threatens the realm.")
    print("Gear up, explore, and save the kingdom!\n")

def game_loop(user):
    print(f"\nWelcome back, {user['username']}!")
    
    while True:
        map_key = user["current_map"]
        r = user["player_row"]
        c = user["player_col"]
        
        render_map(map_key, r, c)
        print(f"\n[Status] HP: {user['hp']}/{user['max_hp']} | Level: {user['level']} | Gold: {user['gold']}g | Quest Step: {user['quest_step']}")
        print("Controls: W, A, S, D | [I]nventory, [Q]uests, [C]haracter, [E]xit")
        
        move = input("Action/Move: ").strip().upper()
        
        if move == "E":
            save_game_data(user["username"], user)
            print("Game saved successfully! Exiting.")
            break
        elif move == "I":
            handle_inventory(user)
            continue
        elif move == "Q":
            check_quests(user)
            continue
        elif move == "C":
            print("\n--- CHARACTER SHEET ---")
            print(f"Username: {user['username']}")
            print(f"Level: {user['level']}")
            print(f"HP: {user['hp']}/{user['max_hp']}")
            print(f"Gold: {user['gold']}g")
            print(f"Skills: {user['skills']}")
            print(f"Inventory: {user['inventory']}")
            continue
            
        new_r, new_c = r, c
        if move == "W": new_r -= 1
        elif move == "S": new_r += 1
        elif move == "A": new_c -= 1
        elif move == "D": new_c += 1
        else:
            print("Invalid command. Use W, A, S, D or menu keys.")
            continue
            
        grid = MAPS[map_key]["grid"]
        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
            target_cell = grid[new_r][new_c]
            if target_cell == "#":
                print("Ouch! That's a solid wall.")
                continue
            
            user["player_row"] = new_r
            user["player_col"] = new_c
            
            if map_key == "town_map":
                if target_cell == "E":
                    talk_to_npc("Elder", user)
                elif target_cell == "N":
                    talk_to_npc("Merchant", user)
                elif target_cell == "B":
                    talk_to_npc("Blacksmith", user)
                elif target_cell == "G":
                    talk_to_npc("Guard", user)
                elif target_cell == "S":
                    open_shop(user)
                elif target_cell == "D":
                    user["current_map"] = "field_map"
                    user["player_row"] = 1
                    user["player_col"] = 1
                    print("You travel into the Wilderness Fields.")
                    
            elif map_key == "field_map":
                if target_cell == "T":
                    user["current_map"] = "town_map"
                    user["player_row"] = 1
                    user["player_col"] = 1
                    print("You return to Safe Haven Town.")
                elif target_cell == "H":
                    talk_to_npc("Hermit", user)
                elif target_cell == "M":
                    monster_pool = [Goblin(), Slime(), Orc(), Skeleton()]
                    chosen_monster = random.choice(monster_pool)
                    won = start_combat(user, chosen_monster)
                    if won:
                        user["monsters_killed"] += 1
                        if user["quest_step"] == 1 and user["monsters_killed"] >= 3:
                            user["quest_step"] = 2
                            print(">> [Main Quest Updated]: You've slain 3 monsters! The Dungeon Boss is unlocked!")
                        if isinstance(chosen_monster, Orc) and not user["side_quest_2_done"]:
                            user["side_quest_2_done"] = True
                            user["gold"] += 50
                            user["xp"] += 40
                            print("Side Quest Completed: Bounty Hunt! Earned 50 Gold & 40 XP.")
                elif target_cell == "B":
                    if user["quest_step"] < 2:
                        print("The dungeon gate is sealed! Defeat 3 monsters and speak to the Elder first.")
                    else:
                        print("You enter the lair of the Shadow Demon...")
                        boss = Boss()
                        won_boss = start_combat(user, boss)
                        if won_boss:
                            user["quest_step"] = 3
                            print("\n*** CONGRATULATIONS! YOU DEFEATED THE SHADOW DEMON AND SAVED THE REALM! ***")
            
            save_game_data(user["username"], user)
        else:
            print("You cannot move past map boundaries.")

if __name__ == "__main__":
    print_story_intro()
    while True:
        print("1. Register Account")
        print("2. Login")
        print("3. Exit Game")
        choice = input("Select option (1-3): ").strip()
        if choice == "1":
            u = input("Choose Username: ").strip()
            p = input("Choose Password: ").strip()
            success, msg = register_user(u, p)
            print(msg)
        elif choice == "2":
            u = input("Username: ").strip()
            p = input("Password: ").strip()
            success, user_data = login_user(u, p)
            if success:
                game_loop(user_data)
            else:
                print(user_data)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")