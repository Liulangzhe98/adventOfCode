

def main():
	most_cal = []
	with open('input.txt', 'r') as file:
		for e in file.read().split("\n\n"):
			most_cal.append( 
				sum([int(x) for x in e.split("\n")]))
	most_cal.sort()
	print(f"Solution 1: {most_cal[-1]}")
	print(f"Solution 2: {sum(most_cal[-3:])}")



if __name__ == "__main__":
	main()