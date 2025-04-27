import psycopg2
conn = psycopg2.connect(dbname='postgres',user='postgres',password='root',host='localhost',port='5432')

cursor=conn.cursor()

cursor.execute("Select * from employees;")
print(cursor.fetchone())

print("Data Retrived Sucessfully")

conn.commit()
conn.close()