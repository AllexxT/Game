import random
import time


class Battle:
    """Battle class"""
    def __init__(self, *players):
        self.players = list(players)     # Convert tuple to list for getting list methods
        self.winner = False              # Flag for breaking self.fight() loop

    def deal_damage(self):
        """Randomly one of Units hits other Unit from self.players list.
        When next Unit 'dies', he will be removed from players list.
        Winner is the last Unit in list.
        """
        dealer = self.next_damage_dealer()
        for fighter in self.players:
            if len(self.players) == 1:
                print('%s is Win with %d health!' % (self.players[0].name, self.players[0].health))
                self.winner = True
                break
            if fighter != dealer:
                dealer.next_step(fighter)
                time.sleep(0.1)
                if fighter.health <= 0:
                    self.players.remove(fighter)
                    print('%s is Killed by %s\n' % (fighter.name, dealer.name))
                    time.sleep(0.2)

    def next_damage_dealer(self):
        """Randomly get next damage dealer from players list"""
        return self.players[random.randint(0, len(self.players)-1)]

    def fight(self):
        """Launches fight loop until self.winner flag is gonna be True"""
        while not self.winner:
            self.deal_damage()
