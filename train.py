# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import cv2, os
import sys

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
window.title("Face_Registration")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)

#window.geometry('1280x720')
window.configure(background='blue')

window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

#path = "profile.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#panel = tk.Label(window, image = img)


#panel.pack(side = "left", fill = "y", expand = "no")

#cv_img = cv2.imread("img541.jpg")
#x, y, no_channels = cv_img.shape
#canvas = tk.Canvas(window, width = x, height =y)
#canvas.pack(side="left")
#photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
# Add a PhotoImage to the Canvas
#canvas.create_image(0, 0, image=photo, anchor=tk.NW)

#msg = Message(window, text='Hello, world!')

# Font is a tuple of (font_family, size_in_points, style_modifier_string)



message = tk.Label(window, text="STUDENT  REGISTRATION" ,bg="WHITE"  ,fg="BLUE"  ,width=50  ,height=3,font=('Arial', 60, 'bold '))

message.place(x=00, y=00)

lbl = tk.Label(window, text="Enter ID",width=20  ,height=2  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') )
lbl.place(x=300, y=250)

txt = tk.Entry(window,width=30  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt.place(x=500, y=255)

lbl2 = tk.Label(window, text="Enter Name",width=20  ,fg="red"  ,bg="yellow"    ,height=2 ,font=('times', 15, ' bold '))
lbl2.place(x=300, y=350)

txt2 = tk.Entry(window,width=30  ,bg="yellow"  ,fg="red",font=('times', 15, ' bold ')  )
txt2.place(x=500, y=355)

lbl3 = tk.Label(window, text="Notification : ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold underline '))
lbl3.place(x=300, y=450)

message = tk.Label(window, text="" ,bg="yellow"  ,fg="red"  ,width=50  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold '))
message.place(x=500, y=450)

# lbl3 = tk.Label(window, text="Attendance : ",width=20  ,fg="red"  ,bg="yellow"  ,height=2 ,font=('times', 15, ' bold  underline'))
# lbl3.place(x=400, y=650)


# message2 = tk.Label(window, text="" ,fg="red"   ,bg="yellow",activeforeground = "green",width=30  ,height=2  ,font=('times', 15, ' bold '))
# message2.place(x=700, y=650)

def clear():
    txt.delete(0, 'end')
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')
    res = ""
    message.configure(text= res)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def TakeImages():
    idd=(txt.get())
    face_id=idd


    ss=str(txt2.get())
    if(is_number(idd) and ss.isalpha()):
        # Start capturing video
        vid_cam = cv2.VideoCapture(0)

        # Detect object in video stream using Haarcascade Frontal Face
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # For each person, one face id
        #
        # print('enter the id ')
        # idd = input()
        # face_id = idd
        # print('enter the nmae ')
        # idd1 = input()
        # ss = str(idd1)

        # Initialize sample face image
        count = 0

        # Start looping
        while (True):

            # Capture video frame
            _, image_frame = vid_cam.read()

            # Convert frame to grayscale
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

            # Detect frames of different sizes, list of faces rectangles
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            # Loops for each faces
            for (x, y, w, h) in faces:
                # Crop the image frame into rectangle
                cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Increment sample face image
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/" + str(ss) + '.' + str(face_id) + '.' + str(count) + ".jpg",
                            gray[y:y + h, x:x + w])

                # Display the video frame, with bounded rectangle on the person's face
                cv2.imshow('frame', image_frame)

            # To stop taking video, press 'q' for at least 100ms
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            # If image taken reach 100, stop taking video
            elif count > 100:
                break

        # Stop video
        vid_cam.release()
        res = "Images Saved for ID : " + idd + " Name : " + ss
        message.configure(text=res)
        # Close all started windows
        cv2.destroyAllWindows()

    else:
        if(is_number(idd)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(ss.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)

def TrainImages():

    # Create Local Binary Patterns Histograms for face recognization
    # recognizer = cv2.face.createLBPHFaceRecognizer()

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Using prebuilt frontal face training model, for face detection

    # Get the faces and IDs
    faces, ids = getImagesAndLabels('dataset')

    # Train the model using the faces and IDs
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer.yml
    recognizer.write('trainer/trainer.yml')

    res = "Image Trained"#+",".join(str(f) for f in Id)
    message.configure(text= res)
    cv2.destroyAllWindows()



def getImagesAndLabels(path):
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # Get all file path
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    # imagePaths = cv2.imread(os.path.abspath(path))

    # Initialize empty face sample
    faceSamples = []

    # Initialize empty id
    ids = []

    # Loop all the file path
    for imagePath in imagePaths:

        # Get the image and convert it to grayscale
        PIL_img = Image.open(imagePath).convert('L')
        # gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

        # PIL image to numpy array
        img_numpy = np.array(PIL_img, 'uint8')

        # Get the image id
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        print(id)

        # Get the face from the training images
        faces = detector.detectMultiScale(img_numpy)

        # Loop for each face, append to their respective ID
        for (x, y, w, h) in faces:
            # Add the image to face samples
            faceSamples.append(img_numpy[y:y + h, x:x + w])

            # Add the ID to IDs
            ids.append(id)

    # Pass the face array and IDs array
    return faceSamples, ids

# def TrackImages():
#     # Create Local Binary Patterns Histograms for face recognization
#     ##recognizer = cv2.face.createLBPHFaceRecognizer()
#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#
#     # Load the trained mode
#     recognizer.read('trainer/trainer.yml')
#
#     # Load prebuilt model for Frontal Face
#     cascadePath = "haarcascade_frontalface_default.xml"
#
#     # Create classifier from prebuilt model
#     faceCascade = cv2.CascadeClassifier(cascadePath);
#
#     # Set the font style
#     font = cv2.FONT_HERSHEY_SIMPLEX
#
#     # Initialize and start the video frame capture
#     cam = cv2.VideoCapture(0)
#
#     f = open("Database.txt", 'a')
#     f.write("\nDATE \t TIME \t \t \t TEACHER NAME \t  STUDENT NAME\n ")
#     print('Executing the script')
#     f.close()
#
#     # Local variable Declaration
#     lecture = 0
#     count1 = 0
#     count2 = 0
#     count3 = 0
#     count4 = 0
#     sample = 0
#     take = 1
#     # Loop
#
#     pas = []
#     lis = []
#     pf = []
#
#     def password():
#
#         pas = []
#         for i in range(0, 4):
#             pas.append(str(randint(0, 9)))
#         # print(pas)
#         account_sid = 'AC20f958ddba458dfa5b605880862bd1a7'
#         auth_token = '70533ab8353096fc2776ae746fddb163'
#         client = Client(account_sid, auth_token)
#         client = Client(account_sid, auth_token)
#         message = client.messages.create(
#             from_='+12054309676',
#             body='OTP is :{}'.format(str(pas)),
#             to='+917892332933'
#         )
#
#         print('enter the password :')
#         str1 = input()
#
#         lis = list(str1)
#
#         if lis == pas:
#             print('password matcheds ')
#             return '1'
#         else:
#             print('2222222222222')
#             return '2'
#
#     once = 1
#     correct = 0
#     while True:
#
#         now = datetime.datetime.now()
#
#         # Read the video frame
#         ret, im = cam.read()
#
#         # Convert the captured frame into grayscale
#         gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#
#         # Get all face from the video frame
#         faces = faceCascade.detectMultiScale(gray, 1.2, 5)
#
#         # For each face in faces
#         for (x, y, w, h) in faces:
#
#             # Create rectangle around the face
#             cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)
#
#             # Recognize the face belongs to which ID
#             Id, i = recognizer.predict(gray[y:y + h, x:x + w])
#
#             print(i)
#             print(Id)
#
#             if once == 1:
#                 li = password()
#                 once = 0
#             if li == '1':
#                 print('matches ')
#                 correct = 1
#                 li = '9'
#             if li == '2':
#                 once = 1
#                 li = '2'
#                 correct = 0
#                 print('Wrong Password Try Again')
#
#             if correct == 1:
#
#                 if i < 55:
#
#                     sample = sample + 1
#                     # Check the ID if exist
#                     if (Id == 1 and take):
#                         take = 0
#                         count1 = 1
#
#                         Id = "Ganesh"
#                         print('Take Attendance ')
#                         lecture = 1
#                         ##                sample =0
#                         time.sleep(10)
#                     # If not exist, then it is Unknown
#                     elif (Id == 2):
#                         count4 = 1
#                         Id = "megha"
#                         Id1 = Id
#                     elif (Id == 3):
#                         count3 = 1
#                         Id = "arun"
#                         Id2 = Id
#                     elif (Id == 4):
#                         count2 = 1
#                         Id = "sushma"
#                         Id3 = Id
#                 else:
#                     print(Id)
#                     Id = "Unknown"
#
#                 # Put text describe who is in the picture
#                 cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
#                 cv2.putText(im, str(Id), (x, y - 40), font, 2, (255, 255, 255), 3)
#
#                 # Display the video frame with the bounded rectangle
#                 cv2.imshow('im', im)
#
#         # If 'q' is pressed, close program
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break
#         if lecture == 1 or lecture == 2 or lecture == 3:
#
#             if sample > 50:
#                 sample = 0
#
#                 f = open("Database.txt", 'a')
#                 if lecture == 1 and count4 == 1:
#                     f.write(str(now) + '\t' + "Ganesh" + '\t' + str(count4) + '\t' + str(Id1) + '\n')
#                 if lecture == 1 and count3 == 1:
#                     f.write(str(now) + '\t' + "Ganesh" + '\t' + str(count3) + '\t' + str(Id2) + '\n')
#                 if lecture == 1 and count4 == 1:
#                     f.write(str(now) + '\t' + "Ganesh" + '\t' + str(count2) + '\t' + str(Id3) + '\n')
#
#                 f.close()
#                 break
#         if cv2.waitKey(1) & 0xff == ord('q'):
#             break
#     # Stop the camera
#     cam.release()
#
#     # Close all windows
#     cv2.destroyAllWindows()


clearButton = tk.Button(window, text="Clear", command=clear  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=800, y=245)
clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="red"  ,bg="yellow"  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton2.place(x=800, y=345)
takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=650, y=500)
trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=650, y=600)
# trackImg = tk.Button(window, text="Track Images", command=TrackImages  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
# trackImg.place(x=800, y=500)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=650, y=700)


window.mainloop()
