from itertools import cycle, product

P1_START = 9
P2_START = 6
P1_TEST = 4
P2_TEST = 8

die_rolls = [sum(x) for x in list(product([1, 2, 3], repeat=3))]
KB = {}

def pawn(loc):
    return 10 if loc%10 == 0 else loc%10


def part_one():
    locations = [P1_START, P2_START]
    scores = [0,0]
    die = cycle(range(1, 101))
    rolled = turn = 0
    for roll, d in enumerate(die, 1):
        rolled += d
        if roll % 3 == 0:
            new_pos = pawn(locations[turn]+rolled)
            if scores[turn]+new_pos >= 1000:
                return roll*scores[1-turn]
            locations[turn] = new_pos
            scores[turn] += new_pos
            rolled = 0
            turn = 1- turn
  

def part_two():
    return max(recursion(0, [9,6], [0,0]))


def recursion(turn, locations, scores):
    if f"{turn} {locations} {scores}" in KB.keys():
        return KB[f"{turn} {locations} {scores}"]
    cur_score = scores[turn]
    wins = [0,0]
    for x in die_rolls:
        new_pos = pawn(locations[turn]+x)
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
    KB[f"{turn} {locations} {scores}"] = wins
    return wins


def main():
    print("(1) What do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?")
    print(f"Answer: {part_one()}")
    print("(2) Find the player that wins in more universes; in how many universes does that player win?")
    print(f"Answer: {part_two()}")


main()
