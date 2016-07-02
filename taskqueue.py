import os
import time

from celery import Celery
from PIL import Image


app = Celery(__name__,
             broker='redis://127.0.0.1:6379/0',
             backend='redis://127.0.0.1:6379/0')


@app.task
def add(a, b):
    time.sleep(3)
    return a+b


@app.task
def sum2(values):
    print('-'*40)
    print(values)
    time.sleep(3)
    return sum(values)


@app.task
def make_thumbnail(path, width, height):
    if not os.path.isfile(path):
        return

    filepath, ext = os.path.splitext(path)
    output = '{}_thumb{}'.format(filepath, ext)

    im = Image.open(path)
    im.thumbnail([width, height, ], Image.ANTIALIAS)
    im.save(output)
    im.close()

    return output
