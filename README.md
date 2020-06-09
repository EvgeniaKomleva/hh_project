# hh_project
 
Программа собирает резюме с hh.ru, отслеживает компании с массовым оттоком сотрудников :

## Как установить

Установите Python пакеты из requirements.txt:

```
pip install -r requirements.txt

```
Запустите скрипты сбора объявлений для сайтов (я предворительно выбрала поиск по Москве и проф. области IT):
```
scrapy runspider script.py -L WARNING --output=data/data.json && python transform_data.py

```
Результаты парсинга сохранятся в *.json файлы внутри каталога data. При повторном запуске парсер добавит новые данные в конец файла и этим сломает JSON, поэтому старые файлы с данными лучше удалять перед повторным запуском. В каталоге resume появляется файл  {current_day}data_sort_new.csv, в котором вы найдете все необходимые данные (count- это число человек, ищущих работу из какой-то определенной компании. Список отсортирован по убыванию count)

## Как изменить параметры

Зайти в файл  get_url. В этом файле происходит формирование url, по которому производиться запрос. По умолчанию ищем резуме IT специалистов по Москве, которые появились в последние 30 дней. За параметры отвечают переменные area, specialization, search_period, auth_status. Можете менять эти параметры, вместо area ставить null - all areas, 1 - Moscow, 2- St. Piterburg, 2019 -MO, more areas- https://api.hh.ru/areas

Вместо specialization ставить 1 - IT, 17- продажи, больше обозначений можно найти на https://api.hh.ru/specializations

Вместо search period можно выбрать из : 1- соответствует 1 дню ,3,7,30 ,365. Все это количестсво дней за которые хотим посмотреть резюме.

Вместо auth_status можно подставить 1 или 0. По умолчанию стоит 0 (т е заходим без использования аккаунта). Если нужно использовать аккант ставим 1 и вводим свой логин и пароль

Если вдруг захочется поменять какие то другие параметры можно зайти на https://hh.ru/search/resume?area=1&isDefaultArea=true&exp_period=all_time&logic=normal&pos=full_text&from=employer_index_header&text=&fromSearch=true, выставить необходимые параметры, скопировать полученную ссылку в переменную url и запустить программу

## Как поставить на расписание 

Хотим чтобы каждый день в папке резюме появлялся новый файл с актуальной информацией
Для этого необходимо создать при задачи. Первая - для удаления файла data/data.json , вторая -для запуска scrapy, третья- для пиона. В меню пуск выбрать планировщик задач, создать  задачу, назвать ее, перейти во вкладку действия, создать действие соответствующее одной из трех поставленных подзадач, перейти во вкладку триггеры и там установть время срабатывания триггера и период, все сохранить. Так делать для каждой задачи.  

Больше информации: https://windowsnotes.ru/powershell-2/zapusk-powershell-skripta-po-raspisaniyu/
