# 12/13/2021
# Author: Shayne Winn

import sys
import numincrease

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

	# call functions
	sums = sliding_sums(nums)
	print(numincrease.num_increasing(sums))


def sliding_sums(nums):
	sums = [];
	for i in range(0, len(nums) - 2):
		sums.append(nums[i] + nums[i+1] + nums[i+2]);
	return sums


if __name__ == "__main__":
	main()