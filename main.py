import sqlite3
import requests
import json
import datetime
from pprint import pprint

connection = sqlite3.connect('carelink_waiting_time.db')

cursor = connection.cursor()

#command1 = """ CREATE TABLE IF NOT EXISTS testing_load(name TEXT, time TEXT, load INTEGER) """
#cursor.execute(command1)

url = 'https://fileupload.carelink.dk/activefeed.json'
payload = {}
headers = {
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
response = requests.request("GET", url, headers=headers, data=payload)
decode_response = response.text.encode().decode('utf-8-sig')
data = json.loads(decode_response)
time = datetime.datetime.now()
command2 = """ INSERT INTO testing_load(name, load, time) VALUES (?, ?, ?)"""

for test_place in data:
    name = test_place['Name']
    load = test_place['Load']
    entries = (name, load, time)
    cursor.execute(command2, entries)
    connection.commit()
    print(test_place)

connection.close()