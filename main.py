import os
import player
from pynput.keyboard import Key, Listener
import time
from random import choice

class Keypress():
    def __init__(self, key):
        self.time = time.time()
        self.key = key


high_filenames = []
med_filenames = []
low_filenames = []
keypresses = []

period = 60

low_thresh = -1
mid_thresh = 100
high_thresh = 180

class thread_hack():
    currently_playing = None

for file in os.listdir("music/high"):
    high_filenames.append(file)

for file in os.listdir("music/med"):
    high_filenames.append(file)

for file in os.listdir("music/low"):
    high_filenames.append(file)

play_obj = player.Player()

def random_in_dir(dirname):
    return dirname + choice(os.listdir(dirname))

def on_press(key):
    keypresses.append(Keypress(key))
    amount = 0

    for key_n in keypresses:
        if key_n.time + period > time.time():
            amount += 1

    if amount > high_thresh:
        if thread_hack.currently_playing != "high":
            print("Playing high")
            play_obj.play_song(random_in_dir("music/high/"))
            thread_hack.currently_playing = "high"
        return

    elif amount > mid_thresh:
        if thread_hack.currently_playing != "med":
            print("Playing med")
            play_obj.play_song(random_in_dir("music/med/"))
            thread_hack.currently_playing = "med"
        return

    elif amount > low_thresh:
        if thread_hack.currently_playing != "low":
            print("Playing low")
            play_obj.play_song(random_in_dir("music/low/"))
            thread_hack.currently_playing = "low"
        return

with Listener(
        on_press=on_press) as listener:
    listener.join()

while True:
    time.sleep(0.1)