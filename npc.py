NPCS = {
    "Elder": {
        "name": "Village Elder Thomas",
        "dialogue": "Welcome traveler! Our kingdom is overrun. Speak with the Hermit in the fields and defeat 3 monsters to save us!"
    },
    "Merchant": {
        "name": "Bazaar Merchant Zara",
        "dialogue": "I sell the finest weapons and potions east of the mountains. Bring coin!"
    },
    "Hermit": {
        "name": "Forest Hermit",
        "dialogue": "Side Quest: Slay a Goblin in these wilds and return to me for a bounty reward!"
    },
    "Guard": {
        "name": "Gate Guard Samuel",
        "dialogue": "The dungeon gate leads to the Shadow Demon. Only strong warriors may pass."
    },
    "Blacksmith": {
        "name": "Master Blacksmith Erik",
        "dialogue": "A sharp iron blade keeps you breathing through the night."
    }
}

def talk_to_npc(npc_key, player_data):
    npc = NPCS.get(npc_key)
    if npc:
        print(f"\n[{npc['name']}] says: \"{npc['dialogue']}\"")
        
        if npc_key == "Elder" and player_data["quest_step"] == 0:
            player_data["quest_step"] = 1
            print(">> [Main Quest Updated]: Visit the Wilderness Fields, talk to the Hermit, and defeat 3 monsters!")
        elif npc_key == "Hermit" and not player_data["side_quest_1_done"]:
            if player_data["monsters_killed"] >= 1:
                player_data["side_quest_1_done"] = True
                player_data["gold"] += 40
                player_data["xp"] += 30
                print(">> [Side Quest Completed]: Hermit's Favor! Earned 40 Gold & 30 XP.")
            else:
                print(">> [Side Quest Active]: Go defeat at least 1 monster in the fields first!")