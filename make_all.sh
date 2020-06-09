#!/bin/bash
#!/usr/bin/env bash
scrapy runspider script.py -L WARNING --output=data/data5.json
python transform_data.py


for all: scrapy runspider script.py -L WARNING --output=data/data7.json && python transform_data.py

