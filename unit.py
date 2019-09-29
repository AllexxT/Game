import random


def damage(min_d=0, max_d=0):
    """
    Decorator which contains setup of range random damage dealing
    of User class steps.
    """
    def decorator(method):
        def wrapper(self, other):
            dmg = random.randint(min_d, max_d)
            other.health -= dmg
            method(self, other, dmg)
        return wrapper
    return decorator


def healing(min_h=0, max_h=0):
    """
    Decorator which contains setup of range random
    healing of User class steps.
    """
    def decorator(method):
        def wrapper(self, other):
            heal = random.randint(min_h, max_h)
            self.health += heal
            if self.health > self.HEALTH_CONST:  # Do not allow get more health points
                self.health = self.HEALTH_CONST  # than given at beginning
            method(self, other, heal)
        return wrapper
    return decorator


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

    @damage(min_d=18, max_d=25)
    def weak_punch(self, other, dmg):
        """Hit method"""
        print('Player %s hits %s by Weak Punch [%d damage]' % (self.name, other.name, dmg))
        print(other)

    @damage(min_d=10, max_d=35)
    def strong_punch(self, other, dmg):
        """Hit method"""
        print('Player %s hits %s by Strong Punch [%d damage]' % (self.name, other.name, dmg))
        print(other)

    @healing(min_h=18, max_h=25)
    def heal(self, other, heal_val):
        """Heal method"""
        print('%s is healed [%d health]' % (self.name, heal_val))
        print(self)

    def next_step(self, other):
        """Randomly chooses kind of the next Unit step"""
        self.step[random.randint(0, len(self.step)-1)](other)

    def __getattribute__(self, item):
        """Increases heal chance by adding one more heal-step
        to the stack of Units steps if his hp become lower then 35%.
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
