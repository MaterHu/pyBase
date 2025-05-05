import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='000000h123',charset='utf8')
cursor = conn.cursor()
cursor.execute("show databases")
result = cursor.fetchall()
print(result)
