import urllib2
import json

def get_commonsense(word, limit):
	rst_list = []
	str1 = 'http://conceptnet5.media.mit.edu/data/5.4/search?end=/c/en/' + word + '&start=/c/en'
	str2 = 'http://conceptnet5.media.mit.edu/data/5.4/search?start=/c/en/' + word + '&end=/c/en'
	response1 = urllib2.urlopen(str1)
	response2 = urllib2.urlopen(str2)
	data1 = json.load(response1)
	data2 = json.load(response2)

	rst_list.extend(extract_n_items(data1, word, min(int(limit / 2), len(data1["edges"]))))
	rst_list.extend(extract_n_items(data2, word, min(int(limit / 2), len(data2["edges"]))))
	return rst_list

def extract_n_items(data, word, n):
	rst_list = []
	for i in range(0, n):
		data_ex = data["edges"][i]["uri"]
		splited_str = data_ex.split(",")
		obj1 = splited_str[1].split("/")[3]
		obj2 = splited_str[2].split("/")[3]
		rst = None
		if obj1 != word :
			rst = obj1
		if obj2 != word :
			rst = obj2
		if rst is None :
			continue
		final_rst = rst.replace("_", " ")
		rst_list.append(final_rst)
	return rst_list