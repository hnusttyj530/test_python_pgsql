# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:37:19 2020

@author: 1670171244@qq.com
"""


import psycopg2
def connectPgDB():
    conn = psycopg2.connect(database="tyj", user="postgres", password="123456", host="127.0.0.1", port="5432")
    print ("Opened database successfully")
    cur = conn.cursor()
    cur.execute("SELECT id, name, address, salary  from COMPANY")
    rows = cur.fetchall()
    for row in rows:
        print ("ID = ", row[0])
        print ("NAME = ", row[1])
        print ("ADDRESS = ", row[2])
        print ("SALARY = ", row[3], "\n")
    print ("Operation done successfully")
    conn.close()
if __name__=='__main__':
    connectPgDB()