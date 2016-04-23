#This script will create the bag of words representation of different texts

from sklearn.cross_decomposition import CCA
from sklearn.externals import joblib
from random import randint
import sys
import json

def make_list_of_zeros(num_zeros):
    return [0] * num_zeros

# convert list of lines to list of list
def convert_word_str_to_words(word_str_list, is_answer_list):
    words_list = []
    for word_str in word_str_list:
        if is_answer_list == True:
            words = []
            words.append(word_str.rstrip())
            words_list.append(words)
        else:
            words_list.append(word_str.rstrip().split())
    return words_list

# each word is uniquely mapped to an integer
def create_word_index(words_list, word_threshold):
    word_index_map = {}
    word_count = {}
    for words in words_list:
        for word in words:
            if word in word_count:
                word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1

    index = 0
    for word in word_count:
        if word_count[word] >= word_threshold and word not in word_index_map:
            word_index_map[word] = index
            index = index + 1

    return word_index_map, len(word_index_map)

def create_BOW_vector(words, word_index_map, n_index):
    BOW_vector = make_list_of_zeros(n_index)
    for word in words:
        if word in word_index_map:
            BOW_vector[word_index_map[word]] = 1
    return BOW_vector

def create_BOW_matrix(words_list, word_index_map, n_index):
    BOW_mat = []
    for words in words_list:
        BOW_mat.append(create_BOW_vector(words, word_index_map, n_index))
    validate_BOW(BOW_mat)
    return BOW_mat

def validate_BOW(BOW_mat):
    for BOW_vec in BOW_mat:
        if len(BOW_vec) <= 0:
            print "Wrong BOW_vec"
        for val in BOW_vec:
            if val != 0 and val != 1:
                print "Wrong BOW value"

def sample_data(answers_list, concepts_list, interval):
    assert(len(answers_list) == len(concepts_list))
    #assert(len(answers_list) % interval == 0)
    answers_sample_list = []
    concepts_sample_list = []
    for i in range(0, len(answers_list), interval):
        rand_num = i + randint(0, interval - 1)
        if rand_num >= len(answers_list):
            rand_num = len(answers_list) - 1
        answers_sample_list.append(answers_list[rand_num])
        concepts_sample_list.append(concepts_list[rand_num])
    return answers_sample_list, concepts_sample_list

def save_BOW_as_CSV(BOW_mat, output_file_path):
    f_out = open(output_file_path, 'w')
    for BOW_vec in BOW_mat:
        str_line = ''
        for BOW_num in BOW_vec:
            str_line = str_line + str(BOW_num) + ','
        f_out.write(str_line[:-1] + '\n')
    f_out.close()


if __name__ == '__main__':
    answer_file_path = sys.argv[1] # coco_trainval2014_concepts.txt
    concepts_file_path = sys.argv[2] # coco_trainval2014_answer.txt
    concept_word_threshold = int(sys.argv[3]) # 6
    answer_word_threshold = 9

    with open(answer_file_path) as f_answer:
        answer_str_list = f_answer.readlines()
    with open(concepts_file_path) as f_concept:
        concept_str_list = f_concept.readlines()
    assert(len(answer_str_list) == len(concept_str_list))

    answers_list = convert_word_str_to_words(answer_str_list, True)
    concepts_list = convert_word_str_to_words(concept_str_list, False)
    #num_samples = len(answers_list)
    #answers_list = answers_list[:num_samples]
    #concepts_list = concepts_list[:num_samples]
    print 'starts sampling'
    print 'original length = ' + str(len(answers_list))
    answers_list, concepts_list = sample_data(answers_list, concepts_list, 12)
    print 'sampled length = ' + str(len(answers_list))
    print 'creating word to index map ...'
    answer_index_map, n_answers = create_word_index(answers_list, answer_word_threshold)
    concepts_index_map, n_concepts = create_word_index(concepts_list, concept_word_threshold)

    print 'saving created answer and concepts index map'
    with open('gt_answer_index_map.json', 'w') as outfile:
        json.dump(answer_index_map, outfile)
    with open('gt_concepts_index_map.json', 'w') as outfile:
        json.dump(concepts_index_map, outfile)

    print '#answers = ' + str(n_answers)
    print '#concepts = ' + str(n_concepts)
    print 'creating bag of words features'
    #Create BOW
    BOW_answers = create_BOW_matrix(answers_list, answer_index_map, n_answers)
    BOW_concepts = create_BOW_matrix(concepts_list, concepts_index_map, n_concepts)
    print 'saving bag of words features to files'
    save_BOW_as_CSV(BOW_answers, 'coco_trainval2014_gt_answer_BOW.txt')
    save_BOW_as_CSV(BOW_concepts, 'coco_trainval2014_gt_concepts_BOW.txt')
