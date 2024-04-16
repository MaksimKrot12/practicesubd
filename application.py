# DBАPI для работы с БД с использованием библиотеки SQLAlchemy и Pandas
from DBAPI import DBAPI
from sqlalchemy import text
import pandas as pd


# Создание экземпляра класса DBAPI
api = DBAPI(host='localhost:5432', login='postgres', password='111', database='eurotrack')

# Инициализация API
api.__init__(host='localhost:5432', login='postgres', password='111', database='eurotrack')

# Создание таблицы++
# df = pd.DataFrame({
#    'name': ['Bloom', 'Flora', 'Musa'],
#    'password': ['********', '********', '**********']
# })
# api.create_table(df, table_name='feechki')

# Удаление строк из таблицы++
# api.delete_row(table_name="feechki", condition= "name = 'Bloom'")


# Отчистка таблицы++
# api.truncate_table(table_name='feechki')

# Чтение данных из запроса++
# query = 'SELECT * FROM feechki'
# data = api.read_sql(text(query))
# print(data)

# Запись данных в таблицу++
# new_data = pd.DataFrame({
#     'name': ['Roxy', 'Tecna', 'Layla'],
#     'password': ['123', '456', '789']
# })
# api.insert_sql(new_data, table_name='feechki', mode='append')
