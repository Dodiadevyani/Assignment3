import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
file = open('Rainfall_England.txt', 'r')
file_content = file.read()
file.close()
query = "INSERT INTO table VALUES (%s)"
c.execute('query (file_content)')
conn.commit()
c.close()


#database= sqlite3.connect('database.db')
#database.execute('creat table(abc txt, bcd txt mno int)')
#database.execute('''Weather data table (YEAR int, JAN float, FEB float, MAR float, APR float, MAY float,
#JUN float, JUL float, AUG float, SEP float, OCT float, NOV float, DEC float, WIN float, SPR float, SUM float, AUT float, ANNUAL float)''')
