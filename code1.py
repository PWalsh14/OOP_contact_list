import sqlite3

conn = sqlite3.connect('Users.db')
c = conn.cursor()
c.execute("""DROP TABLE IF EXISTS USER""")
c.execute("""
CREATE TABLE USER (
    Name VARCHAR(20),
    Address VARCHAR(20),
    Phone_Number INTEGER,
    Birthday VARCHAR INTEGER(20))
""")

conn.commit()
conn.close()
