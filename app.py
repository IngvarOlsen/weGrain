import sqlite3
import sys
import time
from datetime import datetime
from flask import Flask, url_for, render_template, request, g


app = Flask(__name__,
            static_folder='static',
            template_folder='template')


@app.route('/')
def index():
    return render_template("index.html")

########################
##### Db handling ######
########################

# Had to make the db connector to a repeatable callable function, as the connection have to be close everytime it gets used 
def dbConnect():
    global conn
    conn = sqlite3.connect('wegrain.db')
    global curs
    curs = conn.cursor()

# Adds a dht22 reading
# Parsing the input to avoid SQL injection, which is not crazy important in this project, but better to just always use it 
@app.route('/_addReadings', methods=['POST'])
def addReadings(temp, humid, containerId):
    dbConnect()
    sql = """INSERT INTO Readings(temp, humid, containerID) values(:temp, :humid, :containerId)"""
    curs.execute(sql, [temp, humid, containerId])
    conn.commit()
    conn.close()

# Adds a container
@app.route('/_addContainer', methods=['POST'])
def addContainer():
    dbConnect()
    sql = """INSERT INTO Container(loadingDate) values(:dateTime)"""
    dateTime = datetime.now()
    curs.execute(sql,[dateTime])
    conn.commit()
    conn.close()

# return all readings
@app.route('/_getAllReadings', methods=['GET','POST'])
def getAllReadings():
    dbConnect()
    for data in curs.execute("SELECT * FROM Readings;"):
        print(data)  
    conn.close()
    return data

# return inner join, gets all data belonging to specific container
@app.route('/_getContainerReadings', methods=['GET','POST'])
def getContainerReadings(containerId):
    dbConnect()
    sql = """SELECT * FROM Readings INNER JOIN Container ON :containerId = Container.ID"""
    for data in curs.execute(sql, [containerId]):
        print(data)  
    conn.close()
    return data

# Deletes specifc container with ID
@app.route('/_deleteContainer', methods=['POST'])
def deleteContainer(containerId):
    dbConnect()
    sql = """DELETE FROM Container WHERE Container.ID = :containerId"""
    curs.execute(sql, [containerId])
    conn.commit()
    conn.close()

# Deletes specifc container with ID, and all readings of it
@app.route('/_deleteContainerAndReadings', methods=['POST'])
def deleteContainerAndReadings(containerId):
    dbConnect()
    sql = """DELETE FROM Readings WHERE Readings.containerId = :containerId"""
    curs.execute(sql, [containerId])
    sql2 = """DELETE FROM Container WHERE Container.ID = :containerId"""
    curs.execute(sql2, [containerId])
    conn.commit()
    conn.close()


### For testing ###
# getAllReadings()
# addContainer()
# addContainer()
# addReadings(22, 22, 1)
# addReadings(22, 23, 1)
# addReadings(24, 25, 1)
# addReadings(26, 28, 2)
# #getContainerReadings(1)
# #deleteContainerAndReadings(1)
# conn.close()





if __name__ == '__main__':
    app.run(debug=True)

