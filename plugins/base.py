# plugins/base.py
from abc import ABC, abstractmethod
import typing as t

class BrowserPlugin(ABC):
    def __init__(self):
        self.name = self.__class__.__name__
        self.version = "1.0.0"
        self.description = ""
        self.author = ""
        
    @abstractmethod
    def initialize(self, browser_instance):
        """Initialize the plugin"""
        pass
        
    @abstractmethod
    def cleanup(self):
        """Cleanup when plugin is disabled"""
        pass
        
    def get_manifest(self) -> dict:
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "author": self.author
        }
