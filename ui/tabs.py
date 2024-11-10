# ui/tabs.py
import customtkinter as ctk
from tkinter import ttk
from typing import Dict, Optional

class Tab(ctk.CTkFrame):
    def __init__(self, master, title: str, closeable: bool = True):
        super().__init__(master)
        self.title = title
        self.setup_ui(closeable)
        
    def setup_ui(self, closeable: bool):
        self.content = ctk.CTkTextbox(self)
        self.content.pack(fill="both", expand=True)
        
    def display_content(self, content: str):
        self.content.delete("1.0", "end")
        self.content.insert("1.0", content)
        
    def get_title(self) -> str:
        return self.title

class TabManager(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.tabs: Dict[str, Tab] = {}
        self.current_tab: Optional[Tab] = None
        self.setup_ui()
        
    def setup_ui(self):
        # Tab header frame
        self.header = ctk.CTkFrame(self)
        self.header.pack(fill="x", padx=5, pady=2)
        
        # New tab button
        self.new_tab_btn = ctk.CTkButton(
            self.header,
            text="+",
            width=30,
            command=self.add_new_tab
        )
        self.new_tab_btn.pack(side="right", padx=5)
        
        # Tab content frame
        self.content = ctk.CTkFrame(self)
        self.content.pack(fill="both", expand=True)
        
        # Create initial tab
        self.add_new_tab()
        
    def add_new_tab(self, title: str = "New Tab"):
        # Create new tab
        tab = Tab(self.content, title)
        self.tabs[title] = tab
        
        # Create tab button
        tab_btn = ctk.CTkButton(
            self.header,
            text=title,
            command=lambda t=tab: self.switch_to_tab(t)
        )
        tab_btn.pack(side="left", padx=2)
        
        # Switch to new tab
        self.switch_to_tab(tab)
        
    def switch_to_tab(self, tab: Tab):
        if self.current_tab:
            self.current_tab.pack_forget()
        
        tab.pack(fill="both", expand=True)
        self.current_tab = tab
        
    def close_tab(self, tab: Tab):
        if tab in self.tabs.values():
            if self.current_tab == tab:
                # Switch to another tab if available
                other_tabs = [t for t in self.tabs.values() if t != tab]
                if other_tabs:
                    self.switch_to_tab(other_tabs[0])
                    
            tab.destroy()
            # Remove from tabs dict
            self.tabs = {k: v for k, v in self.tabs.items() if v != tab}
            
            if not self.tabs:
                self.add_new_tab()
