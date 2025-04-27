import psycopg2
conn = psycopg2.connect(dbname='postgres',user='postgres',password='root',host='localhost',port='5432')
print('Connected Sucessfully')