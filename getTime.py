from urllib import urlopen
import os
import time

resDate=urlopen('http://just-the-time.appspot.com/')

while(True):
    try:
        strin=r'<span id="currentTime">'
        res=urlopen('http://24timezones.com/es_husohorario/mexico_city_hora_actual.php')
        resDate=urlopen('http://just-the-time.appspot.com/')

        timeStr=res.read().strip()
        dateStr=resDate.read().strip()
        particion=timeStr.split(strin)
        particionDate=dateStr.split(" ")
       
        timeAct=str(particion[1]).split(" ")
        dateAct=str(particionDate[0])
        print dateAct
        print "sudo date -s "+dateAct+" "+timeAct[0]+" "+timeAct[1][0:2]

        os.system("sudo date -s "+dateAct+" "+timeAct[0]+" "+timeAct[1][0:2])
        timeStr=""
        dateStr=""
        particion={}
        particionDate{}
        time.sleep(60)

    except:

        time.sleep(60)
