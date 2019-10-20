import cv2
import os

os.makedirs('cap')
face=cv2.CascadeClassifier('face.xml')

eye=cv2.CascadeClassifier('eye.xml')

vid=cv2.VideoCapture("C:\\Users\\kumar\\Downloads\\cap7.mp4")
count=0
while 1:

	xbool,frame=vid.read()

	if xbool:
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	else:
		print(count)
		break

	chera=face.detectMultiScale(gray,1.3,5)

	for(a,b,c,d) in chera:
		cv2.rectangle(frame,(a,b),(a+c,b+d),(255,255,0),2)
		roig=gray[b:b+d,a:a+c]
		roic=frame[b:b+d,a:a+c]
		
		
		
		# aankh=eye.detectMultiScale(roig)

		# for(x,y,z,w) in aankh:
		# 	cv2.rectangle(roic,(x,y),(x+z,y+w),(0,127,255),2)

		data ='./cap/frame'+ str(count) + '.jpg'
		cv2.imwrite(data, frame)
		count+=1
	
	cv2.imshow('img',frame)

	k=cv2.waitKey(30) & 0xff
	if k == 27:
		break
