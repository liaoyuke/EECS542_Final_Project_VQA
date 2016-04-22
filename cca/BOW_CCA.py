#This script will create the bag of words representation of different texts

from sklearn.cross_decomposition import CCA
from sklearn.externals import joblib
import sys

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

if __name__ == '__main__':
    concepts_file_path = sys.argv[1] # coco_trainval2014_answer.txt
    answer_file_path = sys.argv[2] # coco_trainval2014_concepts.txt
    concept_word_threshold = int(sys.argv[3]) # 6
    answer_word_threshold = 3

    with open(answer_file_path) as f_answer:
        answer_str_list = f_answer.readlines()
    with open(concepts_file_path) as f_concept:
        concept_str_list = f_concept.readlines()
    assert(len(answer_str_list) == len(concept_str_list))

    answers_list = convert_word_str_to_words(answer_str_list, True)
    concepts_list = convert_word_str_to_words(concept_str_list, False)
    num_samples = len(answers_list)
    answers_list = answers_list[:num_samples]
    concepts_list = concepts_list[:num_samples]
    print 'creating word to index map ...'
    answer_index_map, n_answers = create_word_index(answers_list, answer_word_threshold)
    concepts_index_map, n_concepts = create_word_index(concepts_list, concept_word_threshold)
    print '#answers = ' + str(n_answers)
    print '#concepts = ' + str(n_concepts)
    print 'creating bag of words features'
    #Create BOW
    BOW_answers = create_BOW_matrix(answers_list, answer_index_map, n_answers)
    BOW_concepts = create_BOW_matrix(concepts_list, concepts_index_map, n_concepts)
    print 'starts fitting cca model'
    #create the CCA model
    cca = CCA(n_components=1024)
    cca.fit(BOW_concepts,BOW_answers)
    is_gt = False
    if "gt" in concepts_file_path:
        is_gt = True
    cca_save_path = ''
    if is_gt:
        cca_save_path = 'Mycca_gt_' + str(concept_word_threshold) + '.pkl'
    else:
        cca_save_path = 'Mycca_' + str(concept_word_threshold) + '.pkl'
    print 'starts saving trained cca model to ' + cca_save_path
    joblib.dump(cca, cca_save_path, compress = 9)