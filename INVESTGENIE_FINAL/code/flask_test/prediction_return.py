#main program file
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

import pandas as pd
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression, BayesianRidge
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
import mysql.connector


def pred_final(symbol):
    # quandl.ApiConfig.api_key = "hP3_kp16Xy4FxTJZmc8w"
    # df = quandl.get('WIKI/GOOGL')
    # # features that I want
    #
    # df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
    # #features that make sense
    # df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
    # df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
    # #keep only the sensible features in my df
    # df = df[['Adj. Close', 'HL_PCT','PCT_change', 'Adj. Volume']]
    #used for label
    #forecast_col = 'Adj. Close'

    con = mysql.connector.connect(             #connect to the mysql using the root and pwd
    host = 'localhost',
    user = 'root',
    password = 'passwordphrase@123',
    database = 'project'                  #include the database you need to work on
    )
    # features that I want

    df = pd.read_sql("Select open,high,low,close,volume from "+ symbol +" limit 50",con)
    df = df[['open','high','low','close','volume']]
    #features that make sense
    df['HL_PCT'] = (df['high'] - df['close']) / df['close'] * 100.0
    df['PCT_change'] = (df['close'] - df['open']) / df['open'] * 100.0
    #keep only the sensible features in my df
    df = df[['close', 'HL_PCT','PCT_change', 'volume']]

    #used for label
    forecast_col = 'close'
    #if you want to fill an unavailable value
    df.fillna(-99999,inplace=True);
    #round the number into whole
    #print("THIS",len(df))
    #number of values that you predict wrt to the data frame, here len == ~30
    forecast_out = int(math.ceil(0.01*len(df)))

    #the label for each is the adj label shifted by 30 days
    df['label'] = df[forecast_col].shift(-forecast_out)
    df = df.iloc[::-1]
    #print(df)
    #print(df.head());

    X = np.array(df.drop(['label'],1))  #drop label and keep everything
    X = preprocessing.scale(X)
    X = X[:-forecast_out]
    #if I want to predict just one value:
    #X_lately = X[-forecast_out + forecast_out + 1:]
    X_lately = X[-forecast_out:]

    df.dropna(inplace =True)
    y = np.array(df['label'])
    y = np.array(df['label'])

    #split the data for testing and training
    x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

    #using a linear model
    #clf = LinearRegression()
    clf = svm.SVR(kernel="linear")
    clf_2 = BayesianRidge(compute_score=True)
    clf.fit(x_train,y_train)
    clf_2.fit(x_train,y_train)

    #find the accuracy
    accuracy_svm = clf.score(x_test,y_test)     #square error
    accuracy_bayesian = clf_2.score(x_test,y_test)

    #print(accuracy)

    forecast_set = clf.predict(X_lately)
    forecast_set_bayesian = clf_2.predict(X_lately)
    nn = MLPRegressor(
        hidden_layer_sizes=(20, 20), activation='relu', solver='adam', alpha=0.001, batch_size='auto',
        learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=10000, shuffle=True,
        random_state=0, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
        early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

    nn = nn.fit(x_train, y_train)
    # accuracy = nn.score(x_test,y_test)
    # print("Accuracy:",accuracy)
    # test_x = np.arange(0.0, 1, 0.05).reshape(-1, 1)
    ann_value = nn.predict(X_lately)
    # plot the future 35 values
    #print("SVM:",forecast_set,accuracy_svm,forecast_out)
    #print("BAYESIAN:",forecast_set_bayesian,accuracy_bayesian,forecast_out)
    #print("ANN:",ann_value)
    return (forecast_set_bayesian[0] + forecast_set[0] + ann_value) / 3  # avg value of bayesian + SVM
