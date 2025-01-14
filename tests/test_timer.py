# tests/test_timer.py
import pytest
import time
import sys
from pathlib import Path

# Add the source directory to Python path
src_path = str(Path(__file__).parent.parent)
if src_path not in sys.path:
    sys.path.append(src_path)

from src.utils.timer import Timer

def test_timer_initialization():
    """Test timer initialization with default values"""
    timer = Timer(duration=60)
    assert timer.duration == 60
    assert not timer.is_running
    assert timer.start_time is None

def test_timer_start_stop():
    """Test timer start and stop functionality"""
    timer = Timer(duration=60)
    
    timer.start()
    assert timer.is_running
    assert timer.start_time is not None
    
    timer.stop()
    assert not timer.is_running
    assert timer.start_time is None

def test_timer_elapsed_time():
    """Test elapsed time calculation"""
    timer = Timer(duration=60)
    
    timer.start()
    time.sleep(0.1)  # Small delay to ensure time passes
    elapsed = timer.get_elapsed_time()
    
    assert elapsed > 0
    assert elapsed < 60

def test_timer_remaining_time():
    """Test remaining time calculation"""
    duration = 60
    timer = Timer(duration=duration)
    
    assert timer.get_remaining_time() == duration
    
    timer.start()
    time.sleep(0.1)  # Small delay
    remaining = timer.get_remaining_time()
    
    assert remaining < duration
    assert remaining > 0

def test_timer_is_finished():
    """Test timer finished state"""
    timer = Timer(duration=0.1)
    
    timer.start()
    time.sleep(0.2)  # Wait longer than duration
    
    assert timer.is_finished()

def test_timer_not_running():
    """Test timer behavior when not running"""
    timer = Timer(duration=60)
    
    assert timer.get_elapsed_time() == 0
    assert timer.get_remaining_time() == 60
    assert not timer.is_finished()