from moviepy.editor import *
from tkinter import Tk
from tkinter import filedialog

print("Select the directory containing Mp4 Songs")
Tk().withdraw()
path = filedialog.askdirectory()
path=path+"/"

print("Select the directory where you wnat to save the converted Mp3 Songs")
Tk().withdraw()
path2 = filedialog.askdirectory()
path2=path2+"/"

# path='E:/Kpop/2/'
# path2=r'E:/mp3kpop/2/'
list = os.listdir(path)

for f in list:
    # print(path+f)
    # ff,fg=f.split(".")
    new=path2+f+".mp3"
    # print(new)
    try:
        videoclip = VideoFileClip(path+f)

        audioclip = videoclip.audio
        
        audioclip.write_audiofile(new)

        audioclip.close()
        videoclip.close()
    except:
        pass