# 12/13/2021
# Author: Shayne Winn

import sys

def main():
	# capture arguments
	argc = len(sys.argv) - 1
	argv = sys.argv[1::-1]

	# make sure argument count valid
	if not (argc == 1):
		print("Usage: python numincrease.py filename")
		exit()

	# file stuff
	try:
		# open file
		file = open(argv[0], "rt")
		# separate numbers
		lines = file.read().splitlines()
		nums = [int(i) for i in lines]

		# close file
		file.close()
	except:
		# print error
		print("Unable to open file")
		exit()

	# call function
	print(num_increasing(nums))


def num_increasing(nums):
	count = 0
	for i in range(1, len(nums)):
		if(nums[i] > nums[i-1]):
			count += 1
	return count


if __name__ == '__main__':
	main()
