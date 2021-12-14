# 12/13/2021
# Author: Shayne Winn

import sys

def get_file_lines(filename):
	# open file
	file = open(filename, "rt")
	# separate lines
	lines = file.read().splitlines()
	# close file
	file.close()
	# return
	return lines
