import soundfile as sf
import numpy as np
from effects import TubeDistortion, WahWah, RoomReverb
from pipeline import AudioAugmentationPipeline

def main():
    # Load Audio with soundfile
    audio_path = r'guitar1.wav'
    x, fs = sf.read(audio_path)
    
    # If stereo, convert to mono for processing
    if len(x.shape) > 1:
        x = np.mean(x, axis=1)

    # Define the Augmentation Pipeline
    pipeline = AudioAugmentationPipeline([
        TubeDistortion(Q=-0.2, dist=8.0, gain=10.0),
        WahWah(Q=10.0, fc=3000.0, V0=50.0, mix=0.5),
        RoomReverb(room_id=1, mix=0.5, mat_path= r'rooms.mat')
    ])

    # Apply the pipeline
    y = pipeline(x, fs)
    
    # Normalize output to prevent clipping before saving
    y = y / np.max(np.abs(y))

    # 4. Save Output
    output_path = 'guitar1_augmented.wav'
    sf.write(output_path, y, fs)
    print(f"Saved augmented audio to {output_path}")

if __name__ == "__main__":
    main()