import psycopg2
from prettytable import PrettyTable

conn = psycopg2.connect(dbname='users', host='localhost', port='5432', user='postgres', password='your_password')
curr = conn.cursor()

def create_table(table_name):
    try:
        curr.execute(f'CREATE TABLE {table_name}(id serial primary key, name varchar(32),surname varchar(32),Age int)')
    except Exception:
        print('Bunday table mavjud!')
    else:
        print('Yaratildi!')

create_table('student')

def drop_table(table_name_d):
    try:

        curr.execute(f'DROP TABLE {table_name_d}')
    except Exception:
        print('Bunday table mavjud emas!')
    else:
        print("O'chirildi!")
    
drop_table('student')

def alter_table(table_name,column_name,data_type, ext=''):
    try:
        curr.execute(f'ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type} {ext}')
    except Exception as e:
        print(f'Xatolik ({e})!')
    else:
        print("Colum qo'shildi!")
    
alter_table('student','prof','varchar(32)')

def drop_column(table_name,column_name):
    try:
        curr.execute(f'ALTER TABLE {table_name} DROP COLUMN {column_name}')
    except Exception as e:
        print(f'Xatolik ({e})!')
    else:
        print("Colum deleted!")

drop_column('student','age')

def alter_column_type(table_name,column_name,new_data_type):
    try:
        curr.execute(f'ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE {new_data_type}')
    except Exception as e:
        print(f'Xatolik ({e})!')
    else:
        print("Column's data changed!")
    
alter_column_type('student','prof','varchar(64)')

def alter_column_name(table_name,column_name,new_column_name):
    try:
        curr.execute(f'ALTER TABLE {table_name} RENAME COLUMN {column_name} TO {new_column_name}')
    except Exception as e:
        print(f'Xatolik ({e})!')
    else:
        print("Column's name changed!")

alter_column_name('student','name','surname')

def insert_into(table_name):
    try:
        curr.execute(f'INSERT INTO {table_name} VALUES(NAME VARCHAR(32),SKILS VARCHAR(32),WORKING_HOURS VARCHAR(32))')
    except Exception as e:
        print(f'Xatolik ({e})!')
    else:
        print("INSERT INTO")

insert_into('Teacher')

def update(table_name,column_name,value,old_column_name,old_value):
    try:
        curr.execute(f'UPDATE {table_name} SET {column_name} = {value} WHERE {old_column_name} = {old_value}')
    except Exception as e:
        print(f'Xatolik ({e})!')
    else:
        print("UPDATE")

update('teacher','age',39,'name','Zilola')

def rename(table_name,new_table_name):
    try:
        curr.execute(f'ALTER TABLE {table_name} RENAME TO {new_table_name}')
    except Exception as e:
        print(f'Xatolik ({e})!')
    else:
        print("RENAME")

rename('teacher','doctor')

def select_pretty(table_name):
    try:
        table = PrettyTable()
        curr.execute(f"select *from {table_name}")
        data = curr.fetchall()
        table.field_names = [i[0] for i in curr.description]
        table.add_rows(data)
        print(table)
    except Exception as e:
        print(f'Xatolik\n{e}')
conn.commit()
conn.close()