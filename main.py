from question import ask_question
import time

score = 0
x = 1

print("Welcome! Do you know your History?")
choice = input("Press 1 to proceed or Press 2 to quit: ")
if choice == "1":
  print("Let's begin!")
  time.sleep(x) 
elif choice == "2":
  time.sleep(x)
  print("You Quit")
else:
  print("Please pick 1 or 2 next time.")
if choice == "1":

  # This is the start of a question
  score = score + ask_question(
    "1",
    "What was the last battle of the Napoleonic Wars?",
    "(a) Battle of Wavre (b) Battle of the Nile (c) Battle of Waterloo (d) Battle of Trafalgar ",
    "a"
  )
  
  score = score + ask_question(
    "2",
    "Which of the following inventions was the first to be patented?",
    "(a) A Dishwasher (b) A Rubber Band (c) A Cash Register (d) Chewing Gum ",
    "b"
  )

  score = score + ask_question(
    "3",
    "Who was the first U.S president to be impeached?",
    "(a) Bill Clinton (b) Richard Nixon (c) Herbert Hoover (d) Andrew Johnson",
    "d"
  )

  score = score + ask_question(
    "4",
    "Who served as chief minister to King Henry VIII of England from 1532 to 1540?",
    "(a) Thomas Cromwell (b) Robert Cecil (c) Philip Henslowe (d) Walter Raleigh",
    "a"
  )

  score = score + ask_question(
    "5",
    "Who was the first European to discover New Zealand?",
    "(a) Abel Janszoon Tasman (b) James Cook (c) Marc-Joseph Marion Du Fresne (d) Marco Polo",
    "a"
  )

  score = score + ask_question(
    "6",
    "What was the first major war campaign fought entirely by air forces?",
    "(a) Operation Linebacker (b) Battle of Kursk (c) Operation Mole Cricket 19 (d) Battle of Britain",
    "d"
  )

  score = score + ask_question(
    "7",
    "What Greek general is responsible for the project that generated most of the surviving structures on the Acropolis, including the Parthenon?",
    "(a) Alcibiades (b) Leonidas (c) Pericles (d) Xenophon",
    "c"
  )
  
  score = score + ask_question(
    "8",
    "What captain claimed the first naval victory for the United States in the American Revolutionary War?",
    "(a) David Farragut (b) Olivard Hazard Perry (c) Benedict Arnold (d) Captain John Paul Jones",
    "d"
  )
  
  score = score + ask_question( 
    "9",
     "What was the Year of the Five Emperors?",
     "(a) 17 (b) 193 (c) 239 (d) 39",
     "b"
  )

  score = score + ask_question(
    "10",
    "Which of the following was true of Black soldiers in the United States Army during World War I?",
    "(a) They served in segragated units (b) They were only allowed in noncombat positions (c) They weren't allowed to enlist (d) They served in fully integrated units",
    "a"
  )
 
  print ("Waiting for results...")
  time.sleep(3) 

  print("Your total score is " + str(score) + " out of 10!")
  