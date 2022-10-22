import time

score = 0
x = 1


def ask_question(number, question, answers, answer):
  possible_choices = ["a", "b", "c", "d"]
  
  print ("Question " + number)
  print(question)

  while True:
    a = input(answers)
    if a in possible_choices:
      if a is answer:
        print("Correct!")
        time.sleep(x)
        return 1
          
      else:
        print("Wrong.")
        time.sleep(x)
        return 0
    else: 
      time.sleep(x)
      print("Not an answer, please choose either a, b, c, or d next time.")

  time.sleep(x)
