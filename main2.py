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

# "Memory of chatbot with dictionary"

responses = {
     "hi": "Welcome to Ai chatbot",
     "how are you": "i am very fine, thank you",
     "who are you": "i am smart chatbot",
     "what is ai": "Artificial intelligence",
     "what is functions": "block of reusable code",
     "motivate me": "Keep going every bug of your project,makes you a better developer",
      "happy" : "Great to hear that",
     "what is functions?" : "reusable block code",
     "what is phyhon": "Phyton is a programming language",
     "what is ai": "ai stands for artificial intelligence",
     "thank you": "You are most welcome!"
    }

# Method of function get to responses:

def getOfResponses(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
               return responses[eachkey]
        elif "i am sad" in userQuestion:
             return "Dont worry! everything will be fine"
        elif "i am happy" in userQuestion:
             return"thats ! Great Wounderful"

    return "i am not able to that yet i am still in learning mode"

while True:
     userInput = input("\n PlEASE! ask your question : ")

     if "bye" in userInput.lower():
          print("\n Good by! Have a nice day")
          break
     reply = getOfResponses(userInput)