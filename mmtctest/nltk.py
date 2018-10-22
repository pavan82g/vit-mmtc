#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 00:52:30 2018

@author: pavan
"""
import speech_recognition as sr
def stt():
    # get audio from the microphone                                                                       
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.record(source, duration = 10)   
        s = r.recognize_google(audio)
    try:
        print("You said " + r.recognize_google(audio))
        #f.write(s)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    
    return s
                                                                          
s = stt()
f = open('out2.txt','w')
f.write("/n")
f.write(s)

