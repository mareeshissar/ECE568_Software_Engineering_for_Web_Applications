#main program file
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

import mysql.connector
import json

def JSON_DATA(symbol):
    con = mysql.connector.connect(  # connect to the mysql using the root and pwd
        host='localhost',
        user='root',
        password='passwordphrase@123',
        database='project'  # include the database you need to work on
    )
    cur = con.cursor();
    cur.execute("SELECT date_time,open,high,low,close FROM "+symbol)
    row_headers = [x[0] for x in cur.description]  # this will extract row headers
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return (json_data)

