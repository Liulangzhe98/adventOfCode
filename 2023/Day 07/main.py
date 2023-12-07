from enum import Enum, auto
from dataclasses import dataclass
from collections import Counter



@dataclass
class Hand:
    bid: int
    cards: list
    cards_str: str
    rank: int

def part_one(file_path):
    hands = []
    cards = {str(x): e for e, x in enumerate(reversed(["A", "K", "Q", "J", "T"] + list(range(9, 0, -1))))}
    
    with open(file_path, 'r') as file:
        for line in file.read().strip().splitlines():
            hand, bid = line.split(" ")
            split_hand = [cards[c] for c in hand]
            counted = list(Counter(split_hand).values())
            if len(counted) == 1:
                rank = 6
            elif 4 in counted:
                rank = 5
            elif 3 in counted and 2 in counted:
                rank = 4
            elif 3 in counted:
                rank = 3
            elif counted.count(2) == 2:
                rank = 2
            elif 2 in counted:
                rank = 1
            else:
                rank = 0
            hands.append(Hand(bid=int(bid), cards=split_hand, cards_str=hand, rank=rank))
    sorted_hands = (sorted(hands, key=lambda x: (x.rank, x.cards), reverse=False))
    return sum(e*x.bid for e, x in enumerate(sorted_hands, 1))


def part_two(file_path):
    hands = []
    cards = {str(x): e for e, x in enumerate(reversed(["A", "K", "Q", "T"] + list(range(9, 0, -1)) + ["J"]))}
    
    with open(file_path, 'r') as file:
        for line in file.read().strip().splitlines():
            hand, bid = line.split(" ")
            split_hand = [cards[c] for c in hand]
            full_count = Counter(split_hand)
            counted = sorted(list(Counter(split_hand).values()), reverse=True)
            amount_jokers = full_count[0]
            if counted[0] == 5 \
                or counted[0] + amount_jokers == 5 \
                or counted[1] + amount_jokers == 5:
                rank = 6
            elif counted[0] == 4 \
                or (counted[0] + amount_jokers == 4 and len(counted) == 3) \
                or counted[1] + amount_jokers == 4:
                rank = 5
            elif [3, 2] == counted[:2] \
                or ([3,1] == counted[:2] and amount_jokers == 1) \
                or ([2,2] == counted[:2] and amount_jokers == 1):
                rank = 4
            elif counted[0] == 3 \
                or counted[0] + amount_jokers == 3 \
                or counted[1] + amount_jokers == 3:
                rank = 3
            elif [2,2] == counted[:2] \
                or ([2,1] == counted[:2] and amount_jokers == 1):
                rank = 2
            elif counted[0] == 2 or amount_jokers == 1:
                rank = 1
            else:
                rank = 0
            hands.append(Hand(bid=int(bid), cards=split_hand, cards_str=hand, rank=rank))
    sorted_hands = (sorted(hands, key=lambda x: (x.rank, x.cards), reverse=False))
    return sum(e*x.bid for e, x in enumerate(sorted_hands, 1))


def timed_print(text, func, file):
    import time
    start = time.time()
    result = func(file)
    end = time.time()
    print(f"\033[96m{text} took {(end-start)*1000:>8.2f}ms : {result} \033[0m")


def main():
    timed_print("Solution 1T", part_one, "test.txt")
    timed_print("Solution 2T", part_two, "test.txt")
    timed_print("Solution 1 ", part_one, "input.txt")
    timed_print("Solution 2 ", part_two, "input.txt")
    

if __name__ == "__main__":
    main()
