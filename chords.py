import numpy as np
import pyaudio
import keyboard
import threading

def play_audio(p, samples, fs, volume=0.5):
    output_bytes = (volume * samples).astype(np.float32).tobytes()

    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)

    stream.write(output_bytes)

    stream.stop_stream()
    stream.close()

def generate_sine_wave(frequency, duration, fs=44100):
    t = np.arange(int(fs * duration)) / fs
    samples = np.sign(np.sin(2 * np.pi * frequency * t))
    return samples

def play_major_chord(p, frequencies):
    chord_waveforms = [generate_sine_wave(freq, duration=.2) for freq in frequencies]
    chord_waveform = np.sum(chord_waveforms, axis=0)
    play_audio(p, chord_waveform, 44100)

if __name__ == "__main__":
    p = pyaudio.PyAudio()

    c_major = [327.03,  523.25]  # Frequencies for C major chord
    d_major = [366.17,  587.33]  # Frequencies for D major chord
    e_major = [412.87,  659.26]  # Frequencies for E major chord
    f_major = [436.05,  698.46]  # Frequencies for F major chord
    g_major = [489.92,  783.99]  # Frequencies for G major chord
    a_major = [549.72,  880.00]  # Frequencies for A major chord
    b_major = [617.82,  987.77]  # Frequencies for B major chord
    
    def play_c_major():
        play_major_chord(p, c_major)

    def play_d_major():
        play_major_chord(p, d_major)

    def play_e_major():
        play_major_chord(p, e_major)

    def play_f_major():
        play_major_chord(p, f_major)

    def play_g_major():
        play_major_chord(p, g_major)

    def play_a_major():
        play_major_chord(p, a_major)

    def play_b_major():
        play_major_chord(p, b_major)

   

    keyboard.add_hotkey('c', play_c_major)
    keyboard.add_hotkey('d', play_d_major)
    keyboard.add_hotkey('e', play_e_major)
    keyboard.add_hotkey('f', play_f_major)
    keyboard.add_hotkey('g', play_g_major)
    keyboard.add_hotkey('a', play_a_major)
    keyboard.add_hotkey('b', play_b_major)
    
    print("Press 'c' to play C major chord")
    print("Press 'd' to play D major chord")
    print("Press 'e' to play E major chord")
    print("Press 'f' to play F major chord")
    print("Press 'g' to play G major chord")
    print("Press 'a' to play A major chord")
    print("Press 'b' to play B major chord")
    print("Press 'q' to quit")

    keyboard.wait('q')  # Wait for 'q' key to exit

    p.terminate()
