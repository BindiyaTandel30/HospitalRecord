import mysql.connector as sqlc

mydb=sqlc.connect(
    host="localhost",
    user="root",
    password=""
    )

cur=mydb.cursor()
s="CREATE OR REPLACE DATABASE customer_record"
cur.execute(s)

s="USE customer_record"
cur.execute(s)

#open text file for read data in read only mode
try:
    fname=input("Please enter text file name: ")
    f=open(fname,"r")
    for line in f:
        data=line.split("|")    #split line with "|" ,It will return list of words
        if(data[1]=="D"):       #to ignore Header and Trailer record
            country=data[9]
            customer_id=int(data[3])
            try:                #if table already exist it will throw an exception
                s="CREATE TABLE {}(Customer_Name VARCHAR(255) NOT NULL,Customer_ID VARCHAR(18) PRIMARY KEY,Customer_Open_Date DATE NOT NULL,Last_Consulted_Date DATE,Vaccination_Type CHAR(5),Doctor_Consulted CHAR(255),State CHAR(5),Country CHAR(5),Post_Code INT(5),Date_of_Birth DATE,Active_Customer CHAR(1))".format(country)
                cur.execute(s)
                mydb.commit()
            except:
                pass
            finally:
                s="INSERT INTO {} VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(country)
                values=(data[2],customer_id,data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12])
                cur.execute(s,values)
                mydb.commit()
    print("DATA inserted in Tabels succesfully :)")
    f.close()          
except:
    print("Sorry!!! File not found")
finally:   
    mydb.close()
