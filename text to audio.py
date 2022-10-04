from gtts import gTTS
from playsound import playsound
text=input("Enter a sentence(In English) : ") #taking the Sentence from user
speech=gTTS(text=text,lang="en")        #converting to mp3 in English
speech.save(r"C:\Users\jouha\Desktop\jou.mp3")        #saving the .mp3 file in the given directory
playsound(r"C:\Users\jouha\Desktop\jou.mp3")          
