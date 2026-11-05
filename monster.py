import random

class Monster:
    def __init__(self, name, hp, attack, xp_reward, gold_reward):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward

    def drop_loot(self):
        loot = []
        if random.random() < 0.45:
            loot.append("Health Potion")
        return self.gold_reward, loot

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", hp=20, attack=4, xp_reward=15, gold_reward=10)

class Slime(Monster):
    def __init__(self):
        super().__init__("Slime", hp=12, attack=3, xp_reward=10, gold_reward=5)

class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", hp=35, attack=7, xp_reward=30, gold_reward=25)

class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", hp=25, attack=6, xp_reward=22, gold_reward=18)

class Boss(Monster):
    def __init__(self):
        super().__init__("Shadow Demon (Boss)", hp=80, attack=12, xp_reward=150, gold_reward=100)