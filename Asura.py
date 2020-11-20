# модули
import datetime, wikipedia, time
import speech_recognition as sr
import os, re, sys, json
import webbrowser, youtube_dl, random
import smtplib, requests, subprocess, urllib
from pyowm import OWM
import pyttsx3 as p
from bs4 import BeautifulSoup as soup

wikipedia.set_lang("ru")
now = datetime.datetime.now()

def listen():
    text = input("Господин, приказывайте >>> ")
    print(f"Хозяин сказал:{text}")

    return text

def say(text):
    print(f"Asura:{text}")
    
#команды
def handle_command(command):
    command = command.lower()
    if command == "привет":
        say("Приветсвую, господин")
    elif command == 'время':
        now = datetime.datetime.now()
        say("Сейчас {0}:{1}".format(str(now.hour), str(now.minute)))
    elif command == "пока":
        stop()
    elif 'сайт' in command:
        reg_ex = re.search('сайт (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
        else:
            pass
    elif 'расскажи о' in command:
        reg_ex = re.search('расскажи о (.*)', command)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)
                say(ny.content[:1000])
        except Exception as e:
                say(e)
    elif command == "выкл":
        os.system('shutdown /s /f /t 10')
        stop()  
    elif 'случайное число' in command:
        ot=command.find('от')
        do=command.find('до')
        f_num=int(command[ot+3:do-1])
        l_num=int(command[do+3:])
        s=str(random.randint(f_num, l_num))
        say('Asura: ' + s)
    elif command == 'команды':
        say('\nпривет\nсайт(например: сайт vk.com)\nрасскажи о\nкоманды\nслучайное число от до\nпока\nвыкл\nвремя')
    else:
        say("Простите,господин,ваш покорный слуга слишком глуп")

def stop():
    say("До свидания,господин")
    exit()
    
def start():
    print("Asura подключается ...")

    while True:
        command = listen()
        handle_command(command)

try:
    start()
except KeyboardInterrupt:
    stop()
