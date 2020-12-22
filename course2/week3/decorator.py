from abc import ABC


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    def get_stats(self):
        pass

    def get_positive_effects(self):
        pass

    def get_negative_effects(self):
        pass


class AbstractPositive(AbstractEffect, ABC):
    def __init__(self, base):
        super().__init__(base)


class Berserk(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)
        self.stats = {
            "HP": 50,  # health points
            "Strength": 7,  # сила
            "Perception": -3,  # восприятие
            "Endurance": 7,  # выносливость
            "Charisma": -3,  # харизма
            "Intelligence": -3,  # интеллект
            "Agility": 7,  # ловкость
            "Luck": 7  # удача
        }


class Blessing(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)
        self.stats = {
            "Strength": 2,  # сила
            "Perception": 2,  # восприятие
            "Endurance": 2,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 2,  # интеллект
            "Agility": 2,  # ловкость
            "Luck": 2  # удача
        }


class AbstractNegative(AbstractEffect, ABC):
    def __init__(self, base):
        super().__init__(base)


class Weakness(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.stats = {
            "Strength": -4,  # сила
            "Endurance": -4,  # выносливость
            "Agility": -4  # ловкость
        }


class EvilEye(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.stats = {
            "Luck": -10  # удача
        }


class Curse(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.stats = {
            "Strength": -2,  # сила
            "Perception": -2,  # восприятие
            "Endurance": -2,  # выносливость
            "Charisma": -2,  # харизма
            "Intelligence": -2,  # интеллект
            "Agility": -2,  # ловкость
            "Luck": -2  # удача
        }
