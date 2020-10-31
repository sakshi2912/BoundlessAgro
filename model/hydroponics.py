from time import sleep
import random
import pyrebase
import knn_model
import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv("dataset.csv")
df.head()
X1=df[["ppm","temp","ph pump","ppm pump","temp pump"]]
Y1=df['pH']

config = {
    "apiKey": "AIzaSyDHvRKfnEyHYp5YBTU3kQz-p4vtUIacTc8",
    "authDomain": "hydroponics-195ff.firebaseapp.com",
    "databaseURL": "https://hydroponics-195ff.firebaseio.com",
    "projectId": "hydroponics-195ff",
    "storageBucket": "hydroponics-195ff.appspot.com",
    "messagingSenderId": "663121661536",
    "appId": "1:663121661536:web:8e41b89b5794284c8dfd05",
    "measurementId": "G-3WFT4BE3EJ",
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
vals = db.get()

for x in vals.each():
	if x.key() == "Values":
		data_present = x.val()
data_old = data_present
pH_value = float(data_old['pH'])
ppm_value = float(data_old['ppm'])
temp_value = float(data_old['temp'])
weights_list = [[50,50],[10,90],[90,10]]
while True:
	vals = db.get()
	for x in vals.each():
		if x.key() == "Values":
			data_present = x.val()
		if x.key() == "pH":
			pH_weights = weights_list[int(x.val())]
		if x.key() == "ppm":
			ppm_weights = weights_list[int(x.val())]
		if x.key() == "temp":
			temp_weights = weights_list[int(x.val())]
	if data_old != data_present:
		data_old = data_present
		pH_value = float(data_old['pH'])
		ppm_value = float(data_old['ppm'])
		temp_value = float(data_old['temp'])
	else:
		gen_dict = {"pH" : round(pH_value+random.choices([-random.random(),random.random()],weights = pH_weights)[0],3),
		"ppm" : round(ppm_value+random.choices([-random.random(),random.random()],weights = ppm_weights)[0],2),
		"temp" : round(temp_value+random.choices([-random.random(),random.random()],weights = temp_weights)[0],1)}
		print("Data from sensor",gen_dict)	# Take dummy generated value
		pH_com,ppm_com,temp_com = knn_model.main_knn(gen_dict['pH'],gen_dict['ppm'],gen_dict['temp'])
		db.update({"pH":str(pH_com),"ppm":str(ppm_com),"temp":str(temp_com)})
		db.child("Values").update(gen_dict)
		lr=LinearRegression()
		lr.fit(X1,Y1)
		predictedpH=lr.predict([[gen_dict["ppm"],gen_dict["temp"],pH_com,ppm_com,temp_com]])
		db.update({"predpH":round(predictedpH[0],3)})
		print("Linear Regression Value for pH : ",round(predictedpH[0],3))
		sleep(2)