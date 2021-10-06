#!/usr/bin/python

import sqlite3

# Connect the database
conn = None
try:
    conn = sqlite3.connect('Movies.db')
except Error as e:
    print(e)

# Creating the table called Movies
conn.execute("CREATE TABLE Movies(id INTEGER PRIMARY KEY NOT NULL, Title TEXT NOT NULL,Actor CHAR(50) NOT NULL,Actoress CHAR(50) NOT NULL, Director TEXT NOT NULL, Year_of_release INTEGER NOT NULL);")

# Inserting the data to the table Movies
conn.execute(("INSERT INTO Movies(id,Title, Actor, Actoress, Director, Year_of_release) VALUES (1,'Jersey','Nani','Shraddha Srinath','Gowtam Tinnanuri',2019)");

conn.execute(("INSERT INTO Movies(id,Title, Actor, Actoress, Director, Year_of_release) VALUES (2,'Mahanati','Dulquer Salmaan','Keerthy Suresh','Nag Ashwin',2018)");

conn.execute(("INSERT INTO Movies(id,Title, Actor, Actoress, Director, Year_of_release) VALUES (3,'Bahubali 2:The Conclusion','Prabhas','Anuskha Shetty','S.S.Rajamouli',2017)");

conn.execute(("INSERT INTO Movies(id,Title, Actor, Actoress, Director, Year_of_release) VALUES (4,'Kushi','Pavan Kalyan','Bhoomika Chawla','S.J.Suryah',2001)");

conn.execute(("INSERT INTO Movies(id,Title, Actor, Actoress, Director, Year_of_release) VALUES (5,'Sahoo','Prabas','Shraddha Kapoor','Sujeeth',2019)");

conn.commit()

# Selecting the data form Movies
cursor = conn.execute("SELECT * from Movies")

for row in cursor:
    print("Id = "+ str(row[0] + end = " ")
    print("Title = "+ row[1]+ end = " ")
    print("Actor = "+ row[2]+ end = " ")
    print("Actoress = "+ row[3]+ end = " ")
    print("Director = "+ row[4]+ end = " ")
    print("Year_of_release = "+ str(row[5])+ "\n")

# Selecting the actor movies
cursor = conn.execute("SELECT * from Movies WHERE Actor = Prabhas")

for row in cursor:
    print("Id = "+ str(row[0]) + end = " ")
    print("Title = "+ row[1]+ end = " ")
    print("Actor = "+ row[2]+ end = " ")
    print("Actoress = "+ row[3]+ end = " ")
    print("Director = "+ row[4]+ end = " ")
    print("Year_of_release = "+ str(row[5])+ "\n")

 
conn.close()
