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

- [Download the VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Download the Vagrant](https://www.vagrantup.com/downloads.html)
- [Download the VM configuration](https://github.com/udacity/fullstack-nanodegree-vm)  
Then setup the VM:  
`cd fullstack-nanodegree-vm`  
`cd vagrant`  
`vagrant up`  
- [Download the database file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)  
Then unzip this file. The file inside is called newsdata.sql. Put this file into the vagrant directory,
which is shared with your virtual machine. Then run:  
`psql -d news -f newsdata.sql`
- Download the repository

## Getting started

- Open the vm:  
`vagrant ssh`
- Run the script:  
`python log-analysis`

## More info

- The database name: news
- The database tables:
    1. authors: id, name, bio
    2. articles: id, author, title, slug, lead, body
    3. log: id, ip, path, method, status, time
