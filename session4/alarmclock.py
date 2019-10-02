import datetime
datetime.datetime.now()

print('Bay gio la {}'.format(datetime.datetime.now().strftime("%H:%M")))

alarmClock = input("gio ban muon hen: ")

while True:
    currentTime = datetime.datetime.now().strftime(%H:%M)

    if alarmClock == curenTime:
        print("Bao thuc")
        