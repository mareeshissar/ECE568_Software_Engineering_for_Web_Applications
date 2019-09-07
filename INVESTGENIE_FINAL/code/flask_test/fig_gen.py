#main program file
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

import numpy
import math
import pandas as pd
import mysql.connector
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def fig(symbol,timelimit):

    con = mysql.connector.connect(             #connect to the mysql using the root and pwd
        host = 'localhost',
        user = 'root',
        password = 'passwordphrase@123',
        database = 'project'                  #include the database you need to work on
        )
    cursor = con.cursor();
    if(timelimit=="month"):
        dataframe = pd.read_sql("Select * from "+symbol+" limit 30",con)
        dataframe.columns = ['Datetime','Open','High','Low','Close','Volume']
        df = dataframe[['Datetime','Close']]
        df.plot(x='Datetime',y='Close')
        plt.savefig('C:/Users/RDRL/PycharmProjects/flask_test/static/'+symbol+'month.png')
    elif(timelimit=="year"):
        dataframe = pd.read_sql("Select * from "+symbol+" limit 299",con)
        dataframe.columns = ['Datetime','Open','High','Low','Close','Volume']
        df = dataframe[['Datetime','Close']]
        df.plot(x='Datetime',y='Close')
        plt.savefig('C:/Users/RDRL/PycharmProjects/flask_test/static/'+symbol+'year.png')
    elif(timelimit=="day"):
        dataframe = pd.read_sql("Select Date_Time,close,volume from "+symbol+"_rt limit 30",con)
        dataframe.columns = ['Datetime','Close','Volume']
        df = dataframe[['Datetime','Close']]
        df.plot(x='Datetime',y='Close')
        plt.savefig('C:/Users/RDRL/PycharmProjects/flask_test/static/'+symbol+'day.png')

#fig("GOOG","month")
#fig("AMZN","month")