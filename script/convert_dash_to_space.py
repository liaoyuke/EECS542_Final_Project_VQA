#!/usr/bin/python
import sys
import os

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

with open(input_file_path) as fin:
	input_lines = fin.readlines()

fout = open(output_file_path, 'w')
for line in input_lines:
	words = line.rstrip().split('-')
	fout.write(' '.join(words) + "\n")
fout.close()