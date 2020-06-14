import requests
import sys
from configparser import ConfigParser

file = str(sys.argv[3])[5:] #'java.ini'
file1 = file
config = ConfigParser()
config.read(file)


def auth(username, password):
    s = requests.session()

    s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79'})

    r = s.get('https://hh.ru').text

    x = r.find('name="_xsrf"') + 20
    _xsrf = r[x:x + 32]

    data = {'username': username,
            'password': password,
            'backUrl': 'https://hh.ru/',
            'remember': 'yes',
            'action': 'Войти',
            '_xsrf': _xsrf}
    r = s.post('https://hh.ru/account/login?backurl=%2F', data=data)



area = config['parametrs']['area'] #str(input("Enter area number(null - all areas, 1 - Moscow, 2- St. Piterburg, 2019 -MO, more areas-+ https://api.hh.ru/areas): "))
specialization = config['parametrs']['specialization'] # str(input("Enter specialization number (1 - IT, 17- sales, more-https://api.hh.ru/specializations): "))
search_period = config['parametrs']['search_period'] # str(input("Enter search period (1- day,3- 3 days,7,30 - mounth,365): "))
# order_by = str(input("Order by (relevance, publication_time, salary_desc, salary_asc): "))
search_text = config['parametrs']['search_text'].encode('cp1251').decode('utf-8')
auth_status = config['parametrs']['auth_status']  # int(input("Do you whant login? (1-yes, null -no): "))
if (auth_status == 1):
    username = config['account']['username']
    password = config['account']['password']
    auth(username, password)

url = [
    'https://hh.ru/search/resume?clusters=True&area='+area+'&specialization='+specialization+'&order_by=relevance&search_period='+search_period+'&logic=normal&pos=position%2Cworkplace_position&exp_period=last_year&exp_company_size=any&exp_industry=any&no_magic=False&st=resumeSearch&text='+search_text+'&fromSearch=true']
