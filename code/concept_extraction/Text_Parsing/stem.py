import sys
sys.path.append("../lib")
import en

def stem(word):
	result = en.verb.infinitive(word)
	if len(result) != 0 and en.is_verb(result):
		return result
	result = en.noun.singular(word)
	if len(result) != 0 and en.is_noun(result):
		return result
	return word