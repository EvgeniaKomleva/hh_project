import pandas as pd
import datetime
from configparser import ConfigParser

file = 'config.ini'
config = ConfigParser()
config.read(file)

current_datetime = str(datetime.datetime.now())
current_day = current_datetime[0:4]+current_datetime[5:7]+current_datetime[8:11]

data = pd.read_json('data/data.json')
data["href"] = 'https://hh.ru'+data["href"]
count_company = data["last_work_plase"].value_counts()
df_count_company = pd.DataFrame({'last_work_plase':count_company.index, 'count':count_company.values})
data_with_count = data.set_index('last_work_plase').join(df_count_company.set_index('last_work_plase'))
sorted_data = data_with_count.sort_values(by=["count"], ascending=False)
sorted_data.drop(["Индивидуальное предпринимательство / частная практика / фриланс"], inplace = True, errors='ignore')
sorted_data.drop(["Фриланс"], inplace = True, errors='ignore')
sorted_data.drop(["Freelance"], inplace = True, errors='ignore')
sorted_data.drop(["фриланс"], inplace = True, errors='ignore')
sorted_data.to_csv('resume/{}{}data_sort.csv'.format(config['parametrs']['search_text'], current_day), sep='\t', index=False)
