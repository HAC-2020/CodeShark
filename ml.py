import pandas as pd 
import warnings
warnings.filterwarnings('ignore')
# Reading the data from csv file
df=pd.read_csv(r'C:\Users\Sanchit Jain\Downloads\CodeShark-master\CodeShark-master\Visakhapatnam.csv')
df.drop (["Benzene", "Toluene", "Xylene", "NH3","NO", "NOx","AQI_Bucket"], axis = 1, inplace=True)
df["Date"].dtype
df["Date"]=pd.to_datetime(df["Date"])
df["Date"].dtype
df.drop(["City"],axis=1,inplace=True)
df.index=df.Date
df.drop(["Date"],axis=1,inplace=True)
#Finding all the null indexes in PM 2.5 and their total no.
#Finding all the null indexes in PM 2.5 and their total no.
medianm = df ["PM2.5"].median()
df["PM2.5"].fillna(medianm, inplace = True)
sum=0
for i in range(1149):
    if df["PM2.5"][i]==-10:
        print(i)
        sum+=1
#Finding all the null indexes in PM 10 and their total no.
pm10m = df["PM10"].median()
df["PM10"].fillna(pm10m, inplace = True)
sum=0
for i in range(1149):
    if df["PM10"][i]==-100:
        print(i)
        sum+=1
def replace(j):
    if df["PM10"][j]!=(-100):
        return df["PM10"][j]
    else:
        return replace(j+1)
pm10m = df["PM10"].median()
df["PM10"].fillna(pm10m, inplace = True)

for i in range(1149):
    if df["PM10"][i]==-100:
        df["PM10"][i]=(replace(i+1)+df["PM10"][i-1])/2
#Finding all the null indexes in SO2 and their total no.
so2m = df["SO2"].median()
df["SO2"].fillna(so2m, inplace = True)
sum=0
for i in range(1149):
    if df["SO2"][i]==-300:
        print(i)
        sum+=1
def replace(j):
    if df["SO2"][j]!=(-300):
        return df["SO2"][j]
    else:
        return replace(j+1)
        
df["SO2"].fillna(-300, inplace = True)

for i in range(1149):
    if df["SO2"][i]==-300:
        df["SO2"][i]=(replace(i+1)+df["SO2"][i-1])/2
#Finding all the null indexes in nO2 and their total no.
no2m = df["NO2"].median()
df["NO2"].fillna(no2m, inplace = True)
sum=0
for i in range(1149):
    if df["NO2"][i]==-400:
        print(i)
        sum+=1
#Finding all the null indexes in nO2 and their total no.
o3m = df["O3"].median()
df["O3"].fillna(o3m, inplace = True)
sum=0
for i in range(1149):
    if df["O3"][i]==-200:
        print(i)
        sum+=1
#Filling and finding AQI
#Finding all the null indexes in nO2 and their total no.
o3m = df["O3"].median()
df["O3"].fillna(o3m, inplace = True)
for i in range(1149):
    if df["O3"][i]==-200:
        print(i)
        sum+=1
aqim = df["AQI"].median()
df["AQI"].fillna(aqim, inplace = True)
sum=0
for i in range(1149):
    if df["AQI"][i]==-200:
        print(i)
        sum+=1
com = df["CO"].median()
df["CO"].fillna(com, inplace = True)
sum=0
for i in range(1149):
    if df["CO"][i]==-200:
        print(i)
        sum+=1
#Function to convert PM 2.5 to AQI
#Do keep in mind. It won't be exactly accurate

def PMAQI(Ci):
    if Ci>0 and Ci<=12:
        Ahi=50
        Alo=0
        Clo=0
        Chi=12
    elif Ci>12 and Ci<=35.4:
        Ahi=100
        Alo=51
        Clo=12.1
        Chi=35.4
    elif Ci>35.4 and Ci<=55.4:
        Ahi=150
        Alo=101
        Clo=35.5
        Chi=55.4
    elif Ci>55.4 and Ci<=150.4:
        Ahi=200
        Alo=151
        Clo=55.4
        Chi=150.4
    elif Ci>150.4 and Ci<=250.4:
        Ahi=300
        Alo=201
        Clo=150.5
        Chi=250.4
    elif Ci>250.4 and Ci<=1149.4:
        Ahi=400
        Alo=301
        Clo=250.4
        Chi=1149.4
    elif Ci>1149.4 and Ci<=500.4:
        Ahi=500
        Alo=401
        Clo=1149.4
        Chi=500.4
    elif Ci>500.4 and Ci<=999.4:
        Ahi=999
        Alo=501
        Clo=500.4
        Chi=999.4
    AQI=((Ahi-Alo)/(Chi-Clo))*(Ci-Clo)+Alo
    return AQI

#df["AQI"][570]=PMAQI(df["PM2.5"][570])
#df["AQI"][889]=PMAQI(df["PM2.5"][889])
#df["AQI"][890]=PMAQI(df["PM2.5"][890])
#Checking Stationarity
from statsmodels.tsa.vector_ar.vecm import coint_johansen
t=df
coint_johansen(t,-1,1).eig
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
#Creating the validation and train set
train=df[:int(0.8*(len(df)))]
valid=df[int(0.8*(len(df))):]
#fitting the model
from statsmodels.tsa.vector_ar.var_model import VAR

model=VAR(endog=df)
model_fit=model.fit(maxlags=15,ic='aic')
#Making predictions on dataset
prediction=model_fit.forecast(model_fit.y,steps=11)
#Converting our prediction array to Dataframe
Prediction=pd.DataFrame(index=range(0,len(prediction)),columns=df.columns)
for j in range(7):
    for i in range(len(prediction)):
        Prediction.iloc[i][j]=prediction[i][j]
import joblib
joblib.dump(model_fit,'VisakhapatnamVAR.pkl')
print (Prediction)