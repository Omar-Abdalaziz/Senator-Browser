# core/engine.py
import socket
import ssl
import threading
from urllib.parse import urlparse
from .network import NetworkManager
from .parser import HTMLParser
from .renderer import Renderer

class BrowserEngine:
    def __init__(self, config):
        self.config = config
        self.network = NetworkManager()
        self.parser = HTMLParser()
        self.renderer = Renderer()
        self.history = []
        self.bookmarks = []
        
    def load_url(self, url):
        # Validate URL
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = 'https://' + url
            
        # Fetch content
        content = self.network.fetch(url)
        
        # Parse content
        dom = self.parser.parse(content)
        
        # Render page
        rendered_page = self.renderer.render(dom)
        
        # Update history
        self.history.append(url)
        
        return rendered_page
        
    def get_security_info(self, url):
        return self.network.get_security_info(url)
