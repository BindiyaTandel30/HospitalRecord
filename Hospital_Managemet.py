import mysql.connector as sqlc

#create database
mydb=sqlc.connect(
    host="localhost",
    user="root",
    password="",
    database="customer_record")

cur=mydb.cursor()
##s="CREATE OR REPLACE DATABASE customer_record"
##cur.execute(s)

#read data
f=open("customer_record.txt","r")
for line in f:
    data=line.split("|")
    if(data[1]=="D"):
        country=data[9]
        try:
            s="CREATE TABLE {}(Customer_Name VARCHAR(255),Customer_ID VARCHAR(18) PRIMARY KEY,Customer_Open_Date DATE,Last_Consulted_Date DATE,Vaccination_Type CHAR(5),Doctor_Consulted CHAR(255),State CHAR(5),Country CHAR(5),Post_Code INT(5),Date_of_Birth DATE,Active_Customer CHAR(1))".format(country)
            cur.execute(s)
            mydb.commit()
        except:
            print()
        
            
f.close()
