#!/usr/bin/python
import sys
import os

input_folder_path = sys.argv[1]
intput_file_prefix = sys.argv[2]
output_file_path = sys.argv[3]
num_splits = int(sys.argv[4])

list_all = []

for i in range(1, num_splits + 1):
	input_file_path = input_folder_path + "/" + intput_file_prefix + str(i) + ".txt"
	with open(input_file_path) as fin:
		list_input = fin.readlines()
	list_all.extend(list_input)

fout = open(output_file_path, 'w')
for line in list_all:
	fout.write(line)
fout.close()