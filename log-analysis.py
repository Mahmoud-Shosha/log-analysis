import psycopg2

conn = psycopg2.connect(host='localhost', database='news',
                        user='Mahmoud', password='192168-Water')

cur = conn.cursor()
cur.execute("""select lead, count(*) as times
               from articles join log
               on log.path like '/article/' || articles.slug
               group by articles.id
               order by times desc
               limit 3;""")
result = cur.fetchall()

print('What are the most popular three articles of all time?')
for row in result:
    print('* ' + row[0] + ' - ' + str(row[1]) + ' views')

conn.close()
