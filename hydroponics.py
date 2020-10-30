from time import sleep
import random
import pyrebase
import knn_from_scratch

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
weights_list = [[50,50],[25,75],[75,25]]
while True:
	vals = db.get()
	for x in vals.each():
		if x.key() == "Values":
			data_present = x.val()
		elif x.key() == "Prediction":
			pH_weights = weights_list[int(x.val()['pH'])]
			ppm_weights = weights_list[int(x.val()['ppm'])]
			temp_weights = weights_list[int(x.val()['temp'])]
	if data_old != data_present:
		data_old = data_present
		pH_value = float(data_old['pH'])
		ppm_value = float(data_old['ppm'])
		temp_value = float(data_old['temp'])
	else:
		gen_dict = {"pH" : round(pH_value+random.choices([-random.random(),random.random()],weights = pH_weights)[0],3),
		"ppm" : round(ppm_value+random.choices([-random.random(),random.random()],weights = ppm_weights)[0],2),
		"temp" : round(temp_value+random.choices([-random.random(),random.random()],weights = temp_weights)[0],1)}
		print(gen_dict)	# Take dummy generated value
		pH_com,ppm_com,temp_com = knn_from_scratch.main_knn(gen_dict['pH'],gen_dict['ppm'],gen_dict['temp'])
		db.child("Prediction").update({"pH":pH_com,"ppm":ppm_com,"temp":temp_com})
		db.child("Values").update(gen_dict)
	sleep(5)
