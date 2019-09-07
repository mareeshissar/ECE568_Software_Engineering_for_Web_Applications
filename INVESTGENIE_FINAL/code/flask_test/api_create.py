#main program file
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

import numpy
import math
from query_1 import query_1
import pandas as pd
import mysql.connector
from prediction_return import pred_final

def api_queries(symbol,query_type):
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

    elif query_type=="list_comp":
        return query_1()

    elif query_type== "high_val_ten":
        df1 = df10.loc[df10['Close'].idxmax()]
        values = [df1['Close'], df1['Date']]
        return values

    #average stock price for the last one year
    elif query_type== "avg_val_year":
        values =[dataframe['Close'].mean()]
        #print(values)
        return values
        #print("Average stock price for the last 1 year: ",dataframe['Close'].mean())

    #lowest stock price in the last one year
    elif query_type== "lowest_val_year":
        #print("Lowest stock price in the last 1 year: ",dataframe['Close'].min())
        values = [dataframe['Close'].min()]
        #print(values)
        return values
    elif query_type== "lower_lowest":
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
    elif (query_type == "predict"):
        values = pred_final(symbol)
        return values

# a=api_queries("MSFT","high_val_ten");
# print(a)