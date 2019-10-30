import datetime
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


# On which days did more than 1% of requests lead to errors?
cur.execute("""create view log_all as
               select date(time) as day, count(*) as times from log
	           group by date(time);""")
cur.execute("""create view log_error as
               select date(time) as day, count(*) as times from log
               where status like '404%'
	           group by date(time);""")
cur.execute("""select log_all.day, log_all.times, log_error.times
	           from log_all join log_error
	           on log_all.day = log_error.day
	           where (log_error.times::float / log_all.times)*100 > 1;""")
result = cur.fetchall()

print("On which days did more than 1% of requests lead to errors?")
for row in result:
    print('* ' + row[0].strftime("%B %d, %Y") + ' - ' + str((float(row[2])/row[1])*100) + "% errors")
print('\n')


conn.close()
