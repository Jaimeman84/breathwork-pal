# tests/test_timer.py
import pytest
import time
from src.utils.timer import Timer

def test_timer_initialization():
    timer = Timer(duration=60)
    assert timer.duration == 60
    assert not timer.is_running
    assert timer.start_time is None

def test_timer_start_stop():
    timer = Timer(duration=60)
    
    timer.start()
    assert timer.is_running
    assert timer.start_time is not None
    
    timer.stop()
    assert not timer.is_running
    assert timer.start_time is None

def test_timer_elapsed_time():
    timer = Timer(duration=60)
    
    timer.start()
    time.sleep(0.1)
    elapsed = timer.get_elapsed_time()
    
    assert elapsed > 0
    assert elapsed < 60

def test_timer_remaining_time():
    duration = 60
    timer = Timer(duration=duration)
    
    assert timer.get_remaining_time() == duration
    
    timer.start()
    time.sleep(0.1)
    remaining = timer.get_remaining_time()
    
    assert remaining < duration
    assert remaining > 0

def test_timer_is_finished():
    timer = Timer(duration=0.1)
    
    timer.start()
    time.sleep(0.2)
    
    assert timer.is_finished()