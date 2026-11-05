class Skill:
    def __init__(self, name, mana_cost, cooldown):
        self.name = name
        self.mana_cost = mana_cost
        self.cooldown = cooldown

    def use(self, user, target):
        raise NotImplementedError("Subclasses must implement use method.")

class Slash(Skill):
    def __init__(self):
        super().__init__("Slash", mana_cost=0, cooldown=0)

    def use(self, user, target):
        damage = user.attack + 5
        target.hp -= damage
        return f"{user.username} uses Slash on {target.name} for {damage} damage!"

class Fireball(Skill):
    def __init__(self):
        super().__init__("Fireball", mana_cost=10, cooldown=2)

    def use(self, user, target):
        damage = 22
        target.hp -= damage
        return f"{user.username} casts Fireball on {target.name} for {damage} magical damage!"

class Heal(Skill):
    def __init__(self):
        super().__init__("Heal", mana_cost=8, cooldown=3)

    def use(self, user, target=None):
        heal_amt = 25
        user.hp = min(user.max_hp, user.hp + heal_amt)
        return f"{user.username} casts Heal, restoring {heal_amt} HP!"

def get_skill_object(name):
    if name == "Fireball":
        return Fireball()
    elif name == "Heal":
        return Heal()
    return Slash()