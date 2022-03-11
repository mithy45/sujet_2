from Character import Character


class Warrior(Character):
    def __init__(self, name, ad=50, max_hp=100):
        super().__init__(name, "Warrior", max_hp, ad, max_hp)
