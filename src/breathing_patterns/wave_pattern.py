# src/breathing_patterns/wave_pattern.py
from .base_pattern import BreathingPattern
import numpy as np

class WavePattern(BreathingPattern):
    """Wave pattern for inhale/exhale exercises"""
    
    def get_pattern_name(self) -> str:
        return "Wave Breathing (Inhale/Exhale)"
    
    def generate_coordinates(self) -> tuple:
        """Generate coordinates for a wave pattern, properly scaled and centered"""
        # Generate more points for smoother curve
        t = np.linspace(0, 2*np.pi, 100)
        
        # Create scaled wave
        x = t / (2*np.pi) * 2 - 1  # Scale to [-1, 1]
        y = np.sin(t)  # Already in [-1, 1] range
        
        return x, y
    
    def get_start_end_points(self) -> tuple:
        x, y = self.generate_coordinates()
        return (x[0], y[0]), (x[-1], y[-1])
