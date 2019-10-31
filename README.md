# Log analysis

A python database application to create a reporting tool that prints out reports  based on the data in the database.
The reports are:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

## Prerequisites

- Python
- SQL

## Installation

- Install python
- Install Postgresql 
- Install requirements.txt
- Download the repository

## More info

- The database name: news
- The database tables:
    1. authors: id, name, bio
    2. articles: id, author, title, slug, lead, body
    3. log: id, ip, path, method, status, time
- The database viwes used:
```
create view authors_articles as
select authors.id, name, slug from authors join articles
on authors.id = articles.author;
```
```
create view log_all as
select date(time) as day, count(*) as times from log
group by date(time);
```
```
create view log_error as
select date(time) as day, count(*) as times from log
where status like '404%'
group by date(time);
```
