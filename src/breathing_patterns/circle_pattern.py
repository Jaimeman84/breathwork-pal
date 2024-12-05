# src/breathing_patterns/circle_pattern.py
from .base_pattern import BreathingPattern
import numpy as np

class CirclePattern(BreathingPattern):
    """Circle breathing pattern for hold breath exercises"""
    
    def get_pattern_name(self) -> str:
        return "Circle Breathing (Hold Breath)"
    
    def generate_coordinates(self) -> tuple:
        # Generate points for a circle starting from bottom
        t = np.linspace(-np.pi/2, 3*np.pi/2, 100)  # Start from bottom
        x = np.cos(t)
        y = np.sin(t)
        return x, y
    
    def get_start_end_points(self) -> tuple:
        # Override to ensure start/end point is at the bottom of the circle
        return (0, -1), (0, -1)
