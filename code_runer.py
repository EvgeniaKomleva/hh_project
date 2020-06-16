from os import system


def execute(cmd):
    system(cmd)


execute("scrapy runspider script.py -a file=analyst_it.ini -L WARNING --output=data/data.json && python transform_data.py analyst_it.ini")

