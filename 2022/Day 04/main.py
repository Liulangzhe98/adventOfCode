import re

# between 227 and 653
def part_one(file_path):
	fully = 0
	with open(file_path, 'r') as file:
		for line in file.readlines():
			f_min, f_max, s_min, s_max = [int(x) for x in re.match("(\d+)-(\d+),(\d+)-(\d+)", line).groups()]
			
			if(f_min >= s_min and f_max <= s_max) or (s_min >= f_min and s_max <= f_max):
				fully += 1
	return fully

# 961 too high
def part_two(file_path):
	overlap = 0
	with open(file_path, 'r') as file:
		for line in file.readlines():
			f_min, f_max, s_min, s_max = [int(x) for x in re.match("(\d+)-(\d+),(\d+)-(\d+)", line).groups()]
			
			if (f_max >= s_min and f_min <= s_max) :
				overlap += 1


	return overlap

def main():
	print(f"Solution 1T: {part_one('test.txt')}")
	print(f"Solution 2T: {part_two('test.txt')}")
	print(f"Solution 1 : {part_one('input.txt')}")
	print(f"Solution 2 : {part_two('input.txt')}")
	
if __name__ == "__main__":
	main()
