import mysql.connector as sqlc

#create database
mydb=sqlc.connect(
    host="localhost",
    user="root",
    password="")

cur=mydb.cursor()
s="CREATE OR REPLACE DATABASE customer_record"
cur.execute(s)

#read data
f=open("customer_record.txt","r")
for line in f:
    data=line.split("|")
