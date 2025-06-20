import pyttsx3
import datetime

engine = pyttsx3.init()

def process_query(query):
    query = query.lower()
    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"the current time is {now}"
    elif "date" in query:
        date = datetime.datetime.now().strftime("%B,%D,%Y")
        return f"today's date is {date}"
    
    else:
        return "sorry could not understand the command"
    
def main():
    print("Assistant is running enter your choice time , date , exit")
    
    while True:
      choice = input("you :  ")
      if choice == "exit":
          print("Assitant stopped!")
          break
      response = process_query(choice)
      print(f"The response is {response}")
      engine.say(response)
      engine.runAndWait()


main()