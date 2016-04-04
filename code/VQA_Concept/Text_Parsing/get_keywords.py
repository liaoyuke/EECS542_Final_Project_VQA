import sys
sys.path.append("../lib/python-client-sdk-master")

from cortical.client import ApiClient
from cortical.termsApi import TermsApi
from cortical.textApi import TextApi

def get_keywords(sentence):
	client = ApiClient(apiKey="5eeadef0-f9f6-11e5-8378-4dad29be0fab", apiServer="http://api.cortical.io/rest")
	api = TextApi(client)
	keywordList = api.getKeywordsForText("en_associative", sentence)
	print(keywordList)