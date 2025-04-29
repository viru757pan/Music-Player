from tkinter import *
import pygame
from tkinter import filedialog
import os
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

# Global Variables
paused = False
is_playing = False
after_id = None
play_time_after_id = None
songs_folder_path = "songs/"


def add_all_song_automatic():
    files = [f for f in os.listdir(songs_folder_path) if f.endswith('.mp3')]
    for song in files:
        song = song.replace(".mp3", "")
        songs_box.insert(END, song)


def add_song():
    song = filedialog.askopenfilename(initialdir=songs_folder_path, title="Choose a song",
                                      filetypes=(("mp3 Files", "*.mp3"), ("All Files", "*.*")))
    song = song.replace("songs/", "").replace(".mp3", "")
    songs_box.insert(END, song)


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir=songs_folder_path, title="Choose songs",
                                        filetypes=(("mp3 Files", "*.mp3"), ("All Files", "*.*")))
    for song in songs:
        song = song.replace("songs/", "").replace(".mp3", "")
        songs_box.insert(END, song)


def delete_song():
    songs_box.delete(ANCHOR)
    pygame.mixer.music.stop()


def delete_all_songs():
    songs_box.delete(0, END)
    pygame.mixer.music.stop()


def play():
    global is_playing, paused, after_id

    if not songs_box.curselection():
        return

    song = songs_box.get(ACTIVE)
    song_path = f"{songs_folder_path}{song}.mp3"
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0)

    slider.set(0)
    is_playing = True
    paused = False

    if after_id:
        status_bar.after_cancel(after_id)
    play_time()


def stop():
    global status_bar, play_time_after_id
    pygame.mixer.music.stop()
    songs_box.selection_clear(ACTIVE)
    slider.config(value=0)
    status_bar.config(text='00:00')
    if play_time_after_id:
        status_bar.after_cancel(play_time_after_id)
        play_time_after_id = None


def pause(_):
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def next_song():
    global is_playing, paused
    curr_song = songs_box.curselection()
    if not curr_song:
        return
    next_index = (curr_song[0] + 1) % songs_box.size()
    songs_box.selection_clear(0, END)
    songs_box.activate(next_index)
    songs_box.selection_set(next_index)
    paused = False
    is_playing = True
    slider.set(0)
    play()


def prev_song():
    global is_playing, paused
    curr_song = songs_box.curselection()
    if not curr_song:
        return
    prev_index = (curr_song[0] - 1) % songs_box.size()
    songs_box.selection_clear(0, END)
    songs_box.activate(prev_index)
    songs_box.selection_set(prev_index)
    paused = False
    is_playing = True
    slider.set(0)
    play()


def play_time():
    global status_bar, slider, song_len, play_time_after_id, paused

    if paused:
        # If music is paused, skip updating
        play_time_after_id = status_bar.after(1000, play_time)
        return

    current_time = pygame.mixer.music.get_pos() / 1000
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    song = f"{songs_folder_path}{songs_box.get(ACTIVE)}.mp3"
    song_mut = MP3(song)
    song_len = song_mut.info.length
    converted_song_legth = time.strftime('%M:%S', time.gmtime(song_len))

    if int(slider.get()) >= int(song_len):
        status_bar.config(
            text=f'{converted_song_legth} / {converted_song_legth}')
    else:
        slider.config(to=int(song_len), value=int(slider.get()))
        converted_current_time = time.strftime(
            '%M:%S', time.gmtime(int(slider.get())))
        status_bar.config(
            text=f'{converted_current_time} / {converted_song_legth}')
        slider.config(value=int(slider.get()) + 1)

    play_time_after_id = status_bar.after(1000, play_time)


def slide(X):
    song = f"{songs_folder_path}{songs_box.get(ACTIVE)}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))


def main():
    global songs_box, status_bar, slider, root
    root = Tk()
    root.title("Music Player")
    root.geometry("360x350")

    pygame.mixer.init()

    songs_box = Listbox(root, bg="black", fg="white", width=60,
                        selectbackground="gray", selectforeground="white")
    songs_box.pack(pady=20)
    add_all_song_automatic()

    buttons_images_path = "buttons/"
    prev_btn_img = PhotoImage(file=f"{buttons_images_path}prev.png")
    next_btn_img = PhotoImage(file=f"{buttons_images_path}next.png")
    play_btn_img = PhotoImage(file=f"{buttons_images_path}play.png")
    pause_btn_img = PhotoImage(file=f"{buttons_images_path}pause.png")
    stop_btn_img = PhotoImage(file=f"{buttons_images_path}stop.png")

    control_frame = Frame(root)
    control_frame.pack()

    prev_btn = Button(control_frame, image=prev_btn_img,
                      borderwidth=0, command=prev_song)
    play_btn = Button(control_frame, image=play_btn_img,
                      borderwidth=0, command=play)
    pause_btn_widget = Button(
        control_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
    stop_btn = Button(control_frame, image=stop_btn_img,
                      borderwidth=0, command=stop)
    next_btn = Button(control_frame, image=next_btn_img,
                      borderwidth=0, command=next_song)

    prev_btn.pack(padx=7, side=LEFT)
    play_btn.pack(padx=7, side=LEFT)
    pause_btn_widget.pack(padx=7, side=LEFT)
    stop_btn.pack(padx=7, side=LEFT)
    next_btn.pack(padx=7, side=LEFT)

    my_menu = Menu(root)
    root.config(menu=my_menu)

    add_songs_menu = Menu(my_menu)
    my_menu.add_cascade(label="Add Song", menu=add_songs_menu)
    add_songs_menu.add_command(
        label="Add One Song in Playlist", command=add_song)
    add_songs_menu.add_command(
        label="Add Many Songs in Playlist", command=add_many_songs)

    remove_songs_menu = Menu(my_menu)
    my_menu.add_cascade(label="Remove Song", menu=remove_songs_menu)
    remove_songs_menu.add_command(
        label="Remove One Song in Playlist", command=delete_song)
    remove_songs_menu.add_command(
        label="Remove All Songs in Playlist", command=delete_all_songs)

    status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
    status_bar.pack(fill=X, side=BOTTOM, ipady=3)

    slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL,
                       value=0, command=slide, length=300)
    slider.pack(side=BOTTOM)

    root.mainloop()


if __name__ == "__main__":
    main()
