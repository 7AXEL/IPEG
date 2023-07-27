from tkinter import messagebox
import tkinter as tk
import keyboard
import socket
import time
import sys
import os

_libs_ = ['geocoder', 'folium', 'webview', 'colorama']
_module_ = []
_points_ = ['    ', '.   ', '..  ', '... ']

def loading():
    for i in range(4):
        for _load_ in range(len(_points_)):
            _point_ = _points_[_load_]
            print(f'\r{_point_}', end='')
            time.sleep(0.1)

for index in range(len(_libs_)):
    _lib_ = _libs_[index]
    try:
        _module_.append(__import__(_lib_))
        loading()
    except:
        os.system(f'pip install {_lib_}')
        _module_.append(__import__(_lib_))

def error(msg):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", msg)


if sys.platform in ['win64', 'win32']:
    os.system('cls')
    _module_[3].init()
elif sys.platform in ['Linux', 'Linux2']:
    os.system('clear')
else:
    error('Unsupported OS')
    exit()

print('''\033[1;38;5;202m
▀█▀ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█  ┌■■■■┐
▒█░ ▒█▄▄█ ▒█▀▀▀ ▒█░▄▄ (_^..^_)
▄█▄ ▒█░░░ ▒█▄▄▄ ▒█▄▄█   ||||
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n''')

while True:
    host = input('\033[1;38;5;180m║HOST/IP:\033[0;0m')

    if host == '':
        exit()

    try:
        ip = socket.gethostbyname(host)
    except:
        ip = host

    try:
        location = _module_[0].ip(f"{ip}").latlng
        map_obj = _module_[1].Map(location=[location[0], location[1]], zoom_start=13)
        _module_[1].Marker([location[0], location[1]], popup="Host Location").add_to(map_obj)
        map_obj.save("map.html")
        title = host[0:host.find('.')]
        _module_[2].create_window(f'{title} server location',url='map.html', width=700, height=450)
        _module_[2].start()
    except:
        error('Can\'t resolve the IP adress')
