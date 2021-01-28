import os
import json
import platform
from datetime import datetime
import pytz
from importlib import import_module
from pyrogram import Client
lang = open('config.json', encoding='utf8')
data = json.load(lang)

for x in data['config']:
    sett = x

app = Client('session', api_id=sett['api_id'], api_hash=sett['api_hash'], bot_token=sett['bot_token'])

ALIAS = ['@','.','/','#']

def send(chatid, text):
    app.send_message(chatid, text)

def load_modules():
    from os.path import basename, isfile
    import glob
    global modulicaricati
    print(sett['bot_token'])
    mod_paths = glob.glob('fedeisalone/modules/*py')
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith('.py')
    ]
    if len(all_modules) > 0:
        for module_name in all_modules:
            try:
                import_module('fedeisalone.modules.' + module_name)
                print('[*] [ ' + module_name + ' ]')
            except Exception as err:
                print(f'[!] {module_name} | {err}')
    else:
        print("[!] No module loaded")
    return True

def clearbro():
    os.system("clear")
    print("  ______       _           _           \n |  ____|     | |         (_)          \n | |__ ___  __| | ___ _ __ _  ___ ___  \n |  __/ _ \/ _` |/ _ \ '__| |/ __/ _ \ \n | | |  __/ (_| |  __/ |  | | (_| (_) |\n |_|  \___|\__,_|\___|_|  |_|\___\___/ \n                                       ")
