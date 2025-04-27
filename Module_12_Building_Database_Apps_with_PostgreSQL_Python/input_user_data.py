import psycopg2
conn = psycopg2.connect(dbname='postgres',user='postgres',password='root',host='localhost',port='5432')

cursor=conn.cursor()
name = input("Enter Name : ")
id = input("Enter id:")
age = input("Enter age : ")
query = "insert into employees(Name,ID,Age)values(%s,%s,%s);"

cursor.execute(query,(name,id,age))


print("Data Added Sucessfully")

conn.commit()
conn.close()