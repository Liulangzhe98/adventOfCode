class Monkey(object):
    """docstring for Monkey"""
    def __init__(self, items, operation, test, next_m):
        super(Monkey, self).__init__()
        self.items = items
        self.operation = operation
        self.test = test 
        self.next_m = next_m[::-1] # So that true goes to index 1 and false to 0
        self.inspected = 0

    def add_item(self, item):
        self.items.append(item)

    def pop_item(self):
        self.inspected += 1
        return self.items.pop(0)
    
def parser(monkey_blob):
    lines = monkey_blob.splitlines()
    items = [int(x) for x in lines[1].split(":")[1].split(",")]
    op = lines[2].split("=")[1].strip()
    test = int(lines[3].split("by ")[1].strip())
    next_m = [int(x) for i in [4, 5] for x in lines[i].split("monkey ")[1]]
    return Monkey(items, op, test, next_m)

def solve(monkeys, rounds=20, operator = "//3"):
    for _ in range(rounds):
        for m in monkeys:
            while m.items != []:
                old = m.pop_item()
                new = eval(f"({m.operation}) {operator}") 
                monkeys[m.next_m[new % m.test == 0]].add_item(new)
    monkeys = sorted(monkeys, key=lambda x: x.inspected, reverse=True)
    return monkeys[0].inspected*monkeys[1].inspected


def part_one(file_path):
    monkeys : list[Monkey] = []
    with open(file_path, 'r') as file:
        for monkey in file.read().split("\n\n"):
            monkeys.append(parser(monkey))
    return solve(monkeys)


def part_two(file_path):
    monkeys : list[Monkey] = []
    with open(file_path, 'r') as file:
        for monkey in file.read().split("\n\n"):
            monkeys.append(parser(monkey))
    modulo = 1
    for m in monkeys:
        modulo *= m.test
    return solve(monkeys, 10000, f"%{modulo}")


def main():
    print(f"Solution 1T: {part_one('test.txt')}")
    print(f"Solution 2T: {part_two('test.txt')}")
    print(f"Solution 1 : {part_one('input.txt')}")
    print(f"Solution 2 : {part_two('input.txt')}")
    

if __name__ == "__main__":
    main()
