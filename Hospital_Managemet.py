import mysql.connector as sqlc

#create database
mydb=sqlc.connect(
    host="localhost",
    user="root",
    password="" )

cur=mydb.cursor()
s="CREATE DATABASE customer_record"
cur.execute(s)
