from telethon import TelegramClient, sync
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterPhotos
import socks
import configparser

config = configparser.ConfigParser()
config.read('configure.ini')

# Use your own values here,need to configure your own
api_id = config.get('baseconf', 'api_id')
api_hash = config.get('baseconf', 'api_hash')
client = TelegramClient('derren', api_id,api_hash,proxy=(socks.SOCKS5, '127.0.0.1', 1080)
).start()

progress_list = []
with open("telegram_progress_pic.txt","r") as t:
    for line in t.readlines():
        progress_list.append(line.strip("\n"))
print(progress_list)
t.close()

def progress_callback(current, total):
    print(f"\rDownloading {round(current/float(1024)/float(1024),1)} / {round(total/float(1024)/float(1024),1)} MB [{round(current/total,2)*100}%]", end=" ")

try:
    counter = 0
    for message in client.iter_messages("vivi zhou", filter=InputMessagesFilterPhotos):
        if str(message.id) not in progress_list:
            print(f'Progress {counter}/*', message)
            client.download_media(message, progress_callback=progress_callback, file="./telegram_pic/")

            t = open("telegram_progress_pic.txt", "a+")
            t.write(str(message.id)+"\n")
            t.close()

        counter += 1
except KeyboardInterrupt:
    pass
except:
    pass



