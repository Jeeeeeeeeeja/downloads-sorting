from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import re
import time
import shutil


source = ''
username = os.getlogin()
path = f'C:\\Users\\{username}\\Downloads'
picturepath = f'C:\\Users\\{username}\\Pictures'
videospath = f'C:\\Users\\{username}\\Videos'
audiospath = f'C:\\Users\\{username}\\Music'
docspath = f'C:\\Users\\{username}\\Documents'


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
    '.cs': documents
}


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        extension = re.findall(r'\.\w*', event.src_path)[0]
        file_ext_dict[extension](event.src_path)


observer = Observer()
observer.schedule(Handler(), path=path, recursive=False)
observer.start()
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
