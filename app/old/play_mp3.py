import io

import pygame


pygame.mixer.init()


def play_audio(audio_mp3):
    pygame.mixer.music.load(io.BytesIO(audio_mp3))
    pygame.mixer.music.play()

    # Ensuring that the main program waits until the audio playback is complete before moving on.
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Is-Busy check happens 10 times per sec
