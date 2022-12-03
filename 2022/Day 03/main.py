def part_one(file_path):
	prio = 0
	with open(file_path, 'r') as file:
		for line in file.readlines():
			line = line.strip()
			lhs, rhs = set(line[:len(line)//2]), set(line[len(line)//2:])
			duplicate = lhs.intersection(rhs).pop()
			if duplicate.islower():
				score = ord(duplicate) - ord('a') + 1
			else:
				score = ord(duplicate) - ord('A') + 1 +26
			prio += score
	return prio


def part_two(file_path):
	prio = 0
	with open(file_path, 'r') as file:
		lines = file.readlines()
		for i in range(len(lines)//3):
			elves = set(lines[i*3]).intersection(set(lines[i*3+1]), set(lines[i*3+2]))
			elves.discard("\n")
			badge = elves.pop()
			if badge.islower():
				score = ord(badge) - ord('a') + 1
			else:
				score = ord(badge) - ord('A') + 1 +26
			prio += score
	return prio

def main():
	print(f"Solution 1T: {part_one('test.txt')}")
	print(f"Solution 2T: {part_two('test.txt')}")
	print(f"Solution 1 : {part_one('input.txt')}")
	print(f"Solution 2 : {part_two('input.txt')}")
	
if __name__ == "__main__":
	main()
