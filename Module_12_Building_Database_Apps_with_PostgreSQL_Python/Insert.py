import psycopg2
conn = psycopg2.connect(dbname='postgres',user='postgres',password='root',host='localhost',port='5432')
cursor=conn.cursor()
cursor.execute("insert into employees(Name,ID,Age)values('Sam',01,25);")
print("Data Added Sucessfully")

conn.commit()
conn.close()