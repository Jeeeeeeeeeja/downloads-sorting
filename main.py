from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import re
import time
import shutil


source = ''
username = os.getlogin()
if os.name == 'nt':
    path = f'C:\\Users\\{username}\\Downloads'
    picturepath = f'C:\\Users\\{username}\\Pictures'
    videospath = f'C:\\Users\\{username}\\Videos'
    audiospath = f'C:\\Users\\{username}\\Music'
    docspath = f'C:\\Users\\{username}\\Documents'
elif os.name == ('mac' or 'posix'):
    with open('settings.txt', 'r') as file:
        downloads_name = file.readline(0)[:-2]
        pictures_name = file.readline(1)[:-2]
        videos_name = file.readline(2)[:-2]
        music_name = file.readline(3)[:-2]
        docs_name = file.readline(4)
    path = f'/home/{username}/{downloads_name}'
    picturepath = f'/home/{username}/{pictures_name}'
    videospath = f'/home/{username}/{videos_name}'
    audiospath = f'/home/{username}/{music_name}'
    docspath = f'/home/{username}/{docs_name}'
else:
    with open('settings.txt', 'r') as file:
        path = file.readline(0)[:-2]
        picturepath = file.readline(1)[:-2]
        videospath = file.readline(2)[:-2]
        audiospath = file.readline(3)[:-2]
        docspath = file.readline(4)


def pictures(source):
    shutil.move(source, picturepath)


def videos(source):
    shutil.move(source, videospath)


def audios(source):
    shutil.move(source, audiospath)


def documents(source):
    shutil.move(source, docspath)


file_ext_dict = {
    '.png': pictures,
    '.jpg': pictures,
    '.jpeg': pictures,
    '.tif': pictures,
    '.raw': pictures,
    '.bmp': pictures,
    '.mp4': videos,
    '.avi': videos,
    '.webm': videos,
    '.wmv': videos,
    '.mp3': audios,
    '.flac': audios,
    '.wav': audios,
    '.aac': audios,
    '.doc': documents,
    '.docx': documents,
    '.txt': documents,
    '.pdf': documents,
    '.csv': documents,
    '.json': documents,
    '.readme': documents,
    '.md': documents,
    '.py': documents,
    '.fb2': documents,
    '.epub': documents,
    '.mobi': documents,
    '.html': documents,
    '.css': documents,
    '.xlsx': documents,
    '.xls': documents,
    '.cs': documents,
    '.tmp': time.sleep(0.1)
}


class Handler(FileSystemEventHandler):

    def on_modified(self, event):
        try:
            extension = re.findall(r'\.\w*', event.src_path)[0]
            file_ext_dict[extension](event.src_path)
        except TypeError:
            pass


observer = Observer()
observer.schedule(Handler(), path=path, recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
