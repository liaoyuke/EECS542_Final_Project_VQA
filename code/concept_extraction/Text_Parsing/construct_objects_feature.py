#!/usr/bin/python
import sys
import json
from stem import *

question_file_path = sys.argv[1]
objects_file_path = sys.argv[2]
output_file_path = sys.argv[3]


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

with open(objects_file_path) as objects_file:
    objects_list = objects_file.readlines()

objects_features = []
for objects_str in objects_list:
    objects_str = objects_str.rstrip()
    objects_feature = []
    if len(objects_str) == 0:
        objects_features.append(objects_feature)
        continue
    objects = objects_str.split('-')
    objects_feature = list(set(objects))
    objects_features.append(objects_feature)

assert(len(question_features) == len(objects_features))

question_objects_features = []
for i in range(len(question_features)):
    print i
    question_objects_feature = []
    for question_word in question_features[i]:
        #question_concept_feature.append(stem(question_word))
        question_objects_feature.append(stem(question_word))
    for objects_word in objects_features[i]:
        #question_concept_feature.append(stem(concept_word))
        question_objects_feature.append(stem(objects_word))
    question_objects_features.append(question_objects_feature)

fout = open(output_file_path, 'w')
for question_objects_feature in question_objects_features:
    question_objects_str = ' '.join(question_objects_feature)
    # print question_concept_str
    fout.write(question_objects_str + '\n')
fout.close()