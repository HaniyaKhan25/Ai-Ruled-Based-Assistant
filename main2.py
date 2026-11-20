# Ai ruled based asiistent:

import datetime
import time

name = input("Enter your name :" )
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning", name)
elif 11 <= presentHour <= 17:
     print("Good afternoon", name)
elif 17 <= presentHour <= 21:
      print("Good evening", name)
elif 21 <= presentHour <= 24:
      print("Good Night", name)

print("Asslam o alikum ! welcome to Ai buddy")
print(" type to bye user to exit to bot")