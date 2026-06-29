#!/usr/bin/env python3
import os

def speak(text):
    os.system('termux-tts-speak "' + text + '"')


print('Priyanka Unified System Active')
