# Task 2: This is a test of your googling skills :D Using csv module from Standard Library,
#        create a simple csv file of your study group (field names would be "First name",
#        "Last name", "Telegram tag"). You need to use csv.DictWriter class.
#         All the necessary data can be found in documentation.
#         To check how the file looks - open it in excel or any similar program.

# source: https://docs.python.org/3/library/csv.html class csv.DictWriter


import csv
import pprint
import os

cursor_group = {
    1: {"First name": "Andrii", "Last name" : "Tsybulskyi", "Telegram tag": "@ants_ua"},
    2: {"First name": "Alexander", "Last name" : "Kozhokar", "Telegram tag": "@hey_alex"},
    3: {"First name": "Ostap", "Last name" : "Rodomansky", "Telegram tag": "@ostap_rodomansky"},
    4: {"First name": "Victoriia", "Last name" : "Frolova", "Telegram tag": None},
    5: {"First name": "Oleksandr", "Last name" : "Zheliazkov", "Telegram tag": "@pjotr98"},
    6: {"First name": "Igor", "Last name" : "Slobodaniuk", "Telegram tag": "@Igor_Sl"},
    7: {"First name": "Ihor", "Last name" : None, "Telegram tag": "@ihor_95"},
    8: {"First name": "Aleksander", "Last name" : "Vechirko", "Telegram tag": "@alexvechirko"},
    9: {"First name": "Dmytro", "Last name" : "Melnyk", "Telegram tag": "@Ekut_v"},
    10: {"First name": "Yevheniia", "Last name" : "Kyryliuk", "Telegram tag": "@EvgeniaCURSOR"},

}

f = 'cursor_group_telegram_users.csv'


# create csv file
with open(f, 'w', newline='') as csvfile:
    field_names = ["First name", "Last name", "Telegram tag"]
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    for p in cursor_group.values():
        writer.writerow(p)

# read and print csv file
try:
    with open(f, 'r+', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        pprint.pprint(list(reader))
except FileNotFoundError:
    print('File Not Found')

# remove csv file
try:
    os.remove(os.getcwd() + '/' + f)
except FileNotFoundError:
    pass
