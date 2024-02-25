# template
import os
import copy

YEAR = 2015
DAY = 22

def get_advent_folder_name(year, day):
    base = os.environ["ADVENT_HOME"]
    if not base:
        raise "ADVENT_HOME folder not set"
    
    return f"{base}/{year}/data/day{day}"

def get_data(name="data.txt"):
  data = []
  filename = get_advent_folder_name(YEAR, DAY)
  path = f"{filename}/{name}"
  try:
      file = open(path, 'r')
      return file
  except IOError:
      print(f"Could not fetch file {file} ")
      return None

boss = {"hp": 51, "dmg": 9}

class Effect:
    def __init__(self, name, ttl, effect):
        self.ttl = ttl
        self.name = name
        self.effect = effect

class Spell:
    def __init__(self, name, mana_cost, dmg, hp, effect):
        self.name = name
        self.mana_cost = mana_cost
        self.dmg = dmg
        self.hp = hp
        self.effect = effect

boss = {"hp": 51, "dmg": 9}
player = {"hp": 50, "mana": 500, "armor": 0}

magic_missile = Spell("magic_missile", 53, 4, 0, None)
drain = Spell("drain", 73, 2, 2, None)
shield = Spell("shield", 113, 0, 0, Effect("shield", 6, {"armor": 7}))
poison = Spell("poison", 173, 0, 0, Effect("poison", 6, {"dmg": 3}))
recharge = Spell("recharge", 229, 0, 0, Effect("recharge", 5, {"mana": 101}))

class Player:
    def __init__(self, hp, mana):
        self.hp = hp
        self.mana = mana
        self.total_mana_spent = 0
        self.active_effects = dict()
        self.spells = [magic_missile, drain, shield, poison, recharge]
        self.spell_history = []
    def __copy__(self):
        other = Player(self.hp, self.mana)
        other.active_effects = copy.deepcopy(self.active_effects)
        other.total_mana_spent = self.total_mana_spent
        other.spell_history = [i for i in self.spell_history]
        return other

    def apply_effects(self):
        if recharge.name in self.active_effects:
            self.mana += recharge.effect.effect["mana"]
    
    def update_effects(self):
        for i in self.active_effects:
            self.active_effects[i].ttl -= 1
        self.active_effects = {k:v for k,v in self.active_effects.items() if v.ttl > 0}
    
    def can_use_spell(self, spell):
        if self.mana >= spell.mana_cost:
            if spell.name in self.active_effects:
                return self.active_effects[spell.name].ttl <= 1
            return True
        return False
                 
    def get_armor(self):
        if shield.name in self.active_effects:
            return shield.effect.effect["armor"]
        return 0

    def get_poison(self):
        if poison.name in self.active_effects:
            return 3
        return 0

    def get_available_spells(self):
        return filter(self.can_use_spell, self.spells)
        

class Boss:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg


def handle_player_turn(player, boss, spell, hard_mode):
    p = copy.deepcopy(player)
    b = copy.deepcopy(boss)

    if hard_mode:
        p.hp -= 1
    
    if p.hp <= 0:
        return p,b
    
    p.total_mana_spent += spell.mana_cost
    b.hp -= p.get_poison()
    # print("p.get_poison()", p.get_poison())

    if b.hp <= 0:
        return p,b
    p.spell_history.append(spell.name)
    p.update_effects()

    p.mana -= spell.mana_cost
    p.hp += spell.hp
    b.hp -= spell.dmg

    if b.hp <= 0:
        return p,b

    if spell.effect:
        p.active_effects[spell.name] = spell.effect


    return p,b
def handle_boss_turn(player, boss):
    p = copy.deepcopy(player)
    b = copy.deepcopy(boss)  
    # print("p.get_poison()", p.get_poison())
    b.hp -= p.get_poison()
    if b.hp <= 0:
        return p,b
    boss_dmg_dealt = max(1,b.dmg - p.get_armor())
    p.hp -= boss_dmg_dealt

    p.update_effects()
    return p,b

wins_mana_spent = []

def duel(player, boss, turn = 0, hard_mode = False):
    # if turn > 1000: return
    if player.hp <= 0 or (player.mana <= 0 and recharge.name not in player.active_effects) or (len(wins_mana_spent) > 0 and min(wins_mana_spent) < player.total_mana_spent):
        # print("player is dead at turn", turn-1)
        return
    if boss.hp <= 0: 
        wins_mana_spent.append(player.total_mana_spent)
        # print("boss is dead at turn", turn-1, "from ", player.spell_history, "with total mana spent", player.total_mana_spent)
        return
    p = player
    b = boss
    p.apply_effects()
    # print("handling turn")
    if turn % 2 == 0:
        # player turn
        # print("available spells at turn ", turn, list(map(lambda x: x.name, p.get_available_spells())))
        for spell in p.get_available_spells():
            # print("using spell ", spell.name, "on turn ", turn)
            pp, bb = handle_player_turn(p, b, spell, hard_mode)
            # print(bb.hp)
            if boss.hp <= 0: 
                wins_mana_spent.append(player.total_mana_spent)
                # print("boss is dead at turn", turn-1, "from ", player.spell_history)
                return
            duel(pp,bb,turn+1)
        
    else:
        # boss turn
        pp,bb = handle_boss_turn(p, b)
        duel(pp,bb,turn+1)


def main():
    # duel(Player(10,250), Boss(14, 8))
    duel(Player(50,500), Boss(51, 9))
    print(min(wins_mana_spent))
    wins_mana_spent.clear()
    duel(Player(50,500), Boss(51, 9), True)
    print(min(wins_mana_spent))
    pass

if __name__ == "__main__":
    main()

