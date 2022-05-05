import random

class Character:
  def __init__(self, name, list):
    self.name = name
    self.attacks = list
    self.health = 50

  def damage(self, hp):
    self.health -= hp

  def rand_attack(self):
    return random.choice(self.attacks)




class Battle:
  def __init__(self, char1, char2):
    self.player = char1
    self.npc = char2
    self.turns = 0
    self.winner = False
    self.player_wins = 0
    self.comp_wins = 0

  def turn_count(self):
    self.turns += 1