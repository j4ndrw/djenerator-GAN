import numpy as np
from scipy.io import wavfile
import os

raw_gen_samples_path = "./djenerated_samples_raw"
wav_gen_samples_path = "./djenerated_samples_wav"

sr = 44100
for filename in os.listdir(raw_gen_samples_path):
    if filename.endswith(".npy"):
        gen_song_samples = np.load(os.path.join(raw_gen_samples_path, filename))
        wavfile.write(
            os.path.join(wav_gen_samples_path, 
            f"{filename.split('.')[0]}.wav"), 
            sr, 
            np.concatenate(gen_song_samples)
        )
