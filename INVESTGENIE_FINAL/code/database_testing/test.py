#program to fill the historic tables in the database
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

import requests
# import urllib.request
import json
import mysql.connector


#symbols = ["MSFT","AAPL","NVDA","AMZN","FB"]
symbols = ["GOOG", "INTC", "ORCL", "TSLA", "AABA"]
#symbols = ["MSFT"]



symbols_list = []  # to append the data we received

for symbol in symbols:
    parameters = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": "full", "apikey": "7V2V2BYS8TVJ5UYF"}
    response = requests.get("https://www.alphavantage.co/query?", params=parameters)
    data = json.loads(response.text)
    # print(data['Time Series (1min)'].keys())
    # print(data)

    # con = pymysql.connect(host = 'localhost',user = 'root',passwd = 'passwd',db = 'jsontest1')
    # cursor = con.cursor()
    # cursor.execute("DELETE FROM "+symbol)
    # con.commit()

    con = mysql.connector.connect(  # connect to the mysql using the root and pwd

        host='localhost',
        user='root',
        password='passwordphrase@123',
        database='Project'  # include the database you need to work on
    )
    cursor = con.cursor()  # to send the database queries
    cursor.execute("DELETE FROM " + symbol)  # deleting table contents before inserting new stock data
    con.commit()
    i = 0
    for key in data['Time Series (Daily)'].keys():
        if i > 299:
            break
        i = i + 1  # CHANGE**
        # for product in data['Time Series (1min)'][i]:
        product = data['Time Series (Daily)'][key]
        print("Date_time:", key)
        print("open:", product["1. open"])
        print("high:", product["2. high"])
        print("low:", product["3. low"])
        print("close:", product["4. close"])
        print("volume:", product["5. volume"])
        print('---')
        cursor.execute(
            "INSERT INTO " + symbol + " (`Date_time`, open, high, low, close, volume) VALUES (%s,%s,%s,%s,%s,%s)",
            (key, product["1. open"], product["2. high"], product["3. low"], product["4. close"], product["5. volume"]))
        # cursor.execute("INSERT INTO "+symbol+" (`Date/time`, close, volume) VALUES (%s,%s,%s)", (key, product["4. close"], product["5. volume"]))    ##NEW CHANGE CHECK
        con.commit()
# con.commit()                ##NOT SURE ABOUT THIS
con.close()