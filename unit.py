import random


class Unit:
    """Unit class.
    Expandable by adding new kinds of steps
    """
    def __init__(self, health=100, name='Computer', heal_boost=False):
        self.name = name
        self.health = health
        self.HEALTH_CONST = health
        self.heal_boost = heal_boost        # Set flag for increasing heal chance of Unit
        self.step = [self.weak_punch, self.strong_punch, self.heal]

    def weak_punch(self, other):
        """Hit method"""
        other.health -= random.randint(18, 25)
        print('Player %s hits %s by Weak Punch' % (self.name, other.name))
        print(other)

    def strong_punch(self, other):
        """Hit method"""
        other.health -= random.randint(10, 35)
        print('Player %s hits %s by Strong Punch' % (self.name, other.name))
        print(other)

    def heal(self, other):
        """Heal method"""
        self.health += random.randint(18, 25)
        if self.health > self.HEALTH_CONST:         # Do not allow get more health points
            self.health = self.HEALTH_CONST         # than given at beginning
        print('%s is healed' % self.name)
        print(self)

    def next_step(self, other):
        """Randomly chooses kind of the next Units step"""
        self.step[random.randint(0, len(self.step)-1)](other)

    def __getattribute__(self, item):
        """Increases heal chance by adding one more heal-step
        to the stack of Units steps if his hp become lower then 30%.
        Requires self.heal_boost = True.
        """
        superget = object.__getattribute__
        if superget(self, 'heal_boost'):
            if superget(self, 'health') < superget(self, 'HEALTH_CONST') * 35 / 100:
                superget(self, 'step').append(superget(self, 'heal'))
                print("%s's healing chance is increased!!!" % superget(self, 'name'))
                superget(self, '__dict__')['heal_boost'] = False
        return superget(self, item)

    def __str__(self):
        if self.health < 0:
            return '%s have 0 health' % self.name
        return '%s have %d health\n' % (self.name, self.health)
