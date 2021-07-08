import os
import player
from pynput.keyboard import Listener
import time
from random import choice
from threading import *


class Keypress():
    def __init__(self, key):
        self.time = time.time()
        self.key = key

keypresses = []

period = 60

low_thresh = -1
mid_thresh = 100
high_thresh = 180

minimum_run_time = 10

class thread_hack():
    currently_playing = None
    last_changed = 0

play_obj = player.Player()


def random_in_dir(dirname):
    return dirname + choice(os.listdir(dirname))


def process_changes():
    if time.time() < thread_hack.last_changed + minimum_run_time:
        return

    amount = 0

    for key_n in keypresses:
        if key_n.time + period > time.time():
            amount += 1

    if amount > high_thresh:
        if thread_hack.currently_playing != "high":
            print("Playing high")
            play_obj.play_song(random_in_dir("music/high/"))
            thread_hack.currently_playing = "high"

            thread_hack.last_changed = time.time()
        return

    elif amount > mid_thresh:
        if thread_hack.currently_playing != "med":
            print("Playing med")
            play_obj.play_song(random_in_dir("music/med/"))
            thread_hack.currently_playing = "med"

            thread_hack.last_changed = time.time()
        return

    elif amount > low_thresh:
        if thread_hack.currently_playing != "low":
            print("Playing low")
            play_obj.play_song(random_in_dir("music/low/"))
            thread_hack.currently_playing = "low"

            thread_hack.last_changed = time.time()
        return


def on_press(key):
    keypresses.append(Keypress(key))


def periodic():
    while True:
        process_changes()
        time.sleep(1)
        if time.time() > play_obj.song_end_time:
            play_obj.play_song(random_in_dir(f"music/{thread_hack.currently_playing}/"))


Thread(target=periodic).start()

with Listener(
        on_press=on_press) as listener:
    listener.join()
