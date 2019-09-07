#main program file
#written and debugged by: Mareesh Kumar Issar, Kartik Rattan, Suraj Nagaraja, and Ashwin Channakeshava
#assisted by: Sarthak Vengurlekar

import mysql.connector
import pandas as pd
import numpy as np
def show_open_close(symbol):
    con = mysql.connector.connect(             #connect to the mysql using the root and pwd
            host = 'localhost',
            user = 'root',
            password = 'passwordphrase@123',
            database = 'PROJECT'                  #include the database you need to work on
        )
    cursor = con.cursor();
    df = pd.read_sql("Select open,high,low,close,volume from "+symbol+" limit 1",con)
    #results_as_list = [i[0] for i in results]
    #values = np.fromiter(results_as_list, dtype=np.float_)
    pf = df.values.tolist()
    values_return = []
    for i in pf[0]:
        values_return.append(i)
    #print(values_return)
    return values_return

