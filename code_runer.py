from os import system


def execute(cmd):
    system(cmd)


execute("scrapy runspider script.py -a file=analyst.ini -L WARNING --output=data/data.json && python transform_data.py analyst.ini")

