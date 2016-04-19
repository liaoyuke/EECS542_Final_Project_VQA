#!/usr/bin/python
import sys
import os

question_file_path = sys.argv[1]

dir_path = os.path.dirname(question_file_path)
file_name = os.path.basename(question_file_path)
file_pure_name = file_name.split('.')[0]
file_type = file_name.split('.')[1]
question_file_id_path = dir_path + "/" + file_pure_name + "ID." + file_type

with open(question_file_path) as fin:
    question_strs = fin.readlines()
fout = open(question_file_id_path, 'w')
for i in range(1, len(question_strs) + 1):
    fout.write(str(i) + "\n")
fout.close()