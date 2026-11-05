def check_quests(player_data):
    step = player_data["quest_step"]
    print("\n--- QUEST LOG ---")
    if step == 0:
        print("Main Quest: Speak with Village Elder Thomas in town.")
    elif step == 1:
        print(f"Main Quest: Defeat 3 monsters in the Field Map ({player_data['monsters_killed']}/3 defeated).")
    elif step == 2:
        print("Main Quest: Defeat the Shadow Demon Boss in the Dungeon map!")
    elif step >= 3:
        print("Main Quest: Completed! You saved the realm!")

    sq1 = "Completed" if player_data["side_quest_1_done"] else "Active (Find Hermit & Slay Goblin)"
    sq2 = "Completed" if player_data["side_quest_2_done"] else "Active (Defeat an Orc)"
    print(f"Side Quest 1 (Hermit's Favor): {sq1}")
    print(f"Side Quest 2 (Bounty Hunt): {sq2}")