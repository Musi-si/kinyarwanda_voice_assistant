from gtts import gTTS
import pygame
import time
import os

def speak( text ):
    tts = gTTS( text = text, lang = 'sw' )
    file = 'output.mp3'
    tts.save( file )

    pygame.mixer.init()
    pygame.mixer.music.load( file )
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep( 0.5 )

    pygame.mixer.quit()
    os.remove( file )