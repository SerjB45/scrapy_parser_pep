# Проект scrapy parser pep

## Описание
Парсер документов PEP на базе фреймворка Scrapy.
Программа собирает информацию о PEP-документах, анализирует их статусы и формирует документы в CSV формате.

После выполнения программы мы получаем два документа: 
1. Файл со списком PEP 
2. Файл со сводным отчетом по статусам 

## Как развернуть проект:
Клонировать проект:

git clone https://github.com/SerjB45/scrapy_parser_pep.git

Перейти в проект, создать и активировать виртуальное окружение(проект реализован на версии python 3.9, рекомендуется использовать эту версию для избежания проблем с установкой зависимостей):

python3 -m venv venv
Linux/macOS

source venv/bin/activate
Windows

source venv/scripts/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

## Запуск программы
В развернутом окружении перейти в основную директорию программы:
cd scrapy_parser_pep/

Выполнить в терминале команду: 
scrapy crawl pep