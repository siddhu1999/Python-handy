# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:48:19 2020

@author: SIDDHRAJSINH
"""
#import the below packages that are important for the working of this translator
import speech_recognition as sr
import googletrans
from googletrans import Translator
import pyttsx3
from gtts import gTTS
import os

#initiating the recognizer so that it can catch the speech
r=sr.Recognizer()
#defining the microphone to be used(default)
mic=sr.Microphone(device_index=0)
#interacting with the user with a greeting message
speechengine=pyttsx3.init()
speechengine.say("welcome!! to the chotasiri translator")
speechengine.runAndWait()
speechengine.say("do you want to see the supported languages")
speechengine.runAndWait()
c=str(input("(y/n)"))
if c=='y': #show the google trans supported languages dictionary
    print(googletrans.LANGUAGES)
#if no
speechengine.say("Enter the language code without space")
speechengine.runAndWait()
trans=str(input("Language code: -")) #saving the language code for future use
#program will start listening from the mic source
print("Listening....")
with mic as source: #conditional loop
    r.adjust_for_ambient_noise(source) #optional, used to reduce the background noise
    audio=r.listen(source) #listening to the mic and saving it to a variable audio type 'speech_recognition.AudioData'
result=r.recognize_google(audio) #after saving the audio, recognize_google will recognize the language and convert the speech to text

print(result)

#program will try to translate the text obtained from above segment into destination language
p=Translator() 
k=p.translate(result,dest=trans) #user input destination language
translated=str(k.text) # converting "googletrans.models.Translated" to text 
print(translated)

#text to speech
output=gTTS(text=translated,lang=trans) #gTTS will speak the translated word

output.save("Translated.mp3") 
os.system("start Translated.mp3")

