import psycopg2
conn = psycopg2.connect(dbname='postgres',user='postgres',password='root',host='localhost',port='5432')
cursor=conn.cursor()
cursor.execute("Create table employees(Name Text,ID int,Age int);")
print("Table created Sucessfully")

conn.commit()
conn.close()