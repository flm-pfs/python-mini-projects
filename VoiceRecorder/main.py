import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav


def record_audio(duration, sample_rate=44100, output_file='VoiceRecorder\output.wav'):
    print(f"Recording started for {duration} seconds...")
    audio_data = sd.rec(int(duration * sample_rate),
                        samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")

    # Save the recorded audio to a WAV file
    wav.write(output_file, sample_rate, audio_data)
    print(f"Audio saved to {output_file}")


if __name__ == "__main__":
    duration = int(input("Enter the recording duration in seconds: "))
    record_audio(duration)
