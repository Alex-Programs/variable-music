import pygame
import time

pygame.mixer.init()
pygame.init()


def get_song(fname):
    return pygame.mixer.Sound(fname)

class Player():
    def __init__(self):
        self.song1 = None
        self.song2 = None

    def play_song(self, song):
        song = get_song(song)
        if not self.song1:
            self.song1 = song
            self.song1.play()
            if self.song2:
                time.sleep(0.1)
                self.song2.stop()
                self.song2 = None

        else:
            self.song2 = song
            self.song2.play()
            if self.song1:
                time.sleep(0.1)
                self.song1.stop()
                self.song1 = None