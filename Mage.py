from Character import Character


class Mage(Character):
    def __init__(self, name, ad=80, max_hp=50):
        super().__init__(name, "Mage", max_hp, ad, max_hp)
