# 🎛️ DSP Audio Effects Project (Python OOP Port)

This project contains Python implementations of classic digital audio effects applied to guitar recordings, focusing on Tube Distortion, WahWah, and Reverb. Originally written in MATLAB, the project has been ported to Python to build a modular audio processing pipeline.

---

## 🚀 Overview

- 🎸 **Input Audio:** Guitar sample (`guitar1.wav`)  
- 🔊 **Implemented Effects:** - **Tube Distortion:** Simulates analog tube clipping with adjustable bias (Q).
  - **WahWah:** A modulated filter effect using a low-frequency oscillator (LFO).
  - **Reverb:** Convolution reverb using real room impulse responses.
- ⚙️ **Architecture:** Effects are built as Python classes that can be chained together sequentially in a pipeline.

---

## 📂 Project Structure

```text
dsp-audio-fx/
├── python_src/          
│   ├── effects.py       # Python classes for Distortion, WahWah, Reverb
│   ├── pipeline.py      # The pipeline orchestrator
│   └── main.py          # Main execution script
├── matlab_legacy/       # Original MATLAB implementations (.m files)
├── data/                
│   ├── guitar1.wav      # Guitar audio sample
│   └── rooms.mat        # Impulse responses for reverb
├── requirements.txt     # Python library dependencies
└── README.md            # Project documentation