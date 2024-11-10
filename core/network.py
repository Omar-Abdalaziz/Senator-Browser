# core/network.py
import requests
import ssl
from urllib3.util import ssl_
from utils.cache import Cache

class NetworkManager:
    def __init__(self):
        self.cache = Cache()
        self.session = requests.Session()
        self.ssl_context = self._create_ssl_context()
    
    def _create_ssl_context(self):
        context = ssl.create_default_context()
        context.set_ciphers('ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256')
        return context
    
    def fetch(self, url):
        # Check cache first
        cached_content = self.cache.get(url)
        if cached_content:
            return cached_content
            
        # Make secure request
        try:
            response = self.session.get(
                url,
                verify=True,
                headers={
                    'User-Agent': 'CustomBrowser/1.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
                }
            )
            content = response.text
            
            # Cache the result
            self.cache.set(url, content)
            
            return content
        except Exception as e:
            return f"Error loading page: {str(e)}"
