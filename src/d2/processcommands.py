# 12/13/2021
# Author Shayne Winn

import sys
sys.path.append("../common")
import common

def main():
	# capture arguments
	argc = len(sys.argv) - 1
	argv = sys.argv[1::-1]

	# make sure argument count valid
	if not (argc == 1):
		print("Usage: python processcommands.py filename")
		exit()

	try:
		lines = common.get_file_lines(argv[0])
		position = get_position(lines)
		print(position)
		print(position[0] * position[1])

	except:
		print("Unable to open file")
		exit()

def get_position(lines):
	depth = 0
	position = 0

	for line in lines:
		split = line.split(' ')
		if split[0] == "forward":
			position += int(split[1])
		elif split[0] == "down":
			depth += int(split[1])
		elif split[0] == "up":
			depth -= int(split[1])


	return [depth, position]


if __name__ == '__main__':
	main()