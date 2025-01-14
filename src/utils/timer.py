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