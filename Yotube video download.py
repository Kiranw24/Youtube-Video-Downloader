from tkinter import *
from PIL import Image, ImageTk
from pytube import YouTube

root = Tk()
root.geometry('400x250')
root.title('Youtube Video Downloader Application')
root.configure(bg='magenta')

image = Image.open("C:/Users/Kiran Ware/PycharmProjects/tkinter/youtube-logo.png")
image = image.resize((100,50))
photo = ImageTk.PhotoImage(image)

lab = Label(image=photo)
lab.pack()

def download():
    try:
        myVar.set('Downloading...')
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set('Video Downloaded Successfully')
    except Exception as e:
        myVar.set('Something went wrong')
        root.update()
        link.set('Please Enter Correct Link')

Label(root,text='Welcome to Youtube\n Downloader Application',fg='red',font='Consolas 15 bold').pack()

myVar = StringVar()

myVar.set('Enter the link below')
Entry(root,textvariable=myVar,width=25,font='Consolas 15 bold').pack(pady=10)

link = StringVar()
Entry(root,textvariable=link,width=25,font=('bold',15)).pack(pady=10)

Button(root,text='Download Video',bg='yellow',font=('bold',15),command=download).pack()

root,mainloop()
