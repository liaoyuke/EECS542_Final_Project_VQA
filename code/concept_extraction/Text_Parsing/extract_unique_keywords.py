input_files = []
input_files.append("questions/coco_trainval2014_question_keywords_stem.txt")
input_files.append("questions/coco_test-dev2015_question_keywords_stem.txt")
input_files.append("objects/coco_trainval2014_objects_stem.txt")


output_file = "concepts/unique_keywords.txt"

unique_keywords = set()
for input_file in input_files:
    with open(input_file) as fin:
        list_str_words = fin.readlines()
        for str_words in list_str_words:
            str_words = str_words.rstrip()
            words = str_words.split('-')
            for word in words:
                if len(word) > 0:
                    unique_keywords.add(word)

fout = open(output_file, 'w')
for unique_keyword in unique_keywords:
    fout.write(unique_keyword + '\n')
fout.close()