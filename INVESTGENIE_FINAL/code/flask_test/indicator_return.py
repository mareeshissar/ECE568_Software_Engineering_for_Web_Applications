#main program file
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

import numpy as np
import tulipy as ti
import pandas as pd
import mysql.connector

def prediction(symbol):

    #connecting to the MySQL server
    con = mysql.connector.connect(             #connect to the mysql using the root and pwd
        host = 'localhost',
        user = 'root',
        password = 'passwordphrase@123',
        database = 'project'                  #include the database you need to work on
    )
    cursor = con.cursor()
    df = pd.read_sql("Select close from "+symbol+" limit 30",con)
    df = df.iloc[::-1]
    pf = df.transpose()
    pf = pf.values.tolist()
    #print(pf[0])
    values_return = pf[0];
    data3 = np.asanyarray(values_return) #
    #print(data3)

    df = pd.read_sql("Select close from "+symbol+" limit 15",con)
    df = df.iloc[::-1]
    pf = df.transpose()
    pf = pf.values.tolist()
    #print(pf[0])
    values_return = pf[0];
    data2 = np.asanyarray(values_return) #
    #print(data3)

    df = pd.read_sql("Select high,low,close from "+symbol+" limit 15",con)
    df = df.iloc[::-1]
    pf = df.transpose()
    pf = pf.values.tolist()
    #print(pf[0])
    values_return = pf[0]
    data_will_high = np.asanyarray(values_return)
    values_return = pf[1]
    data_will_low = np.asanyarray(values_return)
    values_return = pf[2]
    data_will_close = np.asanyarray(values_return)


    ## use latest 15 values
    emaop = ti.ema(data2, period=12)
    #print("Exponential moving average: ",emaop)
    #print(emaop[(14)] - emaop[(13)]) #if > 0 buy, if < 0 sell, if == 0 hold

    #for volatility ratio, use latest 15 values of closing price
    vrop = ti.volatility(data2, period=14)
    #print("Volatility Ratio: ",vrop)      #

    # #for MACD, use latest 30 values of closing price
    # macdop = ti.macd(data3,short_period=12,long_period=26,signal_period=9)
    # print("MACD: ",macdop)

    will_r = ti.willr(data_will_high,data_will_low,data_will_close,period =15);
    print(will_r)

    if ((emaop[(14)] - emaop[(13)]) > 0 and vrop > 0.5) or -80< will_r <-100:
        return "Buy"
    elif ((emaop[(14)] - emaop[(13)]) < 0 and vrop > 0.5) or -20<will_r<0:
        return "Sell"
    else:
        return "Hold"

#a=prediction("MSFT")