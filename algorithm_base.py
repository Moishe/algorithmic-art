# ABOUTME: Base class interface for all art generation algorithms
# ABOUTME: Provides common structure and methods for algorithm implementations

from abc import ABC, abstractmethod
import click


class AlgorithmBase(ABC):
    """Base class for all art generation algorithms"""
    
    def __init__(self, size, output):
        self.size = size
        self.output = output
    
    @abstractmethod
    def generate(self):
        """Generate the algorithm's data structure"""
        pass
    
    @abstractmethod
    def save_image(self, data):
        """Save the generated data as an image"""
        pass
    
    @classmethod
    @abstractmethod
    def add_cli_options(cls, command):
        """Add algorithm-specific CLI options to a click command"""
        pass
    
    @classmethod
    @abstractmethod
    def create_from_args(cls, **kwargs):
        """Create algorithm instance from parsed CLI arguments"""
        pass