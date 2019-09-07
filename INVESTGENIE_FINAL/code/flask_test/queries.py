#main program file
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

import numpy
import math
from query_1 import query_1
import pandas as pd
import mysql.connector

def queries(symbol,query_type):
    con = mysql.connector.connect(             #connect to the mysql using the root and pwd
        host = 'localhost',
        user = 'root',
        password = 'passwordphrase@123',
        database = 'project'                  #include the database you need to work on
        )
    cursor = con.cursor();

    dataframe = pd.read_sql("Select * from "+symbol,con)
    dataframe.columns = ['Date','Open','High','Low','Close','Volume']
    # df = dataframe[['Datetime','Close']]
    #
    # df.plot(x='Datetime',y='Close')
    #
    # plt.savefig('stock_graph.png')

    #highest price in the last 10 days
    df10 = dataframe.head(10)
    if query_type==0:
        return 0

    elif query_type=="Query 1":
        return query_1()

    elif query_type== "Query 2":
        #values= ["Highest price in the last 10 days:",df10.loc[df10['Close'].idxmax()]]
        df1 = df10.loc[df10['Close'].idxmax()]
        #print(df1['Close'])
        values = ["Highest closing price in the last 10 days:",df1['Close']," on date", df1['Date']]
        return values

    #average stock price for the last one year
    elif query_type== "Query 3":
        values =["Average closing stock price for the last 1 year: ",dataframe['Close'].mean()]
        #print(values)
        return values
        #print("Average stock price for the last 1 year: ",dataframe['Close'].mean())

    #lowest stock price in the last one year
    elif query_type== "Query 4":
        #print("Lowest stock price in the last 1 year: ",dataframe['Close'].min())
        values = ["Lowest closing stock price in the last 1 year: ",dataframe['Close'].min()]
        #print(values)
        return values
    elif query_type== "Query 5":
        minimum = dataframe['Close'].min()
        print(minimum)
        symbols =["MSFT","AAPL","NVDA","AMZN","FB","GOOG", "INTC", "ORCL", "TSLA", "AABA"]
        values =[]
        for i in symbols:
            dataframe_temp = pd.read_sql("Select * from " + i, con)
            dataframe_temp.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
            val = dataframe_temp['Close'].min()
            if val < minimum:
                values.append([i,val])
        #print(values)
        return values

# a=queries("MSFT","Query 2");
# print(a)