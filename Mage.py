from Character import Character


class Mage(Character):
    def __init__(self, name, ad=80, max_hp=50):
        super().__init__(name, "Mage", max_hp, ad, max_hp)

    def __init__(self):
        super().__init__("Théo", "Mage", 50, 30, 50)

    def get_damage(self, ad):
        self.current_hp -= int(ad * 0.90)
        if self.current_hp < 0:
            self.current_hp = 0
