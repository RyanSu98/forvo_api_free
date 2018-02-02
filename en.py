#!/usr/bin/env python3
import re
import requests
import json
import base64

def getEnglishPronunciation(word):
	webPageUrl = "https://forvo.com/word/%s/#en" % word
	webPageText = requests.get(webPageUrl).text
	englishPageTextList = re.findall("<em id=\"en.*?</article>", webPageText, re.DOTALL)
	if len(englishPageTextList) == 0:
		return '{"status":"error"}'
	englishPageText = englishPageTextList[0]
	pronunciations = re.findall("Play\(\d+,'(.*?)'", englishPageText)
	for l in range(len(pronunciations)):
		pronunciations[l] = base64.b64decode(pronunciations[l].decode())
	return json.dumps(pronunciations)