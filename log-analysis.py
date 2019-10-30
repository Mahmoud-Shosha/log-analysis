import psycopg2

conn = psycopg2.connect(host='localhost', database='news',
                        user='Mahmoud', password='192168-Water')

cur = conn.cursor()

# What are the most popular three articles of all time?
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
print('\n')


# Who are the most popular article authors of all time?
cur.execute("""create view authors_articles as
               select authors.id, name, slug from authors join articles
               on authors.id = articles.author;""")
cur.execute("""select name, count(*) as times
	           from authors_articles join log
               on log.path like '/article/' || authors_articles.slug
               group by name
               order by times desc;""")
result = cur.fetchall()

print('Who are the most popular article authors of all time?')
for row in result:
    print('* ' + row[0] + ' - ' + str(row[1]) + ' views')
print('\n')

conn.close()
