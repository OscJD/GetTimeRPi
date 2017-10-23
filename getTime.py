from urllib import urlopen
import os
import time

#res=urlopen('http://just-the-time.appspot.com/')

while(True):
    try:
        strin=r'<span id="currentTime">'

        res=urlopen('http://24timezones.com/es_husohorario/mexico_city_hora_actual.php')

        timeStr=res.read().strip()
        particion=timeStr.split(strin)
        print particion
        timeAct=str(particion[1]).split(" ")
        print "sudo date -s "+timeAct[0]+" "+timeAct[1][0:2]

        os.system("sudo date -s "+timeAct[0]+timeAct[1][0:2])
        timeStr=""
        particion={}
        time.sleep(60)

    except:

        time.sleep(60)
