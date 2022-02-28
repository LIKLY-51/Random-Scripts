import os
import threading

dirpath = ""
key = ""

skip = True # skips files with certain exstensions
# the default ones are mainly just for files that don't contain readable text
skipables = ['exe', 'dll', 'sys', 'jpeg', 'jpg', 'img', 'bmp', 'png', 'gif', 'mp3', 'mp4', 'mkv', 'mov', 'dat', 'jar', 'ttf', 'vtf', 'vmt', 'gma']

to_check = []
threads = []

def setFiles():
    print('Getting files :)')
    for path, subdirs, files in os.walk(dirpath):
        if files:
            for file in files:
                if file.split('.')[-1] in skipables and skip:
                    continue
                to_check.append(os.path.join(path, file))

def checkFile(dir):
    f = open(dir)
    line_num = 1
    try:
        for line in f.readlines():
            if (key in line):
                print(f"Found {key} in {dir} // {line_num}\n", end="")
                return
            line_num = line_num + 1
    except:
        return

if (__name__ == "__main__"):
    dirpath = input('Path: ')
    key = input('Key: ')
    setFiles()
    
    for file in to_check:
        t = threading.Thread(target=checkFile, args=[file])
        t.daemon = True
        threads.append(t)

    for i in range(len(threads)):
        threads[i].start()

    for i in range(len(threads)):
        threads[i].join()