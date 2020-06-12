from os import system
import scrapy


def execute(cmd):
    system(cmd)


execute("scrapy runspider script.py -a file=config.ini -L WARNING --output=data/data.json && python transform_data.py config.ini")

