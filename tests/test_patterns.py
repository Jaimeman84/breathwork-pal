# tests/test_patterns.py
import pytest
import numpy as np
from src.breathing_patterns.circle_pattern import CirclePattern
from src.breathing_patterns.wave_pattern import WavePattern

def test_circle_pattern_coordinates():
    pattern = CirclePattern(60)
    x, y = pattern.generate_coordinates()
    
    assert len(x) == 100
    assert len(y) == 100
    # Test if coordinates form a circle
    assert np.allclose(np.sqrt(x**2 + y**2), 1.0, atol=1e-10)

def test_wave_pattern_coordinates():
    pattern = WavePattern(60)
    x, y = pattern.generate_coordinates()
    
    assert len(x) == 100
    assert len(y) == 100
    # Test if y values are within [-1, 1]
    assert np.all(np.abs(y) <= 1.0)