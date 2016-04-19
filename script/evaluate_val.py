#!/usr/bin/python
import sys
import os
import json

def calc_score_answer(answer, gt_allanswer):
	correct_count = 0.0
	for gt_answer in gt_allanswer:
		if gt_answer == answer:
			correct_count = correct_count + 1
	if correct_count >= 3:
		return 1.0
	else:
		return float(correct_count) / 3

def convert_json_results_to_lines(json_answers):
	answers = []
	for json_answer in json_answers:
		answers.append(json_answer['answer'])
	return answers

gt_allanswers_file_path = sys.argv[1]
json_answers_file_path = sys.argv[2]

final_total_score = 0.0
with open(gt_allanswers_file_path) as fin_gt:
	gt_allanswers_lines = fin_gt.readlines()
with open(json_answers_file_path) as fin_answer:
	json_answers = json.load(fin_answer)

answers = convert_json_results_to_lines(json_answers)
assert(len(gt_allanswers_lines) == len(answers))
for answer, gt_allanswer_line in zip(answers, gt_allanswers_lines):
	gt_allanswer = gt_allanswer_line.rstrip().split(',')
	final_total_score = final_total_score + calc_score_answer(answer, gt_allanswer)
final_avg_score = final_total_score / len(answers)

print "Evaluation Score is: " + str(final_avg_score) + "\n"