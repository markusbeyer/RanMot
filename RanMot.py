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
