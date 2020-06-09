import schedule
import time
import os

def job():
    os.popen("scrapy runspider script.py -L WARNING --output=data/data8.json ")


def cod():
    os.popen("python transform_data.py")





schedule.every(15).seconds.do(job)

if __name__ == '__main__':
    schedule.every(5).seconds.do(job)
    schedule.every(15).seconds.do(cod)
    while True:
        schedule.run_pending()
        time.sleep(1)
