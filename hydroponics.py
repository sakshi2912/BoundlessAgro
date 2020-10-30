from time import sleep
import random
import pyrebase

# Generating dummy values
def gen_list(start,end,precision,step_val):
	gen = []
	gen.append(start)
	while start < end:
		start = start + step_val
		gen.append(round(start,precision))
	gen.append(end)
	return gen

pH_range = gen_list(4.5,5.8,3,0.001)
ppm_range = gen_list(1260,1360,2,0.01)
temp_range = gen_list(22,24,1,0.1)

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

while True:
	vals = db.get()
	for x in vals.each():
		if x.key() == "Values":
			data_present = x.val()
	if data_old != data_present:
		print(data_present)  # Take updated value
		data_old = data_present
		print("DATA FROM UPDATED VALUE")
	else:
		gen_dict = {"pH" : random.choice(pH_range), "ppm" : random.choice(ppm_range), "temp" : random.choice(temp_range)}
		print(gen_dict)	# Take dummy generated value
	sleep(0.25)