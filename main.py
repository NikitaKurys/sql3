import concurrent.futures

import sqlalchemy
import psycopg2
from pprint import pprint

conn = psycopg2.connect(dbname='TwoDataBase', user='postgres',
                         password='Hjuvfyhjuvfy321', host='localhost')
cursor = conn.cursor()


# название и год выхода альбомов, вышедших в 2018 году
def displaying_albums():
    cursor.execute('''SELECT name, releasedate FROM album
        WHERE releasedate BETWEEN '2018-01-01' AND '2018-12-31';
        ''')
    result = cursor.fetchall()
    pprint(f'название и год выхода альбомов, вышедших в 2018 году: {result}')


# название и продолжительность самого длительного трека;
def track_search():
    cursor.execute('''SELECT name, tracklength FROM track
ORDER BY tracklength DESC;
''')
    result = cursor.fetchone()
    pprint(f'название и продолжительность самого длительного трека: {result}')


# название треков, продолжительность которых не менее 3,5 минуты;
def track_length():
    cursor.execute('''SELECT name FROM track
    WHERE tracklength >= 3.5;
    ''')
    result = cursor.fetchall()
    pprint(f'название треков, продолжительность которых не менее 3,5 минуты: {result}')


# названия сборников, вышедших в период с 2018 по 2020 год включительно;
def displaying_collection():
    cursor.execute('''SELECT name FROM collections
    WHERE release_year BETWEEN '2018-01-01' AND '2020-12-31';
    ''')
    result = cursor.fetchall()
    pprint(f'названия сборников, вышедших в период с 2018 по 2020 год включительно: {result}')


# исполнители, чье имя состоит из 1 слова;
def output_name():
    cursor.execute('''SELECT name FROM artist
    WHERE name NOT iLIKE '%% %%'
    ''')
    result = cursor.fetchall()
    pprint(f'исполнители, чье имя состоит из 1 слова: {result}')


# название треков, которые содержат слово "мой"/"my".
def output_my_track():
    cursor.execute('''SELECT name FROM track
    WHERE name iLike '%%my%%'
    ''')
    result = cursor.fetchall()
    pprint(f'название треков, которые содержат слово "мой"/"my: {result}')

def menu():
    print('Чтобы узнать название и год выхода альбомов, вышедших в 2018 году, нажмите 1'
          '\nЧтобы узнать название и продолжительность самого длительного трека, нажмите 2'
          '\nЧтобы узнать название треков, продолжительность которых не менее 3,5 минуты, нажмите 3'
          '\nЧтобы узнать названия сборников, вышедших в период с 2018 по 2020 год включительно, намите 4'
          '\nЧтобы узнать исполнители, чье имя состоит из 1 слова, нажмите 5'
          '\nЧтобы узнать название треков, которые содержат слово "мой"/"my, нажмите 6'
          '\nЧтобы открыть меню, нажмите 7'
          '\nЧтобы закрыть программу, нажмите 8'
          )


menu()
i = 1
while i == 1:
    user_input = int(input('Введи цифру: '))

    if user_input == 1:
        displaying_albums()
    elif user_input == 2:
        track_search()
    elif user_input == 3:
        track_length()
    elif user_input == 4:
        displaying_collection()
    elif user_input == 5:
        output_name()
    elif user_input == 6:
        output_my_track()
    elif user_input == 7:
        print('Чтобы узнать название и год выхода альбомов, вышедших в 2018 году, нажмите 1'
              '\nЧтобы узнать название и продолжительность самого длительного трека, нажмите 2'
              '\nЧтобы узнать название треков, продолжительность которых не менее 3,5 минуты, нажмите 3'
              '\nЧтобы узнать названия сборников, вышедших в период с 2018 по 2020 год включительно, намите 4'
              '\nЧтобы узнать исполнители, чье имя состоит из 1 слова, нажмите 5'
              '\nЧтобы узнать название треков, которые содержат слово "мой"/"my, нажмите 6'
              '\nЧтобы закрыть программу, нажмите 8'
              )
    else:
        i -= 1
