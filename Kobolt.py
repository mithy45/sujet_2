from Character import Character


class Kobolt(Character):
    def __init__(self, name="Vilain", ad=15, max_hp=50, res=0.75):
        super().__init__(name, "Kobolt", max_hp, ad, max_hp, res, True)
