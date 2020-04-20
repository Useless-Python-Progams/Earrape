#Welcome to Terrible Earrape run the program to continue
import winsound
import time
print ("are you sure you want to continue? y/n")
life_or_death = input()
if life_or_death == "y":
    print ("sound will play on 3")
    time.sleep(2)
    print("3")
    time.sleep(2)
    print("2")
    time.sleep(2)
    print("1")
    time.sleep(2)
    winsound.Beep(32767, 100000)
print ("stopped program, lucky")
