# template
import os
import math
import itertools
import functools

YEAR = 2015
DAY = 21

def stat(cost, damage, armor, name="Nothing"):
    return {"cost": cost, "damage": damage, "armor": armor, "name": name}

weapons = [stat(8,4,0, "Dagger"),stat(10,5,0, "Shortsword"),stat(25,6,0, "Warhammer"),stat(40,7,0, "Longsword"),stat(74,8,0, "Greataxe")]
armor =   [stat(0,0,0, "Leather"), stat(13,0,1, "chain"),stat(31,0,2, "splint"),stat(53,0,3, "Banded"),stat(75,0,4, "Plate"),stat(102,0,5)]
rings =   [stat(25,1,0, "+1 Atk"),stat(50,2,0, "+2 Atk"),stat(100,3,0, "+3 Atk"),stat(20,0,1, "+1 Def"),stat(40,0,2, "+2 Def"),stat(80,0,3, "+3 Def")]    

weapons_combos = weapons
armor_combos = armor
rings_combos = list(itertools.chain( [stat(0,0,0)], rings, itertools.combinations(rings,2)))

# for i in rings_combos:
#     if type(i) == tuple:
#         to_print = ",".join((d["name"] for d in i))
#         print(to_print)
#     else:
#         print(i)

def combine_rings(ring1, ring2):
    c_cost = ring1["cost"]+ring2["cost"]
    c_damage = ring1["damage"]+ring2["damage"]
    c_armor = ring1["armor"]+ring2["armor"]
    return stat(c_cost, c_damage, c_armor, ",".join([ring1["name"], ring2["name"]]) )



def all_combinations():
    for w in weapons_combos:
        # print(f"""with weapon={w["name"]}""")
        for a in armor_combos:
            for r in rings_combos:
                ring_contributions = r if type(r) != tuple else functools.reduce(combine_rings, r, stat(0,0,0))
                name = ",".join([w["name"], a["name"], ring_contributions["name"]])
                dmg = w["damage"] + ring_contributions["damage"]
                shd = a["armor"] + ring_contributions["armor"]
                cost = w["cost"] + a["cost"] + ring_contributions["cost"]
                yield  {"hp": 100, "damage": dmg, "armor": shd, "cost": cost, "name": name}

enemy = {"hp": 104, "damage": 8, "armor": 1}
elf  = {"hp": 100, "damage": 0, "armor": 0}

# returns true if person one can defeat person two
def duel(player, boss): 

    
    player_dmg_dealt = player["damage"] - boss["armor"]
    player_dmg_dealt = 1 if player_dmg_dealt <= 0 else player_dmg_dealt
    
    boss_dmg_dealt = boss["damage"] - player["armor"]
    boss_dmg_dealt = 1 if boss_dmg_dealt <= 0 else boss_dmg_dealt
    

    player_turns = math.ceil(boss["hp"] / player_dmg_dealt)
    boss_turns = math.ceil(player["hp"] / boss_dmg_dealt)

#     print(f"""Player has {player["name"]} items""")
#     print(f"""
#     items={player["name"]}
#     attack={player["damage"]}
#     shield={player["armor"]}
#     cost={player["cost"]}
#     player dmg dealt = {player_dmg_dealt}
#     boss dmg dealt = {boss_dmg_dealt}
#     player_turns = {player_turns}
#     boss_turns = {boss_turns}
# ----------------------------------
# """)

    return player_turns <= (boss_turns)



def main():

    min_gold = 1000000000
    max_gold = -1
    for elf in all_combinations():
        player_win = duel(elf, enemy)
        gold = elf["cost"]
        items = elf["name"]
        if player_win:
            print(f"Elf won with {items} for {gold} gold")
            min_gold = min(min_gold, gold)
        else:
            max_gold = max(max_gold, gold)
    print(f"Player won using {min_gold} gold")
    print(f"Player lost using {max_gold} gold")


if __name__ == "__main__":
    main()

