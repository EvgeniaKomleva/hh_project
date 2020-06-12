# hh_project
 
Программа собирает резюме с hh.ru, отслеживает компании с массовым оттоком сотрудников :

## Как установить

Установите Python пакеты из requirements.txt:

```
pip install -r requirements.txt

```
Запустите скрипты сбора объявлений для сайтов (я предворительно выбрала поиск по Москве и проф. области IT):
```
scrapy runspider script.py -a file=config.ini -L WARNING --output=data/data.json && python transform_data.py config.ini

```
Вы можете заменить config.ini на другой файл(файл с другими значениями, но сходной структурой)
Результаты парсинга сохранятся в *.json файлы внутри каталога data. При повторном запуске парсер добавит новые данные в конец файла и этим сломает JSON, поэтому старые файлы с данными лучше удалять перед повторным запуском. В каталоге resume появляется файлы  {seach_text}{current_day}data_sort.csv и {seach_text}{current_day}company_count.csv, в которых вы найдете все необходимые данные (count- это число человек, ищущих работу из какой-то определенной компании. Список отсортирован по убыванию count)

## Как изменить параметры

Зайти в файл  config.ini. В этом файле передаются параметры для формирование url, по которому производиться запрос. По умолчанию ищем резюме джавистов по Москве, которые появились в последние 30 дней. За параметры отвечают переменные area, specialization, search_period, auth_status, search_text. Можете менять эти параметры: 

Вместо area ставить null - all areas, 1 - Moscow, 2- St. Piterburg, 2019 -MO, more areas- https://api.hh.ru/areas

Вместо specialization ставить 1 - IT,5 - Банки, инвестиции, лизинг,  17- продажи, больше обозначений можно найти на https://api.hh.ru/specializations

Вместо search period можно выбрать из : 1- соответствует 1 дню ,3,7,30 ,365. Все это количестсво дней за которые хотим посмотреть резюме.

Вместо search_text вставлять любой текст, который обычно пишете в поисковой строке на сайте hh. Например, аналитик или java

Вместо auth_status можно подставить 1 или 0. По умолчанию стоит 0 (т е заходим без использования аккаунта). Если нужно использовать аккаунт ставим 1 и вводим свой логин и пароль

Если вдруг захочется поменять какие то другие параметры можно зайти на https://hh.ru/search/resume?area=1&isDefaultArea=true&exp_period=all_time&logic=normal&pos=full_text&from=employer_index_header&text=&fromSearch=true, выставить необходимые параметры, скопировать полученную ссылку в переменную url и запустить программу

## Как поставить на расписание 

Хотим чтобы каждый день в папке резюме появлялся новый файл с актуальной информацией
Для этого необходимо создать в планировщике задач windows три задачи. Первая - для удаления файла data/data.json , вторая -для запуска scrapy, третья- для питона. В меню пуск выбрать планировщик задач, создать  задачу, назвать ее, перейти во вкладку действия, создать действие соответствующее одной из трех поставленных подзадач, перейти во вкладку триггеры и там установть время срабатывания триггера и период, все сохранить. Так делать для каждой задачи.  

Больше информации: https://windowsnotes.ru/powershell-2/zapusk-powershell-skripta-po-raspisaniyu/


## Как запустить если нет IDE

```
cd build\exe.win-amd64-3.7

```

https://www.youtube.com/watch?v=n2Cr_YRQk7o
