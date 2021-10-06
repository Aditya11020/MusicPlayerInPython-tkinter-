import pygame
from tkinter import *
import os
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
import shutil
from PIL import ImageTk
from tkinter import messagebox

class Player:
    def __init__(self):
        self.root = Tk()
        
        self.root.title("Music Player")
        self.root.geometry("550x550")
        #self.root.config(background="light blue")
        global paused
        paused = False
        global stopped
        stopped = False
        pygame.init()
        pygame.mixer.init()
        m = PhotoImage(file="E:\Python project\m.png")
        Label(self.root,text="Welcome ",pady=20,font=("Verdana",16)).pack()
        Label(self.root,image=m,pady=5).pack()
        Label(self.root,text="In which language would you like to listen music",pady=20,font=("Verdana",16)).pack()
        self.option=IntVar()
        Radiobutton(self.root,text="English",variable=self.option,padx=14,value=1,font=("Verdana",12)).pack()
        Radiobutton(self.root,text="Hindi",variable=self.option,padx=14,value=2,font=("Verdana",12)).pack()
        Radiobutton(self.root,text="Old Melodies",variable=self.option,padx=14,value=3,font=("Verdana",12)).pack()
        Button(self.root,text="lets play the music",font=("Verdana",14),command=self.clicked,activeforeground="green").pack()
        #Button(self.root,text="Back",font=("Verdana",12),command=self.back_login).pack(pady=5)
        
        self.flag=True
        self.root.mainloop()
    #def back_login(self):
    #    self.root.destroy()
    #    Login()
    def clicked(self):
        current_selection=self.option.get()
    
        if current_selection==1:
            if self.flag:
                if self.root.winfo_exists():
                    self.root.destroy()
                    self.start_English()
                self.flag=False
            else:
                self.start_English()
        elif current_selection==2:
            if self.flag:
                if self.root.winfo_exists():
                    self.root.destroy()
                    self.start_Hindi()
                self.flag=False
            else:
                self.start_Hindi()
            
        elif current_selection==3:
            if self.flag:
                if self.root.winfo_exists():
                    self.root.destroy()
                    self.start_Tamil()
                self.flag=False
            else:
                self.start_Tamil()
        else:
            messagebox.showerror("Error","Please select an option")
        
    def start_English(self):
        
        self.root1=Tk()
        self.root1.title("English Playlist")
        self.root1.geometry("600x570")
        master_frame = Frame(self.root1)
        master_frame.pack(pady=20)
        scrol_y = Scrollbar(master_frame,orient=VERTICAL)
        
        self.playlist = Listbox(master_frame,yscrollcommand=scrol_y.set,selectbackground="gold",width=40,selectmode=SINGLE,font=("vardana",14,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        self.playlist.grid(row=0,column=0)
        scrol_y.grid(row=0,column=0)
        scrol_y.config(command=self.playlist.yview)
        
        # add_to_fav_button = Button(self.root1,text="Add to Favourites",command=self.add_to_fav)
        # add_to_fav_button.pack(pady=5)
        # self.fav_button=Button(self.root1,text="View Favourites",command=self.view_fav)
        # self.fav_button.pack(pady=5)
        
        os.chdir("C:/Users/acer/Downloads/song_English")
        self.songtracks = os.listdir()
        self.track = StringVar()
        for track in self.songtracks:
            # track = track.replace("C:/Users/acer/Downloads/song_English","")
            # track = track.replace(".mp3","")
            self.playlist.insert(END,track)
        play = PhotoImage(file="E:\Python project\play.png")
        pause = PhotoImage(file="E:\Python project\pause.png")
        previous = PhotoImage(file="E:\Python project\previous.png")
        next = PhotoImage(file="E:\Python project\snext.png")
        stop = PhotoImage(file="E:\Python project\stop.png")

        controls_frame = Frame(master_frame)
        controls_frame.grid(row=1,column=0,pady=20)

        b1=Button(controls_frame,image = previous,activeforeground="green",command=self.previous)
        b2=Button(controls_frame,image = play,command = self.play,activeforeground="green")
        b3=Button(controls_frame,image = pause,command = lambda: self.pause(paused),activeforeground="green")
        b4=Button(controls_frame,image = stop,activeforeground="green",command=self.stop)
        b5=Button(controls_frame,image = next,activeforeground="green",command=self.next)
        b1.grid(row=0,column=0,padx=10)
        b2.grid(row=0,column=1,padx=10)
        b3.grid(row=0,column=2,padx=10)
        b4.grid(row=0,column=3,padx=10)
        b5.grid(row=0,column=4,padx=10)
        
    
        self.status_bar = Label(self.root1,text='',bd=1,relief=GROOVE,anchor=E)
        self.status_bar.pack(fill=X,side=BOTTOM,ipady=2)

        self.my_slider=ttk.Scale(master_frame,from_=0,to=100,orient=HORIZONTAL, value=0,command=self.slide,length=360)
        self.my_slider.grid(row=2,column=0,pady=10)
        self.volume_frame = LabelFrame(master_frame,text="Volume")
        self.volume_frame.grid(row=0,column=1,padx=20)
        self.volume_slider=ttk.Scale(self.volume_frame,from_=1,to=0,orient=VERTICAL, value=0.5,command=self.volume,length=125)
        self.volume_slider.pack(pady=10)
        
        self.slider_label =Label(self.volume_frame,text="50")
        self.slider_label.pack(pady=30)
        self.back_button=Button(self.root1,text="Back",activeforeground="green",command=self.back_E)
        self.back_button.pack(pady=5)
        self.root1.mainloop()
        
    def back_E(self):
        self.root1.destroy()
        self.__init__()
    def start_Hindi(self):
        
        self.root3=Tk()
        self.root3.title("Hindi Playlist")
        self.root3.geometry("600x570")
        master_frame = Frame(self.root3)
        master_frame.pack(pady=20)
        scrol_y = Scrollbar(master_frame,orient=VERTICAL)
        self.playlist = Listbox(master_frame,yscrollcommand=scrol_y.set,selectbackground="gold",width=40,selectmode=SINGLE,font=("vardana",14,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        self.playlist.grid(row=0,column=0)
        scrol_y.grid(row=0,column=1)
        scrol_y.config(command=self.playlist.yview)
        # add_to_fav_button = Button(self.root3,text="Add to Favourites",command=self.add_to_fav)
        # add_to_fav_button.pack(pady=5)
        # self.fav_button=Button(self.root3,text="View Favourites",command=self.view_fav_H)
        # self.fav_button.pack(pady=5)
        os.chdir("C:/Users/acer/Downloads/song_Hindi")
        self.songtracks = os.listdir()
        self.track = StringVar()
        for track in self.songtracks:
            # track = track.replace("C:/Users/acer/Downloads/song_English","")
            # track = track.replace(".mp3","")
            self.playlist.insert(END,track)
        play = PhotoImage(file="E:\Python project\play.png")
        pause = PhotoImage(file="E:\Python project\pause.png")
        previous = PhotoImage(file="E:\Python project\previous.png")
        next = PhotoImage(file="E:\Python project\snext.png")
        stop = PhotoImage(file="E:\Python project\stop.png")

        controls_frame = Frame(master_frame)
        controls_frame.grid(row=1,column=0,pady=20)

        b1=Button(controls_frame,image = previous,activeforeground="green",command=self.previous)
        b2=Button(controls_frame,image = play,command = self.play,activeforeground="green")
        b3=Button(controls_frame,image = pause,command = lambda: self.pause(paused),activeforeground="green")
        b4=Button(controls_frame,image = stop,activeforeground="green",command=self.stop)
        b5=Button(controls_frame,image = next,activeforeground="green",command=self.next)
        b1.grid(row=0,column=0,padx=10)
        b2.grid(row=0,column=1,padx=10)
        b3.grid(row=0,column=2,padx=10)
        b4.grid(row=0,column=3,padx=10)
        b5.grid(row=0,column=4,padx=10)
        
    
        self.status_bar = Label(self.root3,text='',bd=1,relief=GROOVE,anchor=E)
        self.status_bar.pack(fill=X,side=BOTTOM,ipady=2)

        self.my_slider=ttk.Scale(master_frame,from_=0,to=100,orient=HORIZONTAL, value=0,command=self.slide,length=360)
        self.my_slider.grid(row=2,column=0,pady=10)
        self.volume_frame = LabelFrame(master_frame,text="Volume")
        self.volume_frame.grid(row=0,column=2,padx=20)
        self.volume_slider=ttk.Scale(self.volume_frame,from_=1,to=0,orient=VERTICAL, value=0.5,command=self.volume,length=125)
        self.volume_slider.pack(pady=10)
        
        self.slider_label =Label(self.volume_frame,text="50")
        self.slider_label.pack(pady=30)
        self.back_button=Button(self.root3,text="Back",activeforeground="green",command=self.back_H)
        self.back_button.pack(pady=5)
        self.root3.mainloop()
    
    def back_H(self):
        self.root3.destroy()
        self.__init__()
    def start_Tamil(self):
        
        self.root4=Tk()
        self.root4.title("Old Melodies Playlist")
        self.root4.geometry("600x570")
        master_frame = Frame(self.root4)
        master_frame.pack(pady=20)
        self.playlist = Listbox(master_frame,selectbackground="gold",width=40,selectmode=SINGLE,font=("vardana",14,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        self.playlist.grid(row=0,column=0)
        # add_to_fav_button = Button(self.root4,text="Add to Favourites",command=self.add_to_fav)
        # add_to_fav_button.pack(pady=5)
        # self.fav_button=Button(self.root4,text="View Favourites",command=self.view_fav_T)
        # self.fav_button.pack(pady=5)
        os.chdir("C:/Users/acer/Downloads/song_Tamil")
        self.songtracks = os.listdir()
        self.track = StringVar()
        for track in self.songtracks:
            # track = track.replace("C:/Users/acer/Downloads/song_English","")
            # track = track.replace(".mp3","")
            self.playlist.insert(END,track)
        play = PhotoImage(file="E:\Python project\play.png")
        pause = PhotoImage(file="E:\Python project\pause.png")
        previous = PhotoImage(file="E:\Python project\previous.png")
        next = PhotoImage(file="E:\Python project\snext.png")
        stop = PhotoImage(file="E:\Python project\stop.png")

        controls_frame = Frame(master_frame)
        controls_frame.grid(row=1,column=0,pady=20)

        b1=Button(controls_frame,image = previous,activeforeground="green",command=self.previous)
        b2=Button(controls_frame,image = play,command = self.play,activeforeground="green")
        b3=Button(controls_frame,image = pause,command = lambda: self.pause(paused),activeforeground="green")
        b4=Button(controls_frame,image = stop,activeforeground="green",command=self.stop)
        b5=Button(controls_frame,image = next,activeforeground="green",command=self.next)
        b1.grid(row=0,column=0,padx=10)
        b2.grid(row=0,column=1,padx=10)
        b3.grid(row=0,column=2,padx=10)
        b4.grid(row=0,column=3,padx=10)
        b5.grid(row=0,column=4,padx=10)
        
    
        self.status_bar = Label(self.root4,text='',bd=1,relief=GROOVE,anchor=E)
        self.status_bar.pack(fill=X,side=BOTTOM,ipady=2)

        self.my_slider=ttk.Scale(master_frame,from_=0,to=100,orient=HORIZONTAL, value=0,command=self.slide,length=360)
        self.my_slider.grid(row=2,column=0,pady=10)
        self.volume_frame = LabelFrame(master_frame,text="Volume")
        self.volume_frame.grid(row=0,column=1,padx=20)
        self.volume_slider=ttk.Scale(self.volume_frame,from_=1,to=0,orient=VERTICAL, value=0.5,command=self.volume,length=125)
        self.volume_slider.pack(pady=10)
        
        self.slider_label =Label(self.volume_frame,text="50")
        self.slider_label.pack(pady=30)
        self.back_button=Button(self.root4,text="Back",activeforeground="green",command=self.back_T)
        self.back_button.pack(pady=5)
        self.root4.mainloop()
    def back_T(self):
        self.root4.destroy()
        self.__init__()
    def play(self):
       
        global stopped
        stopped = False
        
        self.track.set(self.playlist.get(ACTIVE))
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()
        self.play_time()
        
        #slider_position=int(song_length)
        #self.my_slider.config(to=slider_position,value=0)
    def pause(self,is_paused):
        global paused
        paused = is_paused
        if paused:
            
            pygame.mixer.music.unpause()
            paused = False
        else:
            
            pygame.mixer.music.pause()
            paused = True
    def next(self):
        self.status_bar.config(text='')
        self.my_slider.config(value=0)
        next_one = self.playlist.curselection()
        next_one = next_one[0]+1
        song = self.playlist.get(next_one)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        self.playlist.selection_clear(0,END)
        self.playlist.activate(next_one)
        self.playlist.selection_set(next_one, last =None)
    def previous(self):
        self.status_bar.config(text='')
        self.my_slider.config(value=0)
        next_one = self.playlist.curselection()
        next_one =next_one[0]-1
        song = self.playlist.get(next_one)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        self.playlist.selection_clear(0,END)
        self.playlist.activate(next_one)
        self.playlist.selection_set(next_one, last =None)
    def stop(self):
        self.status_bar.config(text='')
        self.my_slider.config(value=0)
        pygame.mixer.music.stop()
        self.playlist.selection_clear(ACTIVE)
        self.status_bar.config(text='')
        global stopped
        stopped = True
    def play_time(self):
        if stopped:
            return
        current_time = pygame.mixer.music.get_pos() / 1000
        convert_current_time=time.strftime('%H:%M:%S',time.gmtime(int(self.my_slider.get())))
        #self.slider_label.config(text=f'Slider: {int(self.my_slider.get())} and Song Pos: {int(current_time)} ')
        
        self.status_bar.config(text=convert_current_time)
        current_song = self.playlist.curselection()
        song = self.playlist.get(current_song)
        song_mut=MP3(song)
        global song_length
        song_length=song_mut.info.length
        convert_song_length=time.strftime('%H:%M:%S',time.gmtime(song_length))
        current_time+=1
        if int(self.my_slider.get()) == int(song_length):
            pass
        elif paused:
            pass
        elif int(self.my_slider.get()) == int(current_time):
            slider_position=int(song_length)
            self.my_slider.config(to=slider_position,value=int(current_time))
        else:
            slider_position=int(song_length)
            self.my_slider.config(to=slider_position,value=int(self.my_slider.get()))
            convert_current_time=time.strftime('%H:%M:%S',time.gmtime(int(self.my_slider.get())))
            self.status_bar.config(text=f'Time Elapsed:  {convert_current_time}   of   {convert_song_length}      ')
            next_time=int(self.my_slider.get()) + 1
            self.my_slider.config(value=next_time)
            

        
        #self.my_slider.config(value=current_time)
        
        

        self.status_bar.after(1000,self.play_time)


    def add_to_fav(self):
        self.current_favourite_song = self.playlist.curselection()
        self.fav_song = self.playlist.get(self.current_favourite_song)
        for x in self.songtracks:
            if x==(self.fav_song):
                #self.new_playlist.insert(END,x)
                shutil.copy(x,'C:/Users/acer/Downloads/fav')
                messagebox.showinfo("Info","Successfully added to Favourites")
    def view_fav_H(self):
        self.root3.destroy()
        self.root2=Tk()
        master_frame = Frame(self.root2)
        master_frame.pack()
        self.root2.geometry("500x500")
        self.new_playlist = Listbox(master_frame,selectbackground="gold",selectmode=SINGLE,font=("vardana",14,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        self.new_playlist.grid(row=0,column=0)
        controls_frame = Frame(master_frame)
        controls_frame.grid(row=1,column=0,pady=20)
        play = PhotoImage(file="E:\Python project\play.png")
        pause = PhotoImage(file="E:\Python project\pause.png")
        previous = PhotoImage(file="E:\Python project\previous.png")
        next = PhotoImage(file="E:\Python project\snext.png")
        stop = PhotoImage(file="E:\Python project\stop.png")
        #b1=Button(controls_frame,image = previous,activeforeground="green",command=self.previous)
        b2=Button(controls_frame,image = play,command = self.fav_play,activeforeground="green")
        b3=Button(controls_frame,image = pause,command = lambda: self.pause(paused),activeforeground="green")
        b4=Button(controls_frame,image = stop,activeforeground="green",command=self.fav_stop)
        #b5=Button(controls_frame,image = next,activeforeground="green",command=self.next)
        #b1.grid(row=0,column=0,padx=10)
        b2.grid(row=0,column=1,padx=10)
        b3.grid(row=0,column=2,padx=10)
        b4.grid(row=0,column=3,padx=10)
        #b5.grid(row=0,column=4,padx=10)
        remove_from_fav_button = Button(self.root2,text="Remove from Favourites",command=self.remove_from_fav)
        remove_from_fav_button.pack(anchor=CENTER)
        back = Button(self.root2,text="Back",command=self.fav_back)
        back.pack()
        os.chdir("C:/Users/acer/Downloads/fav")
        track = StringVar()
        self.fav_songtracks = os.listdir()
        for track in self.fav_songtracks:
            self.new_playlist.insert(END,track)
        self.root2.mainloop()
    def view_fav_T(self):
        self.root4.destroy()
        self.root2=Tk()
        master_frame = Frame(self.root2)
        master_frame.pack()
        self.root2.geometry("500x500")
        self.new_playlist = Listbox(master_frame,selectbackground="gold",selectmode=SINGLE,font=("vardana",14,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        self.new_playlist.grid(row=0,column=0)
        controls_frame = Frame(master_frame)
        controls_frame.grid(row=1,column=0,pady=20)
        play = PhotoImage(file="E:\Python project\play.png")
        pause = PhotoImage(file="E:\Python project\pause.png")
        previous = PhotoImage(file="E:\Python project\previous.png")
        next = PhotoImage(file="E:\Python project\snext.png")
        stop = PhotoImage(file="E:\Python project\stop.png")
        #b1=Button(controls_frame,image = previous,activeforeground="green",command=self.previous)
        b2=Button(controls_frame,image = play,command = self.fav_play,activeforeground="green")
        b3=Button(controls_frame,image = pause,command = lambda: self.pause(paused),activeforeground="green")
        b4=Button(controls_frame,image = stop,activeforeground="green",command=self.fav_stop)
        #b5=Button(controls_frame,image = next,activeforeground="green",command=self.next)
        #b1.grid(row=0,column=0,padx=10)
        b2.grid(row=0,column=1,padx=10)
        b3.grid(row=0,column=2,padx=10)
        b4.grid(row=0,column=3,padx=10)
        #b5.grid(row=0,column=4,padx=10)
        remove_from_fav_button = Button(self.root2,text="Remove from Favourites",command=self.remove_from_fav)
        remove_from_fav_button.pack(anchor=CENTER)
        back = Button(self.root2,text="Back",command=self.fav_back)
        back.pack()
        os.chdir("C:/Users/acer/Downloads/fav")
        track = StringVar()
        self.fav_songtracks = os.listdir()
        for track in self.fav_songtracks:
            self.new_playlist.insert(END,track)
        self.root2.mainloop()
    def view_fav(self):
        
        self.root1.destroy()
        self.root2=Tk()
        master_frame = Frame(self.root2)
        master_frame.pack()
        self.root2.geometry("500x500")
        self.new_playlist = Listbox(master_frame,selectbackground="gold",selectmode=SINGLE,font=("vardana",14,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
        self.new_playlist.grid(row=0,column=0)
        controls_frame = Frame(master_frame)
        controls_frame.grid(row=1,column=0,pady=20)
        play = PhotoImage(file="E:\Python project\play.png")
        pause = PhotoImage(file="E:\Python project\pause.png")
        previous = PhotoImage(file="E:\Python project\previous.png")
        next = PhotoImage(file="E:\Python project\snext.png")
        stop = PhotoImage(file="E:\Python project\stop.png")
        #b1=Button(controls_frame,image = previous,activeforeground="green",command=self.previous)
        b2=Button(controls_frame,image = play,command = self.fav_play,activeforeground="green")
        b3=Button(controls_frame,image = pause,command = lambda: self.pause(paused),activeforeground="green")
        b4=Button(controls_frame,image = stop,activeforeground="green",command=self.fav_stop)
        #b5=Button(controls_frame,image = next,activeforeground="green",command=self.next)
        #b1.grid(row=0,column=0,padx=10)
        b2.grid(row=0,column=1,padx=10)
        b3.grid(row=0,column=2,padx=10)
        b4.grid(row=0,column=3,padx=10)
        #b5.grid(row=0,column=4,padx=10)
        remove_from_fav_button = Button(self.root2,text="Remove from Favourites",command=self.remove_from_fav)
        remove_from_fav_button.pack(anchor=CENTER)
        back = Button(self.root2,text="Back",command=self.fav_back)
        back.pack()
        os.chdir("C:/Users/acer/Downloads/fav")
        track = StringVar()
        self.fav_songtracks = os.listdir()
        for track in self.fav_songtracks:
            self.new_playlist.insert(END,track)
        self.root2.mainloop()
    def remove_from_fav(self):
        self.current_remove_from_song = self.new_playlist.curselection()
        self.remove_song = self.new_playlist.get(self.current_remove_from_song)
        for x in self.songtracks:
            if x==(self.remove_song):
                #self.new_playlist.insert(END,x)
                os.unlink(f'C:/Users/acer/Downloads/fav/{x}')
                self.new_playlist.delete(self.current_remove_from_song)
         
    def slide(self,x):
        #self.slider_label.config(text=f'{int(self.my_slider.get())} of {int(song_length)}')
        self.track.set(self.playlist.get(ACTIVE))
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play(loops=0,start=int(self.my_slider.get()))
    def volume(self,x):
        pygame.mixer.music.set_volume(self.volume_slider.get())
        current_volume = pygame.mixer.music.get_volume()
        self.slider_label.config(text=int(current_volume*100))
    def fav_play(self):
        self.track.set(self.new_playlist.get(ACTIVE))
        pygame.mixer.music.load(self.new_playlist.get(ACTIVE))
        pygame.mixer.music.play()
    def fav_back(self):
        self.root2.destroy()
        self.__init__()
    def fav_stop(self):
            pygame.mixer.music.stop()
            self.new_playlist.selection_clear(ACTIVE)  
