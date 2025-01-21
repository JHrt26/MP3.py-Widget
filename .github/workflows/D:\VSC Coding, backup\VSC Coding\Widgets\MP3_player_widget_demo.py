# Music Player project structure:
''' 
1.Importing all the libraries
2.Initializing the root window and pygame.mixer
3.Defining the play, stop, pause, resume and load functions
4.Creating the LabelFrames and StringVar variables
5.Placing all the objects in all the three LabelFrames
6.Creating the final Label that will display the status of the song 
'''




# importing necessary modules
from tkinter import * # (Tkinter) To create the GUI for the project
from tkinter import filedialog # (Tkinter) To create the GUI for the project
import pygame.mixer as mixer # This is a pygame module that is used to load and play music.
import os # to gather and retrieve the playlist of songs from chosen directory 

# Initializing the mixer
mixer.init()

'''Elements of mixer module
1._.load(filename) - This method is used to load a file so that other actions can be performed on that file. The argument it takes is a file of a supported audio format [.wav, .mp3, .ogg].
2._.play() - This method is used to play the music file that was loaded by the .load() method.
3._.stop() - This method can stop the loaded file such that it cannot be resumed again.
4._.pause() - This method is used to pause a loaded file, at least with this option, it can be played again before needing to be loaded again.
5._.unpause() - This method is used to unpause a loaded audio file, also known as the resume option.'''

# Building the main/master GUI for our music player 
root = Tk()
root.title("SPYDER'S Music Player ")
root.geometry('700x220')
root.resizable(0, 0) # type: ignore ~~




# functions that follow below are: Play, Stop, Load, Pause and Resume
def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()


    status.set("Song PLAYING") # status.set(display text) this allows us to show the status of any music being played 
    # paused, stopped or resumed. For this work I have placed the other statuses below with their partnered functions such as stop_song etc

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))

    tracks = os.listdir()

    for track in tracks: 
        listbox.insert(END, track)

def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")


def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")



# All the frames/frameworks
song_frame = LabelFrame(root, text='Current Song', font= ('DS-DIGITAL', 15, 'bold'), fg=('Yellow'), bg='Navy', width=400, height=80)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', font=('DS-DIGITAL', 15, 'bold'), fg=('Yellow'), bg='NavyBlue', width=400,
height=120)
button_frame.place(y= 80)


Listbox_frame = LabelFrame(root, text= 'Playlist', font= ('DS-DIGITAL', 15, 'bold'), fg=('Yellow'), bg='Navy')
Listbox_frame.place(x=400 , y=0, height=200, width=300)


# All StringVar variables
current_song = StringVar (root, value='<<<< Not selected >>>>')

song_status = StringVar (root, value='< Not Available >')

#Playlist ListBox 
playlist = Listbox (Listbox_frame, font= ('DS-DIGITAL'), selectbackground='RoyalBlue') 

scroll_bar = Scrollbar(Listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=9, pady=5)

#SongFrame Labels 
Label(song_frame, text='CURRENTLY PLAYING :',
bg='SteelBlue', font=('DS-DIGITAL', 13, 'bold'), width=18).place(x=17, y=19)

song_lbl = Label(song_frame, textvariable=current_song, bg= 'DarkOrange', 
font= ("DS-DIGITAL", 13, 'bold'), width=20) 
song_lbl.place(x=195, y=19)

# Buttons in the main screen 
pause_btn = Button(button_frame, text='Pause',
bg='SteelBlue', font=("DS-DIGITAL", 13), width=7,
                    command=lambda:
pause_song(song_status))
pause_btn.place(x=17, y=10)

stop_btn= Button(button_frame, text='Stop',
bg='SteelBlue', font=("DS-DIGITAL", 13), width=7,
                    command=lambda:
stop_song(song_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, text='Play',
bg='SteelBlue', font=("DS-DIGITAL", 13), width=7,
                    command=lambda:
play_song(current_song, playlist, song_status))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, text='Resume',
bg='SteelBlue', font=("DS-DIGITAL", 13), width=7,
                    command=lambda:
resume_song(song_status))
resume_btn.place(x=314, y=10)

load_btn = Button(button_frame, text='Load Directory', bg='SteelBlue', font=("DS-DIGITAL", 13),
width=44, command=lambda: load(playlist))
load_btn.place(x=17, y=52)


# Label below that shows the current condition of the music.
Label(root, textvariable=song_status,
bg='SteelBlue', font=('DS-DIGITAL', 13),
justify=LEFT).pack(side=BOTTOM, fill=X)


# Concluding GUI
root.update()
root.mainloop()
