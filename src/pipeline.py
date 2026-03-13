from typing import List
import numpy as np
from effects import BaseEffect

#Chain multiple audio effects together sequentially
class AudioAugmentationPipeline:
    def __init__(self, effects: List[BaseEffect]):
        self.effects = effects

    def __call__(self, x: np.ndarray, fs: int) -> np.ndarray:
        for effect in self.effects:
            x = effect(x, fs)
        return x