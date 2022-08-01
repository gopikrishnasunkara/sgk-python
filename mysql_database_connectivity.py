# Database connection:
# in this file, we are going to establish a connection between mysql and python.
#inorder to connect between mysql and python, we need to use 4 below steps. they are
#1. import mysql.connector
#2. Establish connection using connect()
#conn_obj = mysql.connector.connect(host = "host_name", user = "user_name", passwd = "password", database = "db_name")

#3.create cursor object
#curr_obj_name = conn_obj.cursor()

#4. Execute the Query
# curr_obj_name.execute("query")


#let's get started with practise and writing below to show all the databases which are avaiable in the mysql.

#import mysql.connector
#conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "root")
#c = conn.cursor()
#c.execute("show databases")
#for i in c:
#    print(i)

#let get start to create a new database for this our practical session.
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "root")
c = conn.cursor()
c.execute("create database employees")


#Create a table inside the Employees database
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "root", database = "employees")
c = conn.cursor()
c.execute("create table student(rollno int not null primary key, sname varchar(20) not null, branch varchar(10) not null)")
c.close()

#Insert records in student table and Insert only one entry at the time.

import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "root", database = "employees")
c = conn.cursor()
q = "insert into student(rollno,sname,branch)values(%s, %s, %s)"
v = (503,"Pavan", "ECE")
try:
    c.execute(q, v)
    conn.commit()
except:
    conn.rollback()
print(c.rowcount, "Rows Inserted")
c.close()

# insert records into student table and Inserting multiple records at a time.
# in this we will create a tuple with multiple entries and use executemany command when we are executing multiple.
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "root", database = "employees")
c = conn.cursor()
q = "insert into student(rollno,sname,branch)values(%s, %s, %s)"
v = [(503,"Pavan_k", "ECE"),(504,"Ram", "CSE"),(505,"Raj", "EEE"),(506,"Syam", "IT")]
try:
    c.executemany(q, v)
    conn.commit()
except:
    conn.rollback()
print(c.rowcount, "Rows Inserted")
c.close()


mysql executed commands practise:
Enter password: ****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 8.0.28 MySQL Community Server - GPL

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| employees          |
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
7 rows in set (0.00 sec)

mysql> use eimployees;
ERROR 1049 (42000): Unknown database 'eimployees'
mysql> use employees;
Database changed
mysql> show tables;
Empty set (0.03 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| employees          |
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
7 rows in set (0.00 sec)

mysql> show database;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'database' at line 1
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| employees          |
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
7 rows in set (0.00 sec)

mysql> use employees;
Database changed
mysql> show tablesl
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'tablesl' at line 1
mysql> show tables;
+---------------------+
| Tables_in_employees |
+---------------------+
| student             |
+---------------------+
1 row in set (0.00 sec)

mysql> desc student;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| rollno | int         | NO   | PRI | NULL    |       |
| sname  | varchar(20) | NO   |     | NULL    |       |
| branch | varchar(10) | NO   |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
3 rows in set (0.03 sec)

mysql> select * from student;
+--------+-------+--------+
| rollno | sname | branch |
+--------+-------+--------+
|    501 | Mani  | MECH   |
|    502 | Pavan | ECE    |
+--------+-------+--------+
2 rows in set (0.00 sec)

mysql> select * from student;
+--------+---------+--------+
| rollno | sname   | branch |
+--------+---------+--------+
|    501 | Mani    | MECH   |
|    502 | Pavan   | ECE    |
|    503 | Pavan_k | ECE    |
|    504 | Ram     | CSE    |
|    505 | Raj     | EEE    |
|    506 | Syam    | IT     |
+--------+---------+--------+
6 rows in set (0.00 sec)

mysql> select * from student;
+--------+---------+--------+
| rollno | sname   | branch |
+--------+---------+--------+
|    501 | Mani    | MECH   |
|    502 | Pavan   | ECE    |
|    503 | Pavan_k | ECE    |
|    504 | Ram     | CSE    |
|    505 | Raj     | EEE    |
|    506 | Syam    | IT     |
+--------+---------+--------+
6 rows in set (0.00 sec)

mysql> show databasesl
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'databasesl' at line 1
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| employees          |
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
7 rows in set (0.02 sec)

mysql> use employees;
Database changed
mysql> show tables;
+---------------------+
| Tables_in_employees |
+---------------------+
| student             |
+---------------------+
1 row in set (0.01 sec)

mysql> desc student;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| rollno | int         | NO   | PRI | NULL    |       |
| sname  | varchar(20) | NO   |     | NULL    |       |
| branch | varchar(10) | NO   |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
3 rows in set (0.01 sec)

mysql> SELECT * FROM student;
+--------+---------+--------+
| rollno | sname   | branch |
+--------+---------+--------+
|    501 | Mani    | MECH   |
|    502 | Pavan   | ECE    |
|    503 | Pavan_k | ECE    |
|    504 | Ram     | CSE    |
|    505 | Raj     | EEE    |
|    506 | Syam    | IT     |
+--------+---------+--------+
6 rows in set (0.00 sec)

mysql>


# sqlite database connectivity:
import sqlite3
conn = sqlite3.connect ('employee.db')
c = conn.cursor()
# c.execute("""CREATE TABLE employees (
# 	     first_Name text,
# 	     Last_Name text,
# 	     Pay interger
# 		)""")

c.execute("INSERT INTO employees VALUES ('Nani', 'Nemmadi', 50000)")
conn.commit()

c.execute("SELECT *FROM employees")
print(c.fetchall())

conn.commit()
conn.close()