# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import simpledialog
from tkinter import *
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import cv2, os
import sys
# Import OpenCV2 for image processing
import cv2
from twilio.rest import Client
# Import numpy for matrices calculations
import numpy as np
import time
import datetime

from random import randint
import cv2
from twilio.rest import Client
# Import numpy for matrices calculations
import numpy as np
import time
import datetime

from random import randint

# Import numpy for matrix calculation
import numpy as np

# Import Python Image Library (PIL)
from PIL import Image
import pandas as pd
import datetime
import time
import glob
# Import numpy for matrix calculation
import numpy as np

# Import Python Image Library (PIL)
from PIL import Image
import tkinter.ttk as ttk
import tkinter.font as font

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, wezight='bold')
window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)

#window.geometry('1280x720')
window.configure(background='blue')

window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="TAKE ATTENDANCE" ,bg="WHITE"  ,fg="BLUE"  ,width=50  ,height=3,font=('times', 60, 'bold '))

message.place(x=0, y=20)

# lbl = tk.Label(window, text="ENTER OTP",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') )
# lbl.place(x=300, y=400)
#
# txt = tk.Entry(window,width=20  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
# txt.place(x=500, y=415)
#
# lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="red"  ,bg="yellow"    ,height=2 ,font=('times', 15, ' bold '))
# lbl2.place(x=300, y=300)
#
# txt2 = tk.Entry(window,width=20  ,bg="yellow"  ,fg="red",font=('times', 15, ' bold ')  )
# txt2.place(x=500, y=315)

lbl3 = tk.Label(window, text="Notification : ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold underline '))
lbl3.place(x=300, y=500)

message = tk.Label(window, text="" ,bg="yellow"  ,fg="red"  ,width=50  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))
message.place(x=500, y=500)


def TrackImages():
    # Create Local Binary Patterns Histograms for face recognization
    ##recognizer = cv2.face.createLBPHFaceRecognizer()
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Load the trained mode
    recognizer.read('trainer/trainer.yml')

    # Load prebuilt model for Frontal Face
    cascadePath = "haarcascade_frontalface_default.xml"

    # Create classifier from prebuilt model
    faceCascade = cv2.CascadeClassifier(cascadePath);

    # Set the font style
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Initialize and start the video frame capture
    cam = cv2.VideoCapture(0)

    f = open("Database.txt", 'a')
    f.write("\nDATE \t TIME \t \t \t TEACHER NAME \t  STUDENT NAME\n ")
    print('Executing the script')
    f.close()

    # Local variable Declaration
    lecture = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    sample = 0
    take = 1
    # Loop

    pas = []
    lis = []
    pf = []



    once = 1
    correct = 0
    while True:

        now = datetime.datetime.now()

        # Read the video frame
        ret, im = cam.read()

        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # Get all face from the video frame
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        # For each face in faces
        for (x, y, w, h) in faces:

            # Create rectangle around the face
            cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)

            # Recognize the face belongs to which ID
            Id, i = recognizer.predict(gray[y:y + h, x:x + w])

            # print(i)
            # print(Id)

            if once == 1:
                li = password()
                once = 0
            if li == '1':
                res="Password Matched"
                message.configure(text=res)
                correct = 1
                li = '9'
            if li == '2':
                once = 1
                li = '2'
                correct = 0
                res="Wrong OTP! Try Later"
                message.configure(text=res)

            if correct == 1:

                if i < 55:

                    sample = sample + 1
                    # Check the ID if exist
                    if (Id == 1 and take):
                        take = 0
                        count1 = 1

                        Id = "Ganesh"
                        print('Take Attendance ')
                        lecture = 1
                        ##                sample =0
                        time.sleep(10)
                    # If not exist, then it is Unknown
                    elif (Id == 2):
                        count4 = 1
                        Id = "megha"
                        Id1 = Id
                    elif (Id == 3):
                        count3 = 1
                        Id = "arun"
                        Id2 = Id
                    elif (Id == 4):
                        count2 = 1
                        Id = "sushma"
                        Id3 = Id
                else:
                    print(Id)
                    Id = "Unknown"

                # Put text describe who is in the picture
                cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
                cv2.putText(im, str(Id), (x, y - 40), font, 2, (255, 255, 255), 3)

                # Display the video frame with the bounded rectangle
                cv2.imshow('im', im)

        # If 'q' is pressed, close program
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        if lecture == 1 or lecture == 2 or lecture == 3:

            if sample > 50:
                sample = 0

                f = open("Database.txt", 'a')
                if lecture == 1 and count4 == 1:
                    f.write(str(now) + '\t' + "Ganesh" + '\t' + str(count4) + '\t' + str(Id1) + '\n')
                if lecture == 1 and count3 == 1:
                    f.write(str(now) + '\t' + "Ganesh" + '\t' + str(count3) + '\t' + str(Id2) + '\n')
                if lecture == 1 and count4 == 1:
                    f.write(str(now) + '\t' + "Ganesh" + '\t' + str(count2) + '\t' + str(Id3) + '\n')

                f.close()
                break
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    # Stop the camera
    cam.release()
    res = "THANK YOU FOR ATTENDANCE"
    message.configure(text=res)

    # Close all windows
    cv2.destroyAllWindows()

def password():

    pas = []
    for i in range(0, 4):
        pas.append(str(randint(0, 9)))
    # print(pas)
    account_sid = 'AC89654cf5c2b10ba37146079573607456'
    auth_token = 'd5f35dfe2744d5c588122d625cad1475'
    client = Client(account_sid, auth_token)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+17165684770',
        body='OTP is :{}'.format(str(pas)),
        to='+919738559888'
    )

    # res='enter the password :'
    # message.configure(text=res)
    # str1 = (txt.get())

    str1=simpledialog.askstring("input","Enter One Time Password")
    lis = list(str1)

    if lis == pas:
        # res = "Password Matched"
        # message.configure(text=res)
        return '1'
    else:
        # res = "Wrong Password! Try Again Later"
        # message.configure(text=res)
        return '2'


button = tk.Button(window, text='Generate OTP',width=20,height=3,font=('times',15,'bold'), command=TrackImages)
button.pack()
button.place(x=600,y=300)
# trackImg = tk.Button(window, text="Generate OTP", command=TrackImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
# trackImg.place(x=600, y=300)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=600, y=600)


window.mainloop()