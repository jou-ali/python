import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter3=chr(random.randint(97,122)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter4=chr(random.randint(0,127)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter5=chr(random.randint(0,127)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter6=chr(random.randint(60,71)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter7=chr(random.randint(97,122)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter8=chr(random.randint(60,71)) #Generate a random Uppercase letter (based on ASCII code)

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + uppercaseLetter7 + uppercaseLetter8 # + ....
password = shuffle(password)

#Ouput
print(password)
