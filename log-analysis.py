import psycopg2

conn = psycopg2.connect(host='localhost', database='news',
                        user='Mahmoud', password='192168-Water')

cur = conn.cursor()
cur.execute("select * from log where method = 'GET';")
result = cur.fetchall()

conn.close()

for row in result:
    for col in row:
        print(col)
        print('-----')
    print('\n')
    print('____________________________________________________________')
    print('\n')
