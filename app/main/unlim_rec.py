import sounddevice as sd
import numpy as np
from pynput.keyboard import Listener, Key
import threading
import queue

from app.settings import *


# Queue to handle the data
q = queue.Queue()

# Event to signal stopping
stop_event = threading.Event()


def _callback(indata, frames, time, status):
    """ Stream audio from microphone to queue """
    q.put(indata.copy())


def _start_recording():
    """ Recording thread to manage audio recording """
    with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype=DTYPE,
            callback=_callback,
    ):
        print('Recording...')
        while not stop_event.is_set():
            sd.sleep(100)

        print('Recording stopped.')


def _on_press(key):
    """ Handle key press """
    if key == Key.space:
        stop_event.set()  # Set stop event to stop recording
        return False  # Return False to stop the listener


def record():
    # Start recording in a separate thread
    rec_thread = threading.Thread(target=_start_recording)
    rec_thread.start()

    # Set up keyboard listener
    listener = Listener(on_press=_on_press)
    listener.start()

    # Wait for the listener to complete before proceeding
    listener.join()
    rec_thread.join()  # Ensure the recording thread is also joined after listener stops

    # Reset stop event
    stop_event.clear()

    # Retrieve the recorded data from the queue
    recorded_data = []
    while not q.empty():
        recorded_data.append(q.get())

    # Convert list of numpy arrays to a single numpy array
    recorded_data = np.concatenate(recorded_data, axis=0)
    return recorded_data
