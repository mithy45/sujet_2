from Character import Character


class Warrior(Character):
    def __init__(self, name, ad=50, max_hp=100):
        super().__init__(name, "Warrior", max_hp, ad, max_hp)

    def __init__(self):
        super().__init__("Karim", "Warrior", 70, 20, 70)

    def get_damage(self, ad):
        self.current_hp -= int(ad * 0.60)
        if self.current_hp < 0:
            self.current_hp = 0

    def speech(self):
        pass
