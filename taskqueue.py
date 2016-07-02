import time

from celery import Celery


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
