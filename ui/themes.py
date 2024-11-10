# ui/themes.py
class Theme:
    def __init__(self, name, colors, fonts):
        self.name = name
        self.colors = colors
        self.fonts = fonts
        
class ThemeManager:
    def __init__(self):
        self.themes = {}
        self.current_theme = None
        self._load_default_themes()
        
    def _load_default_themes(self):
        # Light theme
        self.add_theme(Theme(
            "light",
            colors={
                "primary": "#007AFF",
                "secondary": "#5856D6",
                "background": "#FFFFFF",
                "text": "#000000",
                "accent": "#FF2D55"
            },
            fonts={
                "main": ("Segoe UI", 10),
                "headers": ("Segoe UI", 12, "bold"),
                "monospace": ("Consolas", 10)
            }
        ))
        
        # Dark theme
        self.add_theme(Theme(
            "dark",
            colors={
                "primary": "#0A84FF",
                "secondary": "#5E5CE6",
                "background": "#000000",
                "text": "#FFFFFF",
                "accent": "#FF375F"
            },
            fonts={
                "main": ("Segoe UI", 10),
                "headers": ("Segoe UI", 12, "bold"),
                "monospace": ("Consolas", 10)
            }
        ))
        
    def add_theme(self, theme):
        self.themes[theme.name] = theme
        
    def apply_theme(self, theme_name):
        if theme_name in self.themes:
            self.current_theme = self.themes[theme_name]
            return True
        return False
