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

wordcount = 0

while True:
  words = str(input("Please input a word, if you are done printing words, press x. "))
  print (words)
  if words == "x":
    print("You have entered", wordcount, "words")
    break
  else:
    wordcount += 1


