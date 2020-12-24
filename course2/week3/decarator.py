from abc import ABC, abstractmethod


class AbstractEffect(ABC, Hero):
    @abstractmethod
    def __init__(self, base):
        pass

    def get_stats(self):
        base_stats = self.base.get_stats()
        for characteristic in self.stats:
            base_stats[characteristic] += self.stats[characteristic]
        return base_stats

    def get_positive_effects(self):
        base_positive_effects = self.base.get_positive_effects()
        if isinstance(self, AbstractPositive):
            base_positive_effects.append(self.__class__.__name__)
        return base_positive_effects

    def get_negative_effects(self):
        base_negative_effects = self.base.get_negative_effects()
        if isinstance(self, AbstractNegative):
            base_negative_effects.append(self.__class__.__name__)
        return base_negative_effects


class AbstractPositive(AbstractEffect, ABC):
    @abstractmethod
    def __init__(self, base):
        pass


class Berserk(AbstractPositive):
    def __init__(self, base):
        self.base = base
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
        self.base = base
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
    @abstractmethod
    def __init__(self, base):
        pass


class Weakness(AbstractNegative):
    def __init__(self, base):
        self.base = base
        self.stats = {
            "Strength": -4,  # сила
            "Endurance": -4,  # выносливость
            "Agility": -4  # ловкость
        }


class EvilEye(AbstractNegative):
    def __init__(self, base):
        self.base = base
        self.stats = {
            "Luck": -10  # удача
        }


class Curse(AbstractNegative):
    def __init__(self, base):
        self.base = base
        self.stats = {
            "Strength": -2,  # сила
            "Perception": -2,  # восприятие
            "Endurance": -2,  # выносливость
            "Charisma": -2,  # харизма
            "Intelligence": -2,  # интеллект
            "Agility": -2,  # ловкость
            "Luck": -2  # удача
        }
