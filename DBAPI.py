import pandas as pd
from sqlalchemy import create_engine, text

# Декоратор для модификации функции без измнения кода
def measure_time(func):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Время выполнения функции {func.__name__}: {execution_time} секунд")
        return result
    return wrapper


# Абстрактный класс API 
class DBAPI:
    def __init__(self, host, login, password, database):
        self.engine = create_engine(f'postgresql://{login}:{password}@{host}/{database}')
        self.connection = self.engine.connect()

    # Создание таблицы на основе данных DataFrame
    @measure_time
    def create_table(self, df, table_name):
        df.to_sql(table_name, self.engine, index=False)

    # Удаление строки из таблицы указанных условий
    @measure_time
    def delete_row(self, table_name, condition):
        delete_query = f"DELETE FROM {table_name} WHERE {condition}"
        self.connection.execute(delete_query)


    # Удаляет все строки из таблицы (очищает таблицу)
    @measure_time
    def truncate_table(self, table_name):
        truncate_query = f'TRUNCATE TABLE {table_name}'
        self.connection.execute(text(truncate_query))

    # Чтение данных из запроса
    @measure_time
    def read_sql(self, query):
        df = pd.read_sql(query, self.connection)
        return df

    # Запись данных в таблицу
    @measure_time
    def insert_sql(self, df, table_name, mode='new'):
        if mode == 'new':
            df.to_sql(table_name, self.engine, index=False)
        elif mode == 'append':
            df.to_sql(table_name, self.engine, if_exists='append', index=False)
        elif mode == 'overwrite':
            self.truncate_table(table_name)
            df.to_sql(table_name, self.engine, index=False)
