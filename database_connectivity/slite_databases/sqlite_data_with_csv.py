# SQLite is a software library that implements a lightweight relational database management system

import sqlite3
import pandas as pd

conn = sqlite3.connect('D:/Project/Python_Tutorial/database_connectivity/school.db')

data = pd.read_csv('D:/Project/Python_Tutorial/database_connectivity/Data/DimDate.csv')

cur = conn.cursor()
 

dimdat = '''
DROP TABLE IF EXISTS dimdat;

CREATE TABLE dimdat (
    DateKey                INTEGER NOT NULL PRIMARY KEY,
    DateValue              DATE    NOT NULL,
    DayNumberOfWeek        INTEGER NOT NULL,
    DayNameOfWeek          TEXT    NOT NULL,
    DayNumberOfMonth       INTEGER NOT NULL,
    DayNumberOfYear        INTEGER NOT NULL,
    WeekNumberOfYear       INTEGER NOT NULL,
    MonthName              TEXT NOT NULL,
    MonthNumberOfYear      INTEGER NOT NULL,
    CalendarQuarter        INTEGER NOT NULL,
    CalendarYear           INTEGER NOT NULL,
    FiscalQuarter          INTEGER NOT NULL,
    FiscalYear             INTEGER NOT NULL 
);
''' 

# cur.executescript(dimdat)
try:
    print("load data ")
    data.to_sql('dimat', conn, if_exists='replace', index=False)
except Exception as e:
    print('completed data')

 