# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors) 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# A > C, B > A, C > B

def part_one(file_path):
	score = 0
	with open(file_path, 'r') as file:
		for line in file.readlines():
			a, b = line.split()
			# Lost 
			if (a == "A" and b == "Z") or (a == "B" and b == "X") or (a == "C" and b == "Y"):
				pass

			# draw
			elif (a == "A" and b == "X") or (a == "B" and b == "Y") or (a == "C" and b == "Z"):
				score += 3
			else:
				score += 6
			score += ord(b)-ord('X')+1
	return score

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
# A for Rock, B for Paper, and C for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors) 


blub = {
	"X": {
		"A" : 3,
		"B" : 1,
		"C" : 2,
	}, "Y" : {
		"A" : 4,
		"B" : 5,
		"C" : 6,
	}, "Z" : {
		"A": 8,
		"B": 9,
		"C": 7
	}
}

def part_two(file_path):
	score = 0
	with open(file_path, 'r') as file:
		for line in file.readlines():
			a, b = line.split()
			score += blub[b][a]
	return score 


def main():
	print(f"Solution 1T: {part_one('test.txt')}")
	print(f"Solution 2T: {part_two('test.txt')}")
	print(f"Solution 1 : {part_one('input.txt')}")
	print(f"Solution 1 : {part_two('input.txt')}")
	
if __name__ == "__main__":
	main()
