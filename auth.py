import requests

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
print(r.text)