# src/config.py
"""Configuration settings for the breathwork application"""

PATTERNS = {
    "Circle Breathing": {
        "description": "Hold breath technique. Follow the dot around the circle.",
        "inhale_time": 4,
        "hold_time": 4,
        "exhale_time": 4
    },
    "Wave Breathing": {
        "description": "Basic inhale/exhale technique. Follow the dot up (inhale) and down (exhale).",
        "inhale_time": 4,
        "exhale_time": 4
    },
    "Square Breathing": {
        "description": "Box breathing technique. Follow the dot around the square: inhale, hold, exhale, hold.",
        "inhale_time": 4,
        "hold_time": 4,
        "exhale_time": 4,
        "hold_time_2": 4
    }
}

# src/breathing_patterns/square_pattern.py
from .base_pattern import BreathingPattern
import numpy as np

class SquarePattern(BreathingPattern):
    """Square breathing pattern for inhale-hold-exhale-hold pattern"""
    
    def get_pattern_name(self) -> str:
        return "Square Breathing (Box Breathing)"
    
    def generate_coordinates(self) -> tuple:
        # Generate points for a square
        points_per_side = 25
        
        # Bottom line (inhale)
        x1 = np.linspace(-1, 1, points_per_side)
        y1 = np.full_like(x1, -1)
        
        # Right line (hold)
        y2 = np.linspace(-1, 1, points_per_side)
        x2 = np.full_like(y2, 1)
        
        # Top line (exhale)
        x3 = np.linspace(1, -1, points_per_side)
        y3 = np.full_like(x3, 1)
        
        # Left line (hold)
        y4 = np.linspace(1, -1, points_per_side)
        x4 = np.full_like(y4, -1)
        
        # Combine all points
        x = np.concatenate([x1, x2, x3, x4])
        y = np.concatenate([y1, y2, y3, y4])
        
        return x, y

# src/utils/timer.py
import time
from dataclasses import dataclass
from typing import Optional

@dataclass
class Timer:
    """Timer utility for managing breathing exercises"""
    duration: int
    start_time: Optional[float] = None
    is_running: bool = False
    
    def start(self):
        """Start the timer"""
        self.start_time = time.time()
        self.is_running = True
    
    def stop(self):
        """Stop the timer"""
        self.is_running = False
        self.start_time = None
    
    def get_elapsed_time(self) -> float:
        """Get elapsed time in seconds"""
        if not self.is_running:
            return 0
        return time.time() - self.start_time
    
    def get_remaining_time(self) -> float:
        """Get remaining time in seconds"""
        if not self.is_running:
            return self.duration
        elapsed = self.get_elapsed_time()
        remaining = self.duration - elapsed
        return max(0, remaining)
    
    def is_finished(self) -> bool:
        """Check if timer has finished"""
        return self.get_remaining_time() == 0