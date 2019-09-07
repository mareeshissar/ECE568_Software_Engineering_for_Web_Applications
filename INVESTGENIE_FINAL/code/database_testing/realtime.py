#program to fill the realtime tables in the database
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

import requests
# import urllib.request
import json
import schedule  ##new lib import this
import time
import mysql.connector

schedule.clear()


def job():
    #symbols = ["MSFT", "AAPL", "NVDA", "AMZN", "FB"]
    symbols = ["GOOG", "INTC", "ORCL", "TSLA", "AABA"]
    symbols_list = []  # to append the data we received

    for symbol in symbols:
        parameters = {"function": "TIME_SERIES_INTRADAY", "symbol": symbol, "interval": "1min", "outputsize": "full",
                      "apikey": "7V2V2BYS8TVJ5UYF"}
        response = requests.get("https://www.alphavantage.co/query?", params=parameters)

        data = json.loads(response.text)
        # print(data['Time Series (1min)'].keys())
        # print(data)

        con = mysql.connector.connect(  # connect to the mysql using the root and pwd

            host='localhost',
            user='root',
            password='passwordphrase@123',
            database='Project'  # include the database you need to work on
        )
        cursor = con.cursor()  # to send the database queries
        cursor.execute("DELETE FROM " + symbol+"_rt")
        con.commit()
        i = 0
        for key in data['Time Series (1min)'].keys():
            if i > 389:
                break
            i = i + 1  # CHANGE**
            # for product in data['Time Series (1min)'][i]:
            product = data['Time Series (1min)'][key]
            print("Date_time:", key)
            # print("open:", product["1. open"])
            # print("high:", product["2. high"])
            # print("low:", product["3. low"])
            print("close:", product["4. close"])
            print("volume:", product["5. volume"])
            print('---')
            # cursor.execute("INSERT INTO "+symbol+" (`Date/time`, open, high, low, close, volume) VALUES (%s,%s,%s,%s,%s,%s)", (key, product["1. open"], product["2. high"], product["3. low"], product["4. close"], product["5. volume"]))
            cursor.execute("INSERT INTO " + symbol + "_rt (`Date_time`, close, volume) VALUES (%s,%s,%s)",
                           (key, product["4. close"], product["5. volume"]))  ##NEW CHANGE CHECK
            con.commit()

    # con.commit()                ##NOT SURE ABOUT THIS
    con.close()


schedule.every(60).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(.1)