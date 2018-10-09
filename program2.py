#program to read database


import mysql.connector
import datetime
import sys

global conn,cursor;

conn = mysql.connector.connect(host="localhost",user="root",password="root")

def connection():
    
    if conn.is_connected():
        return True
    else:
        return False

def create_database():
    if connection():
        mycursor = conn.cursor()
        try:
            mycursor.execute("CREATE DATABASE db_181041012")
            print("Database created sucessfully\n" )
        except:
            print("Database already exists\n")
    else:
        print("Could not connect to mysql server\n")


def create_table():
	conn_db = mysql.connector.connect(host="localhost",db="db_181041012",user="root",password="root")
	if conn_db.is_connected:
		cursor = conn_db.cursor()
		try:
			cursor.execute("CREATE TABLE reg_no(id INT(10) PRIMARY KEY, fname VARCHAR(25), lname VARCHAR(25), dob DATE)")
			print("Table created sucessfully")
		except:
			print("Already created")
	else:
		print("Connection failed")
		conn_db.close()	



def insert_values():
	conn_db = mysql.connector.connect(host="localhost",db="db_181041012",user="root",password="root")
	if conn_db.is_connected:
		mycursor=conn_db.cursor()

		query = "INSERT INTO reg_no(id, fname, lname,dob) VALUES (%s,%s,%s,%s)"

		id = input("Enter id\n")
		fname = input("Enter first name\n")
		lname = input("Enter last name\n")
		dob=input("Enter date of birth (yyyy/mm/dd)\n")
		value=(id,fname,lname,dob)
		mycursor.execute(query,value)
		conn_db.commit()
		print("sucessfully inserted")

		if not validate(dob):
			print("Incorrect format.Enter in yyyy/mm/dd format\n ")
			sys.exit()
	conn_db.close()




def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
    	return False


def display():
	conn_db=mysql.connector.connect(host="localhost",db="db_181041012",user="root",password="root")
	if conn_db.is_connected():
		mycursor=conn_db.cursor()
		try:
			mycursor.execute("SELECT * FROM reg_no")
			rows = cursor.fetchall();
			for row in rows:
   				print(row);
		except:
			print("Already created\n")
	else:
		print("Connection failed\n")
	conn_db.close()


def alter_table():
    conn_db = mysql.connector.connect(host="localhost", db="db_181041012", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        column = input("\nEnter column name\n")
        query = "ALTER TABLE reg_no add %s VARCHAR(25)" % (column)

        try:
            mycursor.execute(query)
            conn_db.commit()
            print("Column created\n")
        except:
         	print("column already exist\n")
    else:
    	print("connection failed\n")
    conn_db.close()


def truncate():
	conn_db = mysql.connector.connect(host="localhost",db="db_181041012",user="root",password="root")
	if conn_db.is_connected():
		mycursor = conn_db.cursor()
		query = "DROP TABLE reg_no"
		try:
			mycursor.execute(query)
			conn_db.commit()
			print("column deleted\n")
		except:
			print("Cannot deleted\n")
	else:
		print("connection failed\n")
	conn_db.close()



def main():
	connection();
	while True:
		print("\nEnter your choice:")
		print("Create database - 1:")
		print("Create Table -2:")
		print("Insert value-3:")
		print("display-4:")
		print("Alter-5:")
		print("Truncate-6:")
		print("Quit- q")
		choice = input("Enter the option:")
		if choice == '1':
			create_database();
		if choice == '2':
			create_table(); 
		if choice == '3':
			
			insert_values();
		if choice == '4':
			display();
		if choice == '5':
			alter_table();
		if choice == '6':
			truncate();
		if choice == 'q':
			sys.exit()

if __name__ == '__main__':
	main();
