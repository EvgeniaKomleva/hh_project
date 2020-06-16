from os import system


def execute(cmd):
    system(cmd)


execute("scrapy runspider script.py -a file=java.ini -L WARNING --output=data/data.json && python transform_data.py java.ini")

