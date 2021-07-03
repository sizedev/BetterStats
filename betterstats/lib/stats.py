class Stat:
    def __init__(self, name: str, dimension: int, value = None):
        self.name = name
        self.dimension = dimension
        self.value = value


class BaseStat(Stat):
    def __init__(self, name: str, dimension: int, value, optional = False):
        super().__init__(name, dimension, value = value)
        self.optional = optional


class DerivedStat(Stat):
    def __init__(self, name: str, dimension: int, value):
        super().__init__(name, dimension, value = value)


class BaseStats:
    def __init__(self):
        pass


class Stats:
    def __init__(self):
        pass
