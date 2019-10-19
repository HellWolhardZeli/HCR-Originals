import cv2
import os

vid=cv2.VideoCapture("C:\\Users\\kumar\\Downloads\\cap.mp4")


try:
	if not os.path.exists('frm'):
		os.makedirs('frm')

except OSError:
	print ('Not able to make director frm')

frame=0

while(1):

	x,cap=vid.read()

	if x:
		data ='./frm/cap'+ str(frame) + '.jpg'

		cv2.imwrite(data, cap)

		frame+=1
	else:
		print('')
		break

