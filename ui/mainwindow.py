# ui/mainwindow.py
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from .tabs import TabManager
from .widgets import ModernAddressBar, NavigationBar, Sidebar
from .themes import ThemeManager

class ModernBrowserWindow:
    def __init__(self, engine):
        self.engine = engine
        self.setup_window()
        self.theme_manager = ThemeManager()
        self.setup_ui()
        
    def setup_window(self):
        self.root = ctk.CTk()
        self.root.title("Modern Browser")
        self.root.geometry("1200x800")
        
        # Configure grid
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        
    def setup_ui(self):
        # Create main components
        self.sidebar = Sidebar(self.root)
        self.navigation = NavigationBar(self.root)
        self.address_bar = ModernAddressBar(self.root)
        self.tabs = TabManager(self.root)
        
        # Layout components
        self.sidebar.grid(row=0, column=0, rowspan=3, sticky="nsew")
        self.navigation.grid(row=0, column=1, sticky="ew")
        self.address_bar.grid(row=1, column=1, sticky="ew")
        self.tabs.grid(row=2, column=1, sticky="nsew")
        
        # Add modern styling
        self.apply_styling()
        
        # Bind events
        self.address_bar.on_navigate(self.load_page)
        
    def apply_styling(self):
        style = ttk.Style()
        current_theme = self.theme_manager.current_theme
        
        if current_theme:
            style.configure(
                "Browser.TFrame",
                background=current_theme.colors["background"]
            )
            style.configure(
                "Browser.TLabel",
                background=current_theme.colors["background"],
                foreground=current_theme.colors["text"],
                font=current_theme.fonts["main"]
            )
            
    def load_page(self, url):
        content = self.engine.load_url(url)
        self.tabs.current_tab.display_content(content)
        
    def run(self):
        self.root.mainloop()
class BrowserWindow:
    def __init__(self):
        # كود التنفيذ هنا
        pass