from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import base64
from wsgiref.util import FileWrapper
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# Create your views here.
def home(request):
	return render(request,'home.html')

def content(request):
	data = {"message" :"Heart disease describes a range of conditions that affect your heart. Diseases under the heart disease umbrella include blood vessel diseases, such as coronary artery disease; heart rhythm problems (arrhythmias); and heart defects you're born with (congenital heart defects), among others.The term \"heart disease\" is often used interchangeably with the term \"cardiovascular disease.\" Cardiovascular disease generally refers to conditions that involve narrowed or blocked blood vessels that can lead to a heart attack, chest pain (angina) or stroke. Other heart conditions, such as those that affect your heart's muscle, valves or rhythm, also are considered forms of heart disease."}
	return JsonResponse(data)

def image(request):
	image_data = open("/home/prithvi/Desktop/heart/catalog/static/1234.jpg", "rb").read()
	encoded_string = base64.b64encode(image_data)
	return HttpResponse(encoded_string, content_type="image/png")

#def audio(request):
#    fname="/home/prithvi/Downloads/heart/catalog/static/audio.mp3"
#    f = open(fname,"rb") 
#    response = HttpResponse()
#    response.write(base64.b64encode(f.read()))
#    response['Content-Type'] ='audio/mp3'
#    response['Content-Length'] =os.path.getsize(fname )
#    return response
    
def video(request):
    video_data = open("/home/prithvi/Desktop/heart/catalog/static/video.mp4", "rb").read()
    encoded_string = base64.b64encode(video_data)
    return HttpResponse(encoded_string, content_type="video/mp4")

def link(request):
	with open('links.csv','r') as fin:
		reader = csv.reader(fin,delimiter=',')
		data={}
		i=0
		for row in reader:
			l=[row[0],row[1]]
			data[i]=l
			i=i+1
		print(data)

	return JsonResponse(data)

def check(request):
	return render(request,'check.html')

def pred(request):
	print(request.GET['age'])
	#age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
	loc = request.GET['loc']
	l = [request.GET['age'],request.GET['gen'],request.GET['cpt'],request.GET['rbp'],request.GET['chol'],request.GET['fbs'],request.GET['recg'],request.GET['mhr'],request.GET['eia'],request.GET['st'],request.GET['slope'],request.GET['cv'],request.GET['thal']]
	insert(l)
	return render(request,'result.html',{'loc' :loc})

import csv
def insert(m):
	print("lala")
	l = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
	k = [l,m]
	with open('newdata.csv','w') as fout:
		writer = csv.writer(fout)
		writer.writerows(k)



def result(request):
	res = svm()
	print(res[0])
	data = {'result':int(res[0])}
	return JsonResponse(data)

def doc(request):
	loc = request.GET['loc']
	print(loc)
	with open('doc.csv','r') as fin:
		reader = csv.reader(fin,delimiter=',')
		data={}
		i=0
		for row in reader:
			if row[2]==loc:
				l=[row[0],row[1]]
				data[i]=l
				i=i+1
		print(data)

	return JsonResponse(data)



def svm():
	dataset = pd.read_csv('HealthData.csv')
	X = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, 13].values
	
	imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
	imputer=imputer.fit(X[:,11:13])
	X[:,11:13]=imputer.transform(X[:,11:13])

	X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.25)

	sc_X=StandardScaler()
	X_train=sc_X.fit_transform(X_train)
	X_test=sc_X.transform(X_test)

	svc_scores = []
	kernels = ['linear', 'poly', 'rbf', 'sigmoid']
	for i in range(len(kernels)):
		svc_classifier = SVC(kernel = kernels[i])
		svc_classifier.fit(X_train, Y_train)
		svc_scores.append(svc_classifier.score(X_test, Y_test))

	classifier = SVC(kernel = 'rbf', random_state = 0 ,probability=True)
	classifier.fit(X_train, Y_train)
	y_pred = classifier.predict(X_test)

	cm = confusion_matrix(Y_test, y_pred)
	print(cm)

	Newdataset = pd.read_csv('newdata.csv')
	ynew=classifier.predict(Newdataset)
	print(ynew)
	return ynew
	#return 1
	

	
