import pygame
import keyboard

playlist = ["creep.mp3", "drive.mp3"]
current_song = 0

def play_music():
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    current_song = (current_song + 1) % len(playlist)
    play_music()

def previous_song():
    global current_song
    current_song = (current_song - 1) % len(playlist)
    play_music()

def main():
    pygame.init()
    pygame.mixer.init()

    while True:
        if keyboard.is_pressed('p'):
            play_music()
        elif keyboard.is_pressed('s'):
            stop_music()
        elif keyboard.is_pressed('n'):
            next_song()
        elif keyboard.is_pressed('b'):
            previous_song()

if __name__ == "__main__":
    main()
