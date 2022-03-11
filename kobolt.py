from Character import Character


class Kobolt(Character):
    def __init__(self, name, ad = 50, max_hp = 50):
        super().__init__(name, "Kobolt", max_hp, ad, max_hp)

    def get_damage(self, ad):
        self.current_hp -= int(ad * 0.75)
        if self.current_hp < 0:
            self.current_hp = 0
