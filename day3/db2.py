import pymysql
def connect_db():
    try:
        connection=pymysql.Connect(host='localhost',port=3306,user='root',password='root',database='dhanya_db',charset='utf8')
        print('database connected')
        return connection
    except:
        print('database connection failed')
        
def disconnect_db(connection):
    try:
        connection.close()
        print('DB dis-connect')
    except:
        print('failed disconnecting database')
def create_db():
    connection=connect_db()
    query='create database IF NOT EXISTS dhanya_db;'
    cursor=connection.cursor()
    cursor.execute(query)
    cursor.close()
    disconnect_db(connection)
def create_table():
    connection = connect_db()
    query = "create table IF NOT EXISTS persons(id int primary key, name varchar(32) not null, gender char check(gender in('m','M', 'f','F')), location varchar(32), dob datetime);"
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    print('Table created')
    disconnect_db(connection)
def read_person_details():
    name=input('Enter person name:')
    gender=input('Enter person gender:')[0]
    location=input('Enter person location:')
    dob=input('Enter person date of birth (yyyy/mm/dd):')
    return (name,gender,location,dob)

def insert_row():
    person=read_person_details()
    query='insert into persons(name,gender,location,dob)values(%s,%s,%s,%s)'
    connection=connect_db()
    cursor=connection.cursor()
    cursor.execute(query, person)
    cursor.close()
    disconnect_db(connection)
insert_row()
