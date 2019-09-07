#main program file
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

from flask import Flask,request,render_template, jsonify, redirect, url_for
from firebase import firebase
from show_latest_values_symbols import show_open_close
from prediction_return import pred_final
from queries import queries
from test_JSON import JSON_DATA
from fig_gen import fig
from indicator_return import prediction
from api_create import api_queries
import mysql.connector
import json
app = Flask(__name__)

firebase = \
        firebase.FirebaseApplication('https://messages-2f289.firebaseio.com', None)


@app.route("/startpage", methods=['POST', 'GET'])
def startpage():
    return render_template("startpage.html")

@app.route("/loginpage", methods=['POST', 'GET'])
def loginpage():
    if request.method == 'POST':
        return render_template("loginpage.html")

@app.route("/registerpage", methods=['POST', 'GET'])
def registerpage():
    if request.method == 'POST':
        return render_template("registerpage.html")


# decorator which tells flask what url triggers this fn
@app.route("/messages")
def messages():
    result = firebase.get("/messages", None)
    return render_template("list.html", messages=result)

@app.route("/submit_message", methods=['POST', 'GET'])
def submit_message():
    message = {
        'body': request.form['message'],
        'who': request.form['who']
      }
    firebase.post("/messages", message)
    return redirect(url_for("messages"))


#--------------------------------------------------------------------------------------------------------
@app.route("/main_page", methods=['GET','POST'])
def main_page():
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        query1 = request.form['query']
        values = show_open_close(stock_symbol)
        period = request.form['period']
        final_prediction=prediction(stock_symbol)
        fig(stock_symbol,period)
        return render_template("main_page.html", stock_symbol=stock_symbol, values=values, predicted_value=pred_final(stock_symbol), query=queries(stock_symbol,query1),period=period, final_prediction=final_prediction)

    return render_template("main_page.html", stock_symbol=0, values=[], predicted_value=0, query=0, period=0, final_prediction=0)


@app.route("/api1", methods=['GET', 'POST'])
def api1():
   stock_symbol = request.args.get('stock_symbol')
   return jsonify(JSON_DATA(stock_symbol))

@app.route("/api2", methods=['GET', 'POST'])
def api2():
   stock_symbol = request.args.get('stock_symbol')
   query_type = request.args.get('query_type')
   if query_type == "high_val_ten":
    values = api_queries(stock_symbol,query_type)
    return jsonify({"high":values[0],"date":values[1]})
   elif query_type == "avg_val_year":
       values = api_queries(stock_symbol, query_type)
       return jsonify({"avg": values[0]})
   elif query_type == "lowest_val_year":
       values = api_queries(stock_symbol, query_type)
       return jsonify({"minimum": values[0]})
   elif query_type == "lower_lowest":
       values = api_queries(stock_symbol, query_type)
       return jsonify(values)
   elif query_type == "predict":
       values = api_queries(stock_symbol, query_type)
       return jsonify({"predicted value": values[0]})

if __name__ == '__main__':  #only run if
    # this file is called directly
    app.run(debug=True)

