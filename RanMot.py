import datetime
import os
import random


random.seed()

x   = random.randint(1,1000)
now = str(datetime.datetime.now())

def equalchoice():
    if os.path.exists('choice.txt') == False:
        report = open('choice.txt','w')
        report.write("NOT 17th movie was randomly chosen. " + now)
        report.close()
    elif os.path.exists('choice.txt') == True:
        report = open('choice.txt','a')
        report.write("\nNOT 17th movie was randomly chosen. " + now)
        report.close()

if x < 60:
    os.startfile("1.mp4")
    equalchoice()
elif 60 <= x < 120:
    os.startfile("2.mp4")
    equalchoice()
elif 120 <= x < 180:
    os.startfile("3.mp4")
    equalchoice()
elif 180 <= x < 240:
    os.startfile("4.mp4")
    equalchoice()
elif 240 <= x < 300:
    os.startfile("5.mp4")
    equalchoice()
elif 300 <= x < 360:
    os.startfile("6.mp4")
    equalchoice()
elif 360 <= x < 420:
    os.startfile("7.mp4")
    equalchoice()
elif 420 <= x < 480:
    os.startfile("9.mp4")
    equalchoice()
elif 480 <= x < 540:
    os.startfile("10.mp4")
    equalchoice()
elif 540 <= x < 600:
    os.startfile("11.mp4")
    equalchoice()
elif 600 <= x < 660:
    os.startfile("12.mp4")
    equalchoice()
elif 660 <= x < 720:
    os.startfile("13.mp4")
    equalchoice()
elif 720 <= x < 780:
    os.startfile("14.mp4")
    equalchoice()
elif 780 <= x < 840:
    os.startfile("15.mp4")
    equalchoice()
elif 840 <= x < 900:
    os.startfile("16.mp4")
    equalchoice()
else:
    os.startfile("17.mp4")
    if os.path.exists('choice.txt') == False:
        report = open('choice.txt','w')
        report.write("17th movie was randomly chosen.     " + now)
        report.close()
    elif os.path.exists('choice.txt') == True:
        report = open('choice.txt','a')
        report.write("\n17th movie was randomly chosen.     " + now)
        report.close()
