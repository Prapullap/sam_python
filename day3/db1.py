import pymysql
def connect_db():
     connection=pymysql.Connect(host='localhost',port=3306,user='root',password='root',database='dhanya_db',charset='utf8')
    return connection
def disconnect_db(connection):
     connection.close()
     print('DB dis-connect')
connection=connect_db()
disconnect_db(connection)
     
