#!/usr/bin/python
import sys
import os

input_file_path = sys.argv[1]
output_folder_path = sys.argv[2]
num_splits = int(sys.argv[3])

os.path.splitext

with open(input_file_path) as fin:
    list_input = fin.readlines()

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

num_lines = len(list_input)
split_num_lines = num_lines / num_splits + 2
current_line = 0
for i in range(1, num_splits + 1):
    output_file_path = output_folder_path + "/" + str(i) + ".txt"
    fout = open(output_file_path, 'w')
    for j in range(split_num_lines):
        fout.write(list_input[current_line])
        current_line = current_line + 1
        if current_line == len(list_input):
            break
    fout.close()