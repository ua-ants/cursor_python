# Task 3: Using requests library, download image from this url
#         https://dummyimage.com/600x400/000/fff
#         and save it as a file on your device.

import requests as rq
import os
from shutil import rmtree

url = 'https://dummyimage.com/600x400/000/fff'
wd = 'resources'
f = wd + '/' + 'w03_HW05_TASK03.jpg'
res = rq.get(url)

if wd in os.listdir():
    rmtree(wd)

if res.status_code == 200:
    os.mkdir(os.getcwd() + '/' + wd)
    with open(f, 'wb') as file:
        file.write(res.content)
