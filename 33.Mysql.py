# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:55:21 2018

@author: 18096
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.2.200",
  user="gspadmin",
  passwd="Gspadmin$1234",
  database = "db_timesheet"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM to_timeoffice where emp_no = 18096"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)