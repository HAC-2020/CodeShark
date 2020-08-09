from flask import Flask, render_template, redirect, url_for, request, flash
import requests, yaml
from flask_mysqldb import MySQL
import joblib
db = yaml.load(open('db.yaml'))

app = Flask(__name__)
model = joblib.load ('AhmedabadVAR.pkl')
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
    details = str()

    #values = [133.88,198.83,233.58,253.30,282.32,283.91,292.08,302.11,309.17,317.31,322.92]
    values = float()
    
    details = request.args.get['city']
        #city = details['val']   
        #city = "Ahmedabad"
    if details == "Ahmedabad":
        values = 133.88
    if details == "Mumbai":
        values = 46.69
    '''elif city == "Amravati":
        values = 52.27
    elif city == "Amritsar":
        values = [99.84, 100.85, 103.31, 102.25, 105.99, 110.27, 110.74, 112.27, 112.99, 113.9, 115.2]
    elif city == "Bengaluru":
        values = [53.41, 56.5, 59.08, 61.27, 63.86, 63.84, 63.33, 65.54, 66.38, 66.86, 68.29]
    elif city == "Bhopal":
        values = [60.27, 64.86, 69.83, 74.26, 78.68, 82.6, 86.12, 89.27, 92.11, 94.69, 97.04]
    elif city == "Brajrajnagar":
        values = [139.8, 191.84, 167.39, 153.67, 149.91, 139.1, 137.51, 138.59, 142.49, 157.8, 153.71]
    elif city == "Chandigarh":
        values = [95.91, 98.27, 94.39, 93.49, 92.53, 90.39, 88.52, 87.4, 86.57, 85.98, 85.63]
    elif city == "Chennai":
        values = [86.28, 95.28, 97.15, 101.1, 100.21, 105.65, 105.46, 108.85, 109.73, 106.35, 104.64]
    elif city == "Coimbatore":
        values = [68.76, 68.63, 66.12, 65.34, 64.88, 64.83, 64.92, 65.12, 65.38, 65.68, 66.01]
    elif city == "Delhi":
        values = [125.78, 116.72, 132.55, 143.66, 144.39, 140.03, 129.14, 131.03, 136.33, 142.75, 142.56]
    elif city == "Ernakulam":
        values = [109.17, 107.53, 106.02, 104.65, 103.41, 102.32, 101.36, 100.53, 99.8, 99.16, 98.61]
    elif city == "Gurugram":
        values = [155.06, 171.83, 165.59, 155.19, 161.3, 173.61, 178.48, 174.8, 175.91, 177.65, 182.31]
    elif city == "Guwahati":
        values = [55.77, 66.58, 66.79, 68.42, 76.12, 80.17, 82.91, 87.09, 90.83, 93.45, 96.12]
    elif city == "Hyderabad":
        values = [65.01, 65.53, 64.72, 66.62, 68.75, 66.06, 67.35, 69.04, 71.81, 73.64, 75.09]
    elif city == "Jaipur":
        values = [120.59, 98.37, 91.83, 82.91, 89.56, 101.41, 108.36, 107.4, 106.56, 105.47, 106.95]
    elif city == "Jorapokhar":
        values = [118.49, 121.14, 119.17, 120.43, 119.05, 120.38, 117.17, 115.08, 114.61, 113.39, 113.29]
    elif city == "Kochi":
        values = [130.04, 77.8, 53.7, 78.51, 116.62, 121.72, 116.51, 66.79, 37.12, 54.77, 92.38]
    elif city == "Kolkata":
        values = [36.01, 39.74, 43.33, 45.94, 52.01, 54.67, 54.3, 54.1, 54.56, 56.9, 59.3]
    elif city == "Lucknow":
        values = [79.57, 81.1, 79.46, 82.8, 80.82, 82.57, 83.53, 85.53, 87.45, 89.12, 91.19]
    elif city == "Mumbai":
        values = [46.69, 57.04, 64.63, 64.28, 64.24, 60.49, 59.51, 60.06, 63.89, 69.82, 69.48]
    elif city == "Patna":
        values = [106.16, 113.99, 118.86, 121.15, 124.27, 125.46, 130.31, 135.72, 139.94, 144.16, 147.05]
    elif city == "Shillong":
        values = [31.13, 30.59, 34.35, 35.75, 36.3, 37.54, 38.93, 40.0, 40.78, 41.66, 42.43]
    elif city == "Talcher":
        values = [67.74, 72.28, 81.6, 94.88, 102.51, 102.27, 104.05, 106.43, 110.31, 113.68, 116.21]
    elif city == "Thiruvananthapuram":
        values = [36.51, 44.75, 45.29, 49.6, 53.44, 55.27, 56.73, 54.84, 55.21, 55.69, 57.05]
    elif city == "Visakhapatnam":
        values = [58.21, 63.84, 75.13, 78.07, 80.62, 83.6, 86.8, 89.65, 91.89, 93.92, 95.72]'''
    return render_template("app.html", values=values)

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
