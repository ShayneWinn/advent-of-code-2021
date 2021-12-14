# 12/13/2021
# Author Shayne Winn

# NOTE: There is very little different between this file and the last (processcommands.py).
#           This is intentional to preserve the original solution. 

import sys
sys.path.append("../common")
import common

def main():
	# capture arguments
	argc = len(sys.argv) - 1
	argv = sys.argv[1::-1]

	# make sure argument count valid
	if not (argc == 1):
		print("Usage: python procomcorrect.py filename")
		exit()

	try:
		lines = common.get_file_lines(argv[0])
		position = get_position_correct(lines)
		print(position)
		print(position[0] * position[1])

	except:
		print("Unable to open file")
		exit()

def get_position_correct(lines):
	depth = 0
	position = 0
	aim = 0

	for line in lines:
		split = line.split(' ')
		if split[0] == "forward":
			position += int(split[1])
			depth += int(split[1]) * aim
		elif split[0] == "down":
			aim += int(split[1])
		elif split[0] == "up":
			aim -= int(split[1])


	return [depth, position]


if __name__ == '__main__':
	main()