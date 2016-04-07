#!/usr/bin/python
import sys
from get_keywords import *

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

with open(input_file_path) as fin:
    questions = fin.readlines()
i = 1
answer_strs = []
for question in questions:
    print i
    i = i + 1
    question = question.rstrip()
    answer = get_keywords(question)
    answer_str = '-'.join(answer)
    print answer_str
    answer_strs.append(answer_str)

fout = open(output_file_path, 'w')
for answer_str in answer_strs:
    fout.write(answer_str + '\n')

fout.close()