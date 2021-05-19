#Gets temperature, then coverts into celsius, then prints  
temperature = int(input("What's the temperature (in the american system): "))

newtemp = (temperature - 32) * (5/9)

print("your new temperature (in the rest of the world is:" ,newtemp)

break1 = str(input("BREAK TIME! enter anything to continue "))

#Gets temperature, asks if it is fahrenheit or celsius, splits paths based of answer 
temperature = int(input("What's your temperature? "))
corf = str(input("Now is that fahrenheit or celsius? (F or C) "))

if corf == "F":
  newtemp = (temperature - 32) * (5/9)
  print(newtemp, " Congrats! its now celsius!")
elif corf == "C":
  newtemp = (temperature + 32) * (9/5)
  print(newtemp, " Congrats! Now it's in fahrenheit")
else:
  print("F OR C! I said... F OR C")

break2 = str(input("BREAK TIME! enter anything to continue "))

#creates a wordcount, and while the while loop isn't broken, ask the user to print out as many words as possible, then when the users prersses x stop the count and print his count number
wordcount = 0

while True:
  words = str(input("Please input a word, if you are done printing words, press x. "))
  print (words)
  if words == "x":
    print("You have entered", wordcount, "words")
    break
  else:
    wordcount += 1

break3 = str(input("BREAK TIME! enter anything to continue "))

#creates a password and asks the user to input guesses until he gets the right answer
password = ("Wafflehouse2for1deal")
entryquestion = str(input("You must enter a password to proceed \n"))

while True:
  if entryquestion != password:
    print("Wrong answer, I'm just going to enjoy my waffles now")
    entryquestion = str(input("You must enter another password to proceed \n"))
  else:
    print("congrats! you may proceed")
    break

break4 = str(input("BREAK TIME! enter anything to continue "))

#creates an empty list of numbers that we will fill later, while the user hasn't inputted 10 numbers continue to ask until he is done. After inputting ten numbers print all the numbers bababooey done

numbercount = 0
numberlis = []

while numbercount <= 9: #Lists/arrays start at Zero
  number = (input("Input a number please:"))
  numbercount += 1
  numberlis.append(number)
print("You have inputted: ")
print(" ".join(numberlis))

