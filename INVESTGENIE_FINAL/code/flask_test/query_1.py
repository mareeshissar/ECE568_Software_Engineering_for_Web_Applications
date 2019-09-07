#main program file
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

#FOR HISTORIC DATA
#importing the required libraries
import requests
import json
import time

def query_1():
    symbols = ["MSFT","AAPL","NVDA","AMZN","FB"]
    symbols_1= ["GOOG","ORCL","INTC","TSLA","AABA"]    #symbols for which we are retrieving historic stock data

    values=[]

    #using the API to retrieve all stock data for the defined symbols
    for symbol in symbols:
        parameters = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": "full", "apikey": "7V2V2BYS8TVJ5UYF"}
        response = requests.get("https://www.alphavantage.co/query?", params=parameters)
        data = json.loads(response.text)
        i=1
        for key in data['Time Series (Daily)'].keys():
            if i>1:                   #300 rows depicting one year's data ()
                break
            i=i+1
            product = data['Time Series (Daily)'][key]
            values.append(symbol+" : "+product["4. close"])
    time.sleep(61)
    for symbol in symbols_1:
        parameters = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": "full", "apikey": "J93BW2PM647PZTJ1"}
        response = requests.get("https://www.alphavantage.co/query?", params=parameters)
        data = json.loads(response.text)
        i=1
        for key in data['Time Series (Daily)'].keys():
            if i>1:                   #300 rows depicting one year's data ()
                break
            i=i+1
            product = data['Time Series (Daily)'][key]
            values.append(symbol+" : "+product["4. close"])
    return values

# a=query_1()
# print(a)