import numpy as np
import scipy.io as sio
from scipy.signal import fftconvolve, sawtooth
import os

#Base class for all audio data augmentation effects
class BaseEffect:
    def __call__(self, x: np.ndarray, fs: int) -> np.ndarray:
        raise NotImplementedError("Effect must implement the __call__ method.")

class TubeDistortion(BaseEffect):
    def __init__(self, Q: float = -0.2, dist: float = 8.0, gain: float = 10.0):
        self.Q = Q
        self.dist = dist
        self.gain = gain

    def __call__(self, x: np.ndarray, fs: int) -> np.ndarray:
        max_abs_x = np.max(np.abs(x))
        if max_abs_x == 0: 
            return x
            
        normalized_x = x / max_abs_x
        gained_x = normalized_x * self.gain

        if self.Q != 0:
            diff = gained_x - self.Q
            # Add epsilon to prevent division by zero
            eps = np.finfo(float).eps 
            f = (diff / (1 - np.exp(-self.dist * diff) + eps)) + \
                (self.Q / (1 - np.exp(self.dist * self.Q)))
        else:
            f = (1.0 / self.dist) * np.ones_like(x)

        max_abs_f = np.max(np.abs(f))
        return f / max_abs_f if max_abs_f != 0 else f

class WahWah(BaseEffect):
    def __init__(self, Q: float = 10.0, fc: float = 3000.0, V0: float = 50.0, mix: float = 0.5):
        self.Q = Q
        self.fc = fc
        self.V0 = V0
        self.mix = mix

    def __call__(self, x: np.ndarray, fs: int) -> np.ndarray:
        y_a = np.zeros_like(x)
        
        # Precompute LFO (Low Frequency Oscillator)
        t = np.arange(len(x)) / fs
        saw_wave = sawtooth(2 * np.pi * t, 1) # Width=1 means rising sawtooth
        triangle_wave = 2 * np.abs(np.mod(saw_wave, 2) - 1) - 1
        
        F_array = self.fc * (1 + 0.35 * triangle_wave)
        K_array = np.tan(np.pi * F_array / fs)
        
        for n in range(2, len(x)):
            K = K_array[n]
            b0 = (1 + (K * self.V0 / self.Q) + K**2) / (1 + (K / self.Q) + K**2)
            b1 = 2 * (K**2 - 1) / (1 + (K / self.Q) + K**2)
            b2 = (1 - (K * self.V0 / self.Q) + K**2) / (1 + (K / self.Q) + K**2)
            a1 = b1
            a2 = (1 - (K / self.Q) + K**2) / (1 + (K / self.Q) + K**2)

            y_a[n] = b0 * x[n] + b1 * x[n-1] + b2 * x[n-2] \
                     - a1 * y_a[n-1] - a2 * y_a[n-2]

        return self.mix * y_a + (1 - self.mix) * x

class RoomReverb(BaseEffect):
    def __init__(self, room_id: int = 1, mix: float = 0.5, mat_path: str = 'rooms.mat'):
        self.room_id = room_id
        self.mix = mix
        
        # Load the impulse responses once during initialization, not on every call
        if not os.path.exists(mat_path):
            raise FileNotFoundError(f"Impulse response file {mat_path} not found.")
            
        rooms_data = sio.loadmat(mat_path)
        ir_key = f'h{self.room_id}'
        
        if ir_key not in rooms_data:
            raise ValueError(f"Room {room_id} not found in {mat_path}.")
            
        # Flatten the IR to 1D
        self.impulse_response = rooms_data[ir_key].flatten()

    def __call__(self, x: np.ndarray, fs: int) -> np.ndarray:
        # Using fftconvolve for O(N log N) speed instead of standard O(N^2) convolution
        ya = fftconvolve(x, self.impulse_response, mode='full')
        
        # Trim to original length
        ya = ya[:len(x)]
        
        return self.mix * ya + (1 - self.mix) * x