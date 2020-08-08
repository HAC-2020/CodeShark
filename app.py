from flask import Flask, render_template, redirect, url_for, request, flash
import requests, yaml
from flask_mysqldb import MySQL

db = yaml.load(open('db.yaml'))

app = Flask(__name__)
app.secret_key = 'hello'
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cache', methods=['GET','POST'])
def cache():
    if request.method == 'POST':
        details = request.form
        city = details['city']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO aqi(city) VALUES(%s)', [city])
        mysql.connection.commit()
        cur.close()
        flash(message='done')
    return render_template('app.html')

@app.route('/ml', methods=["GET","POST"])
def ml():
    #Importing the required Modules and Libraries
    import pandas as pd
    import joblib
    city = str()
    Air_quality = float()
    if request.method == 'POST':
        details = request.form
        city = details['city']
        print (22)
        if city == "Mumbai":
            AQIVAR=joblib.load('MumbaiVAR.pkl')
            prediction=AQIVAR.forecast(AQIVAR.y,steps=11)
            # Loading the csv file to get the columns
            df=pd.read_csv(r'Mumbai.csv')
            df.drop(["Date","City", "Benzene", "Toluene", "Xylene", "NH3","NO", "NOx","AQI_Bucket"],axis=1,inplace=True)
            #Converting our prediction array to Dataframe
            Prediction=pd.DataFrame(index=range(0,len(prediction)),columns=df.columns)

            for j in range(7):
                for i in range(len(prediction)):
                    Prediction.iloc[i][j]=prediction[i][j]
            from datetime import datetime
            datetime.today()
            date=datetime.now()

            da=date.day
            hr=date.hour
            mn=date.month
            yr=date.year

            tf=pd.DataFrame({'year':[yr,yr,yr,yr,yr,yr,yr,yr,yr,yr,yr],'month':[mn,mn,mn,mn,mn,mn,mn,mn,mn,mn,mn],'day':[da,da+1,da+2,da+3,da+4,da+5,da+6,da+7,da+8,da+9,da+10]})
            dat=str(pd.to_datetime(tf)).split()
            Dat=[]
            for i in range(1,len(dat)-1,2):
                Dat.append(dat[i])
            RD=pd.DataFrame({'year':[yr],'month':[mn],'day':[da]})
            DAT=str(pd.to_datetime(RD)).split()
            print(DAT)
            '''record=[]
            record.append(DAT[1])
            record.append(PM)
            record.append(PM10)
            record.append(NO2)
            record.append(CO)
            record.append(SO2)
            record.append(O3)
            record.append(AQI)'''
            AQIs = list (Prediction["AQI"])
            Air_quality = (AQIs[0])
    return render_template("app.html", city=city)

@app.route('/failed', methods=["GET","POST"])
def failed():
    if request.method == 'POST':
        details = request.form
        city = details['city']
        pm10 = details['pm10']
        pm25 = details['pm25']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO aqi(city,pm1,pm25) VALUES(%s,%s,%s)', (city,pm10,pm25))
        mysql.connection.commit()
        cur.close()
    return render_template('failed.html')
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM aqi")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
@app.route('/data', methods=["GET","POST"])
def data():
    if request.method == 'POST':
        details = request.form
        data = details['data']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO data(data) VALUES(%s)', [data])
        mysql.connection.commit()
        cur.close()
    return render_template('data.html')


if __name__ == '__main__':
    app.run()
