# ui/widgets.py
import customtkinter as ctk

class ModernAddressBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.setup_ui()
        
    def setup_ui(self):
        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter URL or search...",
            width=600,
            height=35
        )
        self.entry.pack(side="left", padx=10, pady=5, fill="x", expand=True)
        
        self.search_button = ctk.CTkButton(
            self,
            text="Go",
            width=60,
            height=35,
            command=self._on_navigate
        )
        self.search_button.pack(side="right", padx=10, pady=5)
        
    def on_navigate(self, callback):
        self._navigate_callback = callback
        
    def _on_navigate(self):
        if hasattr(self, '_navigate_callback'):
            self._navigate_callback(self.entry.get())

class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=200)
        self.setup_ui()
        
    def setup_ui(self):
        # Bookmarks section
        self.bookmarks_label = ctk.CTkLabel(
            self,
            text="Bookmarks",
            font=("Segoe UI", 12, "bold")
        )
        self.bookmarks_label.pack(pady=10, padx=5, anchor="w")
        
        # History section
        self.history_label = ctk.CTkLabel(
            self,
            text="History",
            font=("Segoe UI", 12, "bold")
        )
        self.history_label.pack(pady=10, padx=5, anchor="w")
        
        # Downloads section
        self.downloads_label = ctk.CTkLabel(
            self,
            text="Downloads",
            font=("Segoe UI", 12, "bold")
        )
        self.downloads_label.pack(pady=10, padx=5, anchor="w")
        
        # Settings button
        self.settings_button = ctk.CTkButton(
            self,
            text="Settings",
            command=self._open_settings
        )
        self.settings_button.pack(pady=10, padx=5, side="bottom")
        
    def _open_settings(self):
        # TODO: Implement settings dialog
        pass


# Example plugin implementation