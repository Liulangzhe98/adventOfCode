from itertools import cycle, product
from itertools import combinations_with_replacement as comb

P1_START = 9
P2_START = 6
P1_TEST = 4
P2_TEST = 8



def part_one():
    players = [
        {
            'pos': P1_START,
            'score': 0
        },{
            'pos': P2_START,
            'score': 0
        }
    ]

    die = cycle(range(1, 101))
    rolled = 0
    turn = 0
    for roll, d in enumerate(die, 1):
        rolled += d
        if roll % 3 == 0:
            new_pos = (players[turn]['pos'] + rolled) %10
            players[turn]['pos'] = (10 if new_pos == 0 else new_pos)
            players[turn]['score'] += players[turn]['pos']
            if players[turn]['score'] >= 1000:
                break
            rolled = 0
            turn = 1- turn
    return roll*players[1-turn]['score']

def rotate(loc):
    return 10 if loc%10 == 0 else loc%10

import json

die_rolls = [sum(x) for x in list(product([1, 2, 3], repeat=3))]


KB = {}

def recursion(turn, locations, scores):
    if f"Player {turn+1} at {locations} {scores}" in KB.keys():
        return KB[f"Player {turn+1} at {locations} {scores}"]
    cur_loc = locations[turn]
    cur_score = scores[turn]
    wins = [0,0]
    for x in die_rolls:
        new_pos = rotate(cur_loc+x)
        if cur_score+new_pos >= 21:
            wins[turn] += 1
        else:
            new_l = locations.copy()
            new_l[turn] = new_pos
            new_s = scores.copy()
            new_s[turn] = cur_score+new_pos
            p1, p2 = recursion(1-turn, new_l, new_s)
            wins[0] += p1
            wins[1] += p2
    KB[f"Player {turn+1} at {locations} {scores}"] = wins
    return wins


def main():
    print("(1) What do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?")
    print(f"Answer: {part_one()}")
    print("(2) Find the player that wins in more universes; in how many universes does that player win?")
    print(f"Answer: {max(recursion(0, [9,6], [0,0]))}")



    



            
main()
