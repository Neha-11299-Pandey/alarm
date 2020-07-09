import datetime

alarmHour = int(input("what hour do you want to wakeup"))
alarmMinute = int(input("what minute do you want to wakeup"))
amPm = str(input("am" or "pm"))


if(amPm == "pm") :
    alarmHour = alarmHour + 12
while(1==1):
    if(alarmHour == datetime.datetime.now().hour and
        alarmMinute == datetime.datetime.now().minute):
     print("wake up you are getting late")
    break

print("exited")
