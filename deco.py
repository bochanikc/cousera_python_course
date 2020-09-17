from abc import ABC, abstractmethod


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

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects

    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects


class AbstractPositive(AbstractEffect):
    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Berserk(AbstractPositive):
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Strength"] += 7
        self.stats["Endurance"] += 7
        self.stats["Agility"] += 7
        self.stats["Luck"] += 7
        self.stats["Perception"] -= 3
        self.stats["Charisma"] -= 3
        self.stats["Intelligence"] -= 3
        self.stats["HP"] += 50
        return self.stats

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append("Berserk")
        return self.positive_effects


class Blessing(AbstractPositive):
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Strength"] += 2
        self.stats["Perception"] += 2
        self.stats["Endurance"] += 2
        self.stats["Charisma"] += 2
        self.stats["Intelligence"] += 2
        self.stats["Agility"] += 2
        self.stats["Luck"] += 2
        return self.stats

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append("Blessing")
        return self.positive_effects


class Weakness(AbstractNegative):
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Strength"] -= 4
        self.stats["Endurance"] -= 4
        self.stats["Agility"] -= 4
        return self.stats

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append("Weakness")
        return self.negative_effects


class EvilEye(AbstractNegative):
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Luck"] -= 10
        return self.stats

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append("EvilEye")
        return self.negative_effects


class Curse(AbstractNegative):
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Strength"] -= 2
        self.stats["Perception"] -= 2
        self.stats["Endurance"] -= 2
        self.stats["Charisma"] -= 2
        self.stats["Intelligence"] -= 2
        self.stats["Agility"] -= 2
        self.stats["Luck"] -= 2
        return self.stats

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append("Curse")
        return self.negative_effects
