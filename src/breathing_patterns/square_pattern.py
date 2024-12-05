# src/breathing_patterns/square_pattern.py
from .base_pattern import BreathingPattern
import numpy as np

class SquarePattern(BreathingPattern):
    """Square breathing pattern for inhale-hold-exhale-hold pattern"""
    
    def get_pattern_name(self) -> str:
        return "Square Breathing (Box Breathing)"
    
    def generate_coordinates(self) -> tuple:
        """Generate coordinates for a square pattern with equal sides"""
        # Number of points per side
        points_per_side = 25
        
        # Create arrays for each side of the square
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
        
        # Combine all coordinates
        x = np.concatenate([x1, x2, x3, x4])
        y = np.concatenate([y1, y2, y3, y4])
        
        return x, y
    
    def get_start_end_points(self) -> tuple:
        # Start and end at bottom left corner
        return (-1, -1), (-1, -1)