#!/usr/bin/python
import sys
import json
from stem import *

question_file_path = sys.argv[1]
output_file_path = sys.argv[2]

question_features = []
with open(question_file_path) as question_file:
    questions = question_file.readlines()
for question in questions:
    question_feature = []
    question = question.rstrip()
    question_words = question.split(' ')
    for question_word in question_words:
        question_feature.append(question_word)
    question_features.append(question_feature)


question_stem_features = []
for i in range(len(question_features)):
    print i
    question_stem_feature = []
    for question_word in question_features[i]:
        question_stem_feature.append(stem(question_word))
    question_stem_features.append(question_stem_feature)

fout = open(output_file_path, 'w')
for question_stem_feature in question_stem_features:
    question_stem_str = ' '.join(question_stem_feature)
    # print question_concept_str
    fout.write(question_stem_str + '\n')
fout.close()