from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from pytube.cli import on_progress
from pytube.contrib.playlist import Playlist

class App (Tk):

    def __init__(self):
        super().__init__()
        
        #   Main Setup 
        self.title('YouTube Downloader')
        self.maxsize(width=700,height=400)
        self.minsize(width=700,height=400)
        self.resizable(False,False)  

        #   
        menu = Menu()
        menu.create_widgets()

        self.mainloop() 

        
class Menu(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.pack()

    def create_widgets(self):

        #   App Title
        title_lab =ttk.Label(self,text=' YouTube Downloader ',anchor=CENTER,foreground='white',
                               font=('Arial',25,'bold'),background='red',relief=FLAT).pack(fill='x')
        
        video_url_frame =ttk.Frame(self)
        down_res_frame = ttk.Frame(self,width=400,height=400,relief=GROOVE)

        video_url_label=ttk.Label(video_url_frame,text='Your Video URL :')
        gets = ttk.Entry(video_url_frame,width=60,text='fff',font=('Arial'),justify=CENTER)


        resolution_label = ttk.Label(down_res_frame,text='resolutions: ')
        resolution_label.grid(padx=50,pady=15)

        choices=['720p','360p','144p','audio']
        resolution_choices = ttk.Combobox(down_res_frame,width=50,values=choices)

        download_button = Button(down_res_frame, width=20, font=('Roboto'), text='DOWNLOAD',background='red',fg="white", relief=FLAT)
        quit_button = Button(down_res_frame,width=15,text='Quit',fg='white',background='red')




        #   Widgets Configurations
        video_url_frame.config(width=800,height=100,relief=GROOVE)
        download_button.config()
        quit_button.config()

        #   Widgets Placement
        video_url_frame.pack()   
        down_res_frame.pack()
        video_url_label.grid(pady=15)
        gets.grid(padx=25,pady=15)
        resolution_choices.grid(row=0,column=1,pady=15,padx=14)
        download_button.grid(row=1,column=1,pady=15,padx=14)
        quit_button.grid(row=3,column=2,padx=55,pady=70)



 
App()