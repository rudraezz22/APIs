import requests
import random
import html

education_id = 9
api_link = f"https://opentdb.com/api.php?amount=10&category={education_id}&type=multiple"

def get_trivia_questions():
    response = requests.get(api_link)
    if response.status_code == 200 :
       data = response.json()
       if data["response_code"]==0 and data["results"]:
           return data["results"]
    else:
           return None
    
def quizz_run():
     questions = get_trivia_questions()
     if not questions:
          print("An error occured")
          return 
     
     score = 0 
           
     print("welcome to trivia quizz")
     for i , q in enumerate(questions,1):
          question = html.unescape(q["question"])
          correct = html.unescape(q["correct_answer"])
          incorrect = [html.unescape(a) for a in q["incorrect_answers"]]
          options = incorrect + [correct]
          random.shuffle(options)

          print("question:" , i , question)
          for idx , option in enumerate(options , 1):
               print(idx,option)

          while True :
                 try:
                  choice = int(input("enter your choice between 1 - 4\n"))
                  if 1<= choice <=4:
                      break
                  else:
                      print("please enter a valid number between 1-4")
                 except ValueError:
                      print("please enter value in numbers")

          if options[choice-1] == correct:
             print("CORRECT ANSWER!\n")
             score = score+1
          else:
              print(f"incorrect answer! the correct answer is {correct}\n")

     print(f"your total score is {score}")
     print(f"your total percentage of correct answers is {(score/len(questions))*100} ")

quizz_run()

       