# 🎛️ DSP Audio Effects Project

This project contains MATLAB implementations of classic digital audio effects applied to guitar recordings, focusing on Tube Distortion, WahWah, and Reverb. It explores audio signal processing concepts through custom effect functions and visualization.

---

## 🚀 Overview

- 🎸 **Input Audio:** Guitar sample (`guitar1.wav`)  
- 🔊 **Implemented Effects:**  
  - Tube Distortion  
  - WahWah (modulated filter effect)  
  - Reverb (using convolution with impulse responses)  
- 📈 **Visualization:** Spectrograms to analyze effect impact  
- 🎧 **Audio Playback:** Using MATLAB’s `sound()` function  

---

## ⚠️ Important Notes

- The WahWah effect uses per-sample filter coefficient calculations, which can be computationally expensive and slow for long audio signals.   

---

## 📂 Project Structure

```
dsp-audio-fx/
├── tube_dist.m          # Tube Distortion function
├── wahwah.m             # WahWah effect function
├── reverb.m             # Reverb function (requires rooms.mat)
├── tube_dist_loaded.m          
├── wahwah_loaded.m             
├── reverb_loaded.m             
├── guitar1.wav          # Guitar audio sample
├── rooms.mat            # Impulse responses for reverb
├── README.md            # Project documentation
```

---


## 📚 What I Learned

- Implementation of digital audio effects using MATLAB  
- Balancing computational complexity and real-time audio processing  
- Using convolution for reverberation effects  
- Techniques for signal visualization and analysis  

---

*Created by George Pyralis as part of my studies in Electrical and Computer Engineering at DUTH.*
