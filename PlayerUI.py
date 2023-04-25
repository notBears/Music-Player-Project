# Author: James Balden
# GitHub username: baldenosu
# Date: 4/22/2023
# Description: User Interface for the player window of the music player app.

# code citations : https://customtkinter.tomschimansky.com/documentation/

# Imports
import customtkinter
from PIL import Image
import pygame
from tinytag import TinyTag
import PlaylistsUI

customtkinter.set_appearance_mode('dark')

# Setup Sound control
pygame.mixer.init()
track = 'Griffin McElroy - Music from The Adventure Zone- Ethersea Vol. 1 - 01 The Adventure Zone- Ethersea - Main Theme.mp3'
metadata = TinyTag.get(track, image=True)
pygame.mixer.music.load(track)
pygame.mixer.music.play()
pygame.mixer.music.pause()


class TrackInformation(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.track_info = customtkinter.CTkLabel(master=self, text=f'Song: {metadata.title} | Artist: {metadata.artist} | Album: {metadata.album}')
        self.track_info.grid(row=1, column=0, columnspan=5)


class Player(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('400x400')
        self.title('Music Player')
        self.minsize(400, 400)

        # Load Images
        self.album_image = customtkinter.CTkImage(light_image=Image.open('astleyAlbumArt.png'), size=(200, 200))
        # self.playlist_image = customtkinter.CTkImage(Image.open('Images/Playlists.png'), size=(28, 21))
        # self.back_image = customtkinter.CTkImage(Image.open('Images/Back.png'), size=(31, 22))
        # self.play_image = customtkinter.CTkImage(Image.open('Images/Play.png'), size=(29, 33))
        # self.pause_image = customtkinter.CTkImage(Image.open('Images/Pause.png'), size=(23, 32))
        # self.skip_image = customtkinter.CTkImage(Image.open('Images/Skip.png'), size=(31, 22))
        # self.repeat_image = customtkinter.CTkImage(Image.open('Images/Repeat.png'), size=(31, 22))

        # Advanced Tools Menu
        self.advanced_var = customtkinter.StringVar(value='Advanced Tools')
        self.tools_menu = customtkinter.CTkOptionMenu(master=self, values=['Trimming Tool'], variable=self.advanced_var)
        self.tools_menu.grid(row=0, column=0, columnspan=2, padx=0, pady=(0, 10))

        # Album Art Image
        self.album_art_label = customtkinter.CTkLabel(master=self, text='', image=self.album_image)
        self.album_art_label.grid(row=1, column=0, columnspan=5)

        # Track Information
        self.track_info = TrackInformation(master=self, width=300, height=25, orientation='horizontal')
        self.track_info.grid(row=2, column=0, columnspan=5)

        # Track Slider
        self.slider = customtkinter.CTkSlider(master=self, from_=0, to=100, width=400, progress_color='purple')
        self.slider.grid(row=3, column=0, columnspan=5)
        self.slider.set(0)

        # Track elapsed time, track information, track length
        self.track_time = customtkinter.CTkLabel(master=self, text=f'{pygame.mixer.music.get_pos()}')
        self.track_length = customtkinter.CTkLabel(master=self, text=f'{int(metadata.duration//60)}:{int(metadata.duration%60):2d}')
        self.track_time.grid(row=4, column=0)
        self.track_length.grid(row=4, column=4)

        # Player Button Controls
        self.playlist_button = customtkinter.CTkButton(master=self, command=self.open_playlists, text='Playlists', width=60)
        self.playlist_button.grid(row=5, column=0)
        self.back_button = customtkinter.CTkButton(master=self, text='Back', width=60)
        self.back_button.grid(row=5, column=1)
        self.play_button = customtkinter.CTkButton(master=self, command=self.play_pause_button, text='Play', width=60)
        self.play_button.grid(row=5, column=2)
        self.skip_button = customtkinter.CTkButton(master=self, text='Skip', width=60)
        self.skip_button.grid(row=5, column=3)
        self.repeat_button = customtkinter.CTkButton(master=self, text='Repeat', width=60)
        self.repeat_button.grid(row=5, column=4)

        self.playlist_window = None

    def open_playlists(self):
        if self.playlist_window is None or not self.playlist_window.winfo_exists():
            self.playlist_window = PlaylistsUI.Playlists(self)
            self.playlist_window.after(20, self.playlist_window.lift)
        else:
            self.playlist_window.focus()

    def play_pause_button(self):
        current_state = self.play_button.cget('text')
        if current_state == 'Play':
            self.play_button.configure(text='Pause')
            pygame.mixer.music.unpause()
        else:
            self.play_button.configure(text='Play')
            pygame.mixer.music.pause()



if __name__ == "__main__":
    app = Player()
    app.mainloop()



