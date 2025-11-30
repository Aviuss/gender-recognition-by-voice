import numpy as np 
import math
from scipy.io import wavfile

def get_hz_signal(data, freqs, n, sample_rate):
    signal_fft = abs(np.fft.fft(data))
    
    end_idx = int(len(signal_fft)/2+1)
    hz_signal = zip(freqs[1:end_idx], signal_fft[1:end_idx])
    return list(hz_signal)

def extract_range_in_hz_signal(hz_signal, hz_from, hz_to):
    return list(filter(lambda x: x[0] >= hz_from and x[0] <= hz_to, hz_signal))

def get_dominant_freq_for_hz_signal(hz_signal):
    dominant_freq = None
    max_value = None
    for (i_freq, i_sig) in hz_signal:
        if i_freq == 0:
            continue
        if max_value == None:
            max_value = i_sig
            dominant_freq = i_freq
        if max_value < i_sig:
            max_value = i_sig
            dominant_freq = i_freq
    
    return dominant_freq
        

if __name__ == "__main__":
    sample_rate, data = wavfile.read("./train/001_K.wav")
    
    n = len(data)
    freqs = np.arange(0, n) * (sample_rate / n)
    

    if (data.shape[1] != 1):
        data = data[:, 1]

    #Mężczyzni 85-180Hz
    #Kobiety 165-255Hz
    
    hz_signal = get_hz_signal(data, freqs, n, sample_rate)
    hz_signal_in_voice_range = extract_range_in_hz_signal(hz_signal, 85, 255)
    dominant_freq = get_dominant_freq_for_hz_signal(hz_signal)

    print("end")