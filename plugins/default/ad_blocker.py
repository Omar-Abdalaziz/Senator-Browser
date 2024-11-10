# plugins/default/ad_blocker.py
from plugins.base import BrowserPlugin

class AdBlocker(BrowserPlugin):
    def __init__(self):
        super().__init__()
        self.name = "AdBlocker"
        self.version = "1.0.0"
        self.description = "Blocks unwanted advertisements"
        self.author = "Browser Team"
        self.blocked_domains = set()
        
    def initialize(self, browser_instance):
        self.browser = browser_instance
        self.load_block_list()
        self.browser.network.register_request_filter(self.filter_request)
        
    def cleanup(self):
        self.browser.network.unregister_request_filter(self.filter_request)
        
    def load_block_list(self):
        # Load blocked domains from file or API
        self.blocked_domains = {
            "ads.example.com",
            "tracker.example.com"
        }
        
    def filter_request(self, url):
        return not any(domain in url for domain in self.blocked_domains)

# plugins/default/dark_mode.py
class DarkMode(BrowserPlugin):
    def __init__(self):
        super().__init__()
        self.name = "DarkMode"
        self.version = "1.0.0"
        self.description = "Enables dark mode for websites"
        self.author = "Browser Team"
        
    def initialize(self, browser_instance):
        self.browser = browser_instance
        self.browser.renderer.register_style_modifier(self.apply_dark_mode)
        
    def cleanup(self):
        self.browser.renderer.unregister_style_modifier(self.apply_dark_mode)
        
    def apply_dark_mode(self, styles):
        dark_styles = """
            :root {
                --page-background: #121212;
                --text-color: #ffffff;
            }
            body {
                background-color: var(--page-background) !important;
                color: var(--text-color) !important;
            }
        """
        return styles + dark_styles