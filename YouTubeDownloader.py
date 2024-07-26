from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from pytube import YouTube

class App(Tk):

    def __init__(self):
        super().__init__()
        
        # Main Setup 
        self.title('YouTube Downloader')
        self.maxsize(width=700, height=400)
        self.minsize(width=700, height=400)
        self.resizable(False, False)  

        # Initialize Menu
        self.menu = Menu(self)
        self.menu.pack()

        self.mainloop() 

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # App Title
        title_lab = ttk.Label(self, text='YouTube Downloader', anchor=CENTER, foreground='white',
                             font=('Arial', 25, 'bold'), background='red', relief=FLAT)

        video_url_frame = ttk.Frame(self)
        down_res_frame = ttk.Frame(self, width=400, height=400, relief=GROOVE)

        video_url_label = ttk.Label(video_url_frame, text='Your Video URL:')
        self.get_url = ttk.Entry(video_url_frame, width=60, font=('Arial'), justify=CENTER)

        resolution_label = ttk.Label(down_res_frame, text='Resolutions: ')
        resolution_label.grid(padx=50, pady=15)

        choices = ['720p', '360p', '144p', 'audio']
        self.resolution_choices = ttk.Combobox(down_res_frame, width=50, values=choices)

        download_button = Button(down_res_frame, width=20, font=('Roboto'), text='DOWNLOAD',
                                 background='red', fg="white", relief=FLAT, command=self.download)
        
        quit_button = Button(down_res_frame, width=15, text='Quit', fg='white', background='red', command=self.quit_app)

        # Widgets Placement
        title_lab.pack(fill='x')
        video_url_frame.pack()   
        down_res_frame.pack()
        video_url_label.grid(pady=15)
        self.get_url.grid(padx=25, pady=15)
        self.resolution_choices.grid(row=0, column=1, pady=15, padx=14)
        download_button.grid(row=1, column=1, pady=15, padx=14)
        quit_button.grid(row=3, column=2, padx=55, pady=70)

    def download(self):
        url = self.get_url.get()
        resolution = self.resolution_choices.get()
        
        choices = ['720p', '360p', '144p', 'audio']
        try:
            YT = YouTube(url)
            if resolution == choices[0]:
                Dw = YT.streams.get_by_resolution("720p")
            elif resolution == choices[1]:
                Dw = YT.streams.get_by_resolution("360p")
            elif resolution == choices[2]:
                Dw = YT.streams.get_by_resolution("144p")
            elif resolution == choices[3]:
                Dw = YT.streams.get_audio_only()
            else:
                raise ValueError("Invalid resolution")
            Dw.download()
            messagebox.showinfo(title='Download Complete', message='Download complete')
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror(title='Error', message="An error occurred while downloading. Please check the URL and resolution.")

    def quit_app(self):
        self.parent.destroy()

if __name__ == "__main__":
    
    #   Run The App
    App()
