from pytube import YouTube
from tkinter import filedialog
from tkinter import *
import tkinter as tk

def selectDocLocation():
    window.filename =  filedialog.askdirectory(initialdir = "/",title = "Select file")


def getYoutubeUrl():
    youtubeurl = youtubeurl_entry.get()
    yt = YouTube(youtubeurl)
    dl = yt.streams.get_highest_resolution()
    dl.download(window.filename)
    completedLabel = tk.Label(window, text="Download Completed...", font="bold", pady=5)
    completedLabel.pack()

# tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.title("Youtube Downloader")
#Get Youtube URL / Youtube adresini kullanıcıdan al
youtubeurl_label = tk.Label(window, text="Youtube URL")
youtubeurl_entry = tk.Entry(window)
youtubeurl_label.pack()
youtubeurl_entry.pack()
# Select Dir / İndirilecek konumu seç
SelectDir = tk.Button(window, text="Select Download Location:", command = selectDocLocation)
SelectDir.pack()
#Download Button / İndir Butonu
DownloadButton = tk.Button(window, text= "Download", command = getYoutubeUrl)
DownloadButton.pack()
#Main Loop
window.mainloop()