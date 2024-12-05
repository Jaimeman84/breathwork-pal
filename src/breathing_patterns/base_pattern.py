# src/breathing_patterns/base_pattern.py
from abc import ABC, abstractmethod
import numpy as np

class BreathingPattern(ABC):
    """Base class for breathing patterns"""
    
    def __init__(self, duration: int):
        self.duration = duration
        
    @abstractmethod
    def generate_coordinates(self) -> tuple:
        """Generate x, y coordinates for the breathing pattern"""
        pass
    
    @abstractmethod
    def get_pattern_name(self) -> str:
        """Return the name of the breathing pattern"""
        pass
    
    def get_start_end_points(self) -> tuple:
        """Get coordinates for start and end points"""
        x, y = self.generate_coordinates()
        return (x[0], y[0]), (x[-1], y[-1])